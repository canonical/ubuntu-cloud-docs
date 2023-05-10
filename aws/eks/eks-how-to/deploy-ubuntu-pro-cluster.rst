Deploy an Ubuntu Pro EKS cluster
================================

This guide shows how to deploy an EKS Cluster with Ubuntu Pro nodes.

Prerequisites
~~~~~~~~~~~~~

You need:

- ``eksctl``: see how to install it `here <https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html>`_
- ``packer``: only needed if you want to enable FIPS for the cluster nodes. Install it with ``sudo snap install packer``
- your AWS access key ID and secret access key
- an Ubuntu Pro token


Cluster deployment preparation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Depending on whether you need to enable FIPS or not, you only need to follow one of the following two sections.

Please note that while there are Ubuntu Pro AMIs available in AWS, at the time
of writing this guide, there is no such offering for the EKS service, so you'll
need to provision the EKS cluster with customised Ubuntu nodes.


Without FIPS
^^^^^^^^^^^^

When FIPS is not enabled, you can use one of the existing Ubuntu EKS AMIs and customise it using cloud-init during deployment.

You should use the cloud-init's
`ubuntu-advantage module <https://cloudinit.readthedocs.io/en/latest/reference/modules.html#ubuntu-advantage>`_.
For this deployment, you'll also need to have an existing
`launch template <https://docs.aws.amazon.com/autoscaling/ec2/userguide/launch-templates.html>`_
on AWS.

Launch template's user-data
***************************

On the advanced section of your launch template (user-data section), copy
the following code (replacing the "token" field by your Pro token):

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

With FIPS
^^^^^^^^^

When enabling FIPS, a reboot of the underlying node is required. If this reboot is done after the cluster is created, in rare cases, it might result in the node being flagged as defective (`troubleshooting options <https://docs.aws.amazon.com/eks/latest/userguide/troubleshooting.html>`_).

For this reason, the most reliable way to deploy an Ubuntu Pro EKS cluster is to build a
custom Ubuntu Pro AMI (with `Packer <https://www.packer.io/>`_) and use it during cluster creation until this `bug <https://bugs.launchpad.net/cloud-images/+bug/2017782>`_ is fixed.


What are the caveats?
*********************

You need to keep rebuilding your custom Ubuntu Pro image in order to have the latest updates and security fixes from upstream.

Also, storing AMI has a cost on AWS, and you will have to replicate it to multiple regions if you need to.

Get and modify the Packer file
******************************

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


Build the custom Ubuntu Pro AMI
*******************************

To build the image, run ``packer build eks-ubuntu-fips.json``.
The resulting logs should look something like:

..  code-block:: bash

    Build 'amazon-ebs' finished after 9 minutes 35 seconds.

    ==> Wait completed after 9 minutes 35 seconds

    ==> Builds finished. The artifacts of successful builds are:
    --> amazon-ebs: amis were created:
    us-east-1: ami-xxxxxx

NOTE: copy the provided AMI ID for the next step.

Create the eksctl config file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

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

	.. tab:: Without FIPS

         .. code-block:: yaml

            managedNodeGroups:
            - name: ng-procluster
            desiredCapacity: 2
            launchTemplate:
              id: lt-12345
              version: "1"
                        
         This config file will allow you to create an EKS cluster using the launch template
         from above, with two nodes. 

	.. tab:: With FIPS

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

         Also, we use AmazonLinux2 as the amiFamily because currently it's the only native option supported by eksctl.

         The "overrideBootstrapCommand" lets you launch the bootstrap script from AWS EKS
         to initialise the nodes.


For further cluster customisation see `this <https://eksctl.io/>`_.

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



To ensure your nodes have an Ubuntu Pro subscription, SSH into one of the cluster nodes
(get the external IP of your node with ``kubectl get nodes -o wide``):

..  code-block:: bash

    $ # Replace the private SSH key and node IP according to your setup
    $ ssh -i yoursshkeyname.pem ubuntu@<external_ip_of_node>
    $ pro status

    SERVICE          ENTITLED  STATUS    DESCRIPTION
    esm-apps         yes       enabled   Expanded Security Maintenance for Applications
    esm-infra        yes       enabled   Expanded Security Maintenance for Infrastructure
    fips             yes       enabled   NIST-certified core packages
    fips-updates     yes       disabled  NIST-certified core packages with priority security updates
    usg              yes       disabled  Security compliance and audit tools

Please note that your services' statuses might differ from this snippet based
on the Pro services that you've chosen to enable in the above configurations.

Conclusion
~~~~~~~~~~

You now have an Ubuntu Pro Kubernetes cluster on EKS. Your Ubuntu Pro subscription can be verified on each of the provisioned nodes with

..  code-block:: bash

    $ pro status
