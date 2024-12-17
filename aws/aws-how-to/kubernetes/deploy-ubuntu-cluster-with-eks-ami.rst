Deploy an Ubuntu EKS cluster
============================

This guide shows how to deploy an Ubuntu EKS cluster using an EKS AMI.

Prerequisites
-------------

You need:

- ``eksctl`` (version 0.190 or newer): Check the instructions to `install eksctl`_
- ``kubectl``: Check the instructions to `install kubectl`_


Create the ``eksctl`` config file
---------------------------------

Create a ``config.yaml`` with the following content:

..  code-block:: yaml

    apiVersion: eksctl.io/v1alpha5
    kind: ClusterConfig
    metadata:
        name: your-cluster
        region: us-east-1
    nodeGroups:
    - name: ng-cluster
      instanceType: m5.large
      amiFamily: Ubuntu2204
      ami: ami-ubuntu
      overrideBootstrapCommand: |
        #!/bin/bash
        /etc/eks/bootstrap.sh your-cluster

To use an Ubuntu specific AMI, set ``amiFamily`` to ``Ubuntu2004`` (for EKS version <= 1.29) or to ``Ubuntu2204`` (for EKS version >= 1.29). For Ubuntu nodes, the ``overrideBootstrapCommand`` is required for both managed and self-managed groups.

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
    ip-xxx-xxx-xx-xxx.us-east-1.compute.internal   Ready    <none>   2m45s   v1.30.x
    ip-xxx-xxx-x-xx.us-east-1.compute.internal     Ready    <none>   2m45s   v1.30.x


.. _`install eksctl`: https://eksctl.io/installation/
.. _`install kubectl`: https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html
.. _`config file schema for eksctl`: https://eksctl.io/usage/schema
