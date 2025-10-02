Find Ubuntu images on AWS
=========================

On AWS, cloud images are referred to as Amazon Machine Images (AMIs). Canonical produces a wide variety of images to support numerous features found on AWS:

* Generally, all images use Elastic Block Storage (EBS) and hardware virtual machine (HVM) virtualization types. Older releases may also support paravirtual (PV) and instance-store, but users benefit from the newer storage and virtualization technologies.
* `Standard` and `minimal` server images are available for both `AMD64` and `ARM64`.
* `Daily` (untested) and `release` versions of the images are published regularly.

All images mentioned below are also available in `AWS Outposts <https://aws.amazon.com/outposts/>`_.


Finding images for EC2 and EKS
------------------------------

To find images on AWS, you can use the `SSM Parameter Store`_, the `describe-images`_ API or the `AWS Web Console`_. All three methods are explained below.

.. tabs::
   .. tab:: Using SSM Parameter Store

      The SSM Parameter Store is a hierarchical data service provided by AWS for configuration management. It can be used to store passwords, license codes, configuration strings, Amazon Machine Image (AMI) IDs, and more. Canonical provides a set of publicly available parameters in the parameter store under the hierarchy ``/aws/service/canonical``. One useful set of parameters available under that hierarchy is the set of latest AMI IDs for Ubuntu images. These IDs can be found programmatically using the AWS CLI.

      .. tabs::
         
         .. tab:: EC2

            For EC2, find the latest AMI ID using:

            .. code-block::

               aws ssm get-parameters --names \
                  /aws/service/canonical/ubuntu/server/24.04/stable/current/amd64/hvm/ebs-gp3/ami-id

            The format for the parameter is:

            .. code-block::

               ubuntu/$PRODUCT/$RELEASE/stable/current/$ARCH/$VIRT_TYPE/$VOL_TYPE/ami-id

            * PRODUCT: `server`, `server-minimal`, `pro-server` or `pro-minimal`
            * RELEASE: `noble`, 24.04, `jammy`, `22.04`, `focal`, `20.04`, `bionic`, `18.04`, `xenial`, or `16.04`
            * ARCH: `amd64` or `arm64`
            * VIRT_TYPE: `hvm` or `pv` (only for legacy releases ≤ 16.04)
            * VOL_TYPE: `ebs-gp3` (for >=23.10), `ebs-gp2` (for <=23.04), `ebs-io1`, `ebs-standard`, or `instance-store`

            In place of `current`, the serial number given to an image can also be used (e.g., `20250804`):

            .. code-block::
               
               ubuntu/$PRODUCT/$RELEASE/stable/$SERIAL/$ARCH/$VIRT_TYPE/$VOL_TYPE/ami-id
               

         .. tab:: EKS
            
            For EKS, the latest EKS AMI ID for each supported EKS version can be found in the SSM parameter store using:

            .. code-block::

               aws ssm get-parameters --names /aws/service/canonical/ubuntu/eks/24.04/1.31/stable/current/amd64/hvm/ebs-gp3/ami-id

            The format for the parameter is:

            .. code-block::

               ubuntu/$EKS_PRODUCT/$RELEASE/$K8S_VERSION/stable/current/$ARCH/hvm/$VOL_TYPE/ami-id

            * EKS_PRODUCT: `eks` or `eks-pro`
            * RELEASE: `noble`, `24.04` (for EKS 1.31 or greater, or EKS Pro); `jammy`, `22.04` (for EKS 1.29 or greater, or EKS Pro); `focal`, `20.04` (for EKS <= 1.29)
            * K8S_VERSION: one of the supported EKS versions (e.g. `1.31`)
            * ARCH: `amd64` or `arm64`
            * VOL_TYPE: `ebs-gp2` (for <= 22.04) and `ebs-gp3` (for >= 24.04)

      In the generated output, the "Value" field will have the required AMI ID. It can be used to instantiate the corresponding image using the ``ec2 run-instances`` command as explained :ref:`here <instantiate-image-on-ec2>`. 

      If you don't want to save the AMI ID before instantiating the image, you can use the ``resolve:ssm`` option and directly pass the required parameter to it in your ``ec2 run-instances`` call:

      .. code::

         aws ec2 run-instances \
            --image-id resolve:ssm:/aws/service/canonical/ubuntu/server/24.04/stable/current/amd64/hvm/ebs-gp3/ami-id \
            --key-name TestKeyPair \
            --instance-type t3.medium

   .. tab:: Using describe-images

      The EC2 ``describe-images`` API is the native AWS discovery mechanism for public AMIs. Instead of looking up a stored parameter, you query the EC2 catalog directly. By filtering on Canonical's owner ID and a name pattern, you can programmatically locate the latest Ubuntu AMI with a single AWS CLI call.

      .. tabs::
         .. tab:: EC2

            For EC2, find the latest AMI ID using:

            .. code-block::

               aws ec2 describe-images \
                  --owners 099720109477 \
                  --filters \
                     "Name=name,Values=ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-*" \
                  --query "Images | sort_by(@, &CreationDate) | [-1].ImageId" \
                  --output text

            In the filter expression, ``Name=name`` specifies that the filter should apply to the AMI's
            **Name** attribute (the human-readable AMI name string) and the ``Values=...`` part provides
            a pattern to match against this field.

            The filter pattern is:

            .. code-block::

               ubuntu/images/$VIRT_TYPE-$VOL_TYPE/ubuntu-$RELEASE-$ARCH-$PRODUCT-*

            * VIRT_TYPE: `hvm` or `pv` (only for legacy releases ≤ 16.04)
            * VOL_TYPE: `ssd-gp3` (for >=23.10), `ssd` (for <=23.04), or `instance-store`
            * RELEASE: `noble-24.04`, `jammy-22.04`, `focal-20.04`, `bionic-18.04`, or `xenial-16.04`
            * ARCH: `amd64` or `arm64`
            * PRODUCT: `server`, `server-minimal`, `pro-server` or `pro-minimal`

            The query sorts by ``CreationDate`` and selects the most recent image. In place of a wildcard(*), the serial number given to an image can also be used (e.g., 20250804):
            
            .. code-block::

               ubuntu/images/$VIRT_TYPE-$VOL_TYPE/ubuntu-$RELEASE-$ARCH-$PRODUCT-$SERIAL

         .. tab:: EKS

            For EKS, find the latest EKS AMI ID using:

            .. code-block::

               aws ec2 describe-images \
                  --owners 099720109477 \
                  --filters \
                     "Name=name,Values=ubuntu-eks/k8s_1.31/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-*" \
                  --query "Images | sort_by(@, &CreationDate) | [-1].ImageId" \
                  --output text

            In the filter expression, ``Name=name`` specifies that the filter should apply to the AMI's
            **Name** attribute (the human-readable AMI name string) and the ``Values=...`` part provides
            a pattern to match against this field.
            
            The filter pattern is:

            .. code-block::

               ubuntu-$EKS_PRODUCT/k8s_$K8S_VERSION/images/hvm-$VOL_TYPE/ubuntu-$RELEASE-$ARCH-server-*

            * EKS_PRODUCT: `eks` or `eks-pro`
            * K8S_VERSION: one of the supported EKS versions (e.g. `1.31`)
            * VOL_TYPE: `ssd` (for <= 22.04) and `ssd-gp3` (for >= 24.04)
            * RELEASE: `noble-24.04` (for EKS 1.31 or greater, or EKS Pro); `jammy-22.04` (for EKS 1.29 or greater, or EKS Pro); `focal-20.04` (for EKS <= 1.29)
            * ARCH: `amd64` or `arm64`
            

            The query sorts by ``CreationDate`` and selects the most recent image. In place of a wildcard(*), the serial number given to an image can also be used (e.g., 20250804):
            
            .. code-block::

               ubuntu-eks/k8s_$K8S_VERSION/images/hvm-$VOL_TYPE/ubuntu-$RELEASE-$ARCH-server-$SERIAL

         The generated output will be the required AMI ID if found. It can be used to instantiate the corresponding image using the ``ec2 run-instances`` command as explained :ref:`here <instantiate-image-on-ec2>`.

      If you don’t want to save the AMI ID before instantiating the image, you can embed the
      ``describe-images`` query directly in your ``ec2 run-instances`` call:

      .. code-block::

         aws ec2 run-instances \
           --image-id "$(aws ec2 describe-images \
                           --owners 099720109477 \
                           --filters \
                             'Name=name,Values=ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-*' \
                           --query 'Images | sort_by(@, &CreationDate) | [-1].ImageId' \
                           --output text)" \
           --instance-type t3.medium \
           --key-name TestKeyPair

   .. tab:: Using the AWS Console

      The AWS Management Console offers a graphical workflow to locate official Ubuntu AMIs.

      .. tabs:: 
         .. tab:: EC2
               Sign in to the `EC2 console`_.

               In the navigation pane on the left, choose :guilabel:`Images` > :guilabel:`AMIs`.
               
               From the drop-down next to the search bar, choose :guilabel:`Public images`.
               
               Apply the following two search filters:

               1. Restrict the results to Ubuntu images that Canonical publishes:

                  .. code-block:: text

                     Owner = 099720109477
               

               2. Restrict the results to images with a specific pattern in their AMI name (described later): 

                  .. code-block:: text

                     AMI name: ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server
               

               Select the most recent image based on *Creation date*.

               Choose :guilabel:`Launch instance from image` (or copy the AMI ID for CLI use).

               **AMI name filter syntax**

               ::

                  ubuntu/images/$VIRT_TYPE-$VOL_TYPE/ubuntu-$RELEASE-$ARCH-$PRODUCT

               * VIRT_TYPE: `hvm` or `pv` (only for legacy releases ≤ 16.04)
               * VOL_TYPE: `ssd-gp3` (for >=23.10), `ssd` (for <=23.04), or `instance-store`
               * RELEASE: `noble-24.04`, `jammy-22.04`, `focal-20.04`, `bionic-18.04`, or `xenial-16.04`
               * ARCH: `amd64` or `arm64`
               * PRODUCT: `server`, `server-minimal`, `pro-server` or `pro-minimal`

         .. tab:: EKS
               Sign in to the `EC2 console`_.
               
               In the left navigation pane, choose :guilabel:`Images` > :guilabel:`AMIs`.
               
               From the drop‑down next to the search bar, choose :guilabel:`Public images`.

               Apply the following two search filters:

               1. Restrict the results to Ubuntu images that Canonical publishes:

                  .. code-block:: text

                     Owner = 099720109477
               

               2. Restrict the results to images with a specific pattern in their AMI name (described later): 

                  .. code-block:: text

                     AMI name: ubuntu-eks/k8s_1.33/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64
       

               Select the most recent image based on Creation date
               
               Choose :guilabel:`Launch instance from image` (or copy the AMI ID for CLI use).

               **AMI name filter syntax**

               ::

                  ubuntu-$EKS_PRODUCT/k8s_$K8S_VERSION/images/hvm-$VOL_TYPE/ubuntu-$RELEASE-$ARCH-server

               * EKS_PRODUCT: `eks` or `eks-pro`
               * K8S_VERSION: one of the supported EKS versions (e.g. `1.31`)
               * VOL_TYPE: `ssd` (for <= 22.04) and `ssd-gp3` (for >= 24.04)
               * RELEASE: `noble-24.04` (for EKS 1.31 or greater, or EKS Pro); `jammy-22.04` (for EKS 1.29 or greater, or EKS Pro); `focal-20.04` (for EKS <= 1.29)
               * ARCH: `amd64` or `arm64`



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

