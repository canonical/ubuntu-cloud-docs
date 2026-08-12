.. meta::
   :description: Discover details about the publicly available Ubuntu cloud images, including LXD, OpenStack, Vagrant, QCOW and Buildd images.


.. _index:

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
      - :ref:`Ubuntu cloud image artifacts <uci-artifacts>` • :ref:`LXD and OpenStack images <lxd-openstack-images>` • :ref:`Vagrant boxes <vagrant-explanation>` • :ref:`Buildd images <buildd>` 
      
    * - **Building and launching images**
      - :ref:`Build a Vagrant box with Bartender <vagrant-bartender>` • :ref:`Run a Vagrant box <run-a-vagrant-box>` • :ref:`Launch QCOW images using libvirt <launch-libvirt>` • :ref:`Launch QCOW images using QEMU <qcow-qemu>`  • :ref:`Run an OVA using VirtualBox <run-an-ova-using-virtualbox>`  • :ref:`Create and use a local cloud-init datasource <use-local-cloud-init-ds>`  • :ref:`Verify an image checksum <verify-image-checksum>` 
      
    * - **Policies**
      - :ref:`Security overview <ubuntu-security-on-public-images>` • :ref:`Image retention policy <public-image-retention-policy>` 
      

How this documentation is organized
------------------------------------

This documentation uses the `Diátaxis documentation structure <https://diataxis.fr/>`__.

* :ref:`How-to guides <public-images-how-to>` assume you have basic familiarity with Ubuntu images on public clouds and want to achieve specific goals. They are instructions covering key operations and common tasks involving different types of public Ubuntu cloud images.

* :ref:`Explanation <public-images-explanation>` includes topic overviews, background and context and detailed discussion. These include key topics, such as the different types of images that we build and support, security aspects and our image retention policy.

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
