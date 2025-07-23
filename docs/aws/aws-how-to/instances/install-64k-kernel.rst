Install 64k page kernel on ARM64 instances 
==========================================

When running ARM64 instances on AWS, you can choose between the 4k and 64k kernel page sizes. The 64k page size kernel for AWS is available for certain Ubuntu releases - 22.04 LTS, 24.04 LTS, 25.04 and newer releases.

Switching to the 64k kernel
---------------------------

To switch to the 64k page size kernel, run:

.. code::

    sudo apt update
    sudo apt install linux-aws-64k

On LTS releases, this command will install the current rolling kernel, called the `HWE kernel`_, which is a newer kernel derived from the interim releases in order to support modern hardware. 

The General Availability (GA) kernel, the original kernel shipped with an Ubuntu LTS release, is also offered. If you want to install the GA kernel instead, run:

.. code::

    sudo apt install linux-aws-64k-lts-<YY.MM>

replacing ``YY.MM`` with the release version number. For instance, on Ubuntu 22.04 LTS, that would result in the linux-aws-64k-lts-22.04 package.

Reboot the instance for the changes to take effect:

.. code::

    sudo reboot


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

Future boots will automatically use the selected kernel flavor.

.. _HWE kernel: https://canonical-kernel-docs.readthedocs-hosted.com/latest/reference/glossary/#term-HWE