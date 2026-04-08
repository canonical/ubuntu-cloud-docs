.. meta::
   :description: Discover Ubuntu on Azure, including optimized images, deployment guides, technical reference, and best practices for cloud workloads.

Ubuntu on Azure
===============

**Ubuntu on Azure is a set of customized Ubuntu images** that allow easy access to a wide range 
of products and services - offered by both Microsoft Azure and Canonical. These images have an optimized
kernel that boots faster, has a smaller footprint and includes Azure-specific drivers.

**These images provide a foundation for deploying cloud-based software solutions,** specifically
for software built on Ubuntu and running on Azure. They focus on providing the optimal tools 
and features needed to run specific workloads.

.. include:: ../reuse/common-intro.txt
   :start-after: Start: Product need and user
   :end-before: End: Product need and user


---------


In this documentation
---------------------

.. list-table::
    :widths: 35 65
    :header-rows: 0

    * - **Canonical's offerings**
      - :doc:`Azure optimizations <azure-explanation/canonical-offerings>` • :doc:`Ubuntu on AKS <azure-explanation/ubuntu-on-aks-worker-nodes>` • :doc:`Support options <azure-reference/support>` • :doc:`Packages maintained <azure-explanation/packages>` • :doc:`Understanding Ubuntu on Azure <azure-explanation/understanding-ubuntu-on-azure>` 
      
    * - **Finding and launching images**
      - :doc:`Install Azure CLI <azure-how-to/instances/install-azure-cli>` • :doc:`Find images <azure-how-to/instances/find-ubuntu-images>` • :doc:`Launch images <azure-how-to/instances/launch-ubuntu-images>` 
      
    * - **Upgrades and maintenance**
      - :doc:`Check for available security updates <azure-how-to/instances/check-available-security-updates>` • :doc:`Get Ubuntu Pro <azure-how-to/instances/get-ubuntu-pro>` • :doc:`Upgrade Ubuntu LTS release <azure-how-to/instances/upgrade-ubuntu-lts-release>` 
      
    * - **Creating golden images**
      - :doc:`Create a Pro golden image <azure-how-to/instances/create-pro-fips-golden-image>` • :doc:`Create a golden image pipeline <azure-how-to/instances/create-a-golden-image-pipeline>` 

    * - **Custom deployments**
      - :doc:`Deploy an Ubuntu VM with SQL Server <azure-how-to/instances/provision-an-ubuntu-virtual-machine-running-sql-server-in-azure>` • `Install Kubeflow on AKS <https://documentation.ubuntu.com/charmed-kubeflow/latest/how-to/install/install-aks/>`_ • :doc:`Deploy Kubeflow with AKS spot instances <azure-how-to/instances/deploy-kubeflow-pipelines-with-aks-spot-instances>` 
      
    * - **Policies**
      - :doc:`Security aspects <azure-explanation/security-overview>` • :doc:`Image retention policy <azure-explanation/image-rentention-policy>`  



How this documentation is organized
------------------------------------


This documentation uses the `Diátaxis documentation structure <https://diataxis.fr/>`__.

* :doc:`How-to guides  <azure-how-to/index>` assume you have basic familiarity with Ubuntu images on Azure and want to achieve specific goals. They are instructions covering key operations and common tasks involving the use of Ubuntu on Azure.

* :doc:`Explanation <azure-explanation/index>` includes topic overviews, background and context and detailed discussion. These include key topics, such as our offerings, security features, package maintenance our image retention policy.

---------

Project and community
---------------------

Ubuntu on Azure is a member of the Ubuntu family and the project warmly welcomes community projects, contributions, suggestions, fixes and constructive feedback.

Get involved
~~~~~~~~~~~~

* `Get support`_
* `Join our online chat`_
* `Discuss on Matrix`_
* `Talk to us about Ubuntu on Azure`_
* :doc:`azure-how-to/contribute-to-these-docs`

Governance and policies
~~~~~~~~~~~~~~~~~~~~~~~

* `Code of conduct`_


.. toctree::
   :hidden:
   :maxdepth: 2

   azure-how-to/index
   azure-explanation/index
   azure-reference/support
   azure-how-to/contribute-to-these-docs

.. _Get support: https://ubuntu.com/cloud/public-cloud
.. _Join our online chat: https://discourse.ubuntu.com/c/project/azure/178
.. _`Discuss on Matrix`: https://matrix.to/#/#ubuntu-cloud:ubuntu.com
.. _Talk to us about Ubuntu on Azure: https://ubuntu.com/azure#get-in-touch
.. _Code of conduct: https://ubuntu.com/community/docs/ethos/code-of-conduct
