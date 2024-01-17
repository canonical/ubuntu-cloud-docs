Canonical's offerings on AWS
============================

Standard Ubuntu images
----------------------

There are customised Amazon Machine Images (AMIs) based on an AWS-optimised kernel. They include improved device drivers
and relevant agents (eg. for `EC2 Instance Connect` and `AWS Systems Manager`). Those images are available
via the `AWS Marketplace`_ and the EC2 console.

`Ubuntu Pro images`_
--------------------

These are premium images that include certified components, hardening options, comprehensive open source security coverage (for packages in main and universe) for 10 years, `kernel Livepatch service`_ and optional 24/7 enterprise-grade support. They are available on amd64 and arm64 (Graviton) architectures, both with an optimised kernel to provide better performance while supporting nearly all instance types available. Those premium images are available via the `AWS Marketplace`_ and
also via the `EC2 console <https://ubuntu.com/blog/ubuntu-pro-is-now-part-of-the-aws-ec2-console>`__.

`Ubuntu Pro FIPS images`_
-------------------------

These are FIPS certified images used to meet compliance requirements in production environments. These are available only through the `AWS Marketplace`_ or through private offers.

Ubuntu Pro with Real-time Kernel
--------------------------------

Theses are images with an `real-time kernel <https://ubuntu.com/real-time>`_. Those images are available
via the `AWS Marketplace`_.

EKS images
----------

These are optimised AMIs for running as worker nodes with the Amazon Elastic Kubernetes Service (EKS).
They uses a slimmed-down minimal image, the AWS-optimized kernel and are optimised for performance
and security on EKS clusters. Those images do contain the required software (eg `kubelet` and `kubectl`)
to run as a Kubernetes worker node. The images are availalbe via the `AWS Marketplace`_ or the `EC2 console <https://cloud-images.ubuntu.com/docs/aws/eks/>`__.

`Ubuntu Workspaces`_
--------------------

Those are virtual Ubuntu desktops powered by AWS. Workspaces is a paid offering supported
through `Amazon Workspaces`_ and the image provided for Workspaces is basically an Ubuntu Desktop running
on EC2, with Ubuntu Pro services (ESM, livepatch) enabled by default.

`Anbox Cloud Appliance`_
------------------------

`Anbox Cloud <https://anbox-cloud.io/>`_ appliance runs Android containers in the cloud. Those images are available via the `AWS Marketplace <https://aws.amazon.com/marketplace/search/results?searchTerms=Anbox&CREATOR=565feec9-3d43-413e-9760-c651546613f2&filters=CREATOR>`__ .


`MicroK8s AWS Appliance`_
-------------------------

`MicroK8s <https://microk8s.io/>`_ is a minimal, CNCF-certified Kubernetes distribution from Canonical.
The appliance is available via the `AWS Marketplace <https://aws.amazon.com/marketplace/search/results?searchTerms=MicroK8s&CREATOR=565feec9-3d43-413e-9760-c651546613f2&filters=CREATOR>`__.

`Charmed Kubeflow on AWS`_
--------------------------

Kubeflow is an open source MLOps platform for efficient AI and ML from research through development to production.
The appliance is available via the `AWS Marketplace <https://aws.amazon.com/marketplace/search/results?searchTerms=Charmed+Kubeflow&CREATOR=565feec9-3d43-413e-9760-c651546613f2&filters=CREATOR>`__.

Optimised kernel
----------------

The ``linux-aws`` kernel used in most of the available offerings enables the following AWS specific features:

* `Elastic Fabric Adapter`_ - This allows high-performance applications to directly access the network adapter and get reliable transport with low-latency. 
* `Nitro enclaves driver`_ - This gives data processing applications a secure enclave with CPU and memory isolation to prevent data leaks.
* `AWS Graviton`_ - The arm64 version of the kernel includes several patches to take advantage of the unique features of AWS Graviton native CPUs.

.. _Elastic Fabric Adapter: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html
.. _Nitro enclaves driver: https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave.html
.. _AWS Graviton: https://docs.aws.amazon.com/whitepapers/latest/aws-graviton-performance-testing/what-is-aws-graviton.html
.. _Ubuntu Pro FIPS images: https://ubuntu.com/aws/fips
.. _Ubuntu Pro images: https://ubuntu.com/aws/pro
.. _Amazon Workspaces: https://aws.amazon.com/workspaces
.. _Ubuntu Workspaces: https://ubuntu.com/aws/workspaces
.. _kernel Livepatch service: https://ubuntu.com/security/livepatch
.. _AWS Marketplace: https://aws.amazon.com/marketplace/search/results?searchTerms=Ubuntu&CREATOR=565feec9-3d43-413e-9760-c651546613f2%2Ce6a5002c-6dd0-4d1e-8196-0a1d1857229b&filters=CREATOR

.. _Anbox Cloud Appliance: https://aws.amazon.com/marketplace/search/results?searchTerms=Anbox+Cloud+Appliance
.. _Charmed Kubeflow on AWS: https://aws.amazon.com/marketplace/pp/prodview-ssgryrrrydtds
.. _MicroK8s AWS Appliance: https://aws.amazon.com/marketplace/pp/prodview-iwqx66ka26u3w
