Canonical's offerings on Oracle Cloud
=====================================

Ubuntu images
-------------

Canonical produces fully optimised Oracle Cloud images that provide a stable base image for running workloads. The two main types of images are:

* **Server images:** General-purpose customised images that include the necessary drivers and kernel modifications to run smoothly in the Oracle Cloud environment. These images launch with the oracle-cloud-agent pre-installed, featuring plugins that collect performance metrics, install OS updates, and perform other instance management tasks.

* **Minimal images:** These are minimal images designed for automated deployment at scale and have a reduced default package set. They are much smaller, boot faster, and require fewer security updates over time due to the fewer installed packages.

Each of these images have variants for AMD64 and ARM64 (Ampere processors). The minimal images for ARM64 are only available from Ubuntu 22.04 onwards. 

The images are built regularly and follow a thorough test framework that helps detect any issues / regressions due to package changes. They are then shared with Oracle privately who publish them on the cloud platform once per month.

With a single image type that is validated to work on both virtual machines and bare metal instances, the images aim to provide a consistent experience for users.

Although only Ubuntu LTS (Long-Term Support) images are publicly available on Oracle Cloud, Canonical also builds Oracle-optimised images for non-LTS releases. This allows for continuous internal testing and ensures that future LTS releases work well on Oracle Cloud.

For instructions on how to find the images, refer to :doc:`../oracle-how-to/find-ubuntu-images`.


Optimisations for Oracle Cloud
------------------------------

Generally the images are built in a qcow2 format and support the following options:

* Boot firmware - boot with BIOS or UEFI (preferred). ARM64 images only support UEFI boot.
* Launch modes - support for both PARAVIRTUALIZED and NATIVE launch modes.  
* Network interfaces - support for VFIO and PARAVIRTUALIZED modes.
* Boot volume -  allows booting through iSCSI or PARAVIRTUALIZED storage.

The customisations include NVMe tunings, iSCSI configurations to allow instances to boot from iSCSI backend when appropriate, logging improvements, iptables and udev configurations specific to Oracle Cloud platform, among others.


Kernel optimisations
--------------------

Ubuntu images available on Oracle Cloud run the linux-oracle kernel. Additional kernel variants are also offered by Canonical, that users can install as appropriate.

By default Ubuntu images use a **rolling kernel model**, which provides the latest upstream bug fixes and performance improvements around task scheduling, I/O scheduling, networking, hypervisor guests and containers. A rolling kernel model transitions the default linux-oracle kernel from one base version to the next as part of its regular patching cycle. That new kernel, called the HWE Kernel (Hardware Enablement Kernel) is the kernel of the latest Ubuntu release.

As an example, users running Ubuntu 22.04 instances that were launched back in 2022, would run the 5.15 kernel by default. But as new Ubuntu versions got released, the linux-oracle kernel rolled on to the next release's kernel version. So an Ubuntu 22.04 instance launched at a later point in time, would include different kernel versions depending on when it was launched - it could be version 6.5 or and more recently 6.8.

If you do not want to roll to a new kernel, and want to stay on the base kernel provided by the LTS release (which continues to get support and receive updates for the length of the LTS), you need to install a specific corresponding kernel variant: `linux-oracle-lts-<release>`. (Refer to the next section for an example.)


Kernel variants
~~~~~~~~~~~~~~~

Canonical provides different kernel variants, all optimised for Oracle Cloud: 

* linux-oracle: The default rolling kernel
* linux-oracle-edge: The -edge kernel provides early access to the next HWE kernel. It is fully supported, but is less exposed to real world use cases since it is relatively new. It eventually transitions to the linux-oracle kernel.
* linux-oracle-lts-<release>: This kernel does not roll and sticks to the original kernel present in the Ubuntu release, for the life of the release (e.g.: linux-oracle-lts-22.04 will always point to a 5.15 kernel for the life of Ubuntu 22.04).
* linux-oracle-64k: This is a kernel specific to ARM64 instances, and uses 64k pages by default (as opposed to 4k pages in other kernels). It is known to improve performance in large ARM64 based instances, but is not meant for general use cases, as it can cause issues with low memory instance types.