You can also add Canonical's OwnerId to allow list:

.. code::

   aws ec2 modify-allowed-images --image-owner $OWNER_ID

By running the command above, you only allow Canonical Ubuntu images and ensure that instances can only be launched with verified, official images.

See the AWS announcement for more details on the `Allowed AMIs feature`_.


Images in the AWS Marketplace
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

AWS Marketplace is a digital catalog with thousands of software listings from independent software vendors that make it easy to find, test, buy, and deploy software that runs on AWS.
Canonical maintains `image listings <https://aws.amazon.com/marketplace/seller-profile?id=565feec9-3d43-413e-9760-c651546613f2>`_ for recent Ubuntu releases and special flavors (e.g. `Anbox`, `Pro`, `Pro FIPS`, `EKS`) on this marketplace.

Customers can also use the AWS Marketplace to launch and subscribe to official Ubuntu Pro images that allow users to pay for additional support.

All the above mentioned Marketplace images can also be found in the SSM parameter store:

.. code-block::

   aws ssm get-parameter --name /aws/service/marketplace/$IDENTIFIER/latest

* IDENTIFIER: use one of the following identifiers (starting with `prod-`)

**AWS Marketplace identifiers**

.. csv-table::
   :file: aws-marketplace-identifiers.csv
   :widths: 135 5 60 5
   :header-rows: 1

.. _SSM Parameter Store: https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html
.. _describe-images: https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-images.html
.. _AWS Web Console: https://aws.amazon.com/console/
.. _EC2 console: https://console.aws.amazon.com/ec2/
.. _Allowed AMIs feature: https://aws.amazon.com/about-aws/whats-new/2024/12/amazon-ec2-allowed-amis-enhance-ami-governance/


