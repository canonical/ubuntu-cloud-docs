Canonical's offerings on AWS
============================

Ubuntu images
-------------

Canonical produces a wide variety of Ubuntu images to support numerous features found on AWS.

* `Server images`_ - These are general-purpose customized Amazon Machine Images (AMIs) based on an AWS-optimized kernel. They include improved device drivers and relevant agents such as `EC2 Instance Connect` and `AWS Systems Manager`.

* `Minimal server images`_ - These are designed for automated deployment at scale and have a reduced default package set. Things like interactive usage tools are omitted. They are much smaller, boot faster, and require fewer security updates over time due to the fewer installed packages.

* `Ubuntu Pro images`_ - These are premium images that include certified components, hardening options, comprehensive open source security coverage for 10 years, `kernel Livepatch service`_ and optional `24/7 enterprise-grade support`_.

* `Ubuntu Pro FIPS images`_ - These are images built on Ubuntu Pro, but with the FIPS-certified modules pre-enabled so that they are used from the first boot of the image.

* Ubuntu Pro with `real-time kernel`_ - These are Ubuntu Pro images with a real-time kernel in them. They are used by enterprises in the automotive, industrial, and telecommunication sectors to unlock real-time compute and reduce development time by validating their code in a cloud environment.

* `Ubuntu server EKS images`_ - These are optimized AMIs that run as worker nodes in Amazon's Elastic Kubernetes Service (EKS). They include the AWS-optimized kernel, a slimmed-down minimal version of Ubuntu, and are optimized for performance and security on EKS clusters. They also come with the Kubernetes worker node related softwares such as ``kubelet`` and ``kubectl``.

* Ubuntu Pro EKS images - These are Ubuntu Pro AMIs optimized to run as worker nodes on EKS. They are similar to the Ubuntu Server EKS images, but also include all the premium features of an Ubuntu Pro image such as certified components, hardening options, kernel livepatch and expanded security maintenance.

Each of these variations have multiple versions that are released at regular intervals. For instance, untested dailies maybe published everyday, while the fully tested release versions include interim versions published every six months and long-term support (LTS) versions published every 2 years. 

The different variations and the means to find them in AWS are summarized below: 

.. list-table::

   * - **Ubuntu Image Options**
     - **AMD64**
     - **ARM64 (Graviton)** 

   * - Server 
     - EC2 console, :doc:`CLI<../aws-how-to/instances/find-ubuntu-images>`, `Marketplace <https://aws.amazon.com/marketplace/search/results?searchTerms=Ubuntu&CREATOR=565feec9-3d43-413e-9760-c651546613f2&AMI_ARCHITECTURE=x86_64&filters=CREATOR%2CAMI_ARCHITECTURE>`__
     - EC2 console, :doc:`CLI<../aws-how-to/instances/find-ubuntu-images>`, `Marketplace <https://aws.amazon.com/marketplace/search/results?searchTerms=Ubuntu&CREATOR=565feec9-3d43-413e-9760-c651546613f2&AMI_ARCHITECTURE=arm64&filters=CREATOR%2CAMI_ARCHITECTURE>`__
   
   * - Server minimal
     - :doc:`CLI<../aws-how-to/instances/find-ubuntu-images>`, `Marketplace <https://aws.amazon.com/marketplace/search/results?searchTerms=Ubuntu+minimal&CREATOR=565feec9-3d43-413e-9760-c651546613f2&AMI_ARCHITECTURE=x86_64&filters=CREATOR%2CAMI_ARCHITECTURE>`__
     - :doc:`CLI<../aws-how-to/instances/find-ubuntu-images>`, `Marketplace <https://aws.amazon.com/marketplace/search/results?searchTerms=Ubuntu+minimal&CREATOR=565feec9-3d43-413e-9760-c651546613f2&AMI_ARCHITECTURE=arm64&filters=CREATOR%2CAMI_ARCHITECTURE>`__
   
   * - Pro
     - :doc:`CLI<../aws-how-to/instances/find-ubuntu-images>`, `Marketplace <https://aws.amazon.com/marketplace/search/results?searchTerms=Ubuntu+pro&AMI_ARCHITECTURE=x86_64&CREATOR=e6a5002c-6dd0-4d1e-8196-0a1d1857229b&filters=AMI_ARCHITECTURE%2CCREATOR>`__
     - EC2 console, :doc:`CLI<../aws-how-to/instances/find-ubuntu-images>`, `Marketplace <https://aws.amazon.com/marketplace/search/results?searchTerms=Ubuntu+pro&AMI_ARCHITECTURE=arm64&CREATOR=e6a5002c-6dd0-4d1e-8196-0a1d1857229b&filters=AMI_ARCHITECTURE%2CCREATOR>`__

   * - Pro FIPS 
     - `Marketplace <https://aws.amazon.com/marketplace/search/results?searchTerms=Ubuntu+pro+fips&CREATOR=565feec9-3d43-413e-9760-c651546613f2&AMI_ARCHITECTURE=x86_64&filters=CREATOR%2CAMI_ARCHITECTURE>`__, Private offers
     - Not available

   * - Pro with Real-time kernel
     - Not available
     - `Marketplace <https://aws.amazon.com/marketplace/search/results?searchTerms=Ubuntu+pro+real&CREATOR=565feec9-3d43-413e-9760-c651546613f2&AMI_ARCHITECTURE=arm64&filters=CREATOR%2CAMI_ARCHITECTURE>`__

   * - EKS server images
     - :doc:`CLI<../aws-how-to/instances/find-ubuntu-images>`, `Marketplace <https://aws.amazon.com/marketplace/search/results?searchTerms=Ubuntu+eks&CREATOR=565feec9-3d43-413e-9760-c651546613f2&AMI_ARCHITECTURE=x86_64&filters=CREATOR%2CAMI_ARCHITECTURE>`__
     - :doc:`CLI<../aws-how-to/instances/find-ubuntu-images>`, `Marketplace <https://aws.amazon.com/marketplace/search/results?searchTerms=Ubuntu+eks&CREATOR=565feec9-3d43-413e-9760-c651546613f2&AMI_ARCHITECTURE=arm64&filters=CREATOR%2CAMI_ARCHITECTURE>`__

   * - EKS Pro images
     - :doc:`CLI<../aws-how-to/instances/find-ubuntu-images>`, `Marketplace <https://aws.amazon.com/marketplace/search/results?searchTerms=Ubuntu+Pro+eks&CREATOR=565feec9-3d43-413e-9760-c651546613f2&AMI_ARCHITECTURE=x86_64&filters=CREATOR%2CAMI_ARCHITECTURE>`__
     - :doc:`CLI<../aws-how-to/instances/find-ubuntu-images>`, `Marketplace <https://aws.amazon.com/marketplace/search/results?searchTerms=Ubuntu+Pro+eks&CREATOR=565feec9-3d43-413e-9760-c651546613f2&AMI_ARCHITECTURE=arm64&filters=CREATOR%2CAMI_ARCHITECTURE>`__

  


