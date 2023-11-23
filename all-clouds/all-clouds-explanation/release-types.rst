Cloud image release types
=========================

Canonical publishes two types of Ubuntu images for different public cloud partners:

*release* images
----------------

These are fully tested, production grade images and are the default option on all public cloud marketplaces. Unless an image is explicitly marked as *daily*, one can safely assume that it is a *release* image.

New *release* images are published whenever an updated package within the image requires a VM reboot for the update to take effect. These include packages such as:

* the Linux kernel
* grub
* openssl
* cloud-init and
* cloud agents (different per cloud)


*daily* images
--------------

These are preview images that contain all the latest updates from the Ubuntu archive. They are not fully tested, and are unsuitable for use in production. They allow people to easily test all the latest packages from the Ubuntu archive in an easy-to-launch image without needing to apply updates.

These *daily* images are not published on all public clouds and are not available for all products, i.e. not all *release* images have corresponding *daily* images.

