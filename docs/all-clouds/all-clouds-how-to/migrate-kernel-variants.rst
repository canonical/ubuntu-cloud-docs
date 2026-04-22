.. meta::
   :description: Step-by-step guide to migrating between Ubuntu kernel variants on the cloud, such as switching from a rolling kernel to an LTS kernel package.

.. _migrate-kernel-variants:

Migrate kernel variants
=======================

There are many scenarios in which you may want to migrate to a different kernel variant than what is currently installed on your virtual machine.

For more information about kernel behaviors on the cloud and why it may be desirable to install a different kernel variant, see :ref:`kernels-on-the-cloud`.

Walk-through
++++++++++++

.. note::
   | This workflow is not intended to be used at scale. This should be done as part of the deployment process for a new instance or as part of creating a golden image. Pre-existing instances may require additional manual intervention to address incompatibilities.

In this example, we assume you have launched an Ubuntu instance on Azure. You started on the ``linux-azure`` kernel package by default and want to migrate to the ``linux-azure-lts-22.04`` kernel package.

.. note::
   | This workflow is identical for all clouds and LTS releases given you replace ``azure`` with the specified cloud (``aws``, ``gcp``, ``gke``, ``oracle``) and ``22.04`` with the LTS release version you are running.
   |
   | You may also find yourself migrating to/from a different kernel variant. The steps are the same as long as you replace ``linux-azure`` with your current kernel variant and ``linux-azure-lts-22.04`` with your target kernel variant.

The kernel versions used in this example are purely for reference. The exact versions in your commands and outputs will be different depending on the cloud, release, and targeted packages.

Get current status
------------------

First, you need to determine which kernel package(s) and version(s) are currently installed on your instance.

Find the currently booted kernel version:

.. code-block:: bash

   uname -r

You should see something like:

.. code-block::

   6.8.0-1051-azure

Find which kernel packages are installed (assuming azure in this example):

.. code-block:: bash

   dpkg --list | grep linux-azure | grep ii

It will output currently installed packages associated to individual kernel versions as well as the kernel package. You'll see something like:

.. code-block::

   ii  linux-azure                            6.8.0-1051.57~22.04.1                   amd64        Complete Linux kernel for Azure systems (vmlinuz).
   ii  linux-azure-6.8-cloud-tools-6.8.0-1051 6.8.0-1051.57~22.04.1                   amd64        Linux kernel version specific cloud tools for version 6.8.0-1051
   ii  linux-azure-6.8-headers-6.8.0-1051     6.8.0-1051.57~22.04.1                   all          Header files related to Linux kernel version 6.8.0
   ii  linux-azure-6.8-tools-6.8.0-1051       6.8.0-1051.57~22.04.1                   amd64        Linux kernel version specific tools for version 6.8.0-1051

Note that ``linux-azure`` is listed on the top line, indicating that the HWE kernel package is installed, and the ``6.8.0-1051`` kernel is also installed and associated to that package. This is the same kernel indicated by the output of ``uname -r`` above, meaning this is the currently active kernel package on the instance.

You may see multiple kernel packages with different versions installed if you previously installed other kernel variants or if the currently installed package fetched a new kernel version.

Generally, the ``linux-<cloud>-edge`` package takes precedence over ``linux-<cloud>``, and ``linux-<cloud>`` takes precedence over ``linux-<cloud>-lts-<release>`` strictly from the fact that GRUB defaults to the highest versioned kernel available at boot time. This is due to the versioning conventions surrounding the different kernel variants and :ref:`kernel behaviors <kernels-on-the-cloud>`.

.. _install-kernel-package:

Install new kernel package
--------------------------

At this point, the new kernel package can be installed. For this example, we are installing the 22.04 LTS kernel package on Azure:

.. code-block:: bash

   sudo apt install linux-azure-lts-22.04 --install-recommends

Once again, list the kernel packages:

.. code-block:: bash

   dpkg --list | grep linux-azure | grep ii


This will now output something like:

