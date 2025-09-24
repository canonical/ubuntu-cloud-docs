Deploy an Ubuntu Pro EKS cluster - using Pro tokens
===================================================

This guide shows how to deploy an EKS cluster with Ubuntu Pro nodes using Ubuntu Pro tokens and EC2 launch templates.

Prerequisites
~~~~~~~~~~~~~

You need:

- ``eksctl``: Check the instructions to `install eksctl`_
- ``packer``: only needed if you want to enable FIPS for the cluster nodes. Install it with ``sudo snap install packer``
- your AWS access key ID and secret access key
- an Ubuntu Pro token


Prepare the cluster for deployment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Although Ubuntu Pro for EKS is available as an AMI for Ubuntu 22.04 LTS (see :doc:`deploy-ubuntu-pro-cluster-with-eks-pro-ami`), there is no such EKS related offer available for Ubuntu 20.04 LTS.
So to use Pro in 20.04 LTS, you need to provision the EKS cluster with customized Ubuntu nodes.

The steps needed for deploying the cluster depend on whether you need to enable FIPS or not.


.. tabs::

    .. group-tab:: Without FIPS
        
        When FIPS is not enabled, you can use one of the existing Ubuntu EKS AMIs and
        customize it using cloud-init's `ubuntu-advantage module`_ during deployment.

        For this deployment, you'll also need to have an existing `launch template`_ on AWS.

        **Update user-data in launch template**        
        
        On the advanced section of your launch template (user-data section), copy
        the following code (replacing the "token" field with your Pro token):

        ..  code-block:: bash

            MIME-Version: 1.0
            Content-Type: multipart/mixed; boundary="==MYBOUNDARY=="

            --==MYBOUNDARY==
            Content-Type: text/cloud-config; charset="us-ascii"
            ubuntu_advantage:
            token: <pro_token>
            enable:
            - esm
        
            --==MYBOUNDARY==
            Content-Type: text/x-shellscript; charset="us-ascii"

            #!/bin/bash
            sudo /etc/eks/bootstrap.sh procluster

            --==MYBOUNDARY==--

        Cloud-init will use this user-data to enable ESM on the cluster nodes and bootstrap the AWS EKS cluster.
      
    
    .. group-tab:: With FIPS
    
        When enabling FIPS, the most reliable way to deploy an Ubuntu Pro EKS cluster is to build a custom Ubuntu Pro AMI (with `Packer`_) and use it during cluster creation.


        **Caveats:**

        To get the latest updates and security fixes from upstream, you'll have to regularly rebuild your custom Ubuntu Pro image. Also, storing an AMI on AWS has a cost associated with it, and if required you might have to replicate it in multiple regions too.


        **Get and modify the Packer file:**

        Create an ``eks-ubuntu-fips.json`` file with the following content (replacing the
        placeholder credentials with your own in the "variables" section):

        ..  code-block:: bash

            { 
                "variables": {
                    "aws_access_key": "YOUR_IAM_ACCESS_KEY",
                    "aws_secret_key": "YOUR_IAM_SECRET_KEY",
                    "pro_token": "YOUR_PRO_TOKEN",
                    "eks_ver": "YOUR_EKS_VERSION"
                },
                "builders": [
                {
                    "type": "amazon-ebs",
                    "access_key": "{{user `aws_access_key`}}",
                    "secret_key": "{{user `aws_secret_key`}}",
                    "region": "us-east-1",
                    "instance_type": "t2.micro",
                    "ami_name": "eks{{user `eks_ver`}}-fips-ubuntu20.04-{{timestamp}}",
                    "source_ami_filter": {
                        "filters": {
                            "virtualization-type": "hvm",
                            "name": "ubuntu-eks/k8s_{{user `eks_ver`}}/images/hvm-ssd/ubuntu-focal-20.04-amd64-server-*",
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
                    "sudo apt-get update && sudo apt-get upgrade -y --with-new-pkgs"
                    ]
                },
                {
                    "type": "shell",
                    "inline": [
                    "sudo pro attach {{user `pro_token`}}",
                    "sudo pro status --wait",
                    "sudo pro enable fips --assume-yes"
                    ]
                },
                {
                    "type": "shell",
                    "inline": [
                    "sudo truncate -s 0 /etc/machine-id",
                    "sudo truncate -s 0 /var/lib/dbus/machine-id"
                    ]
                }
                ]
            }
        
        This is the file that will be used by Packer to build the custom Ubuntu Pro AMI.

        Remember that the final AMI needs to be in the same region as the EKS cluster, 
        so make sure to adjust the "region" above accordingly.
        
        This Packer file takes as a source an existing AMI of an EKS-based Ubuntu Focal
        Server for amd64. It will then launch shell commands to wait for cloud-init to
        finish and upgrade the system. Afterwards, it attaches the machine to a Pro subscription
        using your Pro token and enables FIPS. To conclude, it removes the machine-id
        from the custom image, to have a unique machine-id on every node instantiation.


        **Build the custom Ubuntu Pro AMI:**

        To build the image, run ``packer build eks-ubuntu-fips.json``.
        The resulting logs should look something like:

        .. code-block:: bash

            Build 'amazon-ebs' finished after 9 minutes 35 seconds.

            ==> Wait completed after 9 minutes 35 seconds

            ==> Builds finished. The artifacts of successful builds are:
            --> amazon-ebs: amis were created:
            us-east-1: ami-xxxxxxxx

        .. note::
            Save a copy of the provided AMI ID for the next step.


Create the ``eksctl`` config file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You're now ready to deploy the EKS cluster with Ubuntu Pro nodes.
To do so, start by creating a ``cluster.yaml`` with the following content


..  code-block:: yaml

    apiVersion: eksctl.io/v1alpha5
    kind: ClusterConfig
    metadata:
    name: procluster
    region: us-east-1
    version: 'YOUR_EKS_VERSION'


Add the following content to your file


.. tabs::

	.. group-tab:: Without FIPS

         .. code-block:: yaml

            managedNodeGroups:
            - name: ng-procluster
            desiredCapacity: 2
            launchTemplate:
              id: lt-12345
              version: "1"
                        
         This config file will allow you to create an EKS cluster using the launch template
         from above, with two nodes. 

	.. group-tab:: With FIPS

         .. code-block:: yaml

            managedNodeGroups:
            - name: ng-procluster
            instanceType: t3.small
            desiredCapacity: 2
            labels: {role: worker}
            ami: ami-xxxxx
            amiFamily: AmazonLinux2
            ssh:
                publicKeyName: yoursshkeyname
            overrideBootstrapCommand: |
                #!/bin/bash
                sudo /etc/eks/bootstrap.sh procluster
            
         This config file allows you to create a cluster using the AMI from the previous step,
         with two nodes and SSH access.

         The ``overrideBootstrapCommand`` lets you launch the bootstrap script from AWS EKS
         to initialize the nodes.


For further cluster customization check out `eksctl details`_.


Create the EKS cluster
~~~~~~~~~~~~~~~~~~~~~~

To create the EKS cluster, run ``eksctl create cluster -f cluster.yaml``
(you might need to specify the ``--profile`` option if you have multiple
profiles). When this command finishes, see the nodes with

..  code-block:: bash

    $ kubectl get nodes

    NAME                                           STATUS   ROLES    AGE     VERSION
    ip-xxx-xxx-xx-xxx.us-east-1.compute.internal   Ready    <none>   2m45s   v1.23.x
    ip-xxx-xxx-x-xx.us-east-1.compute.internal     Ready    <none>   2m45s   v1.23.x



(Optional) Verify Pro subscription
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To check that the deployed nodes have Ubuntu Pro, run:

..  code-block:: bash

    $ aws --region <region_name> ec2 describe-instances \
          --filters Name=instance-state-name,Values=running \
          --query 'Reservations[*].Instances[*].[InstanceType, LaunchTime, PlatformDetails]' 
          --output table

    ----------------------------------------------------------------
    |                       DescribeInstances                      |
    +-----------+-----------------------------+--------------------+
    |  t3.medium|  2024-05-07T19:57:33+00:00  |  Ubuntu Pro Linux  |
    |  t3.medium|  2024-05-07T19:57:33+00:00  |  Ubuntu Pro Linux  |
    +-----------+-----------------------------+--------------------+




.. _`install eksctl`: https://eksctl.io/installation/
.. _`ubuntu-advantage module`: https://cloudinit.readthedocs.io/en/latest/reference/modules.html#ubuntu-advantage
.. _`launch template`: https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html
.. _`troubleshooting options`: https://docs.aws.amazon.com/eks/latest/userguide/troubleshooting.html
.. _`Packer`: https://developer.hashicorp.com/packer
.. _`issue`: https://bugs.launchpad.net/cloud-images/+bug/2017782
.. _`eksctl details`: https://docs.aws.amazon.com/eks/latest/eksctl/what-is-eksctl.html
