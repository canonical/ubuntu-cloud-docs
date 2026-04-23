.. meta::
   :description: Learn how to use the 64K page kernel on ARM64 instances on Google Cloud, including supported machine types and how to switch kernel variants.

Use 64K page kernel on ARM64 instances
======================================

ARM64 platforms
-----------------

Google Cloud currently provides two different CPU platforms for ARM64: Ampere Altra (via the "Tau" `T2A` machine type) and Google's own Axion (via the `N4A` and `C4A` machine types).


64K page kernels
-------------------

From Ubuntu 22.04 LTS onwards, two kernel variants are available to run ARM64: `linux-gcp` and `linux-gcp-64k`. "Standard" Ubuntu images on Google Cloud come preinstalled with the default `linux-gcp` kernel (see ``rmadison linux-gcp`` for details) but the "accelerator" Ubuntu image line comes with `linux-gcp-64k`. To see the latest accelerator-based images available, use:

.. code::
    
    gcloud compute images list --project=ubuntu-os-accelerator-images --no-standard-images

.. note::
    
    The `linux-gcp` kernel will work on *both* CPU platforms, but `linux-gcp-64k` *will not* work on `T2A` machine types.


Changing the installed kernel
-----------------------------

Should you wish to swap from the default kernel to the 64K page variant (or vice versa), run:

.. code::

    sudo apt update
    sudo apt install linux-gcp-64k

After installation a pop-up courtesy of ``needrestart`` will appear recommending you to reboot.
You must reboot the instance for the kernel to properly install:

.. code::

    sudo reboot

When you log back into the instance, to confirm the new kernel has indeed installed, run:

.. code::

    uname -r


More information
-----------------
For more information about the different kernel variants and their use cases, refer to

* `Choosing between 4K and 64K kernel options for ARM64`_
* :ref:`Kernels on the cloud <kernels-on-the-cloud>`

.. _`Choosing between 4K and 64K kernel options for ARM64`: https://documentation.ubuntu.com/server/explanation/installation/choosing-between-the-arm64-and-arm64-largemem-installer-options/index.html
