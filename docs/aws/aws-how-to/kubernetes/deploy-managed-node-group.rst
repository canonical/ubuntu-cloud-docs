Deploy managed Ubuntu nodes on EKS
==================================

This guide provides instructions for creating EKS managed node groups using `eksctl`_, starting with a custom image based on the official Ubuntu EKS or Ubuntu Pro EKS base images.

Create a cluster of EKS managed nodes
----------------------------------------

Prepare your base node image
""""""""""""""""""""""""""""

Start with the official Ubuntu EKS or Ubuntu Pro EKS AMI. You can get it using the `AWS CLI`_ or from the `AWS Marketplace`_. Make a note of the AMI ID used.

If you don't need any further customization, you can jump directly to the next step of creating a launch template.

If you need to apply updates, install security tools, enable compliance settings, or perform some other customization to your base worker node image, you can use one of the following methods:

- Manually launch an EC2 instance with an instance type that matches the chosen AMI's architecture. Customize it as needed and create a new AMI from it. Note its AMI ID.
- Use `AWS EC2 Image Builder`_ or `Packer`_. In this case, the AMI ID will be generated automatically after the build completes. 


Create a launch template
""""""""""""""""""""""""

While you can use the AWS EC2 web console to manually create a launch template, using the AWS CLI (as described below) can save time. 

While creating the launch template, you'll need to include a user-data script that is used to bootstrap the node and join it to a cluster. To create the script, in a new file (called, say ``my-user-data.txt``) add:

..  code-block:: bash

    #!/bin/bash
    /etc/eks/bootstrap.sh My-Ubuntu-Cluster

Replace ``My-Ubuntu-Cluster`` above with the (expected) name of your EKS cluster.

The script is supposed to be base64-encoded. If you are on Ubuntu, you can encode it using the ``base64`` command:

..  code-block:: bash

    base64 my-user-data.txt 
   
Now, using this user-data script and the AMI ID saved earlier, create the launch template:

..  code-block:: bash  

    aws ec2 create-launch-template \
        --launch-template-name my-eks-template \
        --version-description "Custom Ubuntu image" \
        --launch-template-data '{
            "ImageId":"ami-xxxxxx",
            "InstanceType":"t3.medium",
            "KeyName":"my-key",
            "SecurityGroupIds":["sg-xxxxxx"],
            "IamInstanceProfile":{"Name":"my-eks-node-role"},
            "UserData":"IyEvYmluL2Jhc2gKL2V0Yy9la3MvYm9vdHN0cmFwLnNoIE15LVVidW50dS1DbHVzdGVyCg=="
        }'

Make a note of the template ID since it'll be needed in the next step.


Create a managed node group for an existing cluster
"""""""""""""""""""""""""""""""""""""""""""""""""""

To create a managed node group for an existing cluster or even to create a new cluster of managed nodes, you'll need to define the node groups in a YAML file (e.g. ``my-ubuntu-cluster.yaml``):

..  code-block:: yaml

    ---
    apiVersion: eksctl.io/v1alpha5
    kind: ClusterConfig

    metadata:
        name: My-Ubuntu-Cluster
        region: us-east-1 # Replace with your desired AWS region
        version: "1.33"

    iam:
      withOIDC: true

    managedNodeGroups:
      - name: my-managed-ng
        launchTemplate:
            id: lt-xxxxxxx # Replace with your Launch Template ID
            version: "1"
        minSize: 1
        desiredCapacity: 2
        maxSize: 3

        iam:
            attachPolicyARNs:
                - arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy
                - arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly
                - arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
                - arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy

Then using the YAML file as an input parameter, run ``eksctl`` to create the node group:

..  code-block:: bash

    AWS_PROFILE=eks eksctl create nodegroup -f my-ubuntu-cluster.yaml

This command creates the new node group and starts deploying the nodes in the cluster.

.. note::
    - If you prefer to create a new cluster instead, you can use the same YAML file to run ``create cluster`` instead of ``create nodegroup``:

    ..  code-block:: bash  

        AWS_PROFILE=eks eksctl create cluster -f my-ubuntu-cluster.yaml


    - Here an AWS CLI profile called ``eks`` is being used, but if your default profile has sufficient permissions, you can omit that profile environment variable.
    - If you already have nodes deployed without a launch template, you cannot convert a self-managed node group into a managed one. You must create a new managed node group.

Wait for the deployment to finish. If you want to control the cluster using `kubectl`_, you can update the ``kubectl`` configuration file as follows:

..  code-block:: bash

    aws eks update-kubeconfig --region us-east-1 --name My-Ubuntu-Cluster --profile eks

Now you can monitor your cluster using ``kubectl``:

..  code-block:: bash  

    kubectl get nodes -o wide

Wait for the node groups to be up and running. The next step is to test how to trigger the upgrading of the nodes.

Trigger automatic node replacement in an existing group of managed nodes
------------------------------------------------------------------------

If your cluster is already running with managed node groups and you need to update the base AMI automatically, you’ll have to create a new version of the launch template and update the node group to use it. This will trigger the “cordon and drain” node replacement strategy automatically.


Create a new launch template version
""""""""""""""""""""""""""""""""""""

To create a new version of the launch template, you need to use your existing launch template ID (created in the previous section), and update only the ``ImageId`` field with the new AMI ID. The CLI command to do this is:

..  code-block:: bash

    aws ec2 create-launch-template-version \
        --launch-template-id lt-0123456789abcdef0 \
        --version-description "Ubuntu Pro EKS image v2" \
        --source-version 1 \
        --launch-template-data '{
            "ImageId":"ami-NEWAMI123456"
        }'

In the command, source-version is set to '1' since we are using the originally created launch template. The new version created will have its version automatically set to '2'.

Update the managed node group to use the new launch template version
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

To update the node group to use the new launch template version, run:

..  code-block:: bash

    eksctl upgrade nodegroup \
        --name=my-managed-ng \
        --cluster=My-Ubuntu-Cluster \
        --region=us-east-1 \
        --launch-template-version 2

This triggers **automatic node replacement**, draining old nodes and launching new ones with the updated image.

Future steps
------------

We have covered the process of using launch templates to build your own managed nodes with Ubuntu, Ubuntu Pro and any customization that you might need.

The next step could be to automate the process:

- Use AWS EC2 Image Builder to generate new AMIs on a schedule.
- Trigger EventBridge events that invoke a Lambda function to:

  - Update the launch template with the new AMI.
  - Point the managed node group to the new template version.

This will keep your cluster always up-to-date with minimal manual effort.


.. _`eksctl`: https://docs.aws.amazon.com/eks/latest/eksctl/installation.html
.. _`AWS CLI`: https://documentation.ubuntu.com/aws/aws-how-to/instances/find-ubuntu-images/
.. _`AWS Marketplace`: https://aws.amazon.com/marketplace/search/results?searchTerms=ubuntu+eks&CREATOR=565feec9-3d43-413e-9760-c651546613f2&filters=CREATOR
.. _`AWS EC2 Image Builder`: https://www.youtube.com/watch?v=ALFuCc5kfpE
.. _`Packer`: https://documentation.ubuntu.com/aws/aws-how-to/instances/build-pro-ami-using-packer/
.. _`kubectl`: https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html

