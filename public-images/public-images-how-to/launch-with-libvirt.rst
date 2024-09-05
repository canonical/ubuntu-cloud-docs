.. _launch-libvirt:

Launch QCOW images using libvirt
================================

Amongst the virtualization tools available for Ubuntu, there is `libvirt`_. libvirt is not a hypervisor, but rather a set of tools and libraries used to manage various other hypervisors, such as `KVM`_ and `QEMU`_.

Although there are many more `applications using libvirt`_, this guide will focus on launching QCOW images. To install the QEMU libvirt driver, along with the command-line programs that'll be used in this guide, install the ``virt-manager`` package:

.. code:: bash

   sudo apt-get install virt-manager


Create cloud-init user-data
---------------------------

Since we are dealing with cloud images here, we'll need a cloud-init user-data file to configure the VM instance. To create one, refer to :ref:`Specifying user data for a local cloud-init data source <specify-cloud-init-user-data>`.


Find and download an image
--------------------------

Ubuntu cloud images are hosted on https://cloud-images.ubuntu.com/. Refer to :doc:`../public-images-reference/artifacts` for a description of the various image types found there.

QCOW images (``.img``) are suitable for use with libvirt and the QEMU driver. Once you have identified a suitable image, download it. For example, the following would download the current daily Ubuntu 24.04 (noble) image for amd64 machines:

.. code:: bash

   wget https://cloud-images.ubuntu.com/noble/current/noble-server-cloudimg-amd64.img


Launch from the command-line
----------------------------

To launch the image, use: 

.. code:: bash

   virt-install \
      --name ubuntu-vm-name \
      --noautoconsole \
      --import \
      --memory 2048 --vcpus=2 \
      --osinfo generic \
      --disk bus=virtio,path=noble-server-cloudimg-amd64.img \
      --network default \
      --cloud-init user-data=user-data

The command will

* create a new VM named ``ubuntu-vm-name``
* skip attaching to the serial console
* import the image (as opposed to running an installer from it)
* create a machine with 2GB of RAM and 2 virtual CPUs
* select a generic OS. Although it might be tempting to specify Ubuntu for ``--osinfo``, don't do that since it would have the effect of trying to perform an installation. Cloud images are pre-installed.
* select the virtio disk driver and the path to a downloaded disk image. This path needs to be accessible by the ``libvirt-daemon``.
* attach the VM to the ``default`` network
* specify the previously created cloud-init user-data file

Once launched, you can interact with the newly created VM with ``virsh``, the ``virt-manager`` graphical application, or any other libvirt application.

To attach to the console, use:

.. code:: bash

   virsh console ubuntu-vm-name

Once attached, you can detach from the console by pressing ``Ctrl-]``


To shutdown the VM, use:

.. code:: bash

   virsh shutdown ubuntu-vm-name


To remove the VM and its disk image, use:

.. code:: bash

   virsh undefine --domain ubuntu-vm-name --remove-all-storage



Alternatively use ``uvtool-libvirt``
------------------------------------

An alternate simpler way of finding, downloading and launching images is through the use of uvtool. uvtool can look at published cloud images using *simplestreams*, then retrieve and launch VM images through libvirt. To find and download an image, use:

.. code:: bash

   uvt-simplestreams-libvirt sync --source STREAM_URL FILTERS

Some common options for ``STREAM_URL`` are:

* releases: https://cloud-images.ubuntu.com/releases/
* daily: https://cloud-images.ubuntu.com/daily/
* minimal releases: https://cloud-images.ubuntu.com/minimal/releases/
* minimal daily: https://cloud-images.ubuntu.com/minimal/daily/

``FILTERS`` are combinations of image attributes. Some common attributes (fields of cloud images simplestreams) are:

* arch: the architecture (e.g. ``amd64``, ``arm64``)
* version: the Ubuntu release version (e.g. ``24.04``)
* release: the Ubuntu release code name (e.g. ``noble``)
* supported: whether that release is still supported
* label: identifies the type of release (e.g. ``release``, ``daily``)

If multiple images match the combination of filters, they will all be downloaded. For example, the following would download the most recent images matching both the amd64 architecture AND the Noble Numbat (24.04) Ubuntu release.

.. code:: bash

   uvt-simplestreams-libvirt sync \
      --source https://cloud-images.ubuntu.com/minimal/daily/ \
      arch=amd64 release=noble

For more examples of querying simplestreams, see the `Simplestreams how-to guides`_.

The downloaded images can be listed with:

.. code:: bash

   uvt-simplestreams-libvirt query


A VM instance can then be launched by specifying a name and a set of filters that exactly match one of the downloaded images:

.. code:: bash

   uvt-kvm create instance-name release=noble arch=amd64 label='minimal daily'


The aforementioned ``virsh`` and ``virt-manager`` (or other libvirt applications) can then be used to interact with the new VM.

Once you are done, all downloaded images can be removed by running:

.. code:: bash

   uvt-simplestreams-libvirt purge


.. _`libvirt`: https://libvirt.org/docs.html
.. _`applications using libvirt`: https://libvirt.org/apps.html
.. _`QEMU`: https://www.qemu.org/docs/master/index.html
.. _`KVM`: https://ubuntu.com/blog/kvm-hyphervisor
.. _`Simplestreams how-to guides`: https://canonical-simplestreams.readthedocs-hosted.com/en/latest/how-to/
