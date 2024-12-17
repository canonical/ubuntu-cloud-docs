Canonical's offerings on Oracle Cloud
=====================================

Ubuntu images
-------------

Canonical produces fully optimized Oracle Cloud images that provide a stable base image for running workloads. The two main types of images are:

* **Server images:** General-purpose customized images that include the necessary drivers and kernel modifications to run smoothly in the Oracle Cloud environment. These images launch with the oracle-cloud-agent pre-installed, featuring plugins that collect performance metrics, install OS updates, and perform other instance management tasks.

* **Minimal server images:** These are images designed for automated deployment at scale and have a reduced default package set. They are much smaller, boot faster, and require fewer security updates over time due to the fewer installed packages.

Each of these images have variants for AMD64 and ARM64 (Ampere processors). The minimal images for ARM64 are only available from Ubuntu 22.04 LTS onwards. 

The images are built regularly and follow a thorough test framework that helps detect any issues / regressions due to package changes. They are then shared with Oracle privately who publish them on the cloud platform once per month.

With a single image type that is validated to work on both virtual machines and bare metal instances, the images aim to provide a consistent experience for users.

For instructions on how to find the images, refer to :doc:`../oracle-how-to/find-ubuntu-images`.


Optimizations for Oracle Cloud
------------------------------

The images support the following options:

* Boot firmware - boot with BIOS or UEFI (preferred). ARM64 images only support UEFI boot.
* Launch modes - support for both PARAVIRTUALIZED and NATIVE launch modes.  
* Network interfaces - support for VFIO and PARAVIRTUALIZED modes.
* Boot volume -  allows booting through iSCSI or PARAVIRTUALIZED storage.

The customizations include NVMe tunings, iSCSI configurations to allow instances to boot from iSCSI backend when appropriate, logging improvements, iptables and udev configurations specific to Oracle Cloud platform, among others.


Kernel optimizations
--------------------

Ubuntu images available on Oracle Cloud run the ``linux-oracle`` kernel by default. Additional kernel variants are also offered by Canonical, as described in the next section.

By default Ubuntu images use a **rolling kernel model**, which provides the latest upstream bug fixes and performance improvements around task scheduling, I/O scheduling, networking, hypervisor guests and containers. A rolling kernel model transitions the default linux-oracle kernel from one base version to the next as part of its regular patching cycle. That new kernel, called the HWE Kernel (Hardware Enablement Kernel) is the kernel of the latest Ubuntu release.

As an example, users running Ubuntu 22.04 LTS instances that were launched back in 2022, would run the 5.15 kernel by default. But as new Ubuntu versions got released, the linux-oracle kernel rolled on to the next release's kernel version. So an Ubuntu 22.04 LTS instance launched at a later point in time, would include different kernel versions depending on when it was launched - it could be version 6.5 or and more recently 6.8. Moreover, all running instances also have their kernels automatically updated upon reboot. So even the instances launched earlier will receive the updated kernels at some point.

For more details about the rolling kernel model, refer to the `Ubuntu kernel release cycle`_ and the relevant `installation options`_.

If you do not want to roll to a new kernel, and want to stay on the base kernel provided by the LTS release (which continues to get support and receive updates for the length of the LTS), you need to install a specific corresponding kernel variant: ``linux-oracle-lts-<release>``. (Refer to the next section for an example.)


Kernel variants
~~~~~~~~~~~~~~~

Canonical provides different kernel variants, all optimized for Oracle Cloud. They are available in the APT archives, and can be installed with the ``apt install`` command.

For x86_64 instances, the variants available are:

* ``linux-oracle-lts-<release>``: Where <release> is replaced by an LTS Ubuntu version, such as 18.04, 20.04, 22.04 or 24.04. This kernel does not roll and sticks to the original kernel present in the Ubuntu release, for the life of the release (e.g.: linux-oracle-lts-22.04 will always point to a 5.15 kernel for the life of Ubuntu 22.04 LTS).
* ``linux-oracle-edge``: The -edge kernel provides early access to the next HWE kernel. It is fully supported, but is less exposed to real world use cases since it is relatively new. It eventually transitions to the linux-oracle kernel. It can for instance be used for testing the upcoming kernels in your specific environment.

For ARM64 instances, we have four variants - the two mentioned above for x86_64 instances and two more:

* ``linux-image-oracle-64k``: This variant uses 64k memory pages by default (instead of the usual 4k memory pages). It is known to improve performance in high-memory ARM64 based instances, such as the Grace Hopper platform. It is not meant for general use cases as it can cause issues with low memory instance types.

* ``linux-image-oracle-64k-edge``: This variant provides early access to the next HWE kernel that is configured to use 64k memory pages by default.



.. _Ubuntu kernel release cycle: https://ubuntu.com/about/release-cycle#ubuntu-kernel-release-cycle
.. _`installation options`: https://ubuntu.com/kernel/lifecycle
