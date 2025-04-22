Using EC2
=========

These how-to guides relate to launching and using Ubuntu-based EC2 instances. They include instructions for performing different sets of tasks.

Launching different types of instances and finding the right image to use:

* :doc:`Launch an instance using CLI <launch-ubuntu-ec2-instance>`
* :doc:`Find images <find-ubuntu-images>`
* :doc:`Launch a desktop <launch-ubuntu-desktop>`
* :doc:`Launch and attest an AMD SEV-SNP instance <launch-and-attest-amd-sev-snp-instances>`
* :doc:`Import a local Ubuntu VM into AWS <import-local-vm-to-aws>`

Creating AMIs and CloudFormation templates:

* :doc:`Build an Ubuntu Pro AMI using Packer <build-pro-ami-using-packer>`
* :doc:`Create CloudFormation templates <build-cloudformation-templates>`

Installing custom drivers and configuring network cards:

* :doc:`Install NVIDIA drivers <install-nvidia-drivers>`
* :doc:`Configure multiple NICs <automatically-setup-multiple-nics>`

Performing upgrades and automating them:

* :doc:`Perform in-place upgrade to Ubuntu Pro <upgrade-in-place-from-lts-to-pro>`
* :doc:`Upgrade from Focal to Jammy <upgrade-from-focal-to-jammy>`
* :doc:`Upgrade to Ubuntu Pro at scale using tokens with SSM <upgrade-to-ubuntu-pro-at-scale-using-tokens-with-ssm>`
* :doc:`Configure automated updates <automatically-update-ubuntu-instances>`

Deploying Canonical Products:

* :doc:`Deploy Charmed Kubernetes <deploy-charmed-kubernetes-on-ubuntu-pro>`
* :doc:`Deploy Canonical Data Science Stack <data-science-stack-on-ec2>`


.. toctree::
   :hidden:
   :maxdepth: 1
   
   Launch instance using CLI <launch-ubuntu-ec2-instance>
   Find images <find-ubuntu-images>  
   Launch a desktop <launch-ubuntu-desktop>
   Launch and attest an AMD SEV-SNP instance <launch-and-attest-amd-sev-snp-instances>
   Import a local Ubuntu VM <import-local-vm-to-aws>
   Build an Ubuntu Pro AMI using Packer <build-pro-ami-using-packer>
   Create CloudFormation templates <build-cloudformation-templates>
   Install NVIDIA drivers <install-nvidia-drivers>
   Configure multiple NICs <automatically-setup-multiple-nics>
   In-place upgrade to Ubuntu Pro <upgrade-in-place-from-lts-to-pro>
   Upgrade from Focal to Jammy <upgrade-from-focal-to-jammy>
   Upgrade to Ubuntu Pro at scale using tokens with SSM <upgrade-to-ubuntu-pro-at-scale-using-tokens-with-ssm>
   Configure automated updates <automatically-update-ubuntu-instances>
   Deploy Charmed Kubernetes <deploy-charmed-kubernetes-on-ubuntu-pro>
   Deploy Data Science Stack <data-science-stack-on-ec2>

