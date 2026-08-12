.. meta::
   :description: List of how-to guides that provide instructions for performing different operations related to Ubuntu on AWS.

.. _aws-how-to-index:

How-to guides
=============

These guides provide instructions for performing different operations related to our products on AWS. They are categorized based on whether EC2 or EKS is being used. Finally, there are a couple of generic how-to guides as well.

Ubuntu on EC2
--------------

Perform tasks such as finding the right image to use and launching different types of instances including desktops, confidential computing instances, local VMs and hardened instances:

* :ref:`Launch an instance using CLI <launch-ubuntu-ec2-instance>`
* :ref:`Find images <find-ubuntu-images>`
* :ref:`Launch a desktop <launch-ubuntu-desktop>`
* :ref:`Launch and attest an AMD SEV-SNP instance <launch-and-attest-amd-sev-snp-instances>`
* :ref:`Import a local Ubuntu VM into AWS <import-local-vm-to-aws>`
* :ref:`Complete hardening of a base CIS Level 1 instance <cis_post_deploy_hardening>`

Create a customized AMI and CloudFormation templates:

* :ref:`Build an Ubuntu Pro AMI using Packer <build-pro-ami-using-packer>`
* :ref:`Build a custom Ubuntu Pro image with EC2 Image Builder <build-ubuntu-pro-image-with-ec2-image-builder>`
* :ref:`Create CloudFormation templates <build-cloudformation-templates>`

Perform custom configurations like installing custom kernels and drivers:

* :ref:`Install 64k page kernel <install-64k-kernel>`
* :ref:`Install NVIDIA drivers <install-nvidia-drivers>`
* :ref:`Configure multiple NICs <automatically-setup-multiple-nics>`

Perform upgrades and configure automated maintenance tasks:

* :ref:`Perform in-place upgrade to Ubuntu Pro <upgrade-in-place-from-lts-to-pro>`
* :ref:`Upgrade Ubuntu LTS release <upgrade-ubuntu-lts-release>`
* :ref:`Upgrade to Ubuntu Pro at scale using tokens with SSM <upgrade-to-ubuntu-pro-at-scale-using-tokens-with-ssm>`
* :ref:`Configure automated updates <automatically-update-ubuntu-instances>`

Use Canonical specific solutions:
 
* :ref:`Deploy Canonical Data Science Stack <data-science-stack-on-ec2>`


Ubuntu on EKS
--------------

If you want to use Ubuntu, enable GPUs or install Kubeflow on Amazon's EKS service, you can refer to these instructions.

Deployment options for using Ubuntu on EKS (using Ubuntu AMIs or Pro tokens):

* :ref:`Deploy an Ubuntu EKS cluster <deploy-ubuntu-cluster-with-eks-ami>`
* :ref:`Deploy an Ubuntu Pro EKS cluster <deploy-ubuntu-pro-cluster-with-eks-pro-ami>`
* :ref:`Deploy an Ubuntu Pro FIPS EKS cluster <deploy-ubuntu-pro-fips-cluster>`
* :ref:`Deploy a Pro cluster (with / without FIPS) using tokens <deploy-ubuntu-pro-cluster>`

Deployment options for node groups:

* :ref:`Deploy a self-managed Ubuntu node group <deploy-self-managed-node-group>`
* :ref:`Deploy managed Ubuntu node groups <deploy-managed-node-group>`

Custom EKS deployments:

* :ref:`Enable GPUs on EKS worker nodes <enable-gpus-on-eks>`
* `Install Kubeflow on EKS (external link)`_


Using security features
-----------------------

AWS provides multiple features for additional security, many of which are supported through our Ubuntu images. This guide walks you through the steps needed to use these security features.

* :ref:`Use Secure Boot and TPM <use-secureboot-and-vtpm>`


.. toctree::
   :hidden:
   :maxdepth: 1
   
   instances/index    
   kubernetes/index
   security/index   

.. _`Install Kubeflow on EKS (external link)`: https://documentation.ubuntu.com/charmed-kubeflow/latest/how-to/install/install-eks/
