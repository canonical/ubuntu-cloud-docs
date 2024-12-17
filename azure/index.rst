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

..  grid:: 1 1 2 2
   :padding: 0

   ..  grid-item:: :doc:`How-to guides <azure-how-to/index>`

      **Step-by-step guides** covering key operations and common tasks

   .. grid-item:: :doc:`Explanation <azure-explanation/index>`

      **Discussion and clarification** of key topics, such as security features and our image retention policy.

---------

Canonical's offerings
---------------------

**Integration with Azure systems** - Ubuntu on Azure cloud integrates with the Systems Manager, ensuring that system management tools work natively for instances on the platform. This includes everything from Azure Update Manager and Security Center, to Azure Policy, to using Azure AD to manage your SSH logins. A number of Microsoft products are built on Ubuntu, such as Azure Kubernetes Service, Databricks, and `SQL Server on Ubuntu Pro`_, which includes end-to-end joint support. Furthermore Canonical is working with Microsoft to bring confidential VMs on the cloud on Ubuntu Advantage and Pro. You can find more information on the public preview of `AMD-based Confidential VMs`_.

**Customized kernel** - The ``linux-azure`` kernel enables accelerated networking for the InfiniBand capable instances, as well as consistent support for the Single Root I/O Virtualization (SR-IOV) on the present hardware, enabling network traffic to bypass the virtualization stack and achieve almost native performance. It comes with FPGA support out of the box, taking advantage of project catapult to provide performance without the cost and complexity of a custom ASIC.

Some other offerings include:

1. Ubuntu server and Ubuntu Pro for all supported LTS versions across all Azure architectures, including ARM
#. Minimal Ubuntu images for Independent Software Vendors and others who want to build on Azure
#. Ubuntu Pro FIPS images that allow US government Ubuntu users to easily move their workloads to Azure
#. Pre-hardened (CIS) Ubuntu minimal images, for those who want best security practices for Ubuntu out of the box
#. The only commercial Linux launch partner for Azure's Confidential Computing platform (both AMD SEV-SNP and TDX)
#. SQL Server on Ubuntu Pro images that include specific SQL-related OS optimizations and joint support from Canonical and Microsoft
#. Anbox on Azure, that allows users to run Android apps on Azure at scale
#. Collaboration with Azure's AKS team to support the Azure Kubernetes worker node image, as these worker nodes nearly always run Ubuntu
#. Collaboration with the Azure Guest Patching Service and Update Manager teams to ensure simple security patch management for users
#. Collaboration with the .Net team on `Chiseled .Net images`_ that have a smaller size and security cross-section 


---------

Project and community
---------------------

Ubuntu on Azure is a member of the Ubuntu family and the project warmly welcomes community projects, 
contributions, suggestions, fixes and constructive feedback.

* `Get support`_
* `Join our online chat`_
* `Discuss on IRC`_
* `Talk to us about Ubuntu on Azure`_
* :doc:`azure-how-to/contribute-to-these-docs`
* `Code of conduct`_


.. toctree::
   :hidden:
   :maxdepth: 2

   azure-how-to/index
   azure-explanation/index


.. _SQL Server on Ubuntu Pro: https://azuremarketplace.microsoft.com/en-us/marketplace/apps/microsoftsqlserver.sql2019-ubuntupro2004?tab=Overview
.. _AMD-based Confidential VMs: https://techcommunity.microsoft.com/blog/azureconfidentialcomputingblog/azure-confidential-vms-dcasv5ecasv5-using-amd-sev-snp-processors-are-now-general/2993530
.. _Chiseled .Net images: https://devblogs.microsoft.com/dotnet/dotnet-6-is-now-in-ubuntu-2204
.. _Get support: https://ubuntu.com/cloud/public-cloud
.. _Join our online chat: https://discourse.ubuntu.com/c/public-cloud/azure/178
.. _`Discuss on IRC`: https://web.libera.chat/#ubuntu-cloud
.. _Talk to us about Ubuntu on Azure: https://ubuntu.com/azure#get-in-touch
.. _Code of conduct: https://ubuntu.com/community/ethos/code-of-conduct
