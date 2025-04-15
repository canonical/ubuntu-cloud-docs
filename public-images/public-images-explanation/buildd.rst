Ubuntu Buildd images
====================

Buildd images are another offering of cloud images built by Canonical that are used primarily to serve the `Launchpad build farm <https://documentation.ubuntu.com/launchpad/en/latest/reference/services/build-farm/#>`_.
These images are publicly available to download and use and can be found under `cloud-images.ubuntu.com/buildd <https://cloud-images.ubuntu.com/buildd/>`_. 

Ubuntu Buildd image use cases
------------------------------
Buildd images are intended to be used for building Ubuntu packages or other Ubuntu images as detailed in the `build farm description <https://documentation.ubuntu.com/launchpad/en/latest/reference/services/build-farm/#detailed-description>`_ section:

* Deb packages for the `Ubuntu Archive <https://archive.ubuntu.com/>`_
* Snaps for Canonical's `Snapcraft <https://snapcraft.io/>`_
* Charms for Canonical's `Charmhub <https://charmhub.io/>`_
* Ubuntu images based on the `Ubuntu Base <https://wiki.ubuntu.com/Base>`_ project.


Difference from other cloud images
----------------------------------

Buildd images are meant to be light and very minimal compared to other cloud images offered by Canonical. This is due to the following:

* They contain only a small set of packages that are required to build new packages (such as debs or snaps), charms, or images.
* Direct access to the internet is not enabled for these images; it can be granted for a restricted set of URLs through token authentication.
* The images published as combined lxd tarballs are not bootable and do not contain a kernel unlike the QCoW disk images.

Due to the lack of common user space tools and the additional configuration required to set up networking and internet access for Buildd images, Canonical does not recommend their use outside the use cases explained above. 

For general consumption, and specifically for cloud-oriented work, minimal or base images found under `cloud-images.ubuntu.com <https://cloud-images.ubuntu.com/>`_ are better suited.