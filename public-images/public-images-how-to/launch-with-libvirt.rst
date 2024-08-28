.. _launch-libvirt:

Launch QCOW images using libvirt
================================

Amongst the virtualization tools available for Ubuntu, there is `libvirt`_. `libvirt`_ is not a hypervisor, but rather a set of tools and libraries to manage various other hypervisors, such as `KVM`_ and `QEMU`_.

Although there are many more `applications using libvirt`_, this guide will focus on common ones.
The *recommended packages* for the ``virt-manager`` package will also install the `QEMU`_ libvirt driver, along with the command-line programs which will be used in this guide.
Those can be installed with the following command:

.. code:: bash

   sudo apt-get install virt-manager


Creating cloud-init user-data
-----------------------------

Since we are dealing with cloud images here, we will need a cloud-init user-data file to configure the VM instance. Refer to
:ref:`use-local-cloud-init-ds`.


Find and download an image
--------------------------

Ubuntu cloud images are hosted on https://cloud-images.ubuntu.com/

QCOW images (``.img``) are suitable for use with `libvirt`_ and the `QEMU`_ driver.
Refer to :doc:`../public-images-reference/artifacts` for a description the various image types found at https://cloud-images.ubuntu.com/.

Once you have identified a suitable image, download it. For example, the following would download the current daily Ubuntu 24.04 (noble) image for amd64 machines:

.. code:: bash

   wget https://cloud-images.ubuntu.com/noble/current/noble-server-cloudimg-amd64.img


Launching from the command-line
-------------------------------

The following command will

* Create a new VM named ``ubuntu-vm-name``.
* Skip attaching to the serial console.
* Import the image (as opposed to running an installer from it).
* Create a machine with 2GB of RAM and 2 virtual CPUs.
* Select a generic OS. Although it might be tempting to specify Ubuntu for ``--osinfo``, this would have the effect of trying to automate an installation. Cloud images are pre-installed.
* Select the virtio disk driver and the path to a downloaded disk image. This path needs to be accessible by the ``libvirt-daemon``.
* Attach the VM to the ``default`` network.
* Specify the cloud-init user-data file previously created.


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


Then, you can then interact with the newly created virtual machine with ``virsh``, the ``virt-manager`` graphical application, or any other libvirt application.

To attach to the console

.. code:: bash

   virsh console ubuntu-vm-name

Once attached, you can also detach from the console by pressing ``Ctrl-]``


To shutdown the VM

.. code:: bash

   virsh shutdown ubuntu-vm-name


To remove the VM and its disk image

.. code:: bash

   virsh undefine --domain ubuntu-vm-name --remove-all-storage



Alternatively using ``uvtool-libvirt``
--------------------------------------

Finding, downloading and launching images can be simplified by the use of uvtool. uvtool can look at published cloud images *simplestreams*, then retrieve and launch VM images through `libvirt`.

.. code:: bash

   uvt-simplestreams-libvirt sync --source STREAM_URL FILTERS

Common stream URLs are

* releases: https://cloud-images.ubuntu.com/releases/
* daily: https://cloud-images.ubuntu.com/daily/
* minimal releases: https://cloud-images.ubuntu.com/minimal/releases/
* minimal daily: https://cloud-images.ubuntu.com/minimal/daily/

*FILTERS* are a combination of image attributes. Common fields of cloud images simplestreams are:

* arch: the architecture (e.g. ``amd64``, ``arm64``)
* version: the Ubuntu release version (e.g. ``24.04``)
* release: the Ubuntu release code name (e.g. ``noble``)
* supported: whether that release is still supported
* label: identifies the type of release (e.g. ``release``, ``daily``)

For more examples of querying simplestreams, see `Simplestreams How-to`_.

If multiple images match the combination of filters, they will all be downloaded. For example, the following would download the most recent images matching both the amd64 architecture AND the Noble Numbat (24.04) Ubuntu release.

.. code:: bash

   uvt-simplestreams-libvirt sync \
      --source https://cloud-images.ubuntu.com/minimal/daily/ \
      arch=amd64 release=noble

Downloaded images can be listed with:

.. code:: bash

   uvt-simplestreams-libvirt query


A VM instance can then be launched by specifying a name and a set of filters matching exactly one of the downloaded image:

.. code:: bash

   uvt-kvm create instance-name release=noble arch=amd64 label='minimal daily'


The aforementioned ``virsh`` and ``virt-manager`` (or other libvirt applications) can then be used to interact with the new virtual machine.

Once you are done, all downloaded images can be removed by running:

.. code:: bash

   uvt-simplestreams-libvirt purge


.. _`libvirt`: https://libvirt.org/docs.html
.. _`applications using libvirt`: https://libvirt.org/apps.html
.. _`QEMU`: https://www.qemu.org/docs/master/index.html
.. _`KVM`: https://ubuntu.com/blog/kvm-hyphervisor
.. _`Simplestreams How-to`: https://canonical-simplestreams.readthedocs-hosted.com/en/latest/how-to/
