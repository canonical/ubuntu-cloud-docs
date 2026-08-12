.. meta::
   :description: Discover Ubuntu on AWS, including optimized images, deployment guides, technical reference, and best practices for cloud workloads.

.. _index:

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
     - :ref:`AWS optimizations <canonical-offerings>` • :ref:`Ubuntu Pro on AWS <pro>` • :ref:`Support options <support>`

   * - **Canonical's policies**
     - :ref:`Security aspects <ubuntu-security-on-aws>` • :ref:`Image testing <aws-image-testing>` • :ref:`Image retention policy <ec2-image-retention-policy>` • :ref:`Ubuntu on AWS Announcements <aws-announcements>`
     
     

Ubuntu on EC2 
~~~~~~~~~~~~~

Ubuntu on EC2 offers a flexible foundation for running cloud workloads, from launching instances and building custom AMIs to applying security hardening and managing upgrades. 

.. list-table::
   :widths: 35 65

   * - **Finding images and launching instances**
     - :ref:`EC2 credentials <ec2-credentials>` • :ref:`Launch an instance using CLI <launch-ubuntu-ec2-instance>` • :ref:`Find images <find-ubuntu-images>` • :ref:`Launch a desktop <launch-ubuntu-desktop>` • :ref:`Import a local Ubuntu VM into AWS <import-local-vm-to-aws>`

   * - **Creating AMIs and templates**
     - :ref:`Build an Ubuntu Pro AMI using Packer <build-pro-ami-using-packer>` • :ref:`Build a custom Ubuntu Pro image with EC2 Image Builder <build-ubuntu-pro-image-with-ec2-image-builder>` • :ref:`Create CloudFormation templates <build-cloudformation-templates>` 

   * - **Custom configurations**
     - :ref:`Install 64K page kernel <install-64k-kernel>` • :ref:`install NVIDIA drivers <install-nvidia-drivers>` • :ref:`Configure multiple NICs <automatically-setup-multiple-nics>` • :ref:`Use UEFI secure boot and TPM <use-secureboot-and-vtpm>` • :ref:`Launch and attest an AMD SEV-SNP instance <launch-and-attest-amd-sev-snp-instances>` • :ref:`Complete hardening of a base CIS Level 1 instance <cis_post_deploy_hardening>` 

   * - **Upgrades and maintenance**
     - :ref:`Perform in-place upgrade to Ubuntu Pro <upgrade-in-place-from-lts-to-pro>` • :ref:`Upgrade Ubuntu LTS release <upgrade-ubuntu-lts-release>` • :ref:`Upgrade to Ubuntu Pro at scale using tokens with SSM <upgrade-to-ubuntu-pro-at-scale-using-tokens-with-ssm>` •  :ref:`Configure automated updates <automatically-update-ubuntu-instances>`

   * - **Using Canonical products**
     - :ref:`Deploy Canonical Data Science Stack <data-science-stack-on-ec2>`
     

Ubuntu on EKS
~~~~~~~~~~~~~

Ubuntu on EKS provides secure, optimized worker node images for Amazon's managed Kubernetes service, with support for Ubuntu Pro, FIPS compliance, and GPU workloads. 

.. list-table::
   :widths: 35 65

   * - **Using Ubuntu AMIs for worker nodes**
     - :ref:`Deploy Ubuntu EKS cluster <deploy-ubuntu-cluster-with-eks-ami>` • :ref:`Deploy Ubuntu Pro EKS cluster <deploy-ubuntu-pro-cluster-with-eks-pro-ami>` • :ref:`Deploy Ubuntu Pro FIPS EKS cluster <deploy-ubuntu-pro-fips-cluster>` 

   * - **Using pro tokens for worker nodes**
     - :ref:`Deploy Ubuntu Pro EKS cluster <deploy-ubuntu-pro-cluster>` 

   * - **Deploying Ubuntu node groups**
     - :ref:`Deploy self-managed node groups <deploy-self-managed-node-group>` • :ref:`Deploy managed node groups <deploy-managed-node-group>` 

   * - **Custom configurations**
     - :ref:`Enable GPUs on EKS <enable-gpus-on-eks>` • `Install Kubeflow on EKS <https://documentation.ubuntu.com/charmed-kubeflow/how-to/install/install-eks/>`_ 

   * - **EKS snaps**
     - :ref:`Snap usage in EKS worker images <eks-snaps>` • :ref:`EKS kubelet snap <eks-kubelet-snap>` 

     



How this documentation is organized
------------------------------------


This documentation uses the `Diátaxis documentation structure <https://diataxis.fr/>`__.

* :ref:`How-to guides <aws-how-to-index>` assume you have basic familiarity with Ubuntu images on AWS and want to achieve specific goals. They are instructions covering key operations and common tasks involving the use of Ubuntu on EC2 and EKS. 

* :ref:`Reference <aws-reference-index>` includes technical information about Ubuntu on AWS, such EC2 credentials, EKS snaps, Ubuntu Pro and the support options available on AWS.

* :ref:`Explanation <aws-explanation-index>` includes topic overviews, background and context and detailed discussion. These include key topics, such as our offerings, our image retention policy and the usage of snaps in our EKS images.

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
* :ref:`contribute-to-these-docs`

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
