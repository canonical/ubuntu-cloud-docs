.. meta::
   :description: List of how-to guides for launching, managing, and upgrading Ubuntu on Azure, including image selection and solution deployment.

How-to guides
=============

These guides provide instructions related to launching and using Ubuntu instances on Azure. They help you to perform different operations related to our products on Azure.

Finding and launching images
----------------------------

Use the Azure CLI to find and launch appropriate images:

* :doc:`Install Azure CLI <instances/install-azure-cli>`
* :doc:`Find images <instances/find-ubuntu-images>`
* :doc:`Launch images <instances/launch-ubuntu-images>`

Upgrades and maintenance
------------------------

Since security is always an important consideration, you might want to check for available security upgrades, install Ubuntu Pro and perform relevant upgrades:

* :doc:`Check for available security updates <instances/check-available-security-updates>`
* :doc:`Get Ubuntu Pro <instances/get-ubuntu-pro>`
* :doc:`Upgrade Ubuntu LTS release <instances/upgrade-ubuntu-lts-release>`

Creating golden images
-----------------------

You can create golden images to simplify your estate management:

* :doc:`Create a Pro golden image <instances/create-pro-fips-golden-image>`
* :doc:`Create a golden image pipeline <instances/create-a-golden-image-pipeline>`

Custom deployments
------------------
If you want to deploy specific solutions like SQL Server and Kubeflow on Azure, use:

* :doc:`Deploy an Ubuntu VM with SQL Server <instances/provision-an-ubuntu-virtual-machine-running-sql-server-in-azure>`
* `Install Kubeflow on AKS (external link)`_
* :doc:`Deploy Kubeflow with AKS spot instances <instances/deploy-kubeflow-pipelines-with-aks-spot-instances>`

.. toctree::
   :hidden:
   :maxdepth: 1

   Install Azure CLI <instances/install-azure-cli>
   Find images <instances/find-ubuntu-images>
   Launch images <instances/launch-ubuntu-images>   
   Check for available security updates <instances/check-available-security-updates>
   Get Ubuntu Pro <instances/get-ubuntu-pro>
   Upgrade Ubuntu LTS release <instances/upgrade-ubuntu-lts-release>
   Create a Pro golden image <instances/create-pro-fips-golden-image>
   Create a golden image pipeline <instances/create-a-golden-image-pipeline>   
   Deploy an Ubuntu VM running SQL Server <instances/provision-an-ubuntu-virtual-machine-running-sql-server-in-azure>
   Deploy Kubeflow with AKS spot instances <instances/deploy-kubeflow-pipelines-with-aks-spot-instances>  
  
.. _`Install Kubeflow on AKS (external link)`: https://documentation.ubuntu.com/charmed-kubeflow/latest/how-to/install/install-aks/

