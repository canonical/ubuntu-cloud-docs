Canonical's offerings on AWS
============================

Ubuntu images
-------------

**For EC2** - These are customised Amazon Machine Images (AMIs) based on an AWS-optimised kernel. They include improved device drivers and out of the box support for accelerators like GPUs. 

**For EKS** - These are optimised AMIs for running Kubernetes. They uses a slimmed-down minimal image, a custom kernel and are optimised for performance and security on EKS clusters.

`Ubuntu Pro images`_ - These are premium images that include certified components, hardening options, comprehensive open source security coverage (for packages in main and universe) for 10 years, kernel Livepatch service and optional 24/7 enterprise-grade support. They are available on AMD64 and Graviton architectures, both with an optimised kernel to provide better performance while supporting nearly all instance types available

`Ubuntu Pro FIPS images`_ - These are FIPS certified images used to meet compliance requirements in production environments. These are available only through the AWS Marketplace or through private offers.

Optimised kernel
----------------

The ``linux-aws`` kernel enables the following AWS specific features:

`Elastic Fabric Adapter`_ - This allows high-performance applications to directly access the network adapter and get reliable transport with low-latency. 

`Nitro enclaves driver`_ - This gives data processing applications a secure enclave with CPU and memory isolation to prevent data leaks.

`AWS Graviton`_ - The arm64 version of the kernel includes several patches to take advantage of the unique features of AWS Graviton native CPUs.

Ubuntu Workspace
----------------

`Ubuntu Workspaces`_ are virtual Ubuntu desktops powered by AWS. Workspaces is a paid offering supported through `Amazon Workspaces`_ and the image provided for Workspaces is basically an Ubuntu Desktop running on EC2, with Ubuntu Pro services (ESM, livepatch) enabled by default.

Anbox Cloud 
-----------

`Anbox Cloud`_ appliance runs Android containers in the cloud.


AWS Marketplace listings
------------------------

The different Ubuntu related options available in the AWS Marketplace are listed below:

* Ubuntu LTS server (EC2 AMI)
* `Ubuntu server minimal`_
* `Ubuntu server for EKS`_ (Minimal Ubuntu for EKS worker nodes)
* `Ubuntu Pro`_ (22.04 only in EC2 quick-start menu)
* `Ubuntu Pro FIPS`_ (Ubuntu Pro with FIPS kernel pre-enabled)
* `Ubuntu Pro with Real-time Kernel`_ (Ubuntu with Real-time kernel pre-enabled)
* `Anbox Cloud Appliance`_ (Run Android containers in the cloud)
* `Charmed Kubeflow on AWS`_ (MLOps platform for AI/ML)
* `MicroK8s Appliance for AWS`_ (minimal CNCF-certified Kubernetes distribution)
* Ubuntu Pro Desktop for Amazon Workspaces



.. _Elastic Fabric Adapter: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html
.. _Nitro enclaves driver: https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave.html
.. _AWS Graviton: https://docs.aws.amazon.com/whitepapers/latest/aws-graviton-performance-testing/what-is-aws-graviton.html
.. _Anbox Cloud: https://anbox-cloud.io/
.. _Ubuntu Pro FIPS images: https://ubuntu.com/aws/fips
.. _Ubuntu Pro images: https://ubuntu.com/aws/pro
.. _Amazon Workspaces: https://aws.amazon.com/workspaces
.. _Ubuntu Workspaces: https://ubuntu.com/aws/workspaces

.. _Ubuntu server minimal: https://aws.amazon.com/marketplace/search/results?searchTerms=minimal+ubuntu&CREATOR=565feec9-3d43-413e-9760-c651546613f2&filters=CREATOR
.. _Ubuntu server for EKS: https://aws.amazon.com/marketplace/search/results?searchTerms=Ubuntu+20.04+LTS+for+EKS&CREATOR=565feec9-3d43-413e-9760-c651546613f2&filters=CREATOR
.. _Ubuntu Pro: https://aws.amazon.com/marketplace/search/results?searchTerms=ubuntu+pro+ec2-ami&CREATOR=e6a5002c-6dd0-4d1e-8196-0a1d1857229b&filters=CREATOR
.. _Ubuntu Pro FIPS: https://aws.amazon.com/marketplace/search/results?searchTerms=ubuntu+pro+fips
.. _Ubuntu Pro with Real-time Kernel: https://aws.amazon.com/marketplace/pp/prodview-lex3tyk25g3ai
.. _Anbox Cloud Appliance: https://aws.amazon.com/marketplace/search/results?searchTerms=Anbox+Cloud+Appliance
.. _Charmed Kubeflow on AWS: https://aws.amazon.com/marketplace/pp/prodview-ssgryrrrydtds
.. _MicroK8s Appliance for AWS: https://aws.amazon.com/marketplace/pp/prodview-iwqx66ka26u3w
