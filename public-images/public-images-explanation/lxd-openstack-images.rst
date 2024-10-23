.. _lxd-openstack-images:

LXD and OpenStack images
========================

`LXD <https://canonical.com/lxd>`__ is an open-source tool for
orchestrating virtual machines and system containers. It is image based,
and provides support for a large number of distributions and
architectures.

`OpenStack <https://ubuntu.com/openstack>`__ is an
open-source cloud platform designed to create and manage cloud
resources. By aggregating physical resources such as distributed
compute, network, and storage into a pool, OpenStack then allocates
virtual resources on-demand to users out of this pool. It does not
handle virtualisation itself, but acts as a wrapper that leverages
existing virtualisation technologies.


What are these images?
----------------------

Canonical provides cloud image artefacts on
`cloud-images.ubuntu.com <https://cloud-images.ubuntu.com/>`__ that have
been customised to run on public clouds, including LXD and OpenStack. To
learn more about these artefacts and supported architectures, visit our
Ubuntu cloud image artefacts documentation :doc:`here <../public-images-reference/artefacts>`.


How do you access them?
-----------------------

Go to `cloud-images.ubuntu.com <https://cloud-images.ubuntu.com/>`__ and
select a release. For the latest LTS release, Ubuntu 24.04 LTS Noble
Numbat, you would navigate to ``noble > current``. Note that all artefacts are
architecture specific, in the format
``<release>-<type>-cloudimg-<architecture>-<artefact>``.

LXD and OpenStack also have `Minimal Cloud
Images <https://cloud-images.ubuntu.com/minimal/>`__:
Ubuntu images that have a reduced runtime footprint, optimised kernel
and boot process. They are smaller and boot faster, but are not designed
for environments requiring human interaction or debugging.


LXD images
~~~~~~~~~~

To import an image into LXD, you will need two artefacts:

1. An LXD tarball:

   - The :ref:`lxd-tarball-ref` artefact has the extension ``*.lxd.tar.xz``
   - It contains the metadata needed by LXD to instantiate a container or virtual machine as well as a folder for any custom templates

2. A file system for a container or a bootable disk image for a virtual
   machine:

   - The file system for a container can be either a 

     * :ref:`root-tarball-ref` (``*-root.tar.xz``), or a 

     * :ref:`squashfs-ref` (``*.squashfs``)

   - The bootable disk image for a virtual machine is a :ref:`qcow-ref` image (``*.img``)

The following is an example command to import an LXD container image based on
downloaded Ubuntu 24.04 artefacts:

.. code :: bash

   lxc image import noble-server-cloudimg-amd64-lxd.tar.xz
   noble-server-cloudimg-amd64-root.tar.xz --alias noble_container


OpenStack images
~~~~~~~~~~~~~~~~

OpenStack uses QCOW images. Download the artefact for your chosen
architecture with the ``*.img`` extension.

Use the `OpenStack command-line
client <https://docs.openstack.org/ocata/admin-guide/common/cli-install-openstack-command-line-clients.html>`__
to interact with OpenStack. An example of uploading an image looks 
something like this:

.. code :: bash

   openstack image create “Ubuntu-24.04” \\
      --file noble-server-cloudimg-amd64.img \\
      --disk-format qcow2 \\
      --container-format bare \\
      --public

To learn more about managing images with OpenStack, you can read their
documentation
`here <https://docs.openstack.org/ocata/admin-guide/common/cli-manage-images.html#create-or-update-an-image-glance>`__.


Configuration
-------------

Configuring an Ubuntu cloud image allows you to make changes that tailor
the image to your specific use case. You can automate the creation of
user accounts, configure SSH access, or install software before the
instance starts.


LXD images
~~~~~~~~~~

You can configure your cloud images in LXD either before you import them
or after. Configuring your images before importing them is most commonly
done by editing the ``metadata.yaml`` file contained in the LXD tarball.
Configuring your images after importing them is done through the CLI.

If you are interested in configuration of LXD containers rather than
images, take a look at the Ubuntu Server documentation
`here <https://documentation.ubuntu.com/server/how-to/containers/lxd-containers/>`__.


Metadata
^^^^^^^^

LXD metadata is stored in the ``metadata.yaml`` file in the LXD tarball. This file contains all of 
the information needed to run an image in LXD. To make changes to this file, you will have to:

1. Uncompress the LXD tarball.
2. Make modifications to the ``metadata.yaml`` file. See the `LXD image
   format
   documentation <https://documentation.ubuntu.com/lxd/en/latest/reference/image_format/#>`__
   to learn more about image metadata and the templates you may wish to
   modify.
3. Compress the metadata and templates.

This snippet from the `How to customise LXD image metadata for
cloud-init <https://discourse.ubuntu.com/t/how-to-customize-lxd-image-metadata-for-cloud-init/25157>`__
guide referenced below demonstrates a typical workflow:

.. code :: bash

   # Uncompress original LXD metadata
   $ tar xf ${RELEASE}-server-cloudimg-amd64-lxd.tar.xz
   # Add directives to create /etc/cloud/cloud.cfg.d/95-use-lxd.cfg
   $ cat > templates/cloud-init-use-lxd.tpl <<EOF
   # Added by LXD metadata.yaml
   datasource_list: [ LXD, NoCloud ]
   EOF
   $ cat > add-lxd.yaml <<EOF
       /etc/cloud/cloud.cfg.d/95-use-lxd.cfg:
           when:
               - create
               - copy
           template: cloud-init-use-lxd.tpl
   EOF
   $ cat add-lxd.yaml >> metadata.yaml
   # Compress LXD metadata and templates
   $ tar -czf ${RELEASE}-server-cloudimg-amd64-prefer-lxd.tar.xz metadata.yaml templates/


Cloud-init
^^^^^^^^^^

`Cloud-init <https://cloudinit.readthedocs.io/en/latest/index.html>`__
is used to initialise cloud instances on first boot. A detailed guide on
customising LXD image metadata for ``cloud-init`` can be found
`here <https://discourse.ubuntu.com/t/how-to-customize-lxd-image-metadata-for-cloud-init/25157>`__.
If you want to configure ``cloud-init`` once an instance has been
created (but not booted), refer to the LXD docs
`here <https://documentation.ubuntu.com/lxd/en/latest/cloud-init/>`__.


CLI
^^^

The `LXD documentation on
images <https://documentation.ubuntu.com/lxd/en/latest/howto/images_manage/>`__
has an extensive guide on managing images. Two of the most common use
cases are to set individual properties or to edit all of the image
properties.

.. code :: bash

   # set a specific image property
   lxc image set-property <image_ID> <key> <value>


.. code :: bash

   # edit the full image properties
   lxc image edit <image_ID>


OpenStack images
~~~~~~~~~~~~~~~~

OpenStack has an extensive guide on `modifying
images <https://docs.openstack.org/image-guide/modify-images.html>`__
that is applicable to the QCOW images Ubuntu provides. It leverages ``libguestfs`` 
`tools <https://libguestfs.org/>`__ in order to access and
modify disk images. You can use the ``guestfish``
`interactive shell <https://libguestfs.org/guestfish.1.html>`__ 
— which exposes the full functionality of the ``guestfs`` API — or
rely on the ``virt-*`` tools from ``libguestfs`` — like ``virt-cat`` for
displaying files, ``virt-df`` for checking free space, and
``virt-inspector`` for inspecting VM images — to perform specific tasks.
