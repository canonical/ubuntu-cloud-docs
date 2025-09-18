Deploy Ubuntu OKE nodes using Console
=======================================

.. Introduction to Ubuntu OKE node

Ubuntu images are available for OKE worker nodes, with support for a select number of suites and Kubernetes versions. For a list of supported OKE configurations, see our :doc:`Ubuntu availability on OKE </oracle-reference/ubuntu-availability-on-oke>` page.


Prerequisites
-------------

You’ll need:

- Oracle Cloud compartment to create the nodes.
- `Domain`_, `Dynamic Group and Policy`_ configured (Self-Managed only).

.. include:: ../../reuse/OKE-nodes.txt
   :start-after: Start: Get Ubuntu image access
   :end-before: End: Get Ubuntu image access

After access is enabled, Ubuntu OKE images will be available for selection when creating a cluster or adding a node pool. You can choose your preferred Ubuntu image during the setup process.

Create an OKE cluster using the Console
---------------------------------------

To create an OKE cluster from the Oracle Cloud Console:

1. In the Oracle Cloud Console, go to **Kubernetes Clusters (OKE)**.
2. Click **Create cluster**. You will see two options:

    - **Quick create**: Creates a new cluster and all required network resources automatically (VCN, gateways, subnets, node pool, etc.). Recommended for new environments.
    - **Custom create**: Let's you use existing network resources or customize the setup. Choose this if you need to integrate with existing VCNs or have specific network requirements.

    .. image:: deploy-ubuntu-oke-nodes/oke-create.png
        :alt: OKE Quick Create


    **Quick create** is used for this example.

3. After submitting, you will be prompted to enter the following cluster details:

    - **Name**: The display name for your cluster.
    - **Compartment**: The compartment where the cluster and resources will be created.
    - **Kubernetes version**: The version of Kubernetes to deploy.
    - **Kubernetes API endpoint**: Choose public or private endpoint access for the Kubernetes API server.
    - **Node type**: Select Managed or Self-Managed nodes.
    - **Kubernetes worker nodes**: Choose whether to create public or private worker nodes.

    The following image shows the options covered so far:

    .. image:: deploy-ubuntu-oke-nodes/oke-info1.png
        :alt: OKE cluster options overview


    - **Shape and image**: Select the compute shape (OCPUs, memory) for your nodes. Then, to use Ubuntu, click **Change image** and choose your required image based on the architecture, Ubuntu suite, and Kubernetes version.

        After selecting your desired image based on the architecture, Ubuntu suite, and Kubernetes version, your configuration should look similar to the image below.

        .. image:: deploy-ubuntu-oke-nodes/oke-info2.png
            :alt: Select Ubuntu image

      .. warning::
         Pay attention to which image you select and ensure its architecture matches your chosen node shape (for example, amd64 or arm64).

    - **Node count**: Set the node count to zero.

5. Click Next to review your configuration and click **Create cluster**.

The cluster will be created. You can add nodes later as needed.

Add nodes to an existing OKE cluster
------------------------------------------------

Once your cluster is created, you can add nodes as follows:

1. On the cluster details page, under **Resources**, select **Node pools**.
2. You will see a list of node pools as shown in the image below.

    .. image:: deploy-ubuntu-oke-nodes/oke-node-pool.png
        :alt: Node pool list

3. Click on the pool name (for example, **pool1**). This opens the node pool details page.
4. Change the node count to your desired value.
5. Scroll to the bottom and select **Show advanced options**.
6. Under **Initialization script**, you can browse or paste your cloud-init script. For example, you can use the following:

    .. code-block:: yaml

        #cloud-config
        runcmd:
          - oke bootstrap

7. Save your changes.

The node pool will update, and new nodes will be created and initialized using your cloud-init script, as shown below.

    .. image:: deploy-ubuntu-oke-nodes/oke-node-list.png
        :alt: Node pool updated

.. include:: ../../reuse/OKE-nodes.txt
   :start-after: Start: References and links
   :end-before: End: References and links
