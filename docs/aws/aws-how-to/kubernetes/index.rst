.. meta::
   :description: List of how-to guides related to using Ubuntu on EKS worker nodes.

.. _kubernetes-index:

Using EKS
=========

Canonical publishes Ubuntu EKS images ready for use in your EKS clusters. These
images come pre-configured to join a cluster and are integrated into ``eksctl``,
the official EKS management CLI tool. Ubuntu LTS and Ubuntu Pro LTS images are
available via the :ref:`AWS CLI <find-ubuntu-images>`,
``eksctl``, or the `AWS Marketplace`_.

The following table details the currently supported images and EKS version
coverage:

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
     - 1.31 – 1.36
   * - ``UbuntuPro2404``
     - 24.04 Noble Numbat (Pro)
     - 1.31 – 1.36
   * - ``Ubuntu2604``
     - 26.04 Resolute Raccoon
     - 1.36 only
   * - ``UbuntuPro2604``
     - 26.04 Resolute Raccoon (Pro)
     - 1.36 only

Cluster deployment options for Ubuntu on EKS
--------------------------------------------

To use Ubuntu as the operating system for your EKS worker nodes, choose from the
following deployment options:

* :ref:`Deploy an Ubuntu EKS cluster <deploy-ubuntu-cluster-with-eks-ami>`
* :ref:`Deploy an Ubuntu Pro EKS cluster <deploy-ubuntu-pro-cluster-with-eks-pro-ami>` (using the pre-activated Ubuntu Pro AMI)
* :ref:`Deploy an Ubuntu Pro FIPS EKS cluster <deploy-ubuntu-pro-fips-cluster>` (using the pre-activated Ubuntu Pro AMI)
* :ref:`Deploy an Ubuntu Pro cluster using tokens <deploy-ubuntu-pro-cluster>`

Deployment options for node groups
----------------------------------

You can create both managed and self-managed node groups using Ubuntu on EKS.
Select from the following options:

* :ref:`Deploy a self-managed Ubuntu node group <deploy-self-managed-node-group>`
* :ref:`Deploy managed Ubuntu node groups <deploy-managed-node-group>`

Custom EKS deployments
----------------------

For custom configurations, such as GPU-enabled deployments or installing
Kubeflow, refer to these guides:

* :ref:`Enable GPUs on EKS worker nodes <enable-gpus-on-eks>`
* `Install Kubeflow on EKS (external link)`_


.. _`AWS Marketplace`: https://aws.amazon.com/marketplace/search/results?searchTerms=Ubuntu+Pro+eks&CREATOR=565feec9-3d43-413e-9760-c651546613f2&filters=CREATOR
.. _`Install Kubeflow on EKS (external link)`: https://documentation.ubuntu.com/charmed-kubeflow/how-to/install/install-eks/



.. toctree::
   :hidden:
   :maxdepth: 1

   Deploy an Ubuntu cluster <deploy-ubuntu-cluster-with-eks-ami>
   Deploy an Ubuntu Pro cluster <deploy-ubuntu-pro-cluster-with-eks-pro-ami>
   Deploy an Ubuntu Pro FIPS cluster <deploy-ubuntu-pro-fips-cluster>
   Deploy an Ubuntu Pro cluster using tokens <deploy-ubuntu-pro-cluster>
   Deploy a self-managed Ubuntu node group <deploy-self-managed-node-group>
   Deploy managed Ubuntu node groups <deploy-managed-node-group>
   Enable GPUs on EKS <enable-gpus-on-eks>
