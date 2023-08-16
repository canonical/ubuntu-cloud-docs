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
We provide images for:

* **EC2** - Customised Amazon Machine Images (AMIs) based on an AWS-optimised kernel. They include improved device drivers and out of the box support for accelerators like GPUs. 

* **EKS** - Optimised AMIs for running Kubernetes. They uses a slimmed-down minimal image, a custom kernel and are optimised for performance and security on EKS clusters.


For each Ubuntu release, multiple Ubuntu images are delivered to AWS. This could be based on the underlying architecture, required features, the storage type and the virtualisation type that is used:

* **architectures** - AMD64, ARM64, AWS Graviton
* **Ubuntu image types** - server, minimal
* **storage types** - instance store, Elastic Block Store (EBS)
* **virtualisation types** - Paravirtual (PV), Hardware Virtual Machine (HVM)
* **support/security compliance levels** - standard, `Ubuntu Pro`_, `Ubuntu Pro FIPS`_


Ubuntu Workspace
~~~~~~~~~~~~~~~~

`Ubuntu Workspaces`_ are virtual Ubuntu desktops powered by AWS. Workspaces is a paid offering supported through `Amazon Workspaces`_ and the image provided for Workspaces is basically an Ubuntu Desktop running on EC2, with Ubuntu Pro services (ESM, livepatch) enabled by default.

Anbox
~~~~~

`Anbox`_ is Android containers in the cloud. There are 2 AWS marketplace listings available to deploy Anbox directly on AWS:

* `Anbox Cloud - AMD64`_
* `Anbox Cloud - ARM64`_

   
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

   aws-how-to/index
   eks-image-retention-policy


.. _Code of conduct: https://ubuntu.com/community/governance/code-of-conduct
.. _Get support: https://ubuntu.com/cloud/public-cloud
.. _Join our online chat: https://discourse.ubuntu.com
.. _Talk to us about Ubuntu on AWS: https://ubuntu.com/aws#get-in-touch
.. _Anbox: https://anbox-cloud.io/
.. _Anbox Cloud - AMD64: https://aws.amazon.com/marketplace/pp/prodview-3lx6xyaapstz4?
.. _Anbox Cloud - ARM64: https://aws.amazon.com/marketplace/pp/prodview-aqmdt52vqs5qk
.. _Ubuntu Pro FIPS: https://ubuntu.com/aws/fips
.. _Ubuntu Pro: https://ubuntu.com/aws/pro
.. _Amazon Workspaces: https://aws.amazon.com/workspaces
.. _Ubuntu Workspaces: https://ubuntu.com/aws/workspaces
