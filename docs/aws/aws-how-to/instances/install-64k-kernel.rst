Install 64k page kernel on ARM64 instances 
==========================================

When running ARM64 instances on AWS, you can choose between the 4k page and 64k page kernels. A 64k page kernel is optimized for workloads that benefit from larger memory pages, such as high-performance computing and machine learning applications.

From Ubuntu 22.04 LTS onwards, the 64k page kernel is available for all active LTS and extended support releases of Ubuntu, as well as all supported interim releases.

Switching to the 64k page kernel
--------------------------------

To switch to the 64k page kernel, run:

.. code::

    sudo apt update
    sudo apt install linux-aws-64k

On LTS releases, this command will install the current rolling kernel, called the `HWE kernel`_, which is a newer kernel derived from the interim releases in order to support modern hardware. 

The General Availability (GA) kernel, the original kernel shipped with an Ubuntu LTS release, is also offered. If you want to install the GA kernel instead, run:

.. code::

    sudo apt install linux-aws-64k-lts-<YY.MM>

replacing ``YY.MM`` with the release version number. For instance, on Ubuntu 22.04 LTS, that would result in the linux-aws-64k-lts-22.04 package.

For the changes to take effect, you'll need to reboot the instance. However, when your instance has multiple versions of the linux kernel installed (as in this case), the latest version is chosen by default.

So if you install the current rolling 64k page kernel, that'll be chosen. But if you install the 64k GA kernel, it would most likely be an older version and won't be chosen automatically. In this case, as described in the next section, you'll have to update grub to ensure that the 64k GA kernel gets selected every time the instance boots.


Selecting the kernel flavor permanently
---------------------------------------

To permanently select the kernel flavor to boot, run:

.. code::

    echo "GRUB_FLAVOUR_ORDER=<desired-flavor>" | sudo tee /etc/default/grub.d/local-order.cfg

replacing <desired-flavor> with

- ``aws-64k``: for the 64k kernel flavor, or 
- ``aws``    : for the default 4k kernel flavor

Then apply the change:

.. code::

    sudo update-grub

and reboot the instance, for the change to take effect:

.. code::

    sudo reboot

Future boots will automatically use the latest version of the selected kernel flavor.

.. _HWE kernel: https://canonical-kernel-docs.readthedocs-hosted.com/latest/reference/glossary/#term-HWE