.. _vagrant-live-build:

Build a Vagrant box with live-build
===================================
`live-build <https://live-team.pages.debian.net/live-manual/html/live-manual/overview-of-tools.en.html#291>`_ is the heart of the image build process. It has been customised by different teams at Canonical and these customisations are shipped as a Debian package named `livecd-rootfs <https://launchpad.net/livecd-rootfs>`_.

Prerequisites
-------------

- A virtual machine running the same Ubuntu release and architecture as the image you want to build
- Access to the serial console of the VM
- Configure the root user to have a password

Configure QEMU
~~~~~~~~~~~~~~

.. code:: bash

   sudo apt install qemu-system-x86

QEMU is an open-source system emulator and virtualiser that can perform hardware virtualisation. If you have never used QEMU before, you can go through the `cloud-init QEMU tutorial <https://cloudinit.readthedocs.io/en/latest/tutorial/qemu.html>`_.

Configure cloud-init
~~~~~~~~~~~~~~~~~~~~
Cloud images expect some sort of image metadata source. This is how a user's ssh keys get on the system. When launching a local image to provide that metadata a user can generate a seed image that cloud-init can discover and read any metadata, vendor data or user data provided.

To get started, install ``cloud-image-utils`` to get the ``cloud-localds`` command. Then create whatever data required, and generate the seed image.

The example below passes a cloud-config YAML as user data. Replace all the ``$VARIABLE$``:

.. code:: bash

   sudo apt update
   sudo apt install --yes cloud-image-utils

   cat > user-data.yaml <<EOF
   #cloud-config
   users:
     - name: root
           disable_root: false
           ssh_authorized_keys:
           - $SSH_PUB_KEY$
   chpasswd:
     expire: false
     users:
           - name: root
           password: $PASSWORD$
           type: text
   packages:
     - livecd-rootfs
   package_update: true
   package_upgrade: true
   write_files:
     - content: |
           Defaults !use_pty
           path: /etc/sudoers.d/disable_pty
   EOF

   cloud-localds seed.img user-data.yaml

.. important::
   It is necessary to input an ssh key for our final step: getting our built image outside of the build VM. You can learn more about generating ssh keys `here <https://ubuntu.com/server/docs/service-openssh>`_.

Download a cloud image
~~~~~~~~~~~~~~~~~~~~~~
You will need a cloud image of the same architecture as the image that you want to build. You can download an image from `Ubuntu Cloud Images <http://cloud-images.ubuntu.com/>`_ and place it in your build folder. Alternatively, you can use ``wget``. For a Ubuntu 22.04 Jammy image, run:

.. code:: bash

   wget https://cloud-images.ubuntu.com/jammy/current/jammy-server-cloudimg-amd64.img

The Vagrant box build process uses more disk space than is available by default on the provided cloud images, so we will resize the image using ``qemu-img``. For our image, ``jammy-server-cloudimg-amd64.img``, run:

.. code:: bash

   sudo apt install qemu-utils
   qemu-img resize jammy-server-cloudimg-amd64.img +10G

This will add 10GB to the virtual disk of our image and give us enough space to complete the Vagrant box build.

Launch a VM with QEMU
---------------------
We will use `SeaBIOS <https://www.seabios.org/SeaBIOS>`_ to boot our image. SeaBIOS booting an image is essentially the easiest as it is the default firmware used by QEMU.

The following command launches a cloud image with:

- KVM acceleration
- the local machine's CPUs
- 2GB of memory
- no graphics and serial output to the console
- snapshot will make writes to a temporary file instead of the disk image itself. This ensures the base disk is not touched. If at some point, you want to persist the changes you've made on the disk, press ``C-a s``
- virtio network device that redirects guest port 22 to host's port 2222
- virtio cloud image
- virtio seed image

.. code:: bash

   qemu-system-x86_64  \
     -cpu host -machine type=q35,accel=kvm -m 2048 \
     -nographic \
     -snapshot \
     -netdev id=net00,type=user,hostfwd=tcp::2222-:22 \
     -device virtio-net-pci,netdev=net00 \
     -drive if=virtio,format=qcow2,file=./jammy-server-cloudimg-amd64.img \
     -drive if=virtio,format=raw,file=seed.img

