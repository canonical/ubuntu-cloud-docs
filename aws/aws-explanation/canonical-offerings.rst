Canonical's offerings on AWS
============================

Ubuntu images
-------------

**For EC2** - These are customised Amazon Machine Images (AMIs) based on an AWS-optimised kernel. They include improved device drivers and out of the box support for accelerators like GPUs. 

**For EKS** - These are optimised AMIs for running Kubernetes. They uses a slimmed-down minimal image, a custom kernel and are optimised for performance and security on EKS clusters.

`Ubuntu Pro`_ - These are premium images that include certified components, hardening options, comprehensive open source security coverage (for packages in main and universe) for 10 years, kernel Livepatch service and optional 24/7 enterprise-grade support. They are available on AMD64 and Graviton architectures.

`Ubuntu Pro FIPS`_ - These are FIPS certified images used to meet compliance requirements in production environments. These are available only through the AWS Marketplace or through private offers.



Optimised kernel
----------------

The ``linux-aws`` kernel enables the following AWS specific features:

`Elastic Fabric Adapter`_ - This allows high-performance applications to directly access the network adapter and get reliable transport with low-latency. 

`Nitro enclaves driver`_ - This gives data processing applications a secure enclave with CPU and memory isolation to prevent data leaks.

`AWS Graviton`_ - The arm64 version of the kernel includes several patches to take advantage of the unique features of AWS Graviton native CPUs.

Ubuntu Workspace
----------------

`Ubuntu Workspaces`_ are virtual Ubuntu desktops powered by AWS. Workspaces is a paid offering supported through `Amazon Workspaces`_ and the image provided for Workspaces is basically an Ubuntu Desktop running on EC2, with Ubuntu Pro services (ESM, livepatch) enabled by default.

Anbox
-----

`Anbox`_ is Android containers in the cloud. There are 2 AWS marketplace listings available to deploy Anbox directly on AWS:

* `Anbox Cloud - AMD64`_
* `Anbox Cloud - ARM64`_

.. _Elastic Fabric Adapter: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html
.. _Nitro enclaves driver: https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave.html
.. _AWS Graviton: https://docs.aws.amazon.com/whitepapers/latest/aws-graviton-performance-testing/what-is-aws-graviton.html
.. _Anbox: https://anbox-cloud.io/
.. _Anbox Cloud - AMD64: https://aws.amazon.com/marketplace/pp/prodview-3lx6xyaapstz4?
.. _Anbox Cloud - ARM64: https://aws.amazon.com/marketplace/pp/prodview-aqmdt52vqs5qk
.. _Ubuntu Pro FIPS: https://ubuntu.com/aws/fips
.. _Ubuntu Pro: https://ubuntu.com/aws/pro
.. _Amazon Workspaces: https://aws.amazon.com/workspaces
.. _Ubuntu Workspaces: https://ubuntu.com/aws/workspaces