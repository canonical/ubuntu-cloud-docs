Launch an Ubuntu-based EC2 instance
===================================

Running Ubuntu on Amazon Web Services requires you to go through the following steps: 

1. Create AWS account
2. Setup credentials
3. Find an Ubuntu AMI
4. Create a security group (Optional)
5. Instantiate the image

Create AWS account
------------------

If you don't have AWS account, go to https://aws.amazon.com, and select :guilabel:`Sign In to the Console` on the right top corner to create. Follow the instructions given in `Create a standard alone AWS account`_ to do so.

After signing up, go to `EC2 console <https://console.aws.amazon.com/ec2/home>`_ and sign in with your account.

Setup Credentials
-----------------

To use AWS and EC2 services, you need key pairs and access keys. Setup your credentials by following instructions from :doc:`../../aws-reference/ec2-credentials`.

* Create key pairs

You need to create key pairs for SSH connection to EC2 instances. Follow instructions at `Create key pairs`_ to create key pairs with using console, AWS CLI or CloudFormation.

* Configure access keys:

To interact with AWS services, configure and set up access keys to access resources. See `Configuration and credential file settings`_ to create config file.

Find an Ubuntu AMI
------------------

To launch an EC2 instance based on an Ubuntu image, you'll need to choose the image and then get the official AMI ID for it. The image can be chosen based on your requirements (underlying architecture to be used, features needed etc.) and follow the instructions at `Find Ubuntu images on AWS`_ to get the AMI ID.

Note that official Ubuntu AMIs are published by the 'Canonical' user, with Amazon ID '099720109477'. Images containing the string 'ubuntu' but not owned by that ID are not official AMIs.

Create a security group (Optional)
----------------------------------

Security groups allow you to specify firewalling rules for your instances. To create your own security group, follow the instructions at `Create a security group`_ from `Amazon EC2 security groups for Linux instances`_. If you don't specify any security groups when you instantiate an instance, it will be added to the default security group.

Instantiate the image
---------------------

Using the key pair and AMI ID obtained above, launch an instance by running:

.. code::

    aws ec2 run-instances --image-id <image id> --key-name <your key pair> --instance-type <instance type>

See `Amazon EC2 Instance Types`_ or `Instance Families and Types`_ for descriptions of the available instance types, and `Amazon EC2 Pricing`_ for the current pricing of instances, data transfer and storage. 

To see the status of your instance, you can run the following command:

.. code::

    aws ec2 describe-instances --instance-ids <your instance id>

You can find your instance id from output by running ``ec2 run-instances`` command above or at :guilabel:`Instances` tab from EC2 console. 

In order to log in to your instance, authorise network access to ssh port security group by running:

.. code::

    aws ec2 authorize-security-group-ingress --group-id <your security group id> --port 22

If you launch instance with default security group, you can skip command above.

You may then log in to the instance using ssh:

.. code::

    ssh -i <private SSH key file> ubuntu@<external-host-name>

The <private SSH key file> is the filename of the private SSH key that corresponds to the Amazon Key Pair that you specified in the ec2-run-instances command. The <external-host-name> can be found using the ``ec2 describe-instances`` command. An example SSH command:

.. code::

    ssh -i ~/.ec2/ec2.pem ubuntu@ec2-135-28-52-91.compute-1.amazonaws.com

Once you have logged in, you may begin to set up and use the instance just like any other Ubuntu machine.

You will be billed as long the host is running, so you will probably want to shut it down when you're done. Note that each partial instance-hour consumed will be billed as a full hour.

.. code::

    aws ec2 terminate-instances --instance -ids <instance id>

.. _`Create a standard alone AWS account`: https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-creating.html
.. _`Create key pairs`: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/create-key-pairs.html
.. _`Configuration and credential file settings`: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html
.. _`Find Ubuntu images on AWS`: https://canonical-aws.readthedocs-hosted.com/en/latest/aws-how-to/instances/find-ubuntu-images/
.. _`Create a security group`: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/working-with-security-groups.html#creating-security-group
.. _`Amazon EC2 security groups for Linux instances`: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security-groups.html
.. _`Amazon EC2 Instance Types`: https://aws.amazon.com/ec2/instance-types/
.. _`Instance Families and Types`: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html
.. _`Amazon EC2 Pricing`: https://aws.amazon.com/ec2/pricing/on-demand/