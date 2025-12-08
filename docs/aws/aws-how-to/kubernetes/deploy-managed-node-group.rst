Deploy managed Ubuntu nodes on EKS
==================================

In this guide, we’ll walk through how to create EKS managed node groups using `eksctl`_, starting from a custom image based on the official Ubuntu EKS or Ubuntu Pro EKS base images.

Part 1: Creating a cluster of EKS managed nodes
-----------------------------------------------

Prepare your base node image
""""""""""""""""""""""""""""

Start from the official Ubuntu EKS or Ubuntu Pro EKS AMI. You can get it either using `AWS CLI`_ or `AWS Marketplace`_ and make note of the AMI ID you will use.

If you don’t need further customization, you can jump directly to the next step.

If you need to customize your base worker node image, for instance, to apply updates, install security tools or enable compliance settings, you can use one of the following methods:
- Manually launch an EC2 instance with an instance type matching the AMI architecture. Customize it as required, create a new AMI from it and note its AMI ID.
- Use `AWS EC2 Image Builder`_ or `Packer`_. In this case, the AMI ID will be generated automatically after the build completes. 


Create a launch template
""""""""""""""""""""""""

While you can use the AWS EC2 web console to manually create a launch template, using the AWS CLI can save time. Note that when creating the launch template, you need to include a UserData script that bootstraps the node and joins it to your cluster. To do that, create a file (say ``my-user-data.txt``) that contains:


..  code-block:: bash

    #!/bin/bash
    /etc/eks/bootstrap.sh My-Ubuntu-Cluster

with ``My-Ubuntu-Cluster`` being replaced with the (expected) name of your EKS cluster.

Since the script is supposed to be base64-encoded, you’ll need to encode it. If you are on Ubuntu, you can encode it using the ``base64`` command:

..  code-block:: bash

    base64 my-user-data.txt 
   
Now create the launch template using:

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

Make a note of your template ID for the next step.

Create a managed node group for an existing cluster
"""""""""""""""""""""""""""""""""""""""""""""""""""

Create a YAML file (e.g. ``my-ubuntu-cluster.yaml``) that will define the node groups for your cluster (or launch the entire cluster if needed):

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

Run ``eksctl`` to create the node group:

..  code-block:: bash

    AWS_PROFILE=eks eksctl create nodegroup -f my-ubuntu-cluster.yaml

This command creates the new node group and starts deploying the nodes in the cluster.

Notes: 

- If you prefer to create a new cluster instead, you can use the same ``yaml`` file:

..  code-block:: bash  

    AWS_PROFILE=eks eksctl create cluster -f my-ubuntu-cluster.yaml


- The example uses an AWS CLI profile called ``eks``. But if your default profile has sufficient permissions, you can omit that profile environment variable.
- If nodes are already deployed without a launch template, you cannot convert a self-managed node group into a managed one. You must create a new managed node group.

Wait for the deployment to finish. If you want to control the cluster using `kubectl`_, you can update the ``kubectl`` configuration file as follows:

..  code-block:: bash

    aws eks update-kubeconfig --region us-east-1 --name My-Ubuntu-Cluster --profile eks

Now you can monitor your cluster using ``kubectl`` as follows:

..  code-block:: bash  

    kubectl get nodes -o wide

Wait for the node groups to be up and running. The next step is to test how to trigger the upgrading of the nodes.

Part 2: Triggering automatic node replacement in an existing managed nodes group
--------------------------------------------------------------------------------

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

In the command, source-version is set to '1' since we are updating the originally created launch template. The new version created will have its version automatically set to '2'.

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

We have covered how using Launch Templates you can build your own managed nodes with Ubuntu, Ubuntu Pro and any customization you would need.

Now that you understand the workflow, the next step is automation:

- Use AWS EC2 Image Builder to generate new AMIs on a schedule.
- Trigger EventBridge events that invoke a Lambda function to:

  - Update the launch template with the new AMI.
  - Point the managed node group to the new template version.

This keeps your cluster always up-to-date with minimal manual effort.


.. _`eksctl`: https://docs.aws.amazon.com/eks/latest/eksctl/installation.html
.. _`AWS CLI`: https://documentation.ubuntu.com/aws/aws-how-to/instances/find-ubuntu-images/
.. _`AWS Marketplace`: https://aws.amazon.com/marketplace/search/results?searchTerms=ubuntu+eks&CREATOR=565feec9-3d43-413e-9760-c651546613f2&filters=CREATOR
.. _`AWS EC2 Image Builder`: https://www.youtube.com/watch?v=ALFuCc5kfpE
.. _`Packer`: https://documentation.ubuntu.com/aws/aws-how-to/instances/build-pro-ami-using-packer/
.. _`kubectl`: https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html

