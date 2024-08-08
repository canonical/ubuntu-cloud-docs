.. _qcow-qemu:

Launch QCOW Images Using QEMU
=============================

Ubuntu cloud images are released in many formats to enable many launch configurations and methods.

Among the many formats for cloud images is the ``.img`` QCOW format. This article will cover the QCOW use case and provide
instructions on how to use the images with QEMU.

For starting with an ISO server image, see the `server documentation`_ on downloading and converting an ISO for use
with QEMU.

QEMU and QCOWs
--------------

`QEMU`_ is a system emulator and "type 2" virtual machine hypervisor. Type 2 hypervisors run on top of the host operating
system. Often, QEMU is used with `KVM`_, which is a Type 1 hypervisor, which can run directly on bare metal. Together,
QEMU and KVM can enable running virtual machines at near-native speeds.

QCOW, which stands for "QEMU Copy On Write," is a format for images used by QEMU. QCOW image files grow according to use,
as opposed to pre-allocating the entire image disk to a file. Ubuntu cloud images with the ``.img`` file type are QCOW
images and are best used with the QEMU hypervisor.

QEMU Shell
~~~~~~~~~~

When launching a system it is handy to know that ctrl-a c is an escape key that will take the user from the monitor or
serial console and to the QEMU monitor. From this shell a user can send keys to the guest via the sendkey option or even
close the guest via quit.

Seeding the Image
-----------------

Since we are dealing with cloud images here, we will need a cloud-init datasource to use. See the guide in this series
called `use-local-ds`_ for steps required for setting up a seed image for a local cloud-init datasource.

Booting the Image with SeaBIOS
------------------------------

SeaBIOS booting an image is essentially the easiest as it is the default
firmware used by QEMU.

The following launches a cloud image with:

* KVM acceleration
* the local machine's CPUs
* 2GB of memory
* no graphics and serial output to the console
* snapshot will make writes to a temporary file instead of the disk image
  itself. This ensures the base disk is not touched. If at some point, you want
  to persist the changes you've made on the disk, press C-a s
* virtio network device that redirect's guest port 22 to host's port 2222
* virtio cloud image
* virtio seed image

.. code:: bash

    qemu-system-x86_64  \
      -cpu host -machine type=q35,accel=kvm -m 2048 \
      -nographic \
      -snapshot \
      -netdev id=net00,type=user,hostfwd=tcp::2222-:22 \
      -device virtio-net-pci,netdev=net00 \
      -drive if=virtio,format=qcow2,file=ubuntu-20.04-server-cloudimg-amd64.img \
      -drive if=virtio,format=raw,file=seed.img

Access to this VM can happen via the serial console or the user can open
another terminal and ssh to the localhost's port 2222:

.. code:: bash

    ssh -o "StrictHostKeyChecking no" ubuntu@0.0.0.0 -p 2222

Booting the Image with uEFI
---------------------------

If a user wishes to not use BIOS, but instead uEFI then a different firmware
is required. Ubuntu ships the ovmf package to provide uEFI firmware. Assuming
that package is installed, then a user can use a different flash image with
the -pflash option.

The following is the same as the above, except the last line which specifies
the pflash option:

.. code::

    qemu-system-x86_64  \
      -cpu host -machine type=q35,accel=kvm -m 2048 \
      -nographic \
      -snapshot \
      -netdev id=net00,type=user,hostfwd=tcp::2222-:22 \
      -device virtio-net-pci,netdev=net00 \
      -drive if=virtio,format=qcow2,file=ubuntu-20.04-server-cloudimg-amd64.img \
      -drive if=virtio,format=raw,file=seed.img \
      -drive if=pflash,format=raw,file=/usr/share/OVMF/OVMF_CODE.fd,readonly

A user can confirm that uEFI was used by checking for the existence of the
/sys/firmware/efi directory:

.. code::

    $ test -d /sys/firmware/efi && echo efi || echo bios
    efi

Additionally, the dmesg and efibootmgr commands will also have EFI related
output:

.. code::

    $ dmesg | grep EFI
    [    0.000000] efi: EFI v2.70 by EDK II
    [    0.505005] fb0: EFI VGA frame buffer device
    [    0.569400] EFI Variables Facility v0.08 2004-May-17
    $ sudo efibootmgr
    BootCurrent: 0002
    Timeout: 0 seconds
    BootOrder: 0000,0001,0002,0003,0004,0005,0006
    Boot0000* UiApp
    Boot0001* UEFI QEMU DVD-ROM QM00005
    Boot0002* UEFI Misc Device
    Boot0003* UEFI Misc Device 2
    Boot0004* UEFI PXEv4 (MAC:525400123456)
    Boot0005* UEFI HTTPv4 (MAC:525400123456)
    Boot0006* EFI Internal Shell

.. _`server documentation`: https://ubuntu.com/server/docs/virtualisation-with-qemu
.. _`QEMU`: https://www.qemu.org/docs/master/index.html
.. _`KVM`: https://ubuntu.com/blog/kvm-hyphervisor