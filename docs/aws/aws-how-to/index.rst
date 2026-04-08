.. meta::
   :description: List of how-to guides that provide instructions for performing different operations related to Ubuntu on AWS.

How-to guides
=============

These guides provide instructions for performing different operations related to our products on AWS. They are categorized based on whether EC2 or EKS is being used. Finally, there are a couple of generic how-to guides as well.

Ubuntu on EC2
--------------

Perform tasks such as finding the right image to use and launching different types of instances including desktops, confidential computing instances, local VMs and hardened instances:

* :doc:`Launch an instance using CLI <instances/launch-ubuntu-ec2-instance>`
* :doc:`Find images <instances/find-ubuntu-images>`
* :doc:`Launch a desktop <instances/launch-ubuntu-desktop>`
* :doc:`Launch and attest an AMD SEV-SNP instance <instances/launch-and-attest-amd-sev-snp-instances>`
* :doc:`Import a local Ubuntu VM into AWS <instances/import-local-vm-to-aws>`
* :doc:`Complete hardening of a base CIS Level 1 instance  <instances/cis-hardening>`

Create a customized AMI and CloudFormation templates:

* :doc:`Build an Ubuntu Pro AMI using Packer <instances/build-pro-ami-using-packer>`
* :doc:`Create CloudFormation templates <instances/build-cloudformation-templates>`

Perform custom configurations like installing custom kernels and drivers:

* :doc:`Install 64k page kernel <instances/install-64k-kernel>`
* :doc:`Install NVIDIA drivers <instances/install-nvidia-drivers>`
* :doc:`Configure multiple NICs <instances/automatically-setup-multiple-nics>`

Perform upgrades and configure automated maintenance tasks:

* :doc:`Perform in-place upgrade to Ubuntu Pro <instances/upgrade-in-place-from-lts-to-pro>`
* :doc:`Upgrade Ubuntu LTS release <instances/upgrade-ubuntu-lts-release>`
* :doc:`Upgrade to Ubuntu Pro at scale using tokens with SSM <instances/upgrade-to-ubuntu-pro-at-scale-using-tokens-with-ssm>`
* :doc:`Configure automated updates <instances/automatically-update-ubuntu-instances>`

Use Canonical specific solutions:
 
* :doc:`Deploy Canonical Data Science Stack <instances/data-science-stack-on-ec2>`


Ubuntu on EKS
--------------

If you want to use Ubuntu, enable GPUs or install Kubeflow on Amazon's EKS service, you can refer to these instructions.

Deployment options for using Ubuntu on EKS (using Ubuntu AMIs or Pro tokens):

* :doc:`Deploy an Ubuntu EKS cluster <kubernetes/deploy-ubuntu-cluster-with-eks-ami>`
* :doc:`Deploy an Ubuntu Pro EKS cluster <kubernetes/deploy-ubuntu-pro-cluster-with-eks-pro-ami>`
* :doc:`Deploy an Ubuntu Pro FIPS EKS cluster <kubernetes/deploy-ubuntu-pro-fips-cluster>`
* :doc:`Deploy a Pro cluster (with / without FIPS) using tokens <kubernetes/deploy-ubuntu-pro-cluster>`

Deployment options for node groups:

* :doc:`Deploy a self-managed Ubuntu node group <kubernetes/deploy-self-managed-node-group>`
* :doc:`Deploy managed Ubuntu node groups <kubernetes/deploy-managed-node-group>`

Custom EKS deployments:

* :doc:`Enable GPUs on EKS worker nodes <kubernetes/enable-gpus-on-eks>`
* `Install Kubeflow on EKS (external link)`_


Using security features
-----------------------

AWS provides multiple features for additional security, many of which are supported through our Ubuntu images. This guide walks you through the steps needed to use these security features.

* :doc:`Use Secure Boot and TPM <security/use-secureboot-and-vtpm>`


.. toctree::
   :hidden:
   :maxdepth: 1
   
   instances/index    
   kubernetes/index
   security/index   

.. _`Install Kubeflow on EKS (external link)`: https://documentation.ubuntu.com/charmed-kubeflow/latest/how-to/install/install-eks/
