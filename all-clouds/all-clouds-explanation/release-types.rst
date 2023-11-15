Cloud-image release types
=========================

Canonical publishes two different class of cloud-images: daily images and release images. While release images are fully tested and production grade, daily images are preview images containing all the latest updates from the archive. Daily images are test images and are not suitable for use in production.

Canonical does not publish daily images on all public clouds and for all products. If a cloud-image or offer is not explicitely tagged as "daily", one can safely assume that it is a "release" image/offer.

New Release images are published when a package affecting the VM first boot experience of the image is updated in the archive. THe release package set includes;

 * the linux kernel
 * systemd
 * glibc
 * grub
 * openssl
 * cloud-init
