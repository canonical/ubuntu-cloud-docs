Deploy an EKS FIPS cluster with Ubuntu Pro
==========================================

This guide will walk you through the steps needed to get an EKS cluster running Ubuntu on FIPS mode to achieve FedRamp compliance. 

The process requires you to create your custom EKS FIPS AMI based on `recently released Ubuntu Pro for EKS`_ AMI using Packer, to then deploy it using eksctl. We will also show how to deploy a demo container that can be used to test and peek inside the cluster.

Prerequisites
~~~~~~~~~~~~~

- An AWS account
- AWS CLI installed and configured
- An access and secret key from IAM
- ``Packer`` version 1.8.1 or newer installed. Check the instructions to `install packer`_
- ``eksctl`` version 1.7.7 or newer installed. Check the instructions to `install eksctl`_
- ``Kubectl`` installed. Install it with ``sudo snap install kubectl --classic``

Step 1. Build your custom EKS AMI using ‘Ubuntu-Pro for EKS’
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a json file (say eks-fips.json) for use with Packer: 


..  code-block:: json

    {
        "variables": {
            "aws_access_key": "<<YOUR_ACCESS_KEY>>",
            "aws_secret_key": "<<YOUR_SECRET_KEY>>",
            "eks_ver": "1.29"
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
                    "name": "ubuntu-eks-pro/k8s_{{user `eks_ver`}}/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*",
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
              "sudo apt-get update && sudo apt-get upgrade -y --with-new-pkgs",
              "sudo pro enable fips-updates --assume-yes"
            ]
          },
          {
            "type": "shell",
            "inline": [
                "sudo rm -rf /var/log/ubuntu-advantage.log",
                "sudo cloud-init clean --machine-id"
            ]
          }
        ]
    }

Add further configuration details to it as required (such as specific OS configurations or additional software). 

Build your image with:

..  code-block:: bash

    packer build eks-fips.json


Once the build is complete, create your EKS FIPS cluster using eksctl as explained in 'Step 2 – alternative A'.

If you already have an EKS cluster running, create a node group and attach it to the existing cluster, as explained in 'Step 2 – alternative B'.

Step 2 – alternative A: Create a cluster with a node group with eksctl
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Define a cluster and its worker nodes (``my-fips-cluster.yaml``):


..  code-block:: yaml

    ---
    apiVersion: eksctl.io/v1alpha5
    kind: ClusterConfig

    metadata:
      name: my-cluster-fips
      region: us-east-1
      version: '1.29'

    iam:
      withOIDC: true

    nodeGroups:
      - name: ng-ubuntu-fips
        instanceType: m5.large
        desiredCapacity: 3
        amiFamily: UbuntuPro2204
        ami: <<INSERT_YOUR_EKSPRO_FIPS_AMI_ID>>
        ssh:
            allow: true
            publicKeyName: <<INSERT_YOUR_KEYPAIR_NAME>>
            enableSsm: true

        overrideBootstrapCommand: |
          #!/bin/bash
          sudo /etc/eks/bootstrap.sh my-cluster-fips


Launch the cluster using eksctl:

..  code-block:: bash

    eksctl create cluster -f my-fips-cluster.yaml


If you are using a profile, you can include it in the command:

..  code-block:: bash

    AWS_PROFILE=eks eksctl create cluster -f my-fips-cluster.yaml


The deployment may take several minutes to get ready.

For further cluster customisation check out `eksctl details`_.

Step 2 – alternative B: Create a FIPS node group and attach it to a running cluster using eksctl
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Define the node group to be deployed in a yaml file (say ``my-fips-nodegroup.yaml``):

..  code-block:: yaml

    apiVersion: eksctl.io/v1alpha5
    kind: ClusterConfig

    metadata:
      name: my-cluster-fips
      region: us-east-1

    nodeGroups:
      - name: ng-ubuntu-pro-fips
        instanceType: m5.large
        desiredCapacity: 2
        amiFamily: UbuntuPro2204
        ssh:
            allow: true
            publicKeyName: myKeyPair
            enableSsm: true

        overrideBootstrapCommand: |
          #!/bin/bash
          sudo /etc/eks/bootstrap.sh my-cluster-fips

Ensure that the correct cluster name is used, in both the metadata and the bootstrap script sections. 

Create the node group:

..  code-block:: bash
    
    eksctl create nodegroup -f my-fips-nodegroup.yaml


If you are using a profile, you can include it in the command as shown below:

..  code-block:: bash

    AWS_PROFILE=eks eksctl create nodegroup -f my-fips-nodegroup.yaml


The deployment may take several minutes to finish.


Step 3: Check if the cluster is functional
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

When eksctl is used to create an EKS cluster, it automatically configures a kubectl config file. So kubectl can be directly used to manage the cluster.

Check if the new nodes are attached to the cluster:

..  code-block:: bash

    kubectl get nodes -o wide


You should see an output similar to:

..  code-block:: bash

    NAME                             STATUS   ROLES    AGE     VERSION   INTERNAL-IP      EXTERNAL-IP      OS-IMAGE             KERNEL-VERSION         CONTAINER-RUNTIME
    ip-192-168-24-23.ec2.internal    Ready    <none>   2m17s   v1.29.3   192.168.24.23    54.224.xxx.xxx   Ubuntu 22.04.4 LTS   5.15.0-1062-aws-fips   containerd://1.7.2
    ip-192-168-60-226.ec2.internal   Ready    <none>   2m17s   v1.29.3   192.168.60.226   34.200.xxx.xxx   Ubuntu 22.04.4 LTS   5.15.0-1062-aws-fips   containerd://1.7.2

All the machines should have the ``-fips`` kernel under ``KERNEL-VERSION``.

If kubectl doesn't show any information about your cluster or just shows an error message, you can re-generate the kubectl config file (use the --profile option only if required): 

..  code-block:: bash

    aws eks update-kubeconfig --region us-east-1 --name my-cluster-fips --profile eks


(Optional) Check if the machines are running a valid Pro license
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Run:

..  code-block:: bash

    aws ec2 describe-instances --region <<YOUR_REGION>> --filters "Name=instance-state-name,Values=running" "Name=tag:eksctl.io/v1alpha2/nodegroup-name,Values=ng-ubuntu-fips" --query 'Reservations[].Instances[].[InstanceType, LaunchTime, PlatformDetails]' --output table

You should see an output similar to:

..  code-block::

    ---------------------------------------------------------------
    |                      DescribeInstances                      |
    +----------+-----------------------------+--------------------+
    |  m5.large|  2024-05-31T16:41:37+00:00  |  Ubuntu Pro Linux  |
    |  m5.large|  2024-05-31T16:41:38+00:00  |  Ubuntu Pro Linux  |
    +----------+-----------------------------+--------------------+


.. _`install eksctl`: https://eksctl.io/installation/
.. _`recently released Ubuntu Pro for EKS`: https://ubuntu.com/blog/ubuntu-pro-for-eks-is-now-generally-available
.. _`install packer`: https://developer.hashicorp.com/packer/tutorials/docker-get-started/get-started-install-cli
.. _`Packer`: https://www.packer.io/
.. _`eksctl details`: https://eksctl.io/
