Ubuntu on AWS
=============


**Ubuntu on AWS is a set of customised Ubuntu images** that allow easy access to a wide range 
of products and services - offered by both Amazon Web Services (AWS) and Canonical.

**These images provide a foundation for deploying cloud-based software solutions,** specifically
for softwares built on Ubuntu and running on AWS. They focus on providing the optimal tools 
and features needed to run specific workloads.

**The images create a stable and secure cloud platform** that is ideal for scaling development work
done on Ubuntu-based systems. Since Ubuntu is one of the most favoured operating systems amongst
developers, using an Ubuntu-based image for the corresponding cloud deployment becomes the simplest
option.

**Everyone from individual developers to large enterprises use these images** for developing and deploying
their softwares. For highly regulated industries from the government, medical and finance sectors, 
various security-certified images are also available.


----------

Canonical's offerings on AWS
----------------------------

Ubuntu images
~~~~~~~~~~~~~

..  grid:: 1 1 2 2

   ..  grid-item:: 
       **EC2 Images:** Customised Ubuntu Amazon Machine Images (AMIs) are available for Elastic Compute Cloud (EC2) instances. These AMIs are based on an AWS-optimised kernel, which includes improved device drivers and out of the box support for accelerators like GPUs. 

   ..  grid-item:: 
      **EKS Images:** Canonical works with the Elastic Kubernetes Services (EKS) team to provide an optimised Ubuntu AMI for running Kubernetes on AWS. The AMI uses a slimmed-down, minimal image, a custom kernel and is optimised for performance and security on EKS clusters.


For each Ubuntu release, multiple Ubuntu images are delivered to AWS. This could be based on the underlying architecture, required features, the storage type and the virtualisation type that is used. For example, a non-exhaustive list is:

.. list-table::
   :stub-columns: 1
  
   * - Architectures
     - AMD64
     - ARM64
   * - Image types
     - Ubuntu server
     - Ubuntu minimal
   * - Storage types
     - Instance store
     - Elastic Block Store (EBS)
   * - Virtualisation types
     - Paravirtual (PV) 
     - Hardware Virtual Machine (HVM)



Ubuntu Pro
~~~~~~~~~~
`Ubuntu Pro for AWS`_ are premium images from Canonical that includes certified components, hardening options,  comprehensive open source security coverage (for packages in main and universe) for 10 years, kernel Livepatch service and optional 24/7 enterprise-grade support. These images are available on AMD64 and Graviton architectures.


Ubuntu Pro FIPS
~~~~~~~~~~~~~~~

`Ubuntu Pro FIPS for AWS`_ are FIPS certified images created by Canonical for AWS compliance in production environments. These premium images are available only through the AWS Marketplace or through private offers.


Ubuntu Workspace
~~~~~~~~~~~~~~~~

`Ubuntu Workspaces`_ are virtual Ubuntu desktops powered by AWS. Workspaces is a paid offering supported through `Amazon Workspaces`_ and the image provided for Workspaces is basically an Ubuntu Desktop running on EC2, with Ubuntu Pro services (ESM, livepatch) enabled by default.

Anbox
~~~~~

`Anbox`_ is Android containers in the cloud. There are 2 AWS marketplace listings available to deploy Anbox directly on AWS:

* `Anbox Cloud - AMD64`_
* `Anbox Cloud - ARM64`_


---------

EKS image retention policy
--------------------------

There are multiple EKS images available for every EKS Kubernetes version (1.23, 1.24, ...). When an EKS Kubernetes version is no longer `supported by AWS <https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html>`_,
all the images for that unsupported version are deleted from the Canonical AWS account, except for the latest released one.

Say the currently available images under the Canonical AWS account are::


    ubuntu-eks/k8s_1.24/images/hvm-ssd/ubuntu-focal-20.04-arm64-server-20221214
    ubuntu-eks/k8s_1.24/images/hvm-ssd/ubuntu-focal-20.04-arm64-server-20221206.1
    ubuntu-eks/k8s_1.23/images/hvm-ssd/ubuntu-focal-20.04-arm64-server-20221214
    ubuntu-eks/k8s_1.23/images/hvm-ssd/ubuntu-focal-20.04-arm64-server-20221011
    ubuntu-eks/k8s_1.23/images/hvm-ssd/ubuntu-focal-20.04-arm64-server-20220822.2


If EKS 1.23 is no longer supported, it would result in the deletion of the following two images::

    ubuntu-eks/k8s_1.23/images/hvm-ssd/ubuntu-focal-20.04-arm64-server-20221011
    ubuntu-eks/k8s_1.23/images/hvm-ssd/ubuntu-focal-20.04-arm64-server-20220822.2

but the latest image ``ubuntu-eks/k8s_1.23/images/hvm-ssd/ubuntu-focal-20.04-arm64-server-20221214`` would still exist.


----------

How-to guides
-------------

Linked below are step-by-step guides for some key operations: finding the right Ubuntu images, deploying an EKS cluster, deploying Charmed Kubernetes on Ubuntu Pro, using UEFI Secure Boot and upgrading from Ubuntu 20.04 to 22.04.

* :doc:`./aws-how-to/find-ubuntu-images`
* :doc:`./aws-how-to/deploy-ubuntu-pro-cluster`
* :doc:`./aws-how-to/deploy-charmed-kubernetes-on-ubuntu-pro`
* :doc:`./aws-how-to/secureboot-and-vtpm`
* :doc:`./aws-how-to/upgrade-from-focal-to-jammy`

   
---------

Project and community
---------------------

Ubuntu on AWS is a member of the Ubuntu family and the project warmly welcomes community projects, contributions, 
suggestions, fixes and constructive feedback.

* `Code of conduct`_
* `Get support`_
* `Join our online chat`_
* `Talk to us about Ubuntu on AWS`_


.. toctree::
   :hidden:
   :maxdepth: 2

   aws-how-to/find-ubuntu-images
   aws-how-to/deploy-ubuntu-pro-cluster
   aws-how-to/deploy-charmed-kubernetes-on-ubuntu-pro
   aws-how-to/secureboot-and-vtpm
   aws-how-to/upgrade-from-focal-to-jammy


.. _Code of conduct: https://ubuntu.com/community/governance/code-of-conduct
.. _Get support: https://ubuntu.com/cloud/public-cloud
.. _Join our online chat: https://discourse.ubuntu.com
.. _Talk to us about Ubuntu on AWS: https://ubuntu.com/aws#get-in-touch
.. _Anbox: https://anbox-cloud.io/
.. _Anbox Cloud - AMD64: https://aws.amazon.com/marketplace/pp/prodview-3lx6xyaapstz4?
.. _Anbox Cloud - ARM64: https://aws.amazon.com/marketplace/pp/prodview-aqmdt52vqs5qk
.. _Ubuntu Pro FIPS for AWS: https://ubuntu.com/aws/fips
.. _Ubuntu Pro for AWS: https://ubuntu.com/aws/pro
.. _Amazon Workspaces: https://aws.amazon.com/workspaces
.. _Ubuntu Workspaces: https://ubuntu.com/aws/workspaces
