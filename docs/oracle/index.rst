.. meta::
   :description: Discover Ubuntu on Oracle Cloud, including optimized images, deployment guides, and best practices for cloud workloads.
   
Ubuntu on Oracle
================

**Ubuntu on Oracle is a set of customized Ubuntu images** that allow easy access to a wide range 
of products and services - offered by both Oracle Cloud and Canonical. These images have an optimized
kernel that boots faster, has a smaller footprint and includes Oracle-specific drivers.

**These images provide a foundation for deploying cloud-based software solutions,** specifically
for software built on Ubuntu and running on Oracle Cloud. They focus on providing the optimal tools 
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
      - :doc:`Oracle optimizations <oracle-explanation/canonical-offerings>` • :doc:`Security overview <oracle-explanation/security-overview>` 
      
    * - **Finding and launching images**
      - :doc:`Find images <oracle-how-to/find-ubuntu-images>` • :doc:`Use a bastion to access <oracle-how-to/use-bastion-to-access-VM>` 
      
    * - **Upgrades and maintenance**
      - :doc:`Upgrade from Ubuntu 20.04 to 22.04 <oracle-how-to/upgrade-from-focal-to-jammy>` • :doc:`Upgrade from Ubuntu 22.04 to 24.04 <oracle-how-to/upgrade-from-jammy-to-noble>`
      
    * - **Deploying Ubuntu OKE worker nodes**
      - :doc:`Availability details <oracle-reference/ubuntu-availability-on-oke>` • :doc:`Deploy using Oracle Cloud Console <oracle-how-to/deploy-ubuntu-oke-nodes-using-console>` • :doc:`Deploy using CLI <oracle-how-to/deploy-ubuntu-oke-nodes-using-cli>` • :doc:`Deploy using Terraform <oracle-how-to/deploy-ubuntu-oke-nodes-using-terraform>` 

    * - **Custom deployments**
      - :doc:`Use full-disk encryption <oracle-how-to/use-fde>` • :doc:`Enable confidential computing <oracle-how-to/enable-confidential-computing>` 

   

How this documentation is organized
------------------------------------


This documentation uses the `Diátaxis documentation structure <https://diataxis.fr/>`__.

* :doc:`How-to guides  <oracle-how-to/index>` assume you have basic familiarity with Ubuntu images on Oracle Cloud and want to achieve specific goals. They are instructions covering key operations and common tasks involving the use of Ubuntu images on Oracle Cloud.

* :doc:`Explanation <oracle-explanation/index>` includes topic overviews, background and context and detailed discussion. These include key topics, such as our offerings on Oracle Cloud, Ubuntu on OKE nodes and an overview of available security features. 


---------

Project and community
---------------------

Ubuntu on Oracle is a member of the Ubuntu family and the project warmly welcomes 
community projects, contributions, suggestions, fixes and constructive feedback.

Get involved
~~~~~~~~~~~~
	
* `Get support`_
* `Join our online chat`_
* `Discuss on Matrix`_
* :doc:`oracle-how-to/contribute-to-these-docs`

Governance and policies
~~~~~~~~~~~~~~~~~~~~~~~

* `Code of conduct`_

.. toctree::
   :hidden:
   :maxdepth: 2

   oracle-how-to/index
   oracle-explanation/index
   oracle-reference/ubuntu-availability-on-oke
   oracle-how-to/contribute-to-these-docs

.. _Ubuntu release cycle: https://ubuntu.com/about/release-cycle
.. _Get support: https://ubuntu.com/cloud/public-cloud
.. _Join our online chat: https://discourse.ubuntu.com/c/project/public-cloud/176
.. _`Discuss on Matrix`: https://matrix.to/#/#ubuntu-cloud:ubuntu.com
.. _Code of conduct: https://ubuntu.com/community/docs/ethos/code-of-conduct

