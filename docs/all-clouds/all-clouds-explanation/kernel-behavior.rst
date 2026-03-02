.. _kernel-behavior:

Rolling kernel model
====================

By default, Ubuntu images use a **rolling kernel model**, which provides the latest upstream bug fixes and performance improvements around task scheduling, I/O scheduling, networking, hypervisor guests and containers. A rolling kernel model transitions the default kernel from one base version to the next as part of its regular patching cycle. That new kernel, called the `Hardware Enablement (HWE) Kernel`_ is the kernel of the latest Ubuntu release.

For example, users running Ubuntu 24.04 LTS instances launched in early 2024 started with the 6.8 kernel by default. However, as new Ubuntu interim versions are released and the kernel patching cycle continues, the kernel "rolls" forward to the next available kernel version. Consequently, an Ubuntu 24.04 LTS instance launched at a later point in time—such as in 2025 or 2026—will include a different kernel version depending on when it was launched; for instance, it might feature version 6.11 or 6.14.

For more details about the rolling kernel model, refer to the `Ubuntu kernel release cycle`_ and the relevant `installation options`_.


Basic kernel packages
+++++++++++++++++++++

On each LTS release on each Ubuntu-supported cloud provider, there are at least 3 kernel variants accessible to the user while the release and kernels are under standard support. These are general-purpose kernels designated for Ubuntu Server and Ubuntu Minimal images and are optimized for use on each cloud.


Rolling kernel package
----------------------

The rolling kernel package (``linux-<cloud>``) is the default kernel package and follows the aforementioned rolling kernel model.


Installation instructions
_________________________

.. code-block:: bash

   # substitute <cloud> for one of: aws azure gcp gke oracle
   sudo apt install linux-<cloud>

If a new kernel is available, the command will notify you, and you can reboot to upgrade to the newest kernel.

.. note:: If you were previously using the ``-edge`` kernel package, you may be on a newer kernel than is available with the ``linux-<cloud>`` package, so you may need to modify your grub behavior through your cloud provider or via manual re-configuration on your virtual machine. Otherwise, grub will default to the newest installed kernel by version, and the rolling kernel package will stay as the ``-edge`` kernel until the next greater HWE kernel version is available in ``linux-<cloud>``.


General Availability (GA) package
---------------------------------

The General Availability (GA) kernel package (``linux-<cloud>-lts-<release>``) maintains the stable kernel associated to a specific release for the standard support lifetime of the release. The GA kernel is more stable than the HWE kernel since it is the accumulation of multiple HWE kernels and is highly scrutinized since the GA package is only produced every 2 years alongside LTS releases. This kernel does not usually receive major kernel upgrades, and is generally limited to bug, security, and performance patches.


Installation instructions
_________________________

.. code-block:: bash

   # substitute <cloud> for one of: aws azure gcp gke oracle
   # substitute <release> with the LTS version number (i.e. 24.04)
   sudo apt install linux-<cloud>-lts-<release>

If a new kernel is available, the command will notify you, and you can reboot to upgrade to the newest kernel. If you are launching

.. note:: If you are launching a virtual machine after the first HWE kernel is available via the ``linux-<cloud>`` package, you will need to modify your grub behavior through your cloud provider or via manual re-configuration on your virtual machine in order to revert to the GA kernel version and then reboot onto the older kernel version. To be safe, you should also purge the previously installed kernel. Otherwise, grub's default behavior is to install the newest kernel by version, and the GA kernel package will never receive a kernel version greater than the HWE kernel version.


Early access HWE package
------------------------

The early access HWE kernel package (``linux-<cloud>-edge``) gives users the ability to experiment with the next HWE kernel before it is adopted into the rolling kernel package. Using this package can allow users to test a new kernel before their deployment (without the ``-edge`` kernel) automatically upgrades to it via the default rolling kernel package. These kernels are still fully supported, but are less exposed to real world use cases since they are relatively new.


Installation instructions
_________________________

.. code-block:: bash

   # substitute <cloud> for one of: aws azure gcp gke oracle
   sudo apt install linux-<cloud>


.. _`Hardware Enablement (HWE) Kernel`: https://canonical-kernel-docs.readthedocs-hosted.com/latest/reference/hwe-kernels/
.. _`Ubuntu kernel release cycle`: https://ubuntu.com/about/release-cycle#ubuntu-kernel-release-cycle
.. _`installation options`: https://ubuntu.com/kernel/lifecycle
