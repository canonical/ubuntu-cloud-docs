Use UEFI Secure Boot and TPM on Ubuntu-based EC2 instances
==========================================================

UEFI Secure Boot is a security feature specified in UEFI, which verifies the state of the boot chain.
With UEFI Secure Boot enabled, after firmware self-initialisation only cryptographically verified UEFI 
binaries are allowed to be executed. This prevents any unauthorised modification of the instance boot flow.

Trusted Platform Module (TPM) is a virtual device provided by the AWS Nitro System. It securely stores artifacts 
(such as passwords, certificates, or encryption keys) that are used to authenticate the instance. Check the `AWS NitroTPM documentation <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/nitrotpm.html>`_ for more details.

Although UEFI Secure Boot is supported by both Ubuntu images and `EC2 <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/uefi-secure-boot.html>`_,
it is not enabled in the EC2 AMIs. So to use UEFI Secure Boot (along with TPM), a couple of configuration steps are needed 
that create and register a new AMI based on an existing Ubuntu AMI:

#. Download a prebuilt UEFI Secure Boot variable store
#. Get an Ubuntu AMI ID to be used as the base image
#. Register a new AMI configured with - UEFI boot mode, the downloaded UEFI Secure Boot variable store and support for a virtual TPM


To follow these steps, you'll need ``aws-cli`` and ``jq``:

.. code-block::

   sudo snap install aws-cli
   sudo apt install jq

Download a prebuilt UEFI Secure Boot variable store
---------------------------------------------------

The variable store is prebuilt and can be downloaded using:

.. code-block::

   wget https://github.com/canonical/aws-secureboot-blob/releases/latest/download/blob.bin

For information on how this binary blob gets created, you can refer to its `source code`_
and read the relevant `AWS documentation <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/aws-binary-blob-creation.html>`_.

Get an Ubuntu AMI ID
--------------------

The SSM parameter store can be used to get e.g. the latest 22.04 LTS AMI ID:

.. code-block::

   AMI=$(aws ssm get-parameters \
       --names /aws/service/canonical/ubuntu/server/22.04/stable/current/amd64/hvm/ebs-gp2/ami-id \
       --query 'Parameters[0].Value' --output text)

If you want to use a different Ubuntu image, refer to :ref:`Find Ubuntu images on AWS`. Once you have the AMI ID, 
use it to get the image name and its snapshot ID. These will be needed during the registration of a new AMI.

.. code-block::

   AMI_NAME=$(aws ec2 describe-images \
       --image-id "${AMI}" \
       | jq -r '.Images[0].Name')
   AMI_SNAPSHOT=$(aws ec2 describe-images  \
       --image-id "${AMI}" \
       | jq -r '.Images[0].BlockDeviceMappings[0].Ebs.SnapshotId')

The ``${AMI}`` variable should now contain a valid AMI ID (e.g. ``ami-0373268fb2dac8b4b``),
``${AMI_NAME}`` should have something like ``ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-20230711`` and
``${AMI_SNAPSHOT}`` should have a valid Snapshot ID (e.g. ``snap-095ef5e2836b5a9e3``).


Register a new AMI
------------------

To register a new AMI, first create a copy of the chosen AMI's snapshot:

.. code-block::

   REGION=$(aws configure get region)
   AMI_SNAPSHOT_NEW=$(aws ec2 copy-snapshot \
       --source-region "${REGION}" \
       --source-snapshot-id "${AMI_SNAPSHOT}" \
       | jq -r '.SnapshotId')
   aws ec2 wait snapshot-completed --snapshot-ids "${AMI_SNAPSHOT_NEW}"

Now register a new AMI with the boot mode set to ``uefi``, TPM support enabled, and the downloaded UEFI variable store attached:

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

``$AMI_NEW`` now contains the new AMI ID. This new registered image can now be booted with UEFI Secure Boot.


Verify secure boot mode
-----------------------

.. note::
   * UEFI boot mode (and in turn Secure Boot) is only supported by certain instance types. Check the `AWS boot mode documentation <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/launch-instance-boot-mode.html#boot-considerations>`_ for details.

   * NitroTPM is only supported by certain instance types. Check the `AWS NitroTPM prerequisites documentation <https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/enable-nitrotpm-prerequisites.html>`_ for details.

Let's start a new instance with the newly created image (``$AMI_NEW``) and verify two things - (1) Secure Boot is enabled and (2) A TPM device is present.
To do this, first set the `KEY_NAME` variable to your keypair name. This allows you to login to the instance over ssh.

.. code-block::

   KEY_NAME=my-uploaded-keypair-name

Next start an instance:

.. code-block::

   INSTANCE=$(aws ec2 run-instances --image-id "${AMI_NEW}" --instance-type t3.medium --key-name "${KEY_NAME}"|jq -r '.Instances[].InstanceId')
   INSTANCE_IP=$(aws ec2 describe-instances --instance-ids "${INSTANCE}"|jq -r '.Reservations[].Instances[].PublicIpAddress')

Now login and check the Secure Boot status:

.. code-block::

   ssh ubuntu@${INSTANCE_IP} mokutil --sb-state

   ... which should output:

   SecureBoot enabled

Finally check that the TPM device is available:

.. code-block::

   ssh ubuntu@${INSTANCE_IP} ls -al /dev/tpm*

   ... which should output something like:

   crw-rw---- 1 tss root  10,   224 Jul 18 10:53 /dev/tpm0
   crw-rw---- 1 tss tss  253, 65536 Jul 18 10:53 /dev/tpmrm0


.. _`source code`: https://github.com/canonical/aws-secureboot-blob/
