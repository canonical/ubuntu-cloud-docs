Install NVIDIA drivers on a GPU-enabled EC2 instance 
=====================================================

    
AWS provides GPU-enabled instance types for workloads that require GPU compute power. G4DN instances are powered by an NVIDIA Tesla T4 GPU. This guide will walk you through the driver installation process, including CUDA for machine learning workloads.

For more comprehensive instructions on checking the available drivers and installing the correct one based on different use-cases, refer to the `Ubuntu server documentation for installing NVIDIA drivers`_.

Launch your instance
--------------------

Launch your Ubuntu 24.04 LTS VM using either `AWS CLI or the web console`_. Make sure you allocate enough disk space for your use case, as ML models tend to need a significant amount. 

SSH access is required, so make sure to either open port 22 or enable SSM to access the machine through Session Manager. 

Install the NVIDIA driver
-------------------------

First, login into your instance and check if the GPU is present with this command:

.. code::

    sudo lshw -c video


If you are using the correct instance type (G4DN in this case), you should see the following results:

.. code-block:: none

      *-display:0 UNCLAIMED
           description: VGA compatible controller
           product: Amazon.com, Inc.
           vendor: Amazon.com, Inc.
           physical id: 3
           bus info: pci@0000:00:03.0
           version: 00
           width: 32 bits
           clock: 33MHz
           capabilities: vga_controller
           configuration: latency=0
           resources: memory:fe400000-fe7fffff memory:c0000-dffff
      *-display:1 
           description: 3D controller
           product: TU104GL [Tesla T4]
           vendor: NVIDIA Corporation
           physical id: 1e
           bus info: pci@0000:00:1e.0
           version: a1
           width: 64 bits
           clock: 33MHz
           capabilities: pm pciexpress msix cap_list
           configuration: latency=0
           resources: iomemory:40-3f iomemory:40-3f memory:fd000000-fdffffff memory:440000000-44fffffff memory:450000000-451ffffff


The NVIDIA Tesla T4 GPU should be listed in the output. Now, install the NVIDIA driver using the `ubuntu-drivers` utility:

.. code::

    sudo apt install -y ubuntu-drivers-common
    sudo ubuntu-drivers install

.. note::
    If you need a specific NVIDIA driver version, use e.g. ``sudo ubuntu-drivers install nvidia:535``.

After the installation, reboot the instance:

.. code::

    sudo reboot


Test if everything got properly installed:

.. code::

    nvidia-smi

This should display the NVIDIA GPU information, including the CUDA version in the top-right corner. 

.. code-block:: none

    +---------------------------------------------------------------------------------------+
    | NVIDIA-SMI 535.104.05             Driver Version: 535.104.05   CUDA Version: 12.2     |
    |-----------------------------------------+----------------------+----------------------+
    | GPU  Name                 Persistence-M | Bus-Id        Disp.A | Volatile Uncorr. ECC |
    | Fan  Temp   Perf          Pwr:Usage/Cap |         Memory-Usage | GPU-Util  Compute M. |
    |                                         |                      |               MIG M. |
    |=========================================+======================+======================|
    |   0  Tesla T4                       On  | 00000000:00:1E.0 Off |                    0 |
    | N/A   26C    P8               9W /  70W |      2MiB / 15360MiB |      0%      Default |
    |                                         |                      |                  N/A |
    +-----------------------------------------+----------------------+----------------------+
                                                                                             
    +---------------------------------------------------------------------------------------+
    | Processes:                                                                            |
    |  GPU   GI   CI        PID   Type   Process name                            GPU Memory |
    |        ID   ID                                                             Usage      |
    |=======================================================================================|
    |  No running processes found                                                           |
    +---------------------------------------------------------------------------------------+


If CUDA was not installed, you can visit the `NVIDIA website`_ to download the CUDA version that matches the driver you just installed.



.. _`AWS CLI or the web console`: https://discourse.ubuntu.com/t/how-to-deploy-ubuntu-pro-in-aws-in-2023/23367
.. _`NVIDIA website`: https://developer.nvidia.com/cuda-downloads
.. _`Ubuntu server documentation for installing NVIDIA drivers`: https://documentation.ubuntu.com/server/nvidia-drivers-installation/

