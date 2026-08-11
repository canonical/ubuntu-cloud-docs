.. meta::
   :description: Learn how to deploy self-managed node groups using Ubuntu nodes on EKS. Specify 'Ubuntu' as the node AMI family when creating a node group with eksctl.


Deploy self-managed Ubuntu nodes
================================

Amazon Web Services provides documentation for `launching self-managed node
groups`_. Canonical publishes Ubuntu LTS and Ubuntu Pro LTS EKS images based on
Ubuntu Minimal, containing the necessary components to launch Ubuntu EKS worker
nodes.

This guide details the process of deploying self-managed node groups using the
``eksctl`` command-line tool.

Requirements:

* AWSCLI installed and configured
* eksctl (make sure to keep it updated to support latest EKS and Ubuntu versions)

Launching nodegroups from the command line
------------------------------------------

Eksctl supports Ubuntu nodes natively. To specify Ubuntu nodes, in the
``eksctl create nodegroup`` command, supply the ``--node-ami-family`` argument
with one of the following supported Node AMI families:

.. list-table::
   :header-rows: 1

   * - ``amiFamily``
     - Ubuntu release
     - Supported EKS versions
   * - ``Ubuntu2204``
     - 22.04 Jammy Jellyfish
     - 1.29 – 1.32
   * - ``UbuntuPro2204``
     - 22.04 Jammy Jellyfish (Pro)
     - 1.29 – 1.34
   * - ``Ubuntu2404``
     - 24.04 Noble Numbat
     - > 1.31
   * - ``UbuntuPro2404``
     - 24.04 Noble Numbat (Pro)
     - > 1.31
   * - ``Ubuntu2604``
     - 26.04 Resolute Raccoon
     - > 1.36 (eksctl > v0.226.0)
   * - ``UbuntuPro2604``
     - 26.04 Resolute Raccoon (Pro)
     - > 1.36 (eksctl > v0.226.0)

.. note::
   If you prefer to use managed node groups, refer to
   :doc:`this guide <deploy-managed-node-group>`. In that scenario, the AMI is
   defined via a launch template, and EKS automatically handles the node
   recycling strategy.

Therefore, launching a new nodegroup with the Ubuntu 24.04 LTS AMI would be:

.. code-block:: bash

   eksctl create nodegroup \
     --cluster my-ubuntu-cluster \
     --name 2404-nodes \
     --node-type t3.medium \
     --nodes 3 \
     --nodes-min 1 \
     --nodes-max 4 \
     --ssh-access \
     --ssh-public-key my-key \
     --node-ami-family ubuntu2404

To use Ubuntu Pro, which enables Kernel Livepatch on the nodes and allows the
cluster to run Ubuntu Pro containers, use the following command:

.. code-block:: bash

   eksctl create nodegroup \
     --cluster my-ubuntu-cluster \
     --name 2404-pro-nodes \
     --node-type t3.medium \
     --nodes 3 \
     --nodes-min 1 \
     --nodes-max 4 \
     --ssh-access \
     --ssh-public-key my-key \
     --node-ami-family ubuntupro2404

Launching nodegroups from a YAML configuration file
---------------------------------------------------

If you need to change default configurations or track configuration changes as
code, you can start the new nodegroup from a cluster configuration YAML file:

.. code-block:: yaml

   ---
   apiVersion: eksctl.io/v1alpha5
   kind: ClusterConfig

   metadata:
     name: my-ubuntu-cluster
     region: us-east-1

   nodeGroups:
     - name: 2404-pro-nodes
       amiFamily: UbuntuPro2404
       instanceType: t3.medium
       desiredCapacity: 3
       minSize: 1
       maxSize: 4
       ssh:
         allow: true
         publicKeyName: my-key

Save this file, say ``nodegroup.yaml`` and launch it with:

.. code-block:: bash

   eksctl create nodegroup -f nodegroup.yaml

Validation
----------

If you have kubectl installed and configured, run ``kubectl get nodes -o wide``
to get extended information about your clusters:

.. code-block:: text

   kubectl get nodes -o wide
   NAME                             STATUS   ROLES    AGE    VERSION   INTERNAL-IP      EXTERNAL-IP      OS-IMAGE           KERNEL-VERSION           CONTAINER-RUNTIME
   ip-192-168-23-188.ec2.internal   Ready    <none>   3h3m   v1.36.2   192.168.23.188   100.62.88.240    Ubuntu 26.04 LTS   7.0.0-1010-aws (amd64)   containerd://2.2.2
   ip-192-168-58-220.ec2.internal   Ready    <none>   3h2m   v1.36.2   192.168.58.220   100.55.160.174   Ubuntu 26.04 LTS   7.0.0-1010-aws (amd64)   containerd://2.2.2

If your ``kubectl`` configuration is missing or incorrect for managing your
cluster, you can regenerate it using the AWS CLI:

.. code-block:: bash

   aws eks update-kubeconfig --region us-east-1 --name my-ubuntu-cluster


.. _`launching self-managed node groups`: https://docs.aws.amazon.com/eks/latest/userguide/launch-workers.html
