How-to guides
=============

These guides provide instructions for performing different operations related to our products on AWS. They are categorized based on whether EC2 or EKS is being used. Finally, there are a couple of generic how-to guides as well.

EC2 - Launching and using Ubuntu instances
------------------------------------------

Perform tasks such as finding the right image to use and launching different types of instances.

* :doc:`Launch an instance using CLI <instances/launch-ubuntu-ec2-instance>`
* :doc:`Find images <instances/find-ubuntu-images>`
* :doc:`Launch a desktop <instances/launch-ubuntu-desktop>`
* :doc:`Launch and attest an AMD SEV-SNP instance <instances/launch-and-attest-amd-sev-snp-instances>`
* :doc:`Import a local Ubuntu VM into AWS <instances/import-local-vm-to-aws>`

Create a customized AMI and templates. 

* :doc:`Build an Ubuntu Pro AMI using Packer <instances/build-pro-ami-using-packer>`
* :doc:`Create CloudFormation templates <instances/build-cloudformation-templates>`

Install kernels and custom drivers.

* :doc:`Install 64k page kernel <instances/install-64k-kernel>`
* :doc:`Install NVIDIA drivers <instances/install-nvidia-drivers>`
* :doc:`Configure multiple NICs <instances/automatically-setup-multiple-nics>`

Perform upgrades and set up automated updates.

* :doc:`Perform in-place upgrade to Ubuntu Pro <instances/upgrade-in-place-from-lts-to-pro>`
* :doc:`Upgrade Ubuntu LTS release <instances/upgrade-ubuntu-lts-release>`
* :doc:`Upgrade to Ubuntu Pro at scale using tokens with SSM <instances/upgrade-to-ubuntu-pro-at-scale-using-tokens-with-ssm>`
* :doc:`Configure automated updates <instances/automatically-update-ubuntu-instances>`

Deploy some Canonical specific solutions.
 
* :doc:`Deploy Charmed Kubernetes <instances/deploy-charmed-kubernetes-on-ubuntu-pro>`
* :doc:`Deploy Canonical Data Science Stack <instances/data-science-stack-on-ec2>`


EKS - Using Ubuntu Pro, GPUs and Kubeflow on EKS
------------------------------------------------

If you want to use Ubuntu, enable GPUs or install Kubeflow on Amazon's EKS service, you can refer to these instructions.

* :doc:`Deploy an Ubuntu EKS cluster <kubernetes/deploy-ubuntu-cluster-with-eks-ami>`
* :doc:`Deploy an Ubuntu Pro cluster <kubernetes/deploy-ubuntu-pro-cluster-with-eks-pro-ami>`
* :doc:`Deploy an Ubuntu Pro FIPS cluster <kubernetes/deploy-ubuntu-pro-fips-cluster>`
* :doc:`Deploy a Pro cluster (with / without FIPS) using tokens <kubernetes/deploy-ubuntu-pro-cluster>`
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

.. _`Install Kubeflow on EKS (external link)`: https://documentation.ubuntu.com/charmed-kubeflow/how-to/install/install-eks/
