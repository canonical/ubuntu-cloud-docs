Ubuntu on Oracle
================

**Ubuntu on Oracle is a set of customised Ubuntu images** that allow easy access to a wide range 
of products and services - offered by both Oracle cloud and Canonical. These images have an optimised
kernel that boots faster, has a smaller footprint and includes Oracle-specific drivers.

**These images provide a foundation for deploying cloud-based software solutions,** specifically
for software built on Ubuntu and running on Oracle cloud. They focus on providing the optimal tools 
and features needed to run specific workloads.

.. include:: ../reuse/common-intro.txt
   :start-after: Start: Product need and user
   :end-before: End: Product need and user

----------

Canonical's offerings on Oracle cloud
-------------------------------------

Customised Ubuntu images for Oracle cloud include the ``linux-oracle`` flavor of our kernel. This kernel enables fast networking and boot by taking advantage of the native hardware, while supporting the live migration of Ubuntu guests. The arm64 version of the kernel also takes advantage of the unique features of Ampere native CPUs.

Ubuntu LTS instances on Oracle cloud can be attached to Ubuntu Advantage subscriptions. This enables access to enterprise lifecycle, kernel livepatching, CIS compliance automation tooling, and FIPS 140 certified cryptography.

----------

How-to guide
-------------
Instructions for upgrading from Ubuntu 20.04 to 22.04 on Oracle cloud virtual machines: :doc:`./oracle-how-to/upgrade-from-focal-to-jammy`


----------

Project and community
---------------------

Ubuntu on Oracle is a member of the Ubuntu family and the project warmly welcomes 
community projects, contributions, suggestions, fixes and constructive feedback.

* `Code of conduct`_
* `Get support`_
* `Join our online chat`_


.. toctree::
   :hidden:
   :maxdepth: 2

   oracle-how-to/upgrade-from-focal-to-jammy

   
.. _Code of conduct: https://ubuntu.com/community/ethos/code-of-conduct
.. _Get support: https://ubuntu.com/cloud/public-cloud
.. _Join our online chat: https://discourse.ubuntu.com
