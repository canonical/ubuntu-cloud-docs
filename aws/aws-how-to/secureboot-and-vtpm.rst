UEFI Secureboot and Trusted Platform Module (TPM)
=================================================

UEFI Secure Boot is a feature specified in UEFI, which verifies the state of the boot chain.
With UEFI Secure Boot enabled only cryptographically verified UEFI binaries can be executed
after the self-initialisation of the firmware.

Trusted Platform Module (TPM) is provided by the AWS Nitro System and conforms to the
TPM 2.0 specification. Check the `AWS NitroTPM Documentation <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm.html>`_ for more details.

EC2 does support `UEFI Secure Boot <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/uefi-secure-boot.html>`_ which prevents unauthorized modification of the instance boot flow.
Ubuntu images do support UEFI Secure Boot. However, UEFI Secure Boot is not enabled in the EC2 AMIs.
So a couple of configuration steps are required to register a new AMI (based on the Ubuntu AMIs)
which allows using UEFI Secure Boot.

#. Download a prebuilt UEFI Secure Boot variable store
#. Get a Ubuntu AMI Id which will be used as a base image
#. Register a new AMI with UEFI boot mode, the UEFI Secure Boot variable store and support for a virtual TPM


To follow this guide, `aws-cli` and `jq` need to be installed:

.. code-block::

   sudo snap install aws-cli
   sudo apt install jq

Download prebuilt UEFI Secure Boot variable store
-------------------------------------------------

The variable store is prebuilt and can be downloaded with:

.. code-block::

   wget https://github.com/canonical/aws-secureboot-blob/releases/latest/download/blob.bin

For information how this binary blob gets created, please checkout out the source code
at https://github.com/canonical/aws-secureboot-blob and read the
relevant `AWS documentation <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/aws-binary-blob-creation.html>`_.

Get a Ubuntu AMI id
-------------------

The SSM parameter store can be used to get eg. the latest 22.04 LTS AMI:

.. code-block::

   AMI=$(aws ssm get-parameters \
       --names /aws/service/canonical/ubuntu/server/22.04/stable/current/amd64/hvm/ebs-gp2/ami-id \
       --query 'Parameters[0].Value' --output text)
   AMI_NAME=$(aws ec2 describe-images \
       --image-id "${AMI}" \
       | jq -r '.Images[0].Name')
   AMI_SNAPSHOT=$(aws ec2 describe-images  \
       --image-id "${AMI}" \
       | jq -r '.Images[0].BlockDeviceMappings[0].Ebs.SnapshotId')

The `${AMI}` variable should now contain a valid AMI Id (eg. `ami-0373268fb2dac8b4b`),
the `${AMI_NAME}` some like `ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-20230711` and
the `${AMI_SNAPSHOT}` variable a valid Snapshot Id (eg `snap-095ef5e2836b5a9e3`).

If you want to use a different Ubuntu image together with UEFI Secure Boot,
check out :ref:`Find Ubuntu images on AWS`.

Register a new AMI
------------------

To register a new AMI, the snapshot needs to be copied and the new AMI registered:

.. code-block::

   REGION=$(aws configure get region)
   AMI_SNAPSHOT_NEW=$(aws ec2 copy-snapshot \
       --source-region "${REGION}" \
       --source-snapshot-id "${AMI_SNAPSHOT}" \
       | jq -r '.SnapshotId')
   aws ec2 wait snapshot-completed --snapshot-ids "${AMI_SNAPSHOT_NEW}"

And finally create a new AMI with the `uefi` boot mode, the UEFI variable store attached and TPM support:

.. code-block::

   AMI_NEW=$(aws ec2 register-image \
       --name "${AMI_NAME}-secureboot" \
       --uefi-data "$(cat blob.bin)" \
       --block-device-mappings "DeviceName=/dev/sda1,Ebs= {SnapshotId=""${AMI_SNAPSHOT_NEW}"",DeleteOnTermination=true}" \
       --architecture x86_64 \
       --root-device-name /dev/sda1 \
       --virtualization-type hvm \
       --ena-support \
       --boot-mode uefi \
       --tpm-support v2.0 \
       | jq -r '.ImageId')
   aws ec2 wait image-available --image-ids "${AMI_NEW}"

`$AMI_NEW` contains now the new AMI ID. That new registered image can now be
booted with UEFI Secure Boot.


Verify secure boot mode
-----------------------

.. note::
   UEFI boot mode (and Secure Boot) is only supported by certain instance types. Check
   the `AWS boot mode documentation <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launch-instance-boot-mode.html#boot-considerations>`_ for details.

.. note::
   NitroTPM is only supported by certain instance types. Check the `AWS NitroTPM prerequisites documentation <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enable-nitrotpm-prerequisites.html>`_ for details.

Let's start a new instance with the newly created image (`$AMI_NEW`) and verify that Secure Boot is enabled.
Set the `KEY_NAME` variable to you keypair name so the login to the instance over ssh does work.

.. code-block::

   KEY_NAME=my-uploaded-keypair-name

Now start an instance:

.. code-block::

   INSTANCE=$(aws ec2 run-instances --image-id "${AMI_NEW}" --instance-type t3.medium --key-name "${KEY_NAME}"|jq -r '.Instances[].InstanceId')
   INSTANCE_IP=$(aws ec2 describe-instances --instance-ids "${INSTANCE}"|jq -r '.Reservations[].Instances[].PublicIpAddress')

Now login into the newly created instance and check the Secure Boot status:

.. code-block::

   ssh ubuntu@${INSTANCE_IP} mokutil --sb-state

   ... which should output:

   SecureBoot enabled

The TPM device should be available as `/dev/tpmrm0`:

.. code-block::

   ssh ubuntu@${INSTANCE_IP} ls -al /dev/tpm*

   ... which should output something like:

   crw-rw---- 1 tss root  10,   224 Jul 18 10:53 /dev/tpm0
   crw-rw---- 1 tss tss  253, 65536 Jul 18 10:53 /dev/tpmrm0
