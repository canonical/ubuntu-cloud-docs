Launch an EC2 instance using CLI
================================

Assuming you have an existing AWS account and some means for terminal based command-line access, you can launch an EC2 instance using CLI (command-line interface). You'll need to:

* setup the required AWS credentials
* install AWS CLI
* find an appropriate Ubuntu AMI (Amazon Machine Image) and
* instantiate an instance with that AMI


Setup credentials
-----------------

You need key pairs and access keys to use AWS and EC2 services. A brief introduction to these credentials can be found in :doc:`../../aws-reference/ec2-credentials`.

Create a key pair
~~~~~~~~~~~~~~~~~

SSH key pairs are needed to log in to an EC2 instance from your local machine. To create an SSH key pair (using the AWS console, CLI or CloudFormation), follow the AWS instructions for `creating key pairs`_.

Create access keys
~~~~~~~~~~~~~~~~~~

Access keys have to be created and set up to access the various AWS services and resources. Create an access key using the :guilabel:`Access keys` tab on the *Security credentials* page of a logged in user. This page is accessible from the drop-down menu under the user's name.

#. Select :guilabel:`Create access key`
#. Choose :guilabel:`Command Line Interface (CLI)` as the *Use case*, provide the required confirmation by ticking the check-box and select :guilabel:`Next`
#. Optionally set a description tag and select :guilabel:`Create access key`
#. Save the created *Access key ID* and *Secret access key* 


Install AWS CLI
---------------

If you are running Ubuntu on your local machine, run:

.. code::

    sudo snap install aws-cli --classic

For other operating systems, follow the appropriate instructions from the `AWS documentation for installing AWS CLI`_.

Before you can start using the AWS CLI, you need to configure it by running:

.. code::

    aws configure

You'll have to enter values for each of:

.. code::

    AWS Access Key ID [None]:       
    AWS Secret Access Key [None]: 
    Default region name [None]:
    Default output format [None]: 

Use the access key details saved earlier, specify a region and choose your preferred `CLI output format`_ from one of ``json``, ``text`` or ``table``.


Find an Ubuntu AMI
------------------

To launch an EC2 instance that uses Ubuntu, you'll need to choose an appropriate Ubuntu image and get the official AMI ID for it. The image can be chosen based on your requirements, e.g. the machine's architecture, features needed from the OS, etc. Once chosen, get the corresponding AMI ID by following the instructions at :doc:`./find-ubuntu-images`.

.. note::
    
    Official Ubuntu AMIs are published by the user 'Canonical' whose Amazon ID is '099720109477'. Images containing the string 'ubuntu' but not owned by this ID are not official AMIs.


Create a security group (optional)
----------------------------------

Security groups allow you to specify firewalling rules for your instances. To understand security groups better, refer to Amazon's documentation for `EC2 security groups`_ and to create your own security group, follow the instructions for `creating a security group`_. If you don't specify any security groups when you instantiate an instance, it will be added to the default security group.


Instantiate the image
---------------------

Using the AMI ID and key pair obtained above, launch an instance by running:

.. code::

    aws ec2 run-instances --image-id <image id> --key-name <your key pair> --instance-type <instance type>

See `Amazon EC2 instance types`_ for descriptions of the available instance types, and `Amazon EC2 pricing`_ for the current pricing of instances, data transfer and storage. An example command would look like:

.. code::

    aws ec2 run-instances --image-id ami-0014ce3e52359afbd --key-name TestKeyPair --instance-type t3.medium

Check status
~~~~~~~~~~~~

To see the status of your instance, run:

.. code::

    aws ec2 describe-instances --instance-ids <your instance id>

where <your instance id> is obtained either from the output of the previous ``ec2 run-instances`` command or from the *Instances* tab of your EC2 console. 


Log in to the instance
~~~~~~~~~~~~~~~~~~~~~~

If you created a security group for your instance, modify it to allow network access for the SSH port: 

.. code::

    aws ec2 authorize-security-group-ingress --group-id <your security group id> --port 22

You can skip the above command if you launched the instance using the default security group.

Log in to the instance using:

.. code::

    ssh -i <private SSH key file> ubuntu@<external-host-name>

where <private SSH key file> is the filename of the private SSH key that corresponds to the key pair specified in the ``ec2 run-instances`` command above. The <external-host-name> can be found using the ``ec2 describe-instances`` command, in the ``PublicDnsName`` field. An example SSH command looks like:

.. code::

    ssh -i TestKeyPair.pem ubuntu@ec2-135-28-52-91.compute-1.amazonaws.com

Once you have logged in, you can set up and use the instance like any other Ubuntu machine. 

Terminate the instance
~~~~~~~~~~~~~~~~~~~~~~

You will be billed as long the instance is running, so you'll probably want to shut it down when you're done:

.. code::

    aws ec2 terminate-instances --instance -ids <instance id>



.. _`creating key pairs`: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html
.. _`AWS documentation for installing AWS CLI`: https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html
.. _`CLI output format`: https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-output-format.html
.. _`EC2 security groups`: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html
.. _`creating a security group`: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-security-groups.html#creating-security-group
.. _`Amazon EC2 instance types`: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html
.. _`Amazon EC2 pricing`: https://aws.amazon.com/ec2/pricing/on-demand/