.. meta::
   :description: Install NVIDIA drivers from the Ubuntu archive on GPU-enabled cloud instances for compute workloads, then verify the installation.

.. _install-nvidia-drivers-all-clouds:

Install NVIDIA drivers
======================

On a GPU-enabled cloud instance, use ``ubuntu-drivers`` to install NVIDIA drivers for compute workloads from the Ubuntu archive.
The ``--gpgpu`` option selects headless server drivers for the detected GPU, architecture, and kernel without pulling in desktop packages.

Prerequisites
-------------

You need:

* An Ubuntu instance with an attached NVIDIA GPU.
* Command-line access with ``sudo`` privileges.
* Access to the Ubuntu archive, including the ``restricted`` component and updates for your Ubuntu release.

Some instance types need a specific driver branch or additional software.
Check your cloud provider's requirements before you install a driver:

* AWS: :ref:`aws:install-nvidia-drivers`
* Azure: `Azure NVIDIA driver setup`_
* Google Cloud: `Google Cloud NVIDIA driver installation`_

.. important::

   Some images ship with NVIDIA drivers already installed, such as Ubuntu Accelerator images on Google Cloud.
   Follow the provider's instructions for those images, and for GRID/vGPU or managed Kubernetes nodes, which may need components that this guide does not install.

Prepare the instance
--------------------

Upgrade the system and reboot first so the running kernel matches the latest prebuilt ``linux-modules-nvidia-*`` packages in the Ubuntu archive.

1. Update the package index and upgrade installed packages:

   .. code-block:: bash

      sudo apt update && sudo apt upgrade

2. Reboot the instance if a new kernel was installed:

   .. code-block:: bash

      sudo reboot

3. Reconnect to the instance and install the driver selection tool:

   .. code-block:: bash

      sudo apt install ubuntu-drivers-common

Install a compute driver
------------------------

1. List the available compute drivers:

   .. code-block:: bash

      sudo ubuntu-drivers list --gpgpu

   The output lists drivers that match the detected hardware and available kernel modules.
   If the list is empty, confirm that the instance has an NVIDIA GPU (``lspci | grep -i nvidia``) and that the ``restricted`` repository component is enabled.

2. Install a driver using automatic selection:

   .. code-block:: bash

      sudo ubuntu-drivers install --gpgpu

   .. note::

      If your workload requires a specific branch, pass the exact name shown by ``list`` without the ``nvidia-driver-`` prefix.
      For example:

      .. code-block:: bash

         sudo ubuntu-drivers install --gpgpu nvidia:580-server-open

      Or, for the proprietary kernel module variant:

      .. code-block:: bash

         sudo ubuntu-drivers install --gpgpu nvidia:580-server

      Open kernel modules require a Turing or later GPU.

3. Check which driver branch was installed:

   .. code-block:: bash

      apt list --installed 'nvidia-headless-no-dkms-*'

   The package name includes the installed branch, for example ``nvidia-headless-no-dkms-580-server-open``.

4. Install the matching NVIDIA utilities (which provide ``nvidia-smi``):

   .. code-block:: bash

      sudo apt install nvidia-utils-580-server

   Replace ``580`` with the branch from the previous step.
   Both ``580-server`` and ``580-server-open`` use ``nvidia-utils-580-server``.
   For a driver without the ``-server`` suffix, use the corresponding utilities package without that suffix.

5. Reboot the instance:

   .. code-block:: bash

      sudo reboot

6. Reconnect to the instance.

Verify the installation
-----------------------

Check that the driver is loaded and can access the GPU:

.. code-block:: bash

   nvidia-smi

The output shows the GPU, the loaded driver version, and the highest CUDA version supported by the driver.
Installing the driver does not install the CUDA Toolkit.
For CUDA development tools, see `CUDA Toolkit installation`_.

If ``nvidia-smi`` is not installed, check the loaded kernel module directly:

.. code-block:: bash

   cat /proc/driver/nvidia/version

Kernel modules and Secure Boot
------------------------------

When the Ubuntu archive has prebuilt NVIDIA kernel modules for your kernel and architecture, ``ubuntu-drivers`` installs them.
Canonical signs these modules, so they load with Secure Boot enabled and do not need a local DKMS build.

If no matching prebuilt modules exist, check for kernel updates first.
The ``--include-dkms`` option lets ``ubuntu-drivers`` consider DKMS packages, which build the modules locally and need the matching kernel headers.
DKMS signs the modules with a locally generated key.
With Secure Boot enabled, you must enroll that key as a Machine Owner Key (MOK) at the next boot, which requires an interactive serial console.
Check that your cloud provider offers serial console access before relying on DKMS with Secure Boot.

For manual installation and troubleshooting, see `Ubuntu Server NVIDIA driver installation`_.
For testing unreleased drivers, see :ref:`install-proposed-nvidia-drivers-for-testing`.

.. _Azure NVIDIA driver setup: https://learn.microsoft.com/en-us/azure/virtual-machines/linux/n-series-driver-setup
.. _Google Cloud NVIDIA driver installation: https://docs.cloud.google.com/compute/docs/gpus/install-drivers-gpu
.. _CUDA Toolkit installation: https://docs.nvidia.com/cuda/cuda-installation-guide-linux/
.. _Ubuntu Server NVIDIA driver installation: https://documentation.ubuntu.com/server/how-to/graphics/install-nvidia-drivers/
