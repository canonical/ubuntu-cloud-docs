.. _vagrant-bartender:

Build a Vagrant box with Bartender
==================================

`Ubuntu Bartender <https://github.com/ubuntu-bartenders/ubuntu-old-fashioned/tree/master/scripts/ubuntu-bartender>`_ (Bartender) is a script based on `Ubuntu Old Fashioned <https://github.com/ubuntu-bartenders/ubuntu-old-fashioned/tree/master>`_ that lets you build Ubuntu cloud images locally using `livecd-rootfs <https://launchpad.net/livecd-rootfs>`_.

Disclaimer
----------
The use of Bartender to build custom Vagrant images is intended for development use only. It is **not** for building production images. Support of the Bartender tool is *only* for bugs within the tool itself, not community help with building images.

Basic setup
-----------
To run Bartender, you will need a copy of the Ubuntu Old Fashioned repository, ``git`` (version control), ``petname`` (for project naming), and availability of one of the build providers (Google Cloud Engine, AWS EC2, Microsoft Azure, or Multipass). In a suitable directory, run:

.. code:: bash

   sudo apt install petname git
   snap install multipass
   git clone https://github.com/ubuntu-bartenders/ubuntu-old-fashioned.git
   cd ubuntu-old-fashioned/scripts/ubuntu-bartender/

Building the box
----------------
Bartender takes in a number of configuration options. There following are of concern for building the Vagrant box:

- ``livecd-rootfs-branch``
   * This needs to match the ``series`` name described below
- ``build-provider``
   * For local builds, use ``multipass``
- ``series``
   * The `series <https://launchpad.net/ubuntu/+series>`_ for the image
   * This must always be specified for Bartender to run
- ``image-target``
   * Refers to the `series hook <https://git.launchpad.net/livecd-rootfs/tree/live-build/ubuntu-cpc/hooks.d/base/series>`_ to call in livecd-rootfs
   * Set this as ``vagrant``
- ``project``
   * This should always be set to ``ubuntu-cpc``

To build a Vagrant box for a given Ubuntu series name, run the following from the ``ubuntu-bartender`` directory. Replace all the ``$VARIABLES$``:

.. tabs::

   .. group-tab:: Generic

      .. code:: bash

         ./ubuntu-bartender \
            --livecd-rootfs-branch ubuntu/$UBUNTU_NAME$ \
            --build-provider $PROVIDER_OF_CHOICE$ \
            -- \
            --series $UBUNTU_NAME$ \
            --image-target vagrant \
            --project ubuntu-cpc

   .. group-tab:: Local Ubuntu 22.04 Jammy

      .. code:: bash

         ./ubuntu-bartender \
            --livecd-rootfs-branch ubuntu/jammy \
            --build-provider multipass \ 
            -- \
            --series jammy \ 
            --image-target vagrant \
            --project ubuntu-cpc

Bartender will get to work building the box. Once it has set up the VM and began building, Bartender will display the name of the project and where it is storing the log files. A quick way to view the detailed build progress is to open another terminal window and run:

.. code:: bash

   tail -f /path/to/ubuntu-bartender/project_name.log

If Bartender is unsuccessful in building, consult the build log to determine the cause of the error. 
If Bartender is successful in building, a tarball containing the build contents will be created with the format ``project_name.tar.gz``.

Running the box
---------------
Extract the contents of the build tarball and ``cd`` to the location of the ``.box`` file. Assuming the default name of ``livecd.ubuntu-cpc.vagrant.box``, run:

.. code:: bash

   vagrant box add livecd.ubuntu-cpc.vagrant.box -–name noble_bartender
   vagrant init noble_bartender
   vagrant up
   vagrant ssh

See :ref:`run-a-vagrant-box` for more details.
