
.. meta::
   :description: Learn about Ubuntu kernel packages on the cloud, including how kernel updates work, and the differences between rolling and LTS kernel variants.
   
.. _kernels-on-the-cloud:

Kernels on the cloud
====================

Basic kernel packages
+++++++++++++++++++++

Each Ubuntu image is built with a pre-installed kernel meta-package. That meta-package determines which kernels are installed via ``unattended-upgrades`` or ``sudo apt update && sudo apt upgrade``. When a new kernel package is available and the instance fetches the archive, the meta-package is updated to the new kernel version, which triggers the installation of all kernel image and modules associated to that new version.

.. note:: After a new kernel version is installed, the instance must be rebooted in order to run the new kernel. Otherwise, the only way to receive kernel updates without rebooting or redeploying is through the `live-patch service on Ubuntu Pro`_, but this is generally limited to security-related patching.

The default meta-package, or kernel variant, for most Ubuntu cloud images is the :ref:`rolling kernel variant <rolling-kernel>`. However, some images may default to another variant specific to the product. For instance, Ubuntu Pro FIPS images default to a cloud-specific variant tailored to the FIPS environment. Different clouds provide and support different variants, but the common packages are listed below.

.. _rolling-kernel:

Rolling kernel package
----------------------

The rolling kernel package (``linux-<cloud>``) is the default kernel package for *most* Ubuntu cloud images and follows a **rolling kernel model**.

This model provides the latest upstream bug fixes and performance improvements around task scheduling, I/O scheduling, networking, hypervisor guests and containers. A rolling kernel model transitions the default kernel from one major version to the next as new kernels are released with interim Ubuntu releases. This rolling kernel package is commonly referred to as the `Hardware Enablement (HWE) Kernel`_.

This package is the default for at least Ubuntu Server and Ubuntu Minimal images across all clouds.

.. note:: Some Ubuntu images do not use this package by default. Products like Ubuntu Pro FIPS and Ubuntu CVM generally have specifically tailored kernel variants that do not follow the rolling kernel model, and instead focus on bug fixes and performance updates to ensure more environmental stability for that product, similar to the behavior of the :ref:`LTS kernel package <lts-kernel>`.

How kernel rolling works
________________________

Each Ubuntu LTS release has an HWE package associated to it that upgrades to new major kernel versions as they become available. When the HWE kernel package is installed on a given LTS image, each subsequent Ubuntu release introduces a new kernel to the rolling kernel package. This cycle continues until the next LTS Ubuntu release. Soon after that point, the kernel will stop rolling, and will maintain the major version of the kernel associated to the new LTS release.

For example, the final HWE kernel for Ubuntu 22.04 was version 6.8, whereas the first HWE kernel for Ubuntu 24.04 was version 6.8. Ubuntu 25.04 released with kernel version 6.14. This kernel version eventually promoted to the HWE package, and then the Ubuntu 24.04 HWE kernel version rolled to kernel version 6.14. Similarly, the release of Ubuntu 25.10 came with kernel version 6.17. This kernel version eventually promoted to the HWE kernel package, and then 24.04 HWE kernel rolled to kernel version 6.17.

Note that this is a general guideline and the exact dates on which kernels roll across the clouds is dependent on a number of external factors.

For more details about the rolling kernel model, refer to the `Ubuntu kernel release cycle`_ and the relevant `installation options`_ as well as the `Hardware Enablement (HWE) Kernel`_ page.

.. _lts-kernel:

LTS package
-----------

The LTS kernel package (``linux-<cloud>-lts-<release>``) maintains the stable kernel associated to a specific release for the standard support lifetime of the release. This package behaves in a manner similar to the ``linux-generic`` kernel package. The only difference is that there are no cloud-specific enhancements in the ``linux-generic`` package.

The LTS kernel is more stable than the HWE kernel since it is the accumulation of multiple HWE kernels and is highly scrutinized since the LTS package is only produced every 2 years alongside LTS releases. This kernel does not usually receive feature upgrades, and is generally limited to bug, security, and performance patches.

.. _edge-kernel:

Early access HWE package
------------------------

The early access HWE kernel package (``linux-<cloud>-edge``) gives users the ability to experiment with the next HWE kernel before it is adopted into the rolling kernel package. Using this package can allow users to test a new kernel before their deployment (without the ``-edge`` kernel) automatically upgrades to it via the default rolling kernel package. These kernels are still fully supported, but are less exposed to real world use cases since they are relatively new.

Installing kernel packages
++++++++++++++++++++++++++

The package names are listed above in each kernel section such that you can replace the following as applicable to derive the exact package name:

- ``<cloud>`` with one of ``azure``, ``aws``, ``gcp``, ``gke``, ``oracle``
- ``<release>`` with the LTS release number corresponding to your instance (i.e. ``22.04`` or ``24.04``)

Given each kernel package receives updates as kernels become available, it is best to follow the walk-through in the :ref:`migrate-kernel-variants` document to ensure you receive updates from the intended kernel package.

.. _`live-patch service on Ubuntu Pro`: https://ubuntu.com/security/livepatch
.. _`Hardware Enablement (HWE) Kernel`: https://canonical-kernel-docs.readthedocs-hosted.com/latest/reference/hwe-kernels/
.. _`Ubuntu kernel release cycle`: https://ubuntu.com/about/release-cycle#ubuntu-kernel-release-cycle
.. _`installation options`: https://ubuntu.com/kernel/lifecycle
