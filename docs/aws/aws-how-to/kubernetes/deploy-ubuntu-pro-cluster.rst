Deploy an Ubuntu Pro EKS cluster — using Pro tokens
===================================================

This guide shows how to deploy an EKS cluster with Ubuntu Pro nodes using Ubuntu Pro tokens and EC2 launch templates.

This guide covers creating Pro clusters using tokens only. If you prefer getting a pre-activated Ubuntu Pro AMI with metered billing, please check :doc:`deploy-ubuntu-pro-cluster-with-eks-pro-ami`.

For FIPS clusters, please note that only Ubuntu 22.04 LTS has NIST-validated FIPS modules at the moment.

Prerequisites
~~~~~~~~~~~~~

- ``eksctl``: Check the instructions to `install eksctl`_
- ``Packer`` version 1.8.1 or newer installed. (`Packer installation instructions`_). Only needed if you want to enable FIPS for the cluster nodes. 
- Your AWS access key ID and secret access key
- An Ubuntu Pro token


Prepare the cluster for deployment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The steps needed for deploying the cluster depend on whether you need to enable FIPS or not.


.. tabs::

    .. group-tab:: Without FIPS
        
        When FIPS is not enabled, you can use one of the existing Ubuntu EKS AMIs and
        customize it using cloud-init's `ubuntu-pro module`_ during deployment.

        For this deployment, you'll also need to have an existing `launch template`_ on AWS.

        **Update user-data in launch template**        
        
        Go to the EC2 console and create a Launch Template for your nodes.
        This Launch Template will be used to create the Node Groups. 

        On the advanced section of your launch template (user-data section), copy
        the following code. 

        Make sure to replace the <PRO_TOKEN> field with your Pro token and <CLUSTER_NAME> with your cluster's name

        ..  code-block:: bash

            MIME-Version: 1.0
            Content-Type: multipart/mixed; boundary="==MYBOUNDARY=="

            --==MYBOUNDARY==
            Content-Type: text/cloud-config; charset="us-ascii"
            ubuntu_advantage:
            token: <PRO_TOKEN>
            enable:
            - esm
        
            --==MYBOUNDARY==
            Content-Type: text/x-shellscript; charset="us-ascii"

            #!/bin/bash
            sudo /etc/eks/bootstrap.sh <CLUSTER_NAME>

            --==MYBOUNDARY==--

        Cloud-init will use this user-data to attach an Ubuntu Pro subscription on the node and bootstrap the AWS EKS cluster.
      
    
    .. group-tab:: With FIPS
    
        When enabling FIPS mode, the most reliable way to deploy an Ubuntu Pro EKS FIPS cluster is to build a custom Ubuntu Pro FIPS AMI (with any image builder tool such as `EC2 Image Builder`_ or `Packer`_) and use it during cluster creation.


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
                    "ami_name": "eks{{user `eks_ver`}}-fips-ubuntu22.04-{{timestamp}}",
                    "source_ami_filter": {
                        "filters": {
                            "virtualization-type": "hvm",
                            "name": "ubuntu-eks/k8s_{{user `eks_ver`}}/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*",
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
                    "sudo pro enable fips-updates --assume-yes"
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
        
        Remember that the final AMI needs to be in the same region as the EKS cluster, 
        so make sure to adjust the "region" above accordingly.

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
    name: <CLUSTER_NAME>
    region: us-east-1
    version: <YOUR_EKS_VERSION>

Change <CLUSTER_NAME> and <YOUR_EKS_VERSION> accordingly. 

Note that Ubuntu 22.04 LTS (non pro) covers EKS versions up to 1.32. For newer EKS versions please use Ubuntu 24.04 LTS or use the already pre activated Pro AMIs which provide broader coverage: :doc:`deploy-ubuntu-pro-cluster-with-eks-pro-ami`).

Add the following content to your file.


.. tabs::

	.. group-tab:: Without FIPS

         .. code-block:: yaml

            managedNodeGroups:
            - name: ng-procluster
            desiredCapacity: 2
            launchTemplate:
              id: <YOUR_LAUNCH_TEMPLATE_ID>
              version: "1"
                        
         This config file will allow you to create an EKS cluster using the launch template
         from above, with two nodes. Remember to replace <YOUR_LAUNCH_TEMPLATE_ID> accordingly.

	.. group-tab:: With FIPS

         .. code-block:: yaml

            managedNodeGroups:
            - name: ng-procluster
            instanceType: t3.small
            desiredCapacity: 2
            labels: {role: worker}
            ami: <AMI_ID>
            amiFamily: Ubuntu2204
            ssh:
                publicKeyName: yoursshkeyname

            overrideBootstrapCommand: |
                #!/bin/bash
                sudo /etc/eks/bootstrap.sh <CLUSTER_NAME>
            
         Remember to change <AMI_ID> and <CLUSTER_NAME> accordingly.


For further cluster customization check out `eksctl details`_.


Create the EKS cluster
~~~~~~~~~~~~~~~~~~~~~~

To create the EKS cluster, run ``eksctl create nodegroup -f cluster.yaml``
(you might need to specify the ``--profile`` option if you have multiple
profiles). When this command finishes, see the nodes with

..  code-block:: bash

    $ kubectl get nodes

    NAME                                           STATUS   ROLES    AGE     VERSION
    ip-xxx-xxx-xx-xxx.us-east-1.compute.internal   Ready    <none>   2m45s   v1.32.x
    ip-xxx-xxx-x-xx.us-east-1.compute.internal     Ready    <none>   2m45s   v1.32.x



.. _`Packer installation instructions`: https://developer.hashicorp.com/packer/tutorials/docker-get-started/get-started-install-cli
.. _`install eksctl`: https://docs.aws.amazon.com/eks/latest/eksctl/installation.html
.. _`ubuntu-pro module`: https://docs.cloud-init.io/en/latest/reference/modules.html#ubuntu-pro
.. _`launch template`: https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html
.. _`troubleshooting options`: https://docs.aws.amazon.com/eks/latest/userguide/troubleshooting.html
.. _`EC2 Image Builder`: https://aws.amazon.com/image-builder
.. _`Packer`: https://developer.hashicorp.com/packer
.. _`issue`: https://bugs.launchpad.net/cloud-images/+bug/2017782
.. _`eksctl details`: https://docs.aws.amazon.com/eks/latest/eksctl/what-is-eksctl.html
