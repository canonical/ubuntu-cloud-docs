.. meta::
   :description: Learn about Ubuntu on public cloud platforms, including AWS, Azure, Google, IBM, Oracle, and optimized cloud images for enterprise workloads.

.. _index:

Ubuntu on public cloud
======================


**Ubuntu is the world's most popular cloud operating system across public clouds.** Thanks to its security, versatility and policy of regular updates, Ubuntu is the leading cloud guest OS and the only free cloud operating system with the option of enterprise-grade commercial support.

**Optimized and certified Ubuntu images are available for various cloud partners,** such as Amazon AWS, Microsoft Azure, Google Cloud, IBM Cloud and Oracle. By design, these images include an optimized Linux kernel for each cloud, resulting in superior performance and functionality across all instance types and services.

**These images allow easy access to a wide range of cloud-related products and services.** They create a stable and secure cloud platform. A platform that can be used for developing and deploying large-scale production-level software solutions.

**Everyone from individual developers to large enterprises use these Ubuntu images** on the public cloud of their choice. Highly regulated industries from the government, medical and finance sectors, use specific security-certified versions of these images for their workloads.

-----------------------------------------------------------------

Public cloud partners
---------------------

Canonical in collaboration with cloud partners such as Amazon, Google, IBM, Microsoft and Oracle, creates optimized Ubuntu images for each of those clouds. These images are available in the respective marketplaces, and work seamlessly across different platforms within each cloud. 

Canonical continuously tracks and delivers updates to these images, ensuring built-in security and stability. As a result, Ubuntu is the platform of choice on most clouds, both for virtual machines and for container workloads.

For further details, refer to the cloud-specific documentation:

..  grid:: 1 1 2 2
   :padding: 0

   .. grid-item-card:: :ref:`Ubuntu on AWS <aws:index>`   
   .. grid-item-card:: :ref:`Ubuntu on Azure <azure:index>`  
   .. grid-item-card:: :ref:`Ubuntu on GCP <google:index>` 
   .. grid-item-card:: :ref:`Ubuntu on IBM <ibm:index>`
   .. grid-item-card:: :ref:`Ubuntu on Oracle <oracle:index>`
   .. grid-item-card:: :ref:`Ubuntu on VMware <vmware:index>`

-----------------------------------------------------------------


Other Ubuntu images
-------------------

Apart from the specific public clouds, Canonical also produces a variety of Ubuntu images for use in other platforms such as LXD, MAAS, QEMU and OCI container registries.


..  grid:: 1 1 2 2
   :padding: 0

   .. grid-item-card:: :ref:`Ubuntu on OCI container registries <oci:index>`
   .. grid-item-card:: :ref:`Ubuntu Public Images <public-images:index>`



-----------------------------------------------------------------

Tooling
-------

For publishing and maintaining the images, Canonical has created some tools.

..  grid:: 1 1 2 2
   :padding: 0

   .. grid-item-card:: `awspub`_

      A tool for publishing images on AWS and for creating AWS Marketplace versions.


-----------------------------------------------------------------


In this documentation
---------------------

.. list-table::
    :widths: 35 65
    :header-rows: 0

    * - **Ubuntu image specifics**
      - :ref:`Understanding cloud images <understanding-ubuntu-cloud-images>` •
        :ref:`Base and minimal images <ubuntu-base-and-minimal-images>` •
        :ref:`Architecture variants support <architecture-variants>` •
        :ref:`Cloud image release types <release-types>` 

    * - **Security aspects**
      - :ref:`Security in Ubuntu cloud images <security-overview>` •
        :ref:`Check CVE status <check-cve-on-instance>` 
        
    * - **Customizations**
      - :ref:`Install NVIDIA drivers from proposed pocket <install-proposed-nvidia-drivers-for-testing>` •
        :ref:`Confidential computing <confidential-computing>` •
        :ref:`Cloud-init metapackages <cloud-init-metapackages>` 
    

-----------------------------------------------------------------


How this documentation is organized
-----------------------------------

This documentation uses the `Diátaxis documentation structure <https://diataxis.fr/>`__.

* :ref:`How-to guides <all-clouds-how-to-index>` assume you have basic familiarity with Ubuntu cloud images and want to achieve specific goals. They are instructions applicable to applicable to any Ubuntu cloud image, regardless of the cloud platform. 

* :ref:`Explanation <all-clouds-explanation-index>` includes topic overviews, background and context and detailed discussion. These are also applicable across all public cloud platforms.

-----------------------------------------------------------------


Project and community
---------------------

Ubuntu public cloud is open source project that warmly welcomes community projects, contributions, suggestions, fixes and constructive feedback.

Get involved
~~~~~~~~~~~~

* `Get support`_
* `Join our online chat`_
* `Discuss on Matrix`_
* `Start using Ubuntu today`_
* :ref:`contribute-to-these-docs`

Governance and policies
~~~~~~~~~~~~~~~~~~~~~~~
* `Code of conduct`_

.. toctree::
   :hidden:
   :maxdepth: 2
   
   all-clouds-how-to/index
   all-clouds-explanation/index
   all-clouds-how-to/contribute-to-these-docs
      

.. _awspub: https://canonical-awspub.readthedocs-hosted.com/
.. _Get support: https://ubuntu.com/cloud/public-cloud
.. _Join our online chat: https://discourse.ubuntu.com/c/project/public-cloud/176
.. _Discuss on Matrix: https://matrix.to/#/#ubuntu-cloud:ubuntu.com
.. _Start using Ubuntu today: https://ubuntu.com/download/cloud
.. _Code of conduct: https://ubuntu.com/community/docs/ethos/code-of-conduct