.. code-block::

   ii  linux-azure                            6.8.0-1051.57~22.04.1                   amd64        Complete Linux kernel for Azure systems (vmlinuz).
   ii  linux-azure-6.8-cloud-tools-6.8.0-1051 6.8.0-1051.57~22.04.1                   amd64        Linux kernel version specific cloud tools for version 6.8.0-1051
   ii  linux-azure-6.8-headers-6.8.0-1051     6.8.0-1051.57~22.04.1                   all          Header files related to Linux kernel version 6.8.0
   ii  linux-azure-6.8-tools-6.8.0-1051       6.8.0-1051.57~22.04.1                   amd64        Linux kernel version specific tools for version 6.8.0-1051
   ii  linux-azure-cloud-tools-5.15.0-1102    5.15.0-1102.111                         amd64        Linux kernel version specific cloud tools for version 5.15.0-1102
   ii  linux-azure-headers-5.15.0-1102        5.15.0-1102.111                         all          Header files related to Linux kernel version 5.15.0
   ii  linux-azure-lts-22.04                  5.15.0.1102.100                         amd64        Complete Linux kernel for Azure systems.
   ii  linux-azure-tools-5.15.0-1102          5.15.0-1102.111                         amd64        Linux kernel version specific tools for version 5.15.0-1102

Note that ``linux-azure-lts-22.04`` is now present in the list alongside the ``5.15.0-1102`` kernel version in addition to the currently active ``linux-azure`` package and the ``6.8.0-1051`` kernel version.

.. _reboot-on-new-kernel:

Reboot and purge old kernel
---------------------------

There are two main scenarios to handle to boot onto your newly installed kernel. Either the new kernel package includes kernels with versions higher than your current kernel package, or it includes kernels with versions lower than your current kernel package.

When migrating to a kernel package with higher versioned kernels, the steps are quite simple. However, since the default GRUB behavior is to boot into kernels based on the highest version available, there are more steps required in order to migrate your kernel package when the new package uses lower versioned kernels than the currently booted kernel.

Once you have installed your new kernel variant, compare the versions and pick your workflow accordingly. In this example, you can see that our target version (``5.15.0-1102``) is lower than our current version (``6.8.0-1051``) which requires the lower versioned workflow.

