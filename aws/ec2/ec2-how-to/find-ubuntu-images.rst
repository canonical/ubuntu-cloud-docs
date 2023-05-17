Find Ubuntu images on AWS EC2
=============================

On EC2, cloud images are referred to as Amazon Machine Images (AMIs).
Canonical produces a wide variety of images to support numerous features found on EC2:

* Generally, all images use Elastic Block Storage (EBS) and hardware virtual machine
  (HVM) virtualisation types.
  Older releases may also support paravirtual (PV) and instance-store, but users benefit
  from the newer storage and virtualisation technologies.
* Standard server images are available for both `amd64` and `arm64`; and minimal images
  are available for `amd64`.
* `Daily` (untested) and `release` versions of the images are published regularly.


Find images with SSM
--------------------
The AWS Systems Manager (SSM) agent is used by Canonical to store the latest AMI
release versions for EC2. This provides users with a programmatic method of
querying for the latest AMI ID.

Canonical stores SSM parameters under `/aws/service/canonical/`.
To find the latest AMI ID, users can use the AWS CLI:

.. code-block::

   aws ssm get-parameters --names \
       /aws/service/canonical/ubuntu/server/20.04/stable/current/amd64/hvm/ebs-gp2/ami-id

The path follows this format:

.. code-block::

   ubuntu/$PRODUCT/$RELEASE/stable/current/$ARCH/$VIRT_TYPE/$VOL_TYPE/ami-id

* PRODUCT: `server`, `server-minimal` or `pro-server`
* RELEASE: `jammy`, `22.04`, `focal`, `20.04`, `bionic`, `18.04`, `xenial`, or `16.04`
* ARCH: `amd64` or `arm64`
* VIRT_TYPE: `pv` or `hvm`
* VOL_TYPE: `ebs-gp2`, `ebs-io1`, `ebs-standard`, or `instance-store`

The serial number given to an image (e.g., `20210222`) can also be used in place of `current`:

.. code-block::
   
   ubuntu/$PRODUCT/$RELEASE/stable/$SERIAL/$ARCH/$VIRT_TYPE/$VOL_TYPE/ami-id


Find EKS images with SSM
------------------------
Amazon’s Elastic Kubernetes Service (EKS) is a managed Kubernetes service provided
by AWS that allows users to run Kubernetes applications in the cloud or on-premises.

Canonical provides minimised Ubuntu images customised for use with EKS
. These are fully tested release images that cover all Kubernetes versions
supported by the EKS service.

The latest EKS AMI ID can be found in the SSM parameter store:

.. code-block::

   aws ssm get-parameters --names /aws/service/canonical/ubuntu/eks/20.04/1.26/stable/current/amd64/hvm/ebs-gp2/ami-id

The path follows this format:

.. code-block::

   ubuntu/eks/$RELEASE/$K8S_VERSION/stable/current/$ARCH/$VIRT_TYPE/$VOL_TYPE/ami-id

Ownership verification
----------------------
By checking the `OwnerId` field of an image, users can verify that an AMI was
published by Canonical. The expected value for Canonical is one of the following:

* `099720109477` (in the default partition)
* `513442679011` (in the GovCloud partition)
* `837727238323` (in the China partition)

This value/ID is stored in SSM as the publisher-id and can be found by running:

.. code-block::

   aws ssm get-parameters --names /aws/service/canonical/meta/publisher-id

Users can then run the `describe-images` command against an AMI ID and verify
that the `OwnerId` field matches the ID returned from the above command.

.. code-block::

   aws ec2 describe-images --image-ids $AMI_ID

Note that listings on the AWS Marketplace will always show the `OwnerId` as
Amazon (e.g. `679593333241`). In these cases, users can verify the Amazon ID
and look for `aws-marketplace/ubuntu` in the `ImageLocation` field.


AWS Marketplace
---------------
AWS Marketplace is a digital catalogue with thousands of software listings
from independent software vendors that make it easy to find, test, buy, and
deploy software that runs on AWS.
Canonical maintains `image listings <https://aws.amazon.com/marketplace/seller-profile?id=565feec9-3d43-413e-9760-c651546613f2>`_ for recent Ubuntu releases and special flavors (e.g. `Anbox`, `Pro`, `Pro FIPS`, `EKS`) on this marketplace.

All the above mentioned marketplace images can also be found in the SSM parameter store:

.. code-block::

   aws ssm get-parameter --name /aws/service/marketplace/$IDENTIFIER/latest

* IDENTIFIER: use one of the following identifiers (starting with `prod-`)

AWS Marketplace identifiers
+++++++++++++++++++++++++++
.. csv-table::
   :file: aws-marketplace-identifiers.csv
   :widths: auto
   :header-rows: 1
