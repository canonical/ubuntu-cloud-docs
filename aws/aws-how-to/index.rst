How-to guides
=============

These guides provide instructions for performing different operations related to our products on AWS.

Launching and using Ubuntu instances
------------------------------------

While using Ubuntu on AWS, you'll need to perform tasks such as launching an instance, finding the right image to use, creating an AMI, installing custom drivers, doing upgrades and setting up automated updates.

* :doc:`Launch instance using CLI <instances/launch-ubuntu-ec2-instance>`
* :doc:`Find images <instances/find-ubuntu-images>`
* :doc:`In-place upgrade to Ubuntu Pro <instances/upgrade-in-place-from-lts-to-pro>`
* :doc:`Build a Pro AMI <instances/build-pro-ami-using-packer>`
* :doc:`Create CloudFormation templates <instances/build-cloudformation-templates>`
* :doc:`Launch a desktop <instances/launch-ubuntu-desktop>`
* :doc:`Configure automated updates <instances/automatically-update-ubuntu-instances>`
* :doc:`Upgrade from Focal to Jammy <instances/upgrade-from-focal-to-jammy>`
* :doc:`Install NVIDIA drivers <instances/install-nvidia-drivers>`


Using Kubernetes
----------------

If you want to use some of our products such as Ubuntu Pro and Charmed Kubernetes on Amazon's EKS service, you can refer to these instructions.

* :doc:`Deploy a Pro cluster <kubernetes/deploy-ubuntu-pro-cluster>`
* :doc:`Enable GPUs <kubernetes/enable-gpus-on-eks>`
* :doc:`Deploy Charmed K8s on Pro <kubernetes/deploy-charmed-kubernetes-on-ubuntu-pro>`


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
  
