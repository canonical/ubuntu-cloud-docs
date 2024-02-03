Ubuntu on Oracle
================

**Ubuntu on Oracle is a set of customised Ubuntu images** that allow easy access to a wide range 
of products and services - offered by both Oracle Cloud and Canonical. These images have an optimised
kernel that boots faster, has a smaller footprint and includes Oracle-specific drivers.

**These images provide a foundation for deploying cloud-based software solutions,** specifically
for software built on Ubuntu and running on Oracle Cloud. They focus on providing the optimal tools 
and features needed to run specific workloads.

.. include:: ../reuse/common-intro.txt
   :start-after: Start: Product need and user
   :end-before: End: Product need and user

----------

Canonical's offerings on Oracle Cloud
-------------------------------------

Canonical builds optimised and certified server images for Oracle Cloud. The images are shared with Oracle privately, who publishes them into the cloud platform once per month. The set of images include:

* All LTS releases still covered by standard security maintenance (see the `Ubuntu release cycle`_)
* Full and minimal versions of the images
* Versions for x86_64 and AArch64 (ARM64) platforms

The customised images include the ``linux-oracle`` flavor of our kernel. This kernel enables fast networking and boot by taking advantage of the native hardware, while supporting the live migration of Ubuntu guests. The arm64 version of the kernel also takes advantage of the unique features of Ampere native CPUs.

The Ubuntu LTS instances can also be attached to Ubuntu Pro subscriptions. This enables access to enterprise lifecycle, kernel livepatching, CIS compliance automation tooling, and FIPS 140 certified cryptography.

----------

How-to guides
-------------
Instructions for some of the basic operations that you would perform on an Oracle Cloud virtual machine:

* :doc:`Find images <./oracle-how-to/find-ubuntu-images>`
* :doc:`Use a bastion for access <./oracle-how-to/use-bastion-to-access-VM>`
* :doc:`./oracle-how-to/upgrade-from-focal-to-jammy`
* :doc:`./oracle-how-to/use-fde`


----------

Project and community
---------------------

Ubuntu on Oracle is a member of the Ubuntu family and the project warmly welcomes 
community projects, contributions, suggestions, fixes and constructive feedback.

* `Get support`_
* `Join our online chat`_
* `Discuss on IRC`_
* :doc:`oracle-how-to/contribute-to-these-docs`
* `Code of conduct`_

.. toctree::
   :hidden:
   :maxdepth: 2

   Find images <oracle-how-to/find-ubuntu-images>
   Use a bastion for access <oracle-how-to/use-bastion-to-access-VM>
   oracle-how-to/upgrade-from-focal-to-jammy
   oracle-how-to/use-fde
   oracle-how-to/contribute-to-these-docs

.. _Ubuntu release cycle: https://ubuntu.com/about/release-cycle
.. _Get support: https://ubuntu.com/cloud/public-cloud
.. _Join our online chat: https://discourse.ubuntu.com/c/public-cloud/176
.. _`Discuss on IRC`: https://web.libera.chat/#ubuntu-cloud
.. _Code of conduct: https://ubuntu.com/community/ethos/code-of-conduct

