How-to guides
=============

These guides provide instructions for performing different operations related to our products on AWS.

EC2 - Launching and using Ubuntu instances
------------------------------------------

While using Ubuntu on AWS, you'll need to perform tasks such as launching an instance, finding the right image to use, creating an AMI, installing custom drivers, doing upgrades and setting up automated updates.

* :doc:`Launch instance using CLI <instances/launch-ubuntu-ec2-instance>`
* :doc:`Find images <instances/find-ubuntu-images>`
* :doc:`Launch a desktop <instances/launch-ubuntu-desktop>`
* :doc:`Build an Ubuntu Pro AMI <instances/build-pro-ami-using-packer>`
* :doc:`Create CloudFormation templates <instances/build-cloudformation-templates>`
* :doc:`Install NVIDIA drivers <instances/install-nvidia-drivers>`
* :doc:`Configure multiple NICs <instances/automatically-setup-multiple-nics>`
* :doc:`In-place upgrade to Ubuntu Pro <instances/upgrade-in-place-from-lts-to-pro>`
* :doc:`Upgrade from Focal to Jammy <instances/upgrade-from-focal-to-jammy>`
* :doc:`Configure automated updates <instances/automatically-update-ubuntu-instances>`


EKS - Using Kubernetes
----------------------

If you want to use some of our products such as Ubuntu Pro and Charmed Kubernetes on Amazon's EKS service, you can refer to these instructions.

* :doc:`Deploy an Ubuntu Pro cluster <kubernetes/deploy-ubuntu-pro-cluster>`
* :doc:`Enable GPUs <kubernetes/enable-gpus-on-eks>`
* :doc:`Deploy Charmed K8s on Ubuntu Pro <kubernetes/deploy-charmed-kubernetes-on-ubuntu-pro>`


Security features
-----------------

AWS provides multiple features for additional security, many of which are supported through our Ubuntu images. These guides walk you through the steps needed to use these security features.

* :doc:`Use Secure Boot and TPM <security/use-secureboot-and-vtpm>`


Contributing to the docs
------------------------

If you come across any problems with this documentation and you want to help with corrections, suggestions or new content, here's how you can do that:


* :doc:`contribute-to-these-docs`

.. toctree::
   :hidden:
   :maxdepth: 1
   
   instances/index    
   kubernetes/index
   security/index   
   contribute-to-these-docs
  
