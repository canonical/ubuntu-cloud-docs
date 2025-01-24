Deploy an Ubuntu EKS cluster
============================

This guide shows how to deploy an Ubuntu EKS cluster using an official EKS AMI.

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
      name: my-cluster
      region: region-code
      version: '1.31'
    
    iam:
      withOIDC: true
    
    nodeGroups:
      - name: ng-ubuntu
        instanceType: m5.large
        desiredCapacity: 3
        amiFamily: Ubuntu2404
        iam:
           attachPolicyARNs:
              - {arn-aws}iam::aws:policy/AmazonEKSWorkerNodePolicy
              - {arn-aws}iam::aws:policy/AmazonEC2ContainerRegistryReadOnly
              - {arn-aws}iam::aws:policy/AmazonSSMManagedInstanceCore
              - {arn-aws}iam::aws:policy/AmazonEKS_CNI_Policy
        ssh:
            allow: true
            publicKeyName: my-ec2-keypair-name

To use an Ubuntu specific AMI, set ``amiFamily`` to one of these choices:
- ``Ubuntu2004`` for EKS version <= 1.29
- ``Ubuntu2204`` for EKS version >= 1.29
- ``Ubuntu2404`` for EKS version >= 1.31

For further cluster customization, check out the `config file schema for eksctl`_ 


Deploy the EKS cluster
----------------------

To deploy the EKS cluster, run:

.. code::

   eksctl create cluster -f config.yaml

You might need to specify the ``--profile`` option if you have multiple profiles.

You can confirm the status of the nodes on your cluster using:

..  code-block:: bash

    $ kubectl get nodes

    NAME                                           STATUS   ROLES    AGE     VERSION
    ip-xxx-xxx-xx-xxx.us-east-1.compute.internal   Ready    <none>   2m45s   v1.31.x
    ip-xxx-xxx-x-xx.us-east-1.compute.internal     Ready    <none>   2m45s   v1.31.x


.. _`install eksctl`: https://eksctl.io/installation/
.. _`install kubectl`: https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html
.. _`config file schema for eksctl`: https://eksctl.io/usage/schema
