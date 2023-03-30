Deploy an Ubuntu Pro EKS cluster
================================

This guide shows how to deploy a Ubuntu Pro EKS Cluster. Depending on whether you need to enable FIPS for your cluster nodes, you only need to follow one of the following two sections.

Prerequisites
~~~~~~~~~~~~~

You need:

- ``eksctl``: see how to install it `here <https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html>`_
- ``packer``: needed if you want to enable FIPS for the cluster nodes ``sudo snap install packer``
- your AWS access key ID and secret access key
- an Ubuntu Pro token

With FIPS
~~~~~~~~~

Why Packer?
***********

We use Packer because to enable FIPS, you need to reboot the node. Packer permits to create a golden AMI to avoid the node being flagged as defective.
 
What are the limitations/caveats of Packer
******************************************

You must rebuild your image to have the latest software versions (including security fixes). Also, storing AMI has a cost on AWS, and you will need to replicate it to multiple regions if you need to.

Get and modify the Packer file
******************************

Create an eks-ubuntu-fips.json file and copy the code below

..  code-block:: bash

    {
        "variables": {
            "aws_access_key": "YOUR_IAM_ACCESS_KEY",
            "aws_secret_key": "YOUR_IAM_SECRET_KEY",
            "ua_token": "YOUR UBUNTU.COM/ADVANTAGE TOKEN",
            "eks_ver": "1.23"
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
            "sudo ua attach {{user `ua_token`}}",
            "sudo ua status --wait",
            "sudo ua enable fips --assume-yes"
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

We will use it with Packer to build our AMI, add your information in the variable section, and modify the source AMI region if needed. Remember that our final AMI needs to be in the same region where you want your cluster.

This Packer file takes as a source an AMI of Ubuntu Focal Server amd64 EKS. After that, he launches shell commands to wait for cloud-init to finish and upgrade the package. After that, he attaches your Pro token with the AMI and enables FIPS. To conclude, he removes the machine-id to have a unique machine-id by node.

Build your AMI
**************

To build your AMI image, do ``packer build eks-ubuntu-fips.json``. At the end of the command, you have crucial logs:

..  code-block:: bash

    Build 'amazon-ebs' finished after 9 minutes 35 seconds.

    ==> Wait completed after 9 minutes 35 seconds

    ==> Builds finished. The artifacts of successful builds are:
    --> amazon-ebs: amis were created:
    us-east-1: ami-xxxxxxx

Create the config file
**********************

So to create your cluster with your custom AMI, create a cluster.yaml file and copy this code

..  code-block:: yaml

    apiVersion: eksctl.io/v1alpha5
    kind: ClusterConfig
    metadata:
    name: procluster
    region: us-east-1
    version: '1.23'
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

This config file permits you to create a cluster using the AMI you created with two nodes and ssh into the node using your ssh key name. The overrideBootstrapCommand permit to launch the bootstrap script of AWS EKS to initialize the nodes. To customize your cluster more, check `here <https://eksctl.io/>`_.


Without FIPS
~~~~~~~~~~~~

We use the `ubuntu-advantage module <https://cloudinit.readthedocs.io/en/latest/reference/modules.html#ubuntu-advantage>`_ from cloud-init. You also need to have a LaunchTemplate existing on AWS.

LaunchTemplate user-data
************************

On the advanced section of your LaunchTemplate (user-data section), copy this code

..  code-block:: bash

    MIME-Version: 1.0
    Content-Type: multipart/mixed; boundary="==MYBOUNDARY=="

    --==MYBOUNDARY==
    Content-Type: text/cloud-config; charset="us-ascii"
    ubuntu_advantage:
    token: <ua_contract_token>
    enable:
    - esm
  
    --==MYBOUNDARY==
    Content-Type: text/x-shellscript; charset="us-ascii"

    #!/bin/bash
    sudo /etc/eks/bootstrap.sh <name_of_the_cluster>

    --==MYBOUNDARY==--

So, this user-data permits you to enable ESM on your nodes. The shell command launches the bootstrap script of AWS EKS to initialize the nodes.

Create the config file
**********************

So to create your cluster with your custom LaunchTemplate, create a cluster.yaml file and copy this code

..  code-block:: yaml

    apiVersion: eksctl.io/v1alpha5
    kind: ClusterConfig

    metadata:
    name: procluster
    region: us-east-1
    version: '1.23'

    managedNodeGroups:
    - name: ng-procluster
      desiredCapacity: 2
      launchTemplate:
        id: lt-12345
        version: "1"
        
So, this config file permits you to create a cluster using the LaunchTemplate you created with two nodes. To customize your cluster more, check `here <https://eksctl.io/>`_.


Create the cluster
~~~~~~~~~~~~~~~~~~

To create the cluster, do ``eksctl create cluster --profile default -f cluster.yaml``. When this command finishes, see the nodes with

..  code-block:: bash

    $ kubectl get nodes

    NAME                                           STATUS   ROLES    AGE     VERSION
    ip-xxx-xxx-xx-xxx.us-east-1.compute.internal   Ready    <none>   2m45s   v1.23.x
    ip-xxx-xxx-x-xx.us-east-1.compute.internal     Ready    <none>   2m45s   v1.23.x



So now check if your nodes have Ubuntu Pro and, if the services are enabled, ssh into a node with this command ( get the external IP of your node with ``kubectl get nodes -o wide``):

..  code-block:: bash

    $ ssh -i yoursshkeyname.pem ubuntu@external_ip_of_node
    $ pro status

    SERVICE          ENTITLED  STATUS    DESCRIPTION
    esm-apps         yes       enabled   Expanded Security Maintenance for Applications
    esm-infra        yes       enabled   Expanded Security Maintenance for Infrastructure
    fips             yes       enabled   NIST-certified core packages
    fips-updates     yes       disabled  NIST-certified core packages with priority security updates
    usg              yes       disabled  Security compliance and audit tools


So we see that our node has Ubuntu Pro and FIPS enable

Conclusion
~~~~~~~~~~

You now have an Ubuntu Pro Kubernetes cluster on EKS. Your Ubuntu Pro subscription can be verified on each of the provisioned nodes with

..  code-block:: bash

    $ pro status
