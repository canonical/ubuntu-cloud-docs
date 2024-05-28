Build an Ubuntu Pro AMI using Packer
====================================

This guide will provide instructions for using Packer to create your own golden image of Ubuntu Pro. You'll be able to customise your Packer template file, while keeping the the Ubuntu Pro activation mechanism intact.

We'll be using Ubuntu Pro 20.04 for this guide, but the method is equally applicable to other Pro versions.

.. note::

   * For **Ubuntu Pro FIPS**, it is better to use a pre-enabled FIPS image from the Marketplace to avoid unnecessary additional steps. 
   * For **Ubuntu LTS**, you can use this method with a small change as explained at the end of the :ref:`define-provisioners` section below. 
   * For **Ubuntu 22.04 and above** you need Packer version 1.8.1 or newer.

Basic setup
-------------

Assuming you already have an AWS account you'll need to install Packer and create your API credentials. If you need a FIPS AMI, you'll also have to subscribe to the Ubuntu Pro listing on the Marketplace.


Install Packer
~~~~~~~~~~~~~~

If you have an Ubuntu workstation, run:

.. code::

   sudo apt install packer

.. note::

   * For building images based on Ubuntu 22.04 and later, you need packer v1.8.1 or newer.
   * The version of Packer present in the Ubuntu archives on Ubuntu 22.04 LTS is v1.6.6. 
   * Packer is no longer available in the Ubuntu repositories on Ubuntu 24.04 LTS.
   * If you need a newer version, please use the appropriate `install Packer`_ instructions.

Subscribe to Ubuntu Pro (Only needed for FIPS AMI)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In the `AWS Marketplace`_ search for 'Ubuntu Pro FIPS'. Select `Ubuntu Pro FIPS 20.04 LTS`_ > :guilabel:`Continue to Subscribe` > :guilabel:`Accept Terms` and wait for the activation to complete. You only get charged when you run an instance of Ubuntu Pro.

If you skip this step and proceed with the build, you can still subscribe later when an error leads you to the Marketplace product page.



Create AWS Credentials
~~~~~~~~~~~~~~~~~~~~~~

Follow the instructions in the *Programmatic access* section of the `IAM page for creating credentials`_. For a list of the minimal set of permissions needed in your IAM user or role policy, refer to `IAM permissions needed for Packer`_.

Save your credentials, they should be similar to:

.. code::
   
   Secret: AKIAIOSFODNN7EXAMPLE
   Access_key: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY


Create a Packer template
------------------------

Our Packer template file will consist of *variables*, *builders* and *provisioners* residing at the same root level of the structure. For a deeper understanding of the structure and the key components of a Packer JSON file, refer to the `Packer website`_.

Add variables
~~~~~~~~~~~~~

Add the saved AWS credentials as *variables* to a blank ``packer.json`` file:

.. code::

   {
      "variables": {
         "aws_access_key": "YOUR_ACCESS_KEY",
         "aws_secret_key": "YOUR_SECRET_KEY"
      },
   }

Define a builder
~~~~~~~~~~~~~~~~

Add details such as image type, region, base image and owner ID in the *builders* component:

.. code::

   "builders": [
      {
        "type": "amazon-ebs",
        "access_key": "{{user `aws_access_key`}}",
        "secret_key": "{{user `aws_secret_key`}}",
        "region": "us-east-1",
        "instance_type": "t2.micro",
        "ami_name": "My-Ubuntu-Pro-20.04-{{timestamp}}",

To add the source image, we can use Packer's image search functionality - ``source_ami_filter``. To get the latest EC2 AMI with name = ubuntu-pro-server*20.04-amd64* and owner = Canonical (where * is a wildcard), use:

.. code::

   "source_ami_filter": {
      "filters": {
            "virtualization-type": "hvm",
            "name": "ubuntu-pro-server*20.04-amd64*",
            "root-device-type": "ebs"
         },
      "owners": ["099720109477"],
      "most_recent": true
   },

If you are using the FIPS listings from AWS Marketplace, then use 679593333241 as the owner ID (AWS' Marketplace ID). Finally, complete the *builders* component by adding the username that'll be used to access the instance during provisioning:

.. code::
      
        "ssh_username": "ubuntu"
      }
   ]

.. _define-provisioners:

Define provisioners
~~~~~~~~~~~~~~~~~~~

The *provisioners* component is used to specify things that have to be installed and their configuration details. This specification can be done via inline shell commands, bash scripts or even using configuration tools such as Ansible, Chef and Puppet. Some of the typical use cases that can be configured are - hardening the image, configuring Active Directory login, adding specific configurations for management and compliance, installing software and copying plain files.

Irrespective of the use-cases and tools being used, there are two sets of commands that have to be included - one at the beginning and the other at the end. These are needed to ensure the smooth functioning of Ubuntu Pro.

The first set used at the beginning includes a ``cloud-init status --wait`` command. Using an "inline shell", it will look like:

.. code::

    "provisioners": [
      {
        "type": "shell",
        "inline": [
          "cloud-init status --wait",
          "sudo apt-get update && sudo apt-get upgrade -y"
        ]
      },

This wait command will tell the script to wait for the completion of all initialisation processes, including the Ubuntu Pro activation. If you skip this command, you may face errors during the build process, since the Ubuntu Pro client needs to change configurations and repositories right after booting up.

The second set of commands are included at the end and are used to perform clean-up:

.. code::

      {
        "type": "shell",
        "inline": [
          "sudo ua detach --assume-yes",
          "sudo rm -rf /var/log/ubuntu-advantage.log",
          "sudo cloud-init clean --machine-id"
        ]
      }
    ]

These commands remove information that is specific to the instance being used to build the image, such as the machine ID and the token generated by Ubuntu Pro. Doing this ensures that a generic AMI is created, and each time you spin up a new instance from this AMI, you'll have a “fresh start” with no duplication of unique information.

The rest of your personalised scripts or provisioning tools should go in between these two sets of commands. These two sets of commands can also be included directly within your script or provisioning tool.


.. note::

   For an **Ubuntu LTS** AMI (i.e. for all non-Pro versions), you can remove the ``cloud-init status --wait`` command from the first set and exclude the second set completely. These commands are not needed since they are Pro specific. However, including them will not lead to any errors and following this guide as it is will also work fine.


Build the AMI
-------------

The complete sample ``packer.json`` looks like:

.. code::

   {
      "variables": {
         "aws_access_key": "YOURACCESSKEY",
         "aws_secret_key": "YOURSECRETKEY"
      },
      "builders": [
         {
            "type": "amazon-ebs",
            "access_key": "{{user `aws_access_key`}}",
            "secret_key": "{{user `aws_secret_key`}}",
            "region": "us-east-1",
            "instance_type": "t2.micro",
            "ami_name": "packer-base-ubuntu-{{timestamp}}",
            "source_ami_filter": {
                  "filters": {
                     "virtualization-type": "hvm",
                     "name": "ubuntu-pro-server*20.04-amd64*",
                     "root-device-type": "ebs"
                  },
               "owners": ["099720109477"],
               "most_recent": true
            },
            "ssh_username": "ubuntu"
         }
      ],
      "provisioners": [
         {
            "type": "shell",
            "inline": [
               "cloud-init status --wait",
               "sudo apt-get update && sudo apt-get upgrade -y"
            ]
         },
         {
            "type": "shell",
            "scripts": ["my_script.sh"]
         },
         {
            "type": "shell",
            "inline": [
               "sudo ua detach --assume-yes",
               "sudo rm -rf /var/log/ubuntu-advantage.log",
               "sudo cloud-init clean --machine-id"
            ]
         }
      ]
   }

Build the AMI by running Packer with the JSON file:

.. code::

   packer build packer.json

Once this process finishes, you should get the AMI ID of your newly created golden image.


Create a VM using the AMI
-------------------------

In the EC2 console, navigate to :guilabel:`Launch instance` > :guilabel:`My AMIs` and select the new AMI. Follow the wizard to configure options such as instance type, disk, security groups, roles, key-pair etc. Remember to use an instance type with the same architecture as that of the newly created AMI (AMD64 was used in this guide).

Log in to the instance and run:

.. code::

   sudo ua status --wait

The results should show that the machine is attached to a Pro subscription and has ``esm-apps``, ``esm-infra`` and ``livepatch`` enabled.



.. _`install Packer`: https://developer.hashicorp.com/packer/install
.. _`AWS Marketplace`: https://aws.amazon.com/marketplace
.. _`Ubuntu Pro FIPS 20.04 LTS`: https://aws.amazon.com/marketplace/pp/prodview-l2hkkatnodedk
.. _`IAM page for creating credentials`: https://docs.aws.amazon.com/IAM/latest/UserGuide/security-creds.html
.. _`IAM permissions needed for Packer`: https://developer.hashicorp.com/packer/integrations/hashicorp/amazon?page=builders&page=amazon#iam-task-or-instance-role
.. _`Packer website`: https://developer.hashicorp.com/packer/tutorials/aws-get-started






