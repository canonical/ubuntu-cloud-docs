.. meta::
   :description: Discover details about the publically available Ubuntu cloud images, including LXD, OpenStack, Vagrant, QCOW and Buildd images.


Ubuntu Public Images
====================

**Canonical produces generic (generic kernel) cloud images, LXD images (rootfs tarballs) and KVM optimized cloud images (KVM kernel)**. These images are public (unlike other cloud-specific images) and are available on `cloud-images.ubuntu.com`_.
Canonical also produces so-called Buildd images that are used primarily by `Launchpad <https://launchpad.net/builders>`_ to serve the purpose of building archive packages and Ubuntu images.

.. include:: ../reuse/common-intro.txt
   :start-after: Start: Product need and user
   :end-before: End: Product need and user


---------

In this documentation
---------------------

.. list-table::
    :widths: 35 65
    :header-rows: 0

    * - **Canonical's offerings**
      - :doc:`Ubuntu cloud image artifacts <public-images-reference/artifacts>` • :doc:`LXD and OpenStack images <public-images-explanation/lxd-openstack-images>` • :doc:`Vagrant boxes <public-images-explanation/vagrant>` • :doc:`Buildd images <public-images-explanation/buildd>` 
      
    * - **Building and launching images**
      - :doc:`Build a Vagrant box with Bartender <public-images-how-to/build-vagrant-with-bartender>` • :doc:`Run a Vagrant box <public-images-how-to/run-a-vagrant-box>` • :doc:`Launch QCOW images using libvirt <public-images-how-to/launch-with-libvirt>` • :doc:`Launch QCOW images using QEMU <public-images-how-to/launch-qcow-with-qemu>`  • :doc:`Run an OVA using VirtualBox <public-images-how-to/run-an-ova-using-virtualbox>`  • :doc:`Create and use a local cloud-init datasource <public-images-how-to/use-local-cloud-init-ds>`  • :doc:`Verify an image checksum <public-images-how-to/verify-image-checksum>` 
      
    * - **Policies**
      - :doc:`Security overview <public-images-explanation/ubuntu-security-on-public-images>` • :doc:`Image retention policy <public-images-explanation/public-image-retention-policy>` 
      

How this documentation is organized
------------------------------------

This documentation uses the `Diátaxis documentation structure <https://diataxis.fr/>`__.

* :doc:`How-to guides  <public-images-how-to/index>` assume you have basic familiarity with Ubuntu images on public clouds and want to achieve specific goals. They are instructions covering key operations and common tasks involving different types of public Ubuntu cloud images.

* :doc:`Explanation <public-images-explanation/index>` includes topic overviews, background and context and detailed discussion. These include key topics, such as the different types of images that we build and support, security aspects and our image retention policy.

---------

Project and community
---------------------

Ubuntu Public Images is a member of the Ubuntu family and the project warmly welcomes community projects, contributions, suggestions, fixes and constructive feedback.


Get involved
~~~~~~~~~~~~
	
* `Get support`_
* `Discuss on Matrix`_
* :ref:`public-images-contribute`

Governance and policies
~~~~~~~~~~~~~~~~~~~~~~~

* `Code of conduct`_


.. toctree::
   :hidden:
   :maxdepth: 1

   public-images-how-to/index
   public-images-explanation/index
   public-images-reference/artifacts
   public-images-how-to/contribute-to-these-docs

.. _Get support: https://ubuntu.com/cloud/public-cloud
.. _`Discuss on Matrix`: https://matrix.to/#/#ubuntu-cloud:ubuntu.com
.. _Code of conduct: https://ubuntu.com/community/docs/ethos/code-of-conduct
.. _cloud-images.ubuntu.com: https://cloud-images.ubuntu.com
