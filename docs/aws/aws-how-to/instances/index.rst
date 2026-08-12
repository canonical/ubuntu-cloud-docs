.. meta::
   :description: List of how-to guides related to launching and using Ubuntu-based EC2 instances.

.. _instances-index:

Using EC2
=========

These how-to guides relate to launching and using Ubuntu-based EC2 instances. They include instructions for performing different sets of tasks.

Finding images and launching instances
--------------------------------------

Guides to help you find the right Ubuntu image for your use case and launch different types of EC2 instances, including desktops, :ref:`confidential computing <all-clouds:confidential-computing>` instances, local VMs and hardened instances.

* :ref:`Launch an instance using CLI <launch-ubuntu-ec2-instance>`
* :ref:`Find images <find-ubuntu-images>`
* :ref:`Launch a desktop <launch-ubuntu-desktop>`
* :ref:`Launch and attest an AMD SEV-SNP instance <launch-and-attest-amd-sev-snp-instances>`
* :ref:`Import a local Ubuntu VM into AWS <import-local-vm-to-aws>`
* :ref:`Complete hardening of a base CIS Level 1 instance <cis_post_deploy_hardening>`

Creating AMIs and CloudFormation templates
------------------------------------------

Guides to help you create custom AMIs and CloudFormation templates using Ubuntu images.

* :ref:`Build an Ubuntu Pro AMI using Packer <build-pro-ami-using-packer>`
* :ref:`Create CloudFormation templates <build-cloudformation-templates>`

Custom configurations
---------------------

Guides to help you install custom kernels and drivers and configure network cards on your EC2 instances.

* :ref:`Install 64k page kernel <install-64k-kernel>`
* :ref:`Install NVIDIA drivers <install-nvidia-drivers>`
* :ref:`Configure multiple NICs <automatically-setup-multiple-nics>`

Upgrades and maintenance
------------------------

Guides to help you perform upgrades and automate them on your EC2 instances.

* :ref:`Perform in-place upgrade to Ubuntu Pro <upgrade-in-place-from-lts-to-pro>`
* :ref:`Upgrade Ubuntu LTS release <upgrade-ubuntu-lts-release>`
* :ref:`Upgrade to Ubuntu Pro at scale using tokens with SSM <upgrade-to-ubuntu-pro-at-scale-using-tokens-with-ssm>`
* :ref:`Configure automated updates <automatically-update-ubuntu-instances>`

Using Canonical Products
----------------------------

Deploy Canonical products such as the data science stack on your EC2 instances.

* :ref:`Deploy Canonical Data Science Stack <data-science-stack-on-ec2>`


.. toctree::
   :hidden:
   :maxdepth: 1
   
   Launch instance using CLI <launch-ubuntu-ec2-instance>
   Find images <find-ubuntu-images>
   Launch a desktop <launch-ubuntu-desktop>
   Launch and attest an AMD SEV-SNP instance <launch-and-attest-amd-sev-snp-instances>
   Import a local Ubuntu VM <import-local-vm-to-aws>
   Complete hardening of a base CIS Level 1 instance <cis-hardening>
   Build an Ubuntu Pro AMI using Packer <build-pro-ami-using-packer>
   Build a custom Ubuntu Pro image with EC2 Image Builder <build-ubuntu-pro-image-with-ec2-image-builder>
   Create CloudFormation templates <build-cloudformation-templates>
   Install 64k page kernel <install-64k-kernel>
   Install NVIDIA drivers <install-nvidia-drivers>
   Configure multiple NICs <automatically-setup-multiple-nics>
   In-place upgrade to Ubuntu Pro <upgrade-in-place-from-lts-to-pro>
   Upgrade Ubuntu LTS release <upgrade-ubuntu-lts-release>
   Upgrade to Ubuntu Pro at scale using tokens with SSM <upgrade-to-ubuntu-pro-at-scale-using-tokens-with-ssm>
   Configure automated updates <automatically-update-ubuntu-instances>
   Deploy Data Science Stack <data-science-stack-on-ec2>

