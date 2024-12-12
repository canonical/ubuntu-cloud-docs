Find Ubuntu images on AWS
=========================

On AWS, cloud images are referred to as Amazon Machine Images (AMIs). Canonical produces a wide variety of images to support numerous features found on AWS:

* Generally, all images use Elastic Block Storage (EBS) and hardware virtual machine (HVM) virtualisation types. Older releases may also support paravirtual (PV) and instance-store, but users benefit from the newer storage and virtualisation technologies.
* `Standard` and `minimal` server images are available for both `amd64` and `arm64`.
* `Daily` (untested) and `release` versions of the images are published regularly.

All images mentioned below are also available in `AWS Outposts <https://aws.amazon.com/outposts/>`_.


Finding images with SSM
-----------------------
The SSM Parameter Store is a hierarchical data service provided by AWS for configuration management. It can be used to store passwords, license codes, configuration strings, Amazon Machine Image (AMI) IDs, and more. Canonical provides a set of publicly available parameters in the parameter store under the hierarchy ``/aws/service/canonical``. One useful set of parameters available under that hierarchy is the set of latest AMI IDs for Ubuntu images. These IDs can be found programmatically using the AWS CLI.

Images for EC2 and EKS
~~~~~~~~~~~~~~~~~~~~~~

.. tabs::
   
   .. tab:: For EC2

      Find the latest AMI ID using:

      .. code-block::

         aws ssm get-parameters --names \
            /aws/service/canonical/ubuntu/server/24.04/stable/current/amd64/hvm/ebs-gp3/ami-id

      The format for the parameter is:

      .. code-block::

         ubuntu/$PRODUCT/$RELEASE/stable/current/$ARCH/$VIRT_TYPE/$VOL_TYPE/ami-id

      * PRODUCT: `server`, `server-minimal`, `pro-server` or `pro-minimal`
      * RELEASE: `noble`, 24.04, `jammy`, `22.04`, `focal`, `20.04`
      * ARCH: `amd64` or `arm64`
      * VIRT_TYPE: `pv` or `hvm`
      * VOL_TYPE: `ebs-gp3` (for >=23.10), `ebs-gp2` (for <=23.04), `ebs-io1`, `ebs-standard`, or `instance-store`

      In place of `current`, the serial number given to an image can also be used (e.g., `20210222`):

      .. code-block::
         
         ubuntu/$PRODUCT/$RELEASE/stable/$SERIAL/$ARCH/$VIRT_TYPE/$VOL_TYPE/ami-id
         

   .. tab:: For EKS
      
      The latest EKS AMI ID for each supported EKS version can be found in the SSM parameter store using:

      .. code-block::

         aws ssm get-parameters --names /aws/service/canonical/ubuntu/eks/22.04/1.31/stable/current/amd64/hvm/ebs-gp2/ami-id

      The format for the parameter is:

      .. code-block::

         ubuntu/$EKS_PRODUCT/$RELEASE/$K8S_VERSION/stable/current/$ARCH/hvm/ebs-gp2/ami-id

      * EKS_PRODUCT: `eks` or `eks-pro`
      * RELEASE: `jammy`, `22.04` (for EKS 1.29 or greater, or EKS Pro); `focal`, `20.04` (for EKS <= 1.29)
      * K8S_VERSION: one of the supported EKS versions (e.g. `1.31`)
      * ARCH: `amd64` or `arm64`

In the generated output, the "Value" field will have the required AMI ID. It can be used to instantiate the corresponding image using the ``ec2 run-instances`` command as explained :ref:`here <instantiate-image-on-ec2>`. 

If you don't want to save the AMI ID before instantiating the image, you can use the ``resolve:ssm`` option and directly pass the required parameter to it in your ``ec2 run-instances`` call:

.. code::

   aws ec2 run-instances \
      --image-id resolve:ssm:/aws/service/canonical/ubuntu/server/24.04/stable/current/amd64/hvm/ebs-gp3/ami-id \
      --key-name TestKeyPair \
      --instance-type t3.medium

Ownership verification
~~~~~~~~~~~~~~~~~~~~~~

By checking the `OwnerId` field of an image, you can verify that an AMI was published by Canonical. To do this, use the `describe-images` command against an AMI ID and check the returned `OwnerId` field:

.. code::

   aws ec2 describe-images --image-ids $AMI_ID

The expected value of `OwnerId` for Canonical is one of the following:

* `099720109477` (in the default partition)
* `513442679011` (in the GovCloud partition)
* `837727238323` (in the China partition)

Note that listings on the AWS Marketplace will always show the `OwnerId` as Amazon (e.g. `679593333241`). In these cases, users can verify the Amazon ID and look for `aws-marketplace/ubuntu` in the `ImageLocation` field.


Images in the AWS Marketplace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AWS Marketplace is a digital catalogue with thousands of software listings from independent software vendors that make it easy to find, test, buy, and deploy software that runs on AWS.
Canonical maintains `image listings <https://aws.amazon.com/marketplace/seller-profile?id=565feec9-3d43-413e-9760-c651546613f2>`_ for recent Ubuntu releases and special flavours (e.g. `Anbox`, `Pro`, `Pro FIPS`, `EKS`) on this marketplace.

Customers can also use the AWS Marketplace to launch and subscribe to official Ubuntu Pro images that allow users to pay for additional support.

All the above mentioned Marketplace images can also be found in the SSM parameter store:

.. code-block::

   aws ssm get-parameter --name /aws/service/marketplace/$IDENTIFIER/latest

* IDENTIFIER: use one of the following identifiers (starting with `prod-`)

**AWS Marketplace identifiers**

.. csv-table::
   :file: aws-marketplace-identifiers.csv
   :widths: auto
   :header-rows: 1