.. tab-set::

   .. tab-item:: Higher versioned target package

      If you are migrating to a higher-versioned package, such as the :ref:`early-access HWE kernel <edge-kernel>` you can simply reboot, given a higher-versioned kernel is available at that time.

      .. code-block:: bash

         sudo reboot

      Check that the new kernel version is the expected target kernel:

      .. code-block:: bash

         uname -r

      If the kernel version does not match the kernel version associated with your kernel variant, check that you have correctly :ref:`installed the new kernel package <install-kernel-package>`. Otherwise, you may be booting onto a lower versioned kernel package, and need to follow those steps instead.

      It is best practice to remove the old kernel images, modules, and tools, but is not strictly required when migrating to a higher versioned kernel package:

      .. code-block:: bash

         dpkg --list | grep "linux-azure\|linux-image" | grep ii

      This will show all packages associated to all installed kernel packages. Simply remove all packages that are **NOT** associated to your currently booted kernel version. You can run something similar to the following, replacing ``azure`` and the kernel versions accordingly:

      .. code-block:: bash

         # Remove kernel packages/tools
         sudo apt purge linux-azure linux-azure-6.8-*-6.8.0-1051
         # Remove kernels
         sudo apt purge linux-image-6.8.0-1051-azure linux-image-azure
         # Autoremove for safe measure
         sudo apt autoremove

   .. tab-item:: Lower versioned target package

      If you are migrating to a lower-versioned package as we are in this example, such as from the :ref:`default rolling kernel package <rolling-kernel>` to the :ref:`LTS kernel package <lts-kernel>` or from the :ref:`early-access HWE kernel <edge-kernel>` to either of the aforementioned kernel variants, additional steps are required in order to boot onto the lower-versioned kernel.

      Two ways to boot onto your new kernel are listed below:

      .. tab-set::

         .. tab-item:: GRUB UI (Preferred)


            This is the safest and most preferred way to downgrade a kernel version while ensuring you still receive expected kernel package updates and upgrades. However, this may be more or less difficult depending on your cloud provider.

            Access the serial console for your virtual machine, reboot, and immediately interrupt the boot process. Find the kernel you want to boot, and resume the boot process.

            Before finishing your migration, first ensure you are booted onto the intended kernel:

            .. code-block::

               uname -r

            In this example, we are expecting to see ``5.15.0-1102-azure``.

            If the kernel version does not match the kernel version associated with your kernel variant, check that you have correctly :ref:`installed the new kernel package <install-kernel-package>` and properly :ref:`rebooted onto the new kernel <reboot-on-new-kernel>`.

            Now you can remove all pre-existing kernel images and packages that are not from the package you are migrating to. Package names may vary depending on which kernel package you are migrating from as well as the cloud and currently available kernel package versions.

            The following command checks for all azure kernel images and packages currently installed on the instance:

            .. code-block:: bash

               dpkg --list | grep "linux-azure\|linux-image" | grep ii

            This will show all packages associated to all installed kernel packages. Simply remove all packages that are **NOT** associated to your currently booted kernel version. You can run something similar to the following, replacing ``azure`` and the kernel versions accordingly:

            .. code-block:: bash

               # Remove kernel packages/tools
               sudo apt purge linux-azure linux-azure-6.8-*-6.8.0-1051
               # Remove kernels
               sudo apt purge linux-image-6.8.0-1051-azure linux-image-azure
               # Autoremove for safe measure
               sudo apt autoremove

            Only after this point can you be sure that you will automatically receive updates to your kernel package (``linux-azure-lts-22.04`` or ``linux-<cloud>-lts-<release>`` in this case).

         .. tab-item:: Purge all other kernels (Not recommended)

            .. note:: This method is dangerous. It involves removing the currently booted kernel while that kernel is active. If done improperly, your virtual machine may be left in an unrecoverable state upon reboot.

            Find the kernel images, modules, and tools:

            .. code-block:: bash

               dpkg --list | grep "linux-azure\|linux-image" | grep ii

            This will output something similar to:

            .. code-block::

               ii  linux-image-5.15.0-1102-azure          5.15.0-1102.111                         amd64        Signed kernel image azure
               ii  linux-image-6.8.0-1051-azure           6.8.0-1051.57~22.04.1                   amd64        Signed kernel image azure
               ii  linux-image-azure                      6.8.0-1051.57~22.04.1                   amd64        Linux kernel image for Azure systems (vmlinuz).
               ii  linux-image-azure-lts-22.04            5.15.0.1102.100                         amd64        Linux kernel image for Azure systems.

            The following command removes the active ``linux-image-azure`` package, the currently booted ``6.8.0-1051-azure`` kernel, and all associated tools and modules:

            .. code-block:: bash

               # Remove kernel packages/tools/modules
               sudo apt purge linux-azure linux-azure-6.8-*-6.8.0-1051
               # Remove kernels
               sudo apt purge linux-image-6.8.0-1051-azure linux-image-azure
               # Autoremove for safe measure
               sudo apt autoremove

            When purging the currently booted kernel you will receive a number of prompts asking if you are sure you want to do this since you are removing the kernel, since it may result in an unrecoverable state upon reboot. Read carefully and remove the currently booted kernel anyway.

            At this point, it is a good idea to check which kernels are still installed on the instance:

            .. code-block::

               dpkg --list | grep linux-image | grep ii

            If you have purged all higher-versioned kernels, you should see exactly one kernel image left with the expected kernel image package, similar to the following:

            .. code-block::

               ii  linux-image-5.15.0-1102-azure          5.15.0-1102.111                         amd64        Signed kernel image azure
               ii  linux-image-azure-lts-22.04            5.15.0.1102.100                         amd64        Linux kernel image for Azure systems.

            If there are multiple kernels installed, repeat the steps to purge those other kernels and their packages. If there are no kernels or you do not see at least two entries, go back to :ref:`install-kernel-package` and ensure you have installed the lower-versioned kernel package.

            If you leave any higher-versioned kernels or their associated image package, GRUB will eventually reboot onto that kernel instead of the intended, lower-versioned kernel.

            After this point, you can reboot:

            .. code-block::

              sudo reboot


            Before finishing your migration, first ensure you are booted onto the intended kernel:

            .. code-block::

               uname -r

            In this example, we are expecting to see ``5.15.0-1102-azure``.

            If the kernel version does not match the kernel version associated your kernel variant, check that you have correctly :ref:`installed the new kernel package <install-kernel-package>` and properly :ref:`rebooted onto the new kernel <reboot-on-new-kernel>`.

            At this point, you can expect to reliably receive kernel updates for your kernel variant.
