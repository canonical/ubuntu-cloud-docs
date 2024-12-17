Import a local Ubuntu VM into AWS
==================================

This document will guide you to import local virtual machines (VMs) to AWS.
Please refer to the official `AWS Documentation: Import your VM as an image`_ for more details. 

Requirements
------------

- An AWS account
- AWS CLI installed and configured
- A virtual machine exported in Open Virtual Appliance (OVA) format. AWS also supports Virtual Machine Disk (``VMDK``), Virtual Hard Disk (``VHD/VHDX``), and raw.

.. note::
        Users running Ubuntu on KVM, OpenStack, LXD and other virtualization environments will most likely have ``qcow2`` files and not ``OVA``. Although ``qcow2`` is not supported, it is possible to use ``qemu-img`` to convert it to raw as follows: 
        
        ``sudo qemu-img convert -O raw /var/lib/libvirt/images/my-machine.qcow2 my-machine.raw``
    


Upload your OVM machine image to S3
-----------------------------------


Go to S3, create or reuse a bucket and upload the image there. Make a note of your bucket name. 

Create a containers JSON file
-----------------------------

This file (say ``containers.json``) will specify the bucket and full path to the uploaded image for a single disk machine. In case of a multiple disk machine, each disk has to be defined in this file as a separate container (for instance, separate ``VDMK`` files). If you are importing a raw image, make sure to change the format and the image URL accordingly.

.. code::

    [
          {
            "Description": "My imported Ubuntu august 2024",
            "Format": "ova",
            "Url": "s3://ubuntu-artifacts/ubuntu22.04.ova"
          }
    ]


Create an IAM role for the VM import process
--------------------------------------------


Go to IAM, create a role called ``vmimport`` and get the access key. 


In the process of creating the IAM role, you will create two files: ``role-policy.json`` and ``trust-policy.json``, as described in the AWS documentation. While ``trust-policy.json`` is used in the role creation process, ``role-policy.json`` will be used to create a policy allowing this role to read objects from the source S3 bucket and upload to the export S3 bucket.



Import the VM
-------------


.. code::

        aws ec2 import-image --description "My imported ubuntu server VM" --disk-containers "file://containers.json" --profile default --region us-east-1


This command will return a task ID (``ImportTaskId``), which can be used to check its status. The task itself will take some time since it will import, convert, launch, and create an AMI.

You can check the status with: 

.. code::

        aws ec2 describe-import-image-tasks 


Once the status says "completed", make a note of the AMI ID. It’ll be used to launch the VM.


Launch it and install AWS-specific packages
-------------------------------------------


Your machine has been imported and is ready to be launched. We recommend some final steps to include an AWS-optimized kernel for better performance and other tools for enabling services such as SSM management (``amazon-ssm-agent``), EC2 instance connect (``ec2-instance-connect``) and hibernation (``ec2-hibinit-agent``).

Launch your EC2 server using the AMI ID obtained in the previous step. This can be done using the AWS CLI or the EC2 web console. 

Ensure that you attach a security group that permits SSH access, as this will be the only method available to connect to the instance until tools like the SSM Agent or EC2 Instance Connect are installed.

To learn more about launching an instance using AWS CLI, refer to our `official documentation`_.

Once the machine is up and running, open an SSH session to your machine. If you are using Linux (including WSL on Windows) or MacOS, open a terminal window and connect to your machine using:

.. code::

        ssh -i <<YOUR_KEYPAIR>> ubuntu@<<YOUR_MACHINE_IP>>



If you are connecting from Windows, you can use PuTTy.

Install the aws kernel:

.. code::

        sudo apt update && sudo apt install linux-aws



Restart the machine.


(Optional) Install SSM agent and other tools
--------------------------------------------

.. code::

        sudo snap install amazon-ssm-agent --classic

        sudo apt-get install ec2-instance-connect ec2-hibinit-agent


Get the VM image ready for production
-------------------------------------

The VM image is almost ready to be used at scale on AWS. The last step is to allow cloud-init to reinitialize the machine ID. This ensures that each instance launched from this image will generate its own machine ID and will re-detect the cloud that  it is running on so that certain features specific to AWS can be enabled. This is also needed if you’re planning to upgrade to Ubuntu Pro in the future.

Run:

.. code::

        sudo cloud-init clean  


Your machine is now ready. You can either continue using this VM as a normal EC2 instance or create another AMI from this instance to have your final golden image, ready for production.



.. _`AWS documentation: Import your VM as an image`: https://docs.aws.amazon.com/vm-import/latest/userguide/import-vm-image.html
.. _`official documentation`: https://documentation.ubuntu.com/aws/en/latest/aws-how-to/instances/launch-ubuntu-ec2-instance/#launch-the-instance


