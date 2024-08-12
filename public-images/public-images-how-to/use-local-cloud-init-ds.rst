.. _use-local-ds:

Create and use a local cloud-init datasource
============================================

Purpose
-------

The steps in this how-to guide will allow you to create an Ubuntu seed image that defines a custom cloud-init datasource.

Using a custom local datasource is a great way to inject custom user data or metadata into cloud images launched
locally, e.g. with `QEMU`. Launching images in this way is handy for anything from testing to running private workloads.

Requirements
------------

We'll be using the `cloud-localds`_ command, which comes from the `cloud-image-utils`_ package. For launching an image
with `QEMU`_, you will need `qemu-system-x86`. These can be installed via Apt with:

.. code::

    sudo apt update
    sudo apt install --yes cloud-image-utils qemu-system-x86

Specify user data
-----------------

Create a YAML file with your desired user data. User data specifies user-defined configuration and content required at
boot time, such as SSH keys or login preferences.

Example:

.. code::

    cat > user-data.yaml <<EOF
    #cloud-config
    password: password
    chpasswd:
      expire: False
    ssh_pwauth: True
    ssh_authorized_keys:
      - ssh-rsa AAAA...UlIsqdaO+w==
    EOF

Specify datasource metadata (optional)
--------------------------------------

If desired, create a YAML file with your desired datasource `metadata`_. Metadata describes typically cloud-defined
configuration and content required at boot time, such as server name or instance id.

.. code::

    echo "instance-id: $(uuidgen || echo i-abcdefg)" > my-meta-data.yaml

Create the seed image
---------------------

Now that you've defined the relevant pieces of user data and metadata, you can create the datasource seed image, which
is simply a disk image containing the user data and metadata cloud-init will need to do its job:

.. code::

    cloud-localds my-seed.img user-data.yaml my-meta-data.yaml

Download and launch an Ubuntu cloud image with QEMU
---------------------------------------------------

Download the latest Ubuntu server image, then pass that and your newly-created seed image to the QEMU launch command.

The following command launches a cloud image with:

* KVM acceleration
* the local machine's CPUs
* 2GB of memory
* no graphics, only serial output to the console
* snapshot -- this option will make writes to a temporary file instead of the disk image itself. This ensures that the base disk is not touched. If at some point, you want to persist the changes you've made on the disk, press ``ctrl-a`` (the default QEMU escape sequence) followed by ``s``
* virtio network device that redirects the guest (cloud image) port 22 to host (desktop OS) port 2222
* virtio cloud image
* virtio seed image

.. code::

    curl -O http://cloud-images.ubuntu.com/noble/current/noble-server-cloudimg-amd64.img
    qemu-system-x86_64  \
      -cpu host -machine type=q35,accel=kvm -m 2048 \
      -nographic \
      -snapshot \
      -netdev id=net00,type=user,hostfwd=tcp::2222-:22 \
      -device virtio-net-pci,netdev=net00 \
      -drive if=virtio,format=qcow2,file=noble-server-cloudimg-amd64.img \
      -drive if=virtio,format=raw,file=my-seed.img

.. _cloud-localds: https://manpages.ubuntu.com/manpages/noble/en/man1/cloud-localds.1.html
.. _cloud-image-utils: https://github.com/canonical/cloud-utils
.. _cloud-init: https://cloudinit.readthedocs.io/en/latest/reference/custom_modules/custom_datasource.html
.. _metadata: https://cloudinit.readthedocs.io/en/latest/explanation/instancedata.html#instance-metadata
.. _QEMU: https://www.qemu.org/docs/master/
