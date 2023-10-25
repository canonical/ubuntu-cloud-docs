Create CloudFormation templates with the latest Ubuntu AMI
==========================================================

While launching instances using `CloudFormation templates`_, it is a common practice to map hard-coded AMI IDs with their respective regions.  While this solves the problem of having a unique AMI ID per region, it does not help with getting the latest AMI for a given Ubuntu version.

If you are using an old AMI, the update & upgrade process during boot-up takes time and it might even result in a reboot. Using the latest AMI avoids this process, resulting in faster boot times and lesser reboots.


Get the latest AMI ID
---------------------

You can query the SSM parameter store to get the latest AMI IDs. Each AMI has its own parameter store namespace which returns the regional image ID when queried. Once you know the query string for the namespace (the 'Default' value in the subsections below), the process is the same for different Ubuntu versions.


Ubuntu LTS
~~~~~~~~~~

In the *Parameters* section of your CloudFormation template, add:

.. code::

       LatestAmiId:
                Type: 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
                Default: '/aws/service/canonical/ubuntu/server/jammy/stable/current/amd64/hvm/ebs-gp2/ami-id'

The Ubuntu version (e.g. jammy, focal, bionic) and the architecture (ARM64 or AMD64) can be changed as required. In the *Resources* section, this parameter can be accessed as:

.. code::

       MyInstance:
            Type: AWS::EC2::Instance
            Properties:
                  ImageId: !Ref LatestAmiId


Ubuntu Pro
~~~~~~~~~~

Change the query string to:

.. code::

       LatestAmiId:
                Type: 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
                Default: '/aws/service/canonical/ubuntu/pro-server/jammy/stable/current/amd64/hvm/ebs-gp2/ami-id'


Ubuntu Pro FIPS
~~~~~~~~~~~~~~~

Since Ubuntu Pro FIPS is only available at the AWS Marketplace, the product ID needs to be chosen from:

.. list-table::
   :header-rows: 1
   :align: center

   * - **NAME**
     - **ARCHITECTURE**
     - **IDENTIFIER**
   * - Ubuntu Pro FIPS 16.04 LTS
     - amd64
     - ``prod-hykkbajyverq4``
   * - Ubuntu Pro FIPS 18.04 LTS
     - amd64
     - ``prod-7izp2xqnddwdc``
   * - Ubuntu Pro FIPS 20.04 LTS
     - amd64
     - ``prod-k6fgbnayirmrc``

To create the parameter in your CloudFormation template, choose a product ID from above and use it in place of <product-id> in:

.. code::

       LatestAmiId:
                Type: 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
                Default: '/aws/service/marketplace/<product-id>/latest'

.. note::

   Before launching any Marketplace product you'll have to subscribe to it, even if it is free of charge.


Ubuntu LTS for EKS
~~~~~~~~~~~~~~~~~~

For Ubuntu-EKS AMI IDs, use the following query string with any required changes to Ubuntu version, EKS version and architecture:

.. code::

       LatestAmiId:
                Type: 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
                Default: '/aws/service/canonical/ubuntu/eks/20.04/1.23/stable/current/amd64/hvm/ebs-gp2/ami-id'


Create template
---------------

A very basic CloudFormation template for Ubuntu LTS could look like:

.. code::

   AWSTemplateFormatVersion: 2010-09-09
   Description: Launch EC2 instance with the latest Ubuntu AMI

   Parameters:
      AvailabilityZone:
         Type: AWS::EC2::AvailabilityZone::Name
      LatestAmiId:
                  Type: 'AWS::SSM::Parameter::Value<AWS::EC2::Image::Id>'
                  Default: '/aws/service/canonical/ubuntu/server/jammy/stable/current/amd64/hvm/ebs-gp2/ami-id'
      KeyPair:
         Description: Amazon EC2 Key Pair used to ssh to the cluster nodes
         Type: "AWS::EC2::KeyPair::KeyName"
      InstanceType:
         Type: String
         Default: t2.micro
         AllowedValues:
               - t2.micro
               - t2.medium
               - t2.large
               - t2.xlarge
               - t2.2xlarge

   Resources:
      MyInstance:
         Type: AWS::EC2::Instance
         Properties:
               ImageId: !Ref LatestAmiId
               InstanceType: !Ref InstanceType
               AvailabilityZone: !Ref AvailabilityZone
               KeyName: !Ref KeyPair
               SecurityGroupIds:
                  - !Ref MyBasicSecurityGroup

      MyBasicSecurityGroup:
         Type: AWS::EC2::SecurityGroup
         Properties:
               GroupName: "A very basic Security group"
               GroupDescription: "Allows SSH inbound traffic"
               SecurityGroupIngress:
                  - IpProtocol: tcp
                     FromPort: 22
                     ToPort: 22
                     CidrIp: 0.0.0.0/0

   Outputs:
      InstanceIP:
         Value: !GetAtt MyInstance.PublicIp
         Description: Instance public IP


Further references
------------------

* :ref:`Find Ubuntu images on AWS`
* `AWS reference for SSM based querying of latest AMI IDs`_
* `AWS reference for integrating CloudFormation with SSM parameter store`_

.. _`CloudFormation templates`: https://aws.amazon.com/cloudformation/resources/templates/
.. _`AWS reference for SSM based querying of latest AMI IDs`: https://aws.amazon.com/blogs/compute/query-for-the-latest-amazon-linux-ami-ids-using-aws-systems-manager-parameter-store/
.. _`AWS reference for integrating CloudFormation with SSM parameter store`: https://aws.amazon.com/blogs/mt/integrating-aws-cloudformation-with-aws-systems-manager-parameter-store/
