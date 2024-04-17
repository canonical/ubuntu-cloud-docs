.. _run-a-vagrant-box:

Run a Vagrant box
=====================
The quickest way to get a vagrant environment up and running is ``vagrant init <BOX>``. For upstream, use a call such as ``vagrant init ubuntu/focal64``. To bring up the image, ``vagrant up``. This will create a VM, create an ssh key and associate it with the vagrant user, and mount the default synced directory (``./`` to ``/vagrant``). The image should boot relatively quickly, dependent on hardware. The default Vagrant timeout is five minutes, and if it's even close to that, something has gone wrong.

Custom boxes
------------
For working on development boxes built by Bartender or live-build, you'll need to import the box: ``vagrant box add <path/to/box> --name <name-for-box>``. You can then use the newly added box by name. Once a box is added, it is unpacked in ``~/.vagrant.d/boxes/``. The structure then follows the pattern ``<BOX_NAME>/<VERSION>/<PROVIDER>/`` with the unpacked tar .box files. This is useful if you're making changes to the Vagrantfile in ``livecd-rootfs`` and want to check the Vagrantfile was written properly.

To ssh into a server, run ``vagrant ssh``. This will use the default generated ssh key for the vagrant user.

Combining the above, to launch a Vagrant box from a custom box, run:

.. code:: bash

   sudo apt-get update && apt-get install vagrant virtualbox
   vagrant box add <path/to/box> --name <name-for-box>
   vagrant init <BOX>	 
   vagrant up		 
   vagrant ssh

On the host, you can run ``uname -a`` or ``lsb_release -a`` to check that the distribution is as expected based on the build process.

The Vagrantfile
---------------
Vagrantfiles are written in Ruby. This is handy to know, as you do have access to the core Ruby language. Running ``vagrant init`` provides a fairly extensive, commented file for review. If you need something smaller to start, you can copy the template below to spin up a vm:

.. code:: ruby

   # -*- mode: ruby -*-
   # vi: set ft=ruby :
   Vagrant.configure("2") do |config|
     config.vm.box = "ubuntu/groovy64"
   end

The default Vagrantfile created for our images is in the `livecd-rootfs hook <https://git.launchpad.net/livecd-rootfs/tree/live-build/ubuntu-cpc/hooks.d/base/vagrant.binary#n141>`_. It includes creating a serial connection to a NULL file as well as front-loaded imports required for base box Vagrantfiles.

Common errors
-------------
Below you can find some of the more common errors that occur when attempting to run your Vagrant box.

Multiple Hypervisor Incompatibility
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
KVM/QEMU, Multipass, and VirtualBox are all hypervisors that may be used during the course of building or running Vagrant boxes. You may run into issues if you attempt to use multiple hypervisors at the same time.

QEMU running
^^^^^^^^^^^^
When you try and start Vagrant after building your box, you may get a variation on the following error:

.. terminal::

   VirtualBox can't enable the AMD-V extension. Please disable the KVM kernel extension, recompile your kernel and reboot (VERR_SVM_IN_USE)

First check that the QEMU VM isn’t running. If it is then shut it down by pressing ``C-a x``. If this doesn’t resolve the error, use a process manager like ``htop`` to search for and end any ``kvm`` processes.

VirtualBox (Vagrant) running
^^^^^^^^^^^^^^^^^^^^^^^^^^^^
If you have VirtualBox (Vagrant) running and you try and launch a QEMU VM, you may encounter the a variation on the following error:

.. terminal::

   ioctl(KVM_CREATE_VM) failed: 16 Device or resource busy
   qemu-system-x86_64: failed to initialize kvm: Device or resource busy

First check that your Vagrant box isn’t running with ``vagrant status``. You can stop the running Vagrant machine with ``vagrant halt``. If this doesn’t resolve the error, use a process manager like ``htop`` to search for and end any ``vbox`` / ``virtualbox`` processes.

Remote host identification has changed
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
If you create and launch multiple different Vagrant boxes, you may get a scary looking warning when you try and connect via ``vagrant ssh``:                                                                                                                                  

.. terminal::

   WARNING: REMOTE HOST IDENTIFICATION HAS CHANGED!

This occurs when you try to connect to the same localhost connection, but the underlying guest VM has changed. To resolve this issue, you can run the following command (typically provided as part of the error message):

.. code:: bash

   ssh-keygen -f "/home/$USER$/.ssh/known_hosts" -R "[localhost]:2222"

This removes the connection from your ``known_hosts`` file and allows you to add the keys from the new guest VM and connect as expected.
