Deploy an Ubuntu Pro EKS cluster - using a Pro AMI
==================================================

This guide shows how to deploy an Ubuntu Pro EKS cluster using an EKS Pro AMI. 

An EKS Pro AMI is an Ubuntu EKS AMI that includes the `Pro subscription`_, which provides services such as Livepatch for LTS-based nodes and Expanded Security Maintenance (ESM). It also grants the cluster a license to run Pro containers with no limitations on quantity or variety.

Ubuntu Pro 22.04 LTS supports EKS up to version 1.34, while Ubuntu 24.04 LTS will continue supporting current and future EKS versions. Currently, only 22.04 LTS provides NIST-validated FIPS components. For earlier versions or other combinations of EKS and Ubuntu releases, use Pro tokens as described in :doc:`./deploy-ubuntu-pro-cluster`. To include FIPS, refer to :doc:`./deploy-ubuntu-pro-fips-cluster`.

Prerequisites
-------------

You need:

- ``eksctl`` (version v0.201.0 or newer): Check the instructions to `install eksctl`_
- ``kubectl``: Check the instructions to `install kubectl`_


Create the ``eksctl`` config file
---------------------------------

Create a ``config.yaml`` with the following content:


..  code-block:: yaml

    ---
    apiVersion: eksctl.io/v1alpha5
    kind: ClusterConfig
    
    metadata:
      name: my-pro-cluster
      region: us-east-1
      version: '1.35'
    
    iam:
      withOIDC: true
    
    nodeGroups:
      - name: ng-ubuntu-pro-2404
        instanceType: m5.large
        desiredCapacity: 3
        amiFamily: UbuntuPro2404
        iam:
           attachPolicyARNs:
              - arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy
              - arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly
              - arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
              - arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy
        ssh:
            allow: true
            publicKeyName: myKeyPair


This config file will allow you to use ``eksctl`` to create an EKS cluster and node groups. By specifying ``amiFamily: UbuntuPro2404``, we ensure that the EKS Pro AMI will be used during creation and deployment.

To use an Ubuntu specific Ubuntu Pro AMI version, set ``amiFamily`` to one of these choices:

- ``UbuntuPro2204`` for EKS version >= 1.29 and < 1.35
- ``UbuntuPro2404`` for EKS version >= 1.31

For further cluster customization check out `eksctl details`_.


Deploy the EKS cluster
----------------------

To create the EKS cluster, run:

.. code::

   eksctl create cluster -f config.yaml

You might need to specify the ``--profile`` option if you have multiple profiles.

You can confirm the status of the nodes on your cluster using:

..  code-block:: bash

    $ kubectl get nodes

    NAME                                           STATUS   ROLES    AGE     VERSION
    ip-xxx-xxx-xx-xxx.us-east-1.compute.internal   Ready    <none>   2m45s   v1.35.x
    ip-xxx-xxx-x-xx.us-east-1.compute.internal     Ready    <none>   2m45s   v1.35.x


(Optional) Verify Pro subscription
----------------------------------

To check that the deployed nodes have Ubuntu Pro, run:

..  code-block:: bash

    $ aws --region <region_name> ec2 describe-instances \
          --filters Name=instance-state-name,Values=running \
          --query 'Reservations[*].Instances[*].[InstanceType, LaunchTime, PlatformDetails]' 
          --output table

    ----------------------------------------------------------------
    |                       DescribeInstances                      |
    +-----------+-----------------------------+--------------------+
    |  m5.large |  2024-05-07T19:57:33+00:00  |  Ubuntu Pro Linux  |
    |  m5.large |  2024-05-07T19:57:33+00:00  |  Ubuntu Pro Linux  |
    +-----------+-----------------------------+--------------------+




.. _`Pro subscription`: https://ubuntu.com/pro
.. _`install eksctl`: https://docs.aws.amazon.com/eks/latest/eksctl/installation.html
.. _`install kubectl`: https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html
.. _`eksctl details`: https://docs.aws.amazon.com/eks/latest/eksctl/what-is-eksctl.html
