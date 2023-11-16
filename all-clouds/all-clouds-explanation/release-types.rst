Cloud image release types
=========================

.. include:: ../../reuse/common-intro.txt
   :start-after: Start: Daily vs release images
   :end-before: End: Daily vs release images

Daily images are not published for all products and on all public clouds. If a cloud image or offer is not explicitly tagged as "daily", one can safely assume that it is a "release" image.

New release images are published whenever an updated package within the image requires a VM reboot for the update to take effect. These include packages such as:

* the Linux kernel
* grub
* openssl
* cloud-init and
* cloud agents (different per cloud)