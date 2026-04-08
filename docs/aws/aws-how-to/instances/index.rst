.. meta::
   :description: List of how-to guides related to launching and using Ubuntu-based EC2 instances.

Using EC2
=========

These how-to guides relate to launching and using Ubuntu-based EC2 instances. They include instructions for performing different sets of tasks.

Finding images and launching instances
--------------------------------------

Guides to help you find the right Ubuntu image for your use case and launch different types of EC2 instances, including desktops, confidential computing instances, local VMs and hardened instances.

* :doc:`Launch an instance using CLI <launch-ubuntu-ec2-instance>`
* :doc:`Find images <find-ubuntu-images>`
* :doc:`Launch a desktop <launch-ubuntu-desktop>`
* :doc:`Launch and attest an AMD SEV-SNP instance <launch-and-attest-amd-sev-snp-instances>`
* :doc:`Import a local Ubuntu VM into AWS <import-local-vm-to-aws>`
* :doc:`Complete hardening of a base CIS Level 1 instance <cis-hardening>`

Creating AMIs and CloudFormation templates
------------------------------------------

Guides to help you create custom AMIs and CloudFormation templates using Ubuntu images.

* :doc:`Build an Ubuntu Pro AMI using Packer <build-pro-ami-using-packer>`
* :doc:`Create CloudFormation templates <build-cloudformation-templates>`

Custom configurations
---------------------

Guides to help you install custom kernels and drivers and configure network cards on your EC2 instances.

* :doc:`Install 64k page kernel <install-64k-kernel>`
* :doc:`Install NVIDIA drivers <install-nvidia-drivers>`
* :doc:`Configure multiple NICs <automatically-setup-multiple-nics>`

Upgrades and maintenance
------------------------

Guides to help you perform upgrades and automate them on your EC2 instances.

* :doc:`Perform in-place upgrade to Ubuntu Pro <upgrade-in-place-from-lts-to-pro>`
* :doc:`Upgrade Ubuntu LTS release <upgrade-ubuntu-lts-release>`
* :doc:`Upgrade to Ubuntu Pro at scale using tokens with SSM <upgrade-to-ubuntu-pro-at-scale-using-tokens-with-ssm>`
* :doc:`Configure automated updates <automatically-update-ubuntu-instances>`

Using Canonical Products
----------------------------

Deploy Canonical products such as the data science stack on your EC2 instances.

* :doc:`Deploy Canonical Data Science Stack <data-science-stack-on-ec2>`


.. toctree::
   :hidden:
   :maxdepth: 1
   
   Launch instance using CLI <launch-ubuntu-ec2-instance>
   Find images <find-ubuntu-images>  
   Launch a desktop <launch-ubuntu-desktop>
   Launch and attest an AMD SEV-SNP instance <launch-and-attest-amd-sev-snp-instances>
   Import a local Ubuntu VM <import-local-vm-to-aws>
   Complete hardening of a base CIS Level 1 instance  <cis-hardening>
   Build an Ubuntu Pro AMI using Packer <build-pro-ami-using-packer>
   Create CloudFormation templates <build-cloudformation-templates>
   Install 64k page kernel <install-64k-kernel>
   Install NVIDIA drivers <install-nvidia-drivers>
   Configure multiple NICs <automatically-setup-multiple-nics>
   In-place upgrade to Ubuntu Pro <upgrade-in-place-from-lts-to-pro>
   Upgrade Ubuntu LTS release <upgrade-ubuntu-lts-release>
   Upgrade to Ubuntu Pro at scale using tokens with SSM <upgrade-to-ubuntu-pro-at-scale-using-tokens-with-ssm>
   Configure automated updates <automatically-update-ubuntu-instances>
   Deploy Data Science Stack <data-science-stack-on-ec2>

