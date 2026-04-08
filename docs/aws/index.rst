.. meta::
   :description: Discover Ubuntu on AWS, including optimized images, deployment guides, technical reference, and best practices for cloud workloads.

Ubuntu on AWS
=============


**Ubuntu on AWS is a set of customized Ubuntu images** that allow easy access to a wide range 
of products and services - offered by both Amazon Web Services (AWS) and Canonical. These images 
have an optimized kernel that boots faster, has a smaller footprint and includes AWS-specific drivers.

**These images provide a foundation for deploying cloud-based software solutions,** specifically
for software built on Ubuntu and running on AWS. They focus on providing the optimal tools 
and features needed to run specific workloads.

.. include:: ../reuse/common-intro.txt
   :start-after: Start: Product need and user
   :end-before: End: Product need and user


---------



In this documentation
---------------------

Ubuntu on AWS 
~~~~~~~~~~~~~

Canonical provides a range of optimized Ubuntu images and services tailored for AWS, backed by clear policies on security and image lifecycle management. 

.. list-table::
   :widths: 35 65

   * - **Canonical's offerings**
     - :doc:`AWS optimizations <aws-explanation/canonical-offerings>` • :doc:`Ubuntu Pro on AWS <aws-reference/pro>` • :doc:`Support options <aws-reference/support>`

   * - **Canonical's policies**
     - :doc:`Security aspects <aws-explanation/ubuntu-security-on-aws>` • :doc:`Image retention policy <aws-explanation/ec2-image-retention-policy>` • :doc:`Ubuntu on AWS Announcements <aws-reference/aws-announcements>`
     
     

Ubuntu on EC2 
~~~~~~~~~~~~~

Ubuntu on EC2 offers a flexible foundation for running cloud workloads, from launching instances and building custom AMIs to applying security hardening and managing upgrades. 

.. list-table::
   :widths: 35 65

   * - **Finding images and launching instances**
     - :doc:`EC2 credentials <aws-reference/ec2-credentials>` • :doc:`Launch an instance using CLI <aws-how-to/instances/launch-ubuntu-ec2-instance>` • :doc:`Find images <aws-how-to/instances/find-ubuntu-images>` • :doc:`Launch a desktop <aws-how-to/instances/launch-ubuntu-desktop>` • :doc:`Import a local Ubuntu VM into AWS <aws-how-to/instances/import-local-vm-to-aws>`

   * - **Creating AMIs and templates**
     - :doc:`Build an Ubuntu Pro AMI using Packer <aws-how-to/instances/build-pro-ami-using-packer>` • :doc:`Create CloudFormation templates <aws-how-to/instances/build-cloudformation-templates>` 

   * - **Custom configurations**
     - :doc:`Install 64K page kernel <aws-how-to/instances/install-64k-kernel>` • :doc:`install NVIDIA drivers <aws-how-to/instances/install-nvidia-drivers>` • :doc:`Configure multiple NICs <aws-how-to/instances/automatically-setup-multiple-nics>` • :doc:`Use UEFI secure boot and TPM <aws-how-to/security/use-secureboot-and-vtpm>` • :doc:`Launch and attest an AMD SEV-SNP instance <aws-how-to/instances/launch-and-attest-amd-sev-snp-instances>` • :doc:`Complete hardening of a base CIS Level 1 instance <aws-how-to/instances/cis-hardening>` 

   * - **Upgrades and maintenance**
     - :doc:`Perform in-place upgrade to Ubuntu Pro <aws-how-to/instances/upgrade-in-place-from-lts-to-pro>` • :doc:`Upgrade Ubuntu LTS release <aws-how-to/instances/upgrade-ubuntu-lts-release>` • :doc:`Upgrade to Ubuntu Pro at scale using tokens with SSM <aws-how-to/instances/upgrade-to-ubuntu-pro-at-scale-using-tokens-with-ssm>` •  :doc:`Configure automated updates <aws-how-to/instances/automatically-update-ubuntu-instances>`

   * - **Using Canonical products**
     - :doc:`Deploy Canonical Data Science Stack <aws-how-to/instances/data-science-stack-on-ec2>`
     

