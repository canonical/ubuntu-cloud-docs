.. meta::
   :description: Learn how to create a Google Kubernetes Engine (GKE) cluster with Ubuntu nodes using the gcloud CLI, and verify the node OS image.


Create a GKE cluster with Ubuntu nodes
======================================

`Google Kubernetes Engine`_ (GKE) is a managed Kubernetes service on Google Cloud
that lets you deploy and manage containerized applications. Ubuntu can be used as
the base operating system for GKE nodes, giving you a familiar, well-supported
foundation for your workloads.

Using Ubuntu for your GKE nodes provides several benefits:

* **Flexible.** Ubuntu can be used across a variety of Kubernetes distributions, so
  your teams get a standardized experience across multiple clouds, such as Azure
  Kubernetes Service (AKS) and Amazon Elastic Kubernetes Service (EKS).
* **Secure.** Timely updates and patches, building on Ubuntu's security track record.
* **Stable.** Long-term support with a consistent, predictable lifecycle. Each GKE
  version ships a customized version of Ubuntu that supports its latest features.
* **Seamless.** A developer-friendly, smooth experience from development to production.

This guide uses the `gcloud CLI tool`_ to create a cluster with Ubuntu nodes. To
create a cluster from the Google Cloud console instead, refer to the `GKE
documentation on creating clusters`_.


Prerequisites
-------------

Before you begin, make sure that you have:

* Installed and initialized the `gcloud CLI tool`_.
* Installed ``kubectl`` and the ``gke-gcloud-auth-plugin`` authentication plugin.
* Selected the project you want to work in:

  .. code::

    gcloud config set project <project-id>

* Enabled the Kubernetes Engine API for your project:

  .. code::

    gcloud services enable container.googleapis.com


Choose a cluster mode
---------------------

GKE offers two modes of operation: Autopilot and Standard. In Autopilot mode,
Google manages the infrastructure for you, and you cannot manually select node image
types. To explicitly configure and manage Ubuntu nodes, create a **Standard**
cluster, which lets you customize your node pools and specify the ``UBUNTU_CONTAINERD``
image type.


Create a cluster with Ubuntu nodes
----------------------------------

Create a Standard cluster and set the node image type to Ubuntu with containerd
using the ``--image-type`` flag:

.. code::

    gcloud container clusters create <cluster-name> \
        --image-type UBUNTU_CONTAINERD \
        --zone <zone> \
        --num-nodes <number-of-nodes>

.. note::
   You can substitute ``--zone <zone>`` with ``--region <region>`` if you are deploying
   a high-availability regional cluster.

For example, to create a cluster named ``ubuntu-cluster`` with three nodes in the
``us-central1-c`` zone:

.. code::

    gcloud container clusters create ubuntu-cluster \
        --image-type UBUNTU_CONTAINERD \
        --zone us-central1-c \
        --num-nodes 3

The ``UBUNTU_CONTAINERD`` image type corresponds to the "Ubuntu with containerd
(ubuntu_containerd)" option in the Google Cloud console.


Use Ubuntu nodes in a specific node pool
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you already have an existing cluster, or want only specific node pools to run Ubuntu,
create a node pool with the Ubuntu image type:

.. code::

    gcloud container node-pools create <node-pool-name> \
        --cluster <cluster-name> \
        --image-type UBUNTU_CONTAINERD \
        --zone <zone> \
        --num-nodes <number-of-nodes>


Get cluster credentials
-----------------------

To interact with your cluster using ``kubectl``, fetch its credentials:

.. code::

    gcloud container clusters get-credentials <cluster-name> --zone <zone>


Verify the node OS image
------------------------

Once the cluster is running, confirm that the nodes are using Ubuntu.

Using ``kubectl``, check the ``OS-IMAGE`` column:

.. code::

    kubectl get nodes --output=wide

.. code::

    NAME                                            STATUS   ROLES    AGE   VERSION               INTERNAL-IP    EXTERNAL-IP    OS-IMAGE            KERNEL-VERSION    CONTAINER-RUNTIME
    gke-ubuntu-cluster-default-pool-52e0bb17-4032   Ready    <none>   23m   v1.35.6-gke.1127000   x.x.x.x        x.x.x.x        Ubuntu 24.04.4 LTS  6.8.0-1055-gke    containerd://2.1.5
    gke-ubuntu-cluster-default-pool-52e0bb17-vjw0   Ready    <none>   23m   v1.35.6-gke.1127000   x.x.x.x        x.x.x.x        Ubuntu 24.04.4 LTS  6.8.0-1055-gke    containerd://2.1.5
    gke-ubuntu-cluster-default-pool-52e0bb17-vjxf   Ready    <none>   23m   v1.35.6-gke.1127000   x.x.x.x        x.x.x.x        Ubuntu 24.04.4 LTS  6.8.0-1055-gke    containerd://2.1.5

Alternatively, inspect the image type of a node pool directly via ``gcloud``:

.. code::

    gcloud container node-pools describe <node-pool-name> \
        --cluster <cluster-name> \
        --zone <zone> \
        --format="value(config.imageType)"

The output should return ``UBUNTU_CONTAINERD``.

You now have a GKE cluster running Ubuntu nodes, ready to deploy your containerized
applications.


.. _`Google Kubernetes Engine`: https://cloud.google.com/kubernetes-engine
.. _`gcloud CLI tool`: https://docs.cloud.google.com/sdk/gcloud
.. _`GKE documentation on creating clusters`: https://cloud.google.com/kubernetes-engine/docs/how-to/creating-a-zonal-cluster