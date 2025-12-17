Canonical's offerings on Azure
==============================

Ubuntu images
-------------

Canonical produces a wide variety of Ubuntu images to support numerous features found on Azure.

* `Server images`_ are general-purpose images customized for Azure Virtual Machines. These images are also available with `Ubuntu Pro`_ enabled.

* :doc:`Minimal images <all-clouds:all-clouds-explanation/ubuntu-base-and-minimal-images>` are designed for automated deployment at scale with a reduced default package set. Things like interactive usage tools are omitted. They are much smaller, boot faster, and require fewer security updates over time due to the fewer installed packages. These images are also available with `Ubuntu Pro`_ enabled.

* `Confidential Virtual Machine (CVM) images`_ provide enhanced security features designed to protect data at rest, in use, and during boot. CVM images are intended for use with Azure's confidential computing capabilities using hardware-enabled security features. These images are also available with `Ubuntu Pro`_ enabled.

* GB200-Compatible Server images are optimized for AI and designed to run on `NVIDIA GB200 hardware`_. These images are also available with `Ubuntu Pro`_ enabled.

* `Ubuntu Pro images`_ are premium images that include comprehensive security coverage for at least ten years, `kernel Livepatch service`_, and optional `24/7 enterprise-grade support`_. Additional Pro entitlements such as `FIPS-certified modules`_ and the `Ubuntu Security Guide`_ are also available to install.

* `Ubuntu Pro FIPS images`_ are built on Ubuntu Pro, but with the FIPS-certified modules pre-installed so that they are used from the first boot of the image. Intended for high-security or government usage.

* `Ubuntu Pro Minimal CIS images`_ are built on Ubuntu Pro and are CIS-hardened with a minimal footprint to maximize security. These images are available with CIS Level 1 or CIS Level 2 hardening.

The availability of each of these images and the means to find them on Azure can be found `here <https://documentation.ubuntu.com/azure/azure-how-to/instances/find-ubuntu-images/>`_.

Optimizations for Azure
-----------------------

Integration with Azure systems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ubuntu on Azure cloud integrates with the Systems Manager, ensuring that system management tools work natively for instances on the platform. This includes everything from Azure Update Manager and Security Center, to Azure Policy, to using Azure AD to manage your SSH logins. A number of Microsoft products are built on Ubuntu, such as Azure Kubernetes Service and Databricks.

Customized kernel
~~~~~~~~~~~~~~~~~

The ``linux-azure`` kernel enables accelerated networking for the InfiniBand capable instances, as well as consistent support for the Single Root I/O Virtualization (SR-IOV) on the present hardware, enabling network traffic to bypass the virtualization stack and achieve almost native performance. It comes with FPGA support out of the box, taking advantage of Project Catapult to provide performance without the cost and complexity of a custom ASIC.

Kernel variants
+++++++++++++++

In addition to the default ``linux-azure`` kernel on Azure, Canonical produces kernel variants:

- ``linux-azure-fde``: Enables support for Azure Confidential Compute and is installed in :ref:`Ubuntu CVM images <azure-cvms>`.
- ``linux-azure-nvidia``: The kernel for GB200-Compatible Server images to enable support for `NVIDIA GB200 hardware`_.
- ``linux-azure-fips``: The FIPS-compliant kernel for Ubuntu images on Azure. Installed in `Ubuntu Pro FIPS images`_.

Collaborative Optimizations
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. `Anbox on Azure`_, that allows users to run Android apps on Azure at scale
#. Collaboration with Azure's AKS team to support the `Azure Kubernetes worker node`_ image, as these worker nodes nearly always run Ubuntu
#. Collaboration with the Azure Guest Patching Service and Update Manager teams to ensure simple security patch management for users
#. Collaboration with the .Net team on `Chiseled .Net images`_ that have a smaller size and security cross-section
#. `Landscape on Azure`_, for managing your Ubuntu deployments at scale

.. _`Server images`: https://ubuntu.com/azure
.. _`Ubuntu Pro`: https://ubuntu.com/azure/pro
.. _`Minimal images`: https://documentation.ubuntu.com/public-cloud/all-clouds-explanation/ubuntu-base-and-minimal-images/
.. _`Confidential Virtual Machine (CVM) images`: http://documentation.ubuntu.com/azure/azure-explanation/security-overview/#confidential-virtual-machines-cvms
.. _`NVIDIA GB200 hardware`: https://learn.microsoft.com/en-us/azure/virtual-machines/sizes/gpu-accelerated/nd-gb200-v6-series?tabs=sizebasic
.. _`Ubuntu Pro images`: https://ubuntu.com/azure/pro
.. _`kernel Livepatch service`: https://ubuntu.com/security/livepatch
.. _`24/7 enterprise-grade support`: https://ubuntu.com/azure/support
.. _`FIPS-certified modules`: https://documentation.ubuntu.com/security/compliance/fips/fips-overview/
.. _`Ubuntu Security Guide`: https://documentation.ubuntu.com/security/compliance/usg/
.. _`Ubuntu Pro FIPS images`: https://ubuntu.com/azure/fips
.. _`Ubuntu Pro Minimal CIS images`: https://ubuntu.com/security/cis
.. _`Anbox on Azure`: https://documentation.ubuntu.com/anbox-cloud/howto/install-appliance/install-on-azure/
.. _`Azure Kubernetes worker node`: http://documentation.ubuntu.com/azure/azure-explanation/ubuntu-on-aks-worker-nodes
.. _`Chiseled .Net images`: https://devblogs.microsoft.com/dotnet/dotnet-6-is-now-in-ubuntu-2204
.. _`Landscape on Azure`: https://documentation.ubuntu.com/landscape/how-to-guides/landscape-installation-and-set-up/cloud-providers/install-on-microsoft-azure/
