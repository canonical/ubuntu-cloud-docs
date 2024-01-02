Launch an Ubuntu-based EC2 instance
===================================

To launch an Ubuntu-based EC2 instance, you need to create an AWS account with associated credentials, find an Ubuntu AMI and instantiate an instance with that AMI.

Create an AWS account
---------------------

If you don't have an AWS account, go to https://aws.amazon.com, and create one using the :guilabel:`Sign In to the Console` button on the top right corner. To do so, follow the instructions for `creating a standalone AWS account`_.

After signing up, go to the `EC2 console <https://console.aws.amazon.com/ec2/home>`_ and sign in with your account.

Setup credentials
-----------------

To use AWS and EC2 services, you need key pairs and access keys. Some details about these credentials, including where they are used and how to create them are given in a reference topic titled :doc:`../../aws-reference/ec2-credentials`.

Create key pairs
~~~~~~~~~~~~~~~~

To be able to SSH into EC2 instances, you need to create SSH key pairs. You can do that using the AWS console, CLI or CloudFormation, just follow the instructions for `creating key pairs`_  given in the AWS documentation.

Create access keys
~~~~~~~~~~~~~~~~~~

To interact with AWS services and access various resources, you need to create and set up access keys. Access keys can be created from the :guilabel:`Access keys` tab on the *Security credentials* page of a logged in user. The page is accessible from the drop-down menu under the user name. 

To create a config file for frequently used configuration settings and credentials, refer to the AWS documentation for `configuration and credential file settings`_.


Find an Ubuntu AMI
------------------

To launch an EC2 instance based on an Ubuntu image, you'll need to choose the image and get the official AMI ID for it. The image can be chosen based on your requirements such as the underlying architecture to be used, features needed etc. Then get the corresponding AMI ID by following the instructions at :doc:`./find-ubuntu-images`.

.. note::
    
    Official Ubuntu AMIs are published by the user 'Canonical' whose Amazon ID is '099720109477'. Images containing the string 'ubuntu' but not owned by this ID are not official AMIs.

Create a security group (optional)
----------------------------------

Security groups allow you to specify firewalling rules for your instances. To understand security groups better, refer to Amazon's documentation for `EC2 security groups`_ and to create your own security group, follow the instructions for `creating a security group`_. If you don't specify any security groups when you instantiate an instance, it will be added to the default security group.

Instantiate the image
---------------------

If you don't have the AWS CLI installed on your local machine, install it. Then using the key pair and AMI ID obtained above, launch an instance by running:

.. code::

    aws ec2 run-instances --image-id <image id> --key-name <your key pair> --instance-type <instance type>

See `Amazon EC2 instance types`_ for descriptions of the available instance types, and `Amazon EC2 pricing`_ for the current pricing of instances, data transfer and storage. 

Check status
~~~~~~~~~~~~

To see the status of your instance, run:

.. code::

    aws ec2 describe-instances --instance-ids <your instance id>

where *your instance id* is obtained either from the output of the previous ``ec2 run-instances`` command or from the *Instances* tab of your EC2 console. 


Log in to the instance
~~~~~~~~~~~~~~~~~~~~~~

If you created a security group for your instance, modify it to allow network access for the SSH port: 

.. code::

    aws ec2 authorize-security-group-ingress --group-id <your security group id> --port 22

You can skip the above command if you launched the instance using the default security group.

Log in to the instance using:

.. code::

    ssh -i <private SSH key file> ubuntu@<external-host-name>

where <private SSH key file> is the filename of the private SSH key that corresponds to the key pair specified in the ``ec2 run-instances`` command above. The <external-host-name> can be found using the ``ec2 describe-instances`` command. An example SSH command looks like:

.. code::

    ssh -i ~/.ec2/ec2.pem ubuntu@ec2-135-28-52-91.compute-1.amazonaws.com

Once you have logged in, you can set up and use the instance like any other Ubuntu machine. 

Terminate the instance
~~~~~~~~~~~~~~~~~~~~~~

You will be billed as long the instance is running, so you'll probably want to shut it down when you're done:

.. code::

    aws ec2 terminate-instances --instance -ids <instance id>

Note that each partial instance-hour consumed will be billed as a full hour.


.. _`creating a standalone AWS account`: https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html
.. _`creating key pairs`: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html
.. _`configuration and credential file settings`: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html
.. _`creating a security group`: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-security-groups.html#creating-security-group
.. _`EC2 security groups`: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html
.. _`Amazon EC2 instance types`: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html
.. _`Amazon EC2 pricing`: https://aws.amazon.com/ec2/pricing/on-demand/