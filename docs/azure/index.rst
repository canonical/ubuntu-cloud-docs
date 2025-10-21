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

      **Step-by-step guides** covering key operations and common tasks involving the use of Ubuntu images on Azure.

   .. grid-item:: :doc:`Explanation <azure-explanation/index>`

      **Discussion and clarification** of key topics, such as security features, Ubuntu on AKS nodes and our image retention policy.

---------

Azure-optimized Ubuntu images
-----------------------------

Ubuntu images are specifically fine-tuned to maximize performance on Azure infrastructure and support the latest cloud features as they are released. The images integrate with core Azure services, such as Azure Pricing, Azure Guest Patching Service (AzGPS), and Update Management Center.

* **Server images**: General-purpose customized images based on an Azure-optimized kernel. 

* **Minimal server images** - Images designed for automated deployment at scale with a reduced default package set.

* **Ubuntu Pro images** - Premium images that include optional FIPS certified components, CIS hardening options, ESM-enabled comprehensive open source security coverage for up to 12 years, Kernel Livepatch service, estate management service through Landscape and an optional 24/7 enterprise-grade support. 

* **Ubuntu Pro FIPS images** - Images built on Ubuntu Pro, but with the FIPS-certified modules pre-enabled so that it's easier for users moving their workload to Azure to avail FIPS coverage from first boot of the image.

* **CIS hardened images** - Pre-hardened (CIS) Ubuntu Pro minimal images, designed for those who want to implement security best practices for Ubuntu out of the box.

* **Confidential VM images** - Confidential-compute capable images that support chipsets from both AMD SEV-SNP and Intel TDX.

* **NVIDIA VM images** - Images optimized for use in virtual machines running on NVIDIA GB200 hardware.



More details are available in our explanation about :doc:`azure-explanation/canonical-offerings`

---------

Project and community
---------------------

Ubuntu on Azure is a member of the Ubuntu family and the project warmly welcomes community projects, 
contributions, suggestions, fixes and constructive feedback.

* `Get support`_
* `Join our online chat`_
* `Discuss on Matrix`_
* `Talk to us about Ubuntu on Azure`_
* :doc:`azure-how-to/contribute-to-these-docs`
* `Code of conduct`_


.. toctree::
   :hidden:
   :maxdepth: 2

   azure-how-to/index
   azure-explanation/index
   azure-how-to/contribute-to-these-docs

.. _Get support: https://ubuntu.com/cloud/public-cloud
.. _Join our online chat: https://discourse.ubuntu.com/c/project/azure/178
.. _`Discuss on Matrix`: https://matrix.to/#/#ubuntu-cloud:ubuntu.com
.. _Talk to us about Ubuntu on Azure: https://ubuntu.com/azure#get-in-touch
.. _Code of conduct: https://ubuntu.com/community/docs/ethos/code-of-conduct
