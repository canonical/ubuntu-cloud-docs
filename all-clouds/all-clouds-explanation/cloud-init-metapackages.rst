Cloud-init metapackages
=======================

Starting in Ubuntu 25.04, `cloud-init <https://docs.cloud-init.io>`_
added `cloud-specific metapackages <https://launchpad.net/ubuntu/+source/cloud-init>`_
to better express cloud-specific dependencies and reduce image size.

The original ``cloud-init`` is still available as a metapackage and a smaller
version (called ``cloud-init-base``) has been created to include just the essential
dependencies.
A few specific metapackages have been created, while more cloud-specific ones are
under development. The current set include:

* ``cloud-init-base`` - package that contains the cloud-init code along with the
  minimal set of dependencies

* ``cloud-init`` - is a metapackage that retains every previous dependency

* ``cloud-init-cloud-sigma`` and ``cloud-init-smart-os`` - metapackages with an
  additional dependency on python3-serial. They can be installed if the target
  platform is `CloudSigma <https://www.cloudsigma.com>`_ or
  `SmartOS <https://docs.smartos.org>`_

If you are an image builder:

* Install ``cloud-init``, containing all dependencies, if the target platform is unknown

* Install ``cloud-init-base`` if the target platform(s) are known and do not
  require specific dependencies

* Install a cloud-specific metapackage if the target platform has some specific
  dependency requirements.