.. note::
   To exit the QEMU shell, press ``C-a x``

Configure the environment
-------------------------
All the commands can be run in an ssh session except ``lb build`` that **has to be run via the serial console**. 

Create and configure the build directory
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

   mkdir -p /build/auto && cd /build
   ln -s /usr/share/livecd-rootfs/live-build/auto/* auto/

Configure the environment variables
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Write this file on the VM. Modify it with your build parameters. 

- ``SUITE``: same as VM Ubuntu series name 
- ``IMAGE_TARGETS``: ``vagrant``
- ``NOW``: current date (``YYYYMMDD``)

.. code:: bash

   cat << EOF > /build/inputs.sh
   #########################################
   # usually you don't need to change those

   export PROJECT=ubuntu-cpc
   export IMAGEFORMAT=ext4

   #########################################
   # Those are the same parameters used with ubuntu-bartender or livefs

   # those should be the same as the VM running the build
   export SUITE=jammy
   export ARCH=amd64

   # Defines the binary hooks that will be run.
   # eg. azure, ec2, qcow2, oracle, etc...
   # it is a comma separated list of strings
   export IMAGE_TARGETS=vagrant

   # this is the serial that will be set in /etc/cloud/build.info
   export NOW=20240409

   #########################################
   EOF

In practice, you can place this file anywhere on the VM but don't forget to source it before running ``lb config`` or ``lb build``.

.. code:: bash

   source /build/inputs.sh

Run live-build
~~~~~~~~~~~~~~
Now you can run the configuration stage:

.. code:: bash

   cd /build
   lb config

Once the configuration is done, make sure no SSH connection is open. For example, you can run ``w`` to check only one session is open on a serial port.

Finally, start the build:

.. code:: bash

   cd /build
   lb build 2>&1 | tee /build/build.log

Once the build is done, the build artifacts are in ``/build`` on the guest VM.

Troubleshooting and cleanup
---------------------------
Here, you need to be aware of what your binary hook produces and where the build failed. But in general, you want to:

#. Unmount the disk-image.

   a. Run ``mount`` or ``lsblk`` and look for loop devices mounted in a sub-directory of ``/build`` or in the temp directory ``/tmp``.

   #. Use ``umount -R $DIRECTORY`` to unmount everything mounted in that directory.

#. Remove all the loop devices attached to disk-image files.

   a. Run ``lsblk`` and look for loop devices that are attached to a file in ``/build`` or attached to nothing.

   #. Run ``kpartx -v -d /dev/loop$N`` to clean the loop.

#. Remove the "derivative image" used by your binary hook.

   a. Look in ``/build/binary/boot``. If your hook calls ``create_derivative [uefi|disk] NAME``, look for a file named ``/build/binary/boot/NAME[-uefi].ext4``.

   #. remove this file

#. If you want to be able to ssh into the VM (instead of only using the serial console).

   a. remount ``devpts`` on ``/dev/pts`` with ``mount -t devpts devpts /dev/pts``.

Getting the image
-----------------
After the image has finished building, ensure that the ``livecd.ubuntu-cpc.vagrant.box`` file exists in ``/build``.

We will use ``scp`` to transfer the image from the guest VM back to our host system. In a suitable folder on the host system, while the guest VM is running, run:

.. code:: bash

   scp -P 2222 root@localhost:/build/livecd.ubuntu-cpc.vagrant.box .

This makes use of the ports we forwarded when launching the QEMU VM, as well as the ssh keys added to the cloud-init YAML file.

Running the box
---------------
Assuming the default name of ``livecd.ubuntu-cpc.vagrant.box``, run:

.. code:: bash

   vagrant box add livecd.ubuntu-cpc.vagrant.box –name jammy_bartender
   vagrant init jammy_bartender
   vagrant up
   vagrant ssh

See :ref:`run-a-vagrant-box` for more details.
