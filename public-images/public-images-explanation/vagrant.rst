.. _vagrant-explanation:

Vagrant
=======
`Vagrant <https://www.vagrantup.com/>`_ is a multi-provider tool for building and managing virtual machines by HashiCorp. For more information, you can check out the `Vagrant documentation <https://developer.hashicorp.com/vagrant/intro>`_.

Boxes
-----
Vagrant boxes are ``tar`` files containing an image or container specific to the provider, Vagrant metadata, and a base `Vagrantfile <https://developer.hashicorp.com/vagrant/docs/vagrantfile>`_. They are essentially `OVA <https://docs.vmware.com/en/VMware-vSphere/7.0/com.vmware.vsphere.vm_admin.doc/GUID-AE61948B-C2EE-436E-BAFB-3C7209088552.html>`_ files with extra metadata and preinstalled packages.

What are they for
~~~~~~~~~~~~~~~~~
The Vagrant boxes `provided <http://cloud-images.ubuntu.com/>`_ by Canonical are meant for local development use. They are not meant to be used in a production environment.

When are they published
~~~~~~~~~~~~~~~~~~~~~~~
Boxes are published daily.

Despite their publication date, all boxes published to Vagrant Cloud point to the latest published version hosted on cloud-images.ubuntu.com.

How are they built
~~~~~~~~~~~~~~~~~~
The VirtualBox Vagrant box is produced as part of a "Base" build with the code living in `livecd-roofs <https://git.launchpad.net/livecd-rootfs/tree/live-build/ubuntu-cpc/hooks.d/base/vagrant.binary>`_. The build generates a ``box.ovf`` config file, a config drive ``vmdk``, the base server ``vmdk``, Vagrantfile, and Vagrant metadata. These build components are then combined in the ``.box`` tarball.

See :ref:`public-images-how-to` for more on building and running Vagrant boxes.

Support
-------
Vagrant has been dropped by Ubuntu due to the adoption of the  `Business Source License (BSL) <https://www.hashicorp.com/bsl>`_.  Following this change, **Canonical will no longer publish Vagrant images** directly starting with Ubuntu 24.04 LTS (Noble Numbat).

Support Matrix
~~~~~~~~~~~~~~
- Support is provided for images utilising ``vagrant`` and ``virtualbox`` packages from the archive.
- Best support will be given for matching guest and host Ubuntu. 
- Best efforts will be made when the guest and host differ. 
- There is no support for extra plugins.
- There is no support for images starting with Ubuntu 24.04 LTS and beyond.
- Support for matching `Guest Additions <https://help.ubuntu.com/community/VirtualBox/GuestAdditions>`_.