Ubuntu on EKS
~~~~~~~~~~~~~

Ubuntu on EKS provides secure, optimized worker node images for Amazon's managed Kubernetes service, with support for Ubuntu Pro, FIPS compliance, and GPU workloads. 

.. list-table::
   :widths: 35 65

   * - **Using Ubuntu AMIs for worker nodes**
     - :doc:`Deploy Ubuntu EKS cluster <aws-how-to/kubernetes/deploy-ubuntu-cluster-with-eks-ami>` • :doc:`Deploy Ubuntu Pro EKS cluster <aws-how-to/kubernetes/deploy-ubuntu-pro-cluster-with-eks-pro-ami>` • :doc:`Deploy Ubuntu Pro FIPS EKS cluster <aws-how-to/kubernetes/deploy-ubuntu-pro-fips-cluster>` 

   * - **Using pro tokens for worker nodes**
     - :doc:`Deploy Ubuntu Pro EKS cluster  <aws-how-to/kubernetes/deploy-ubuntu-pro-cluster>` •

   * - **Deploying Ubuntu node groups**
     - :doc:`Deploy self-managed node groups <aws-how-to/kubernetes/deploy-self-managed-node-group>` • :doc:`Deploy managed node groups <aws-how-to/kubernetes/deploy-managed-node-group>` 

   * - **Custom configurations**
     - :doc:`Enable GPUs on EKS <aws-how-to/kubernetes/enable-gpus-on-eks>` • `Install Kubeflow on EKS <https://documentation.ubuntu.com/charmed-kubeflow/how-to/install/install-eks/>`_ 

   * - **EKS snaps**
     - :doc:`Snap usage in EKS worker images <aws-explanation/eks-snaps>` • :doc:`EKS kubelet snap <aws-reference/eks-kubelet-snap>` 

     



How this documentation is organized
------------------------------------


This documentation uses the `Diátaxis documentation structure <https://diataxis.fr/>`__.

* :doc:`How-to guides  <aws-how-to/index>` assume you have basic familiarity with Ubuntu images on AWS and want to achieve specific goals. They are instructions covering key operations and common tasks involving the use of Ubuntu on EC2 and EKS. 

* :doc:`Reference <aws-reference/index>` includes technical information about Ubuntu on AWS, such  EC2 credentials, EKS snaps, Ubuntu Pro and the support options available on AWS.

* :doc:`Explanation <aws-explanation/index>` includes topic overviews, background and context and detailed discussion. These include key topics, such as our offerings, our image retention policy and the usage of snaps in our EKS images.

---------

Project and community
---------------------

Ubuntu on AWS is a member of the Ubuntu family and the project warmly welcomes community projects, contributions, suggestions, fixes and constructive feedback.


Get involved
~~~~~~~~~~~~

* `Get support`_
* `Join our online chat`_
* `Discuss on Matrix`_
* `Talk to us about Ubuntu on AWS`_
* :doc:`aws-how-to/contribute-to-these-docs`

If none of the above options are suitable for you, and you still want to get in touch, send us an email: aws@canonical.com.

Governance and policies
~~~~~~~~~~~~~~~~~~~~~~~
* `Code of conduct`_


.. toctree::
   :hidden:
   :maxdepth: 1

   aws-how-to/index
   aws-explanation/index
   aws-reference/index
   aws-how-to/contribute-to-these-docs


.. _Get support: https://ubuntu.com/cloud/public-cloud
.. _Join our online chat: https://discourse.ubuntu.com/c/project/aws/177
.. _`Discuss on Matrix`: https://matrix.to/#/#ubuntu-cloud:ubuntu.com
.. _Talk to us about Ubuntu on AWS: https://ubuntu.com/aws#get-in-touch
.. _Code of conduct: https://ubuntu.com/community/docs/ethos/code-of-conduct