Optimizations for AWS
---------------------

Generally, all images use Elastic Block Storage (EBS) and hardware virtual machine (HVM) virtualization types. For Ubuntu versions 23.10 and newer, the images use `ebs-gp3 volumes`_. 

The optimized ``linux-aws`` kernel used in most of the available offerings enables specific AWS features:

* `Elastic Fabric Adapter`_ - which allows high-performance applications to directly access the network adapter and get reliable transport with low-latency. 
* `Nitro enclaves driver`_ - which gives data processing applications a secure enclave with CPU and memory isolation to prevent data leaks.
* `AWS Graviton`_ - The arm64 version of the kernel includes several patches to take advantage of the unique features of AWS Graviton native CPUs.


Appliances and paid-for offerings
---------------------------------

Ubuntu WorkSpaces
~~~~~~~~~~~~~~~~~

`Ubuntu WorkSpaces`_ are virtual Ubuntu desktops powered by AWS. WorkSpaces is a paid offering supported through `Amazon Workspaces`_ and the image provided for workspaces is basically an Ubuntu Desktop running on EC2, with Ubuntu Pro services (ESM, livepatch) enabled by default.

Anbox cloud appliance
~~~~~~~~~~~~~~~~~~~~~

The `Anbox cloud`_ appliance runs Android containers in the cloud, providing mobile development capabilities. It is available at the `AWS marketplace (Anbox cloud)`_.


MicroK8s AWS appliance
~~~~~~~~~~~~~~~~~~~~~~

`MicroK8s`_ is a minimal, CNCF-certified Kubernetes distribution from Canonical. It is available as an appliance at the `AWS marketplace (MicroK8s)`_.


Charmed Kubeflow on AWS
~~~~~~~~~~~~~~~~~~~~~~~

`Charmed Kubeflow`_ is an open-source, end-to-end, production-ready MLOps platform on top of cloud native technologies. It is available as an appliance at the `AWS marketplace (Charmed Kubeflow)`_.

.. _`Server images`: https://ubuntu.com/aws
.. _`Minimal server images`: https://wiki.ubuntu.com/Minimal
.. _`Ubuntu Pro images`: https://ubuntu.com/aws/pro
.. _`kernel Livepatch service`: https://ubuntu.com/security/livepatch
.. _`24/7 enterprise-grade support`: https://ubuntu.com/aws/support
.. _`Ubuntu Pro FIPS images`: https://ubuntu.com/aws/fips
.. _`real-time kernel`: https://ubuntu.com/real-time
.. _`Ubuntu server EKS images`: https://cloud-images.ubuntu.com/docs/aws/eks/
.. _`ebs-gp3 volumes`: https://aws.amazon.com/ebs/general-purpose/
.. _`Elastic Fabric Adapter`: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/efa.html
.. _`Nitro enclaves driver`: https://docs.aws.amazon.com/enclaves/latest/user/nitro-enclave.html
.. _`AWS Graviton`: https://aws.amazon.com/ec2/graviton/
.. _`Ubuntu WorkSpaces`: https://ubuntu.com/aws/workspaces
.. _`Amazon WorkSpaces`: https://aws.amazon.com/workspaces-family/
.. _`Anbox cloud`: https://anbox-cloud.io/ 
.. _`AWS marketplace (Anbox cloud)`: https://aws.amazon.com/marketplace/search/results?searchTerms=Anbox&CREATOR=565feec9-3d43-413e-9760-c651546613f2&filters=CREATOR
.. _`MicroK8s`: https://microk8s.io/
.. _`AWS marketplace (MicroK8s)`: https://aws.amazon.com/marketplace/pp/prodview-iwqx66ka26u3w
.. _`Charmed Kubeflow`: https://charmed-kubeflow.io/
.. _`AWS marketplace (Charmed Kubeflow)`: https://aws.amazon.com/marketplace/search/results?searchTerms=Charmed+Kubeflow&CREATOR=565feec9-3d43-413e-9760-c651546613f2&filters=CREATOR


