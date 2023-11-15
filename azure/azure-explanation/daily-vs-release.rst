Release and Daily cloud-images on Azure
=======================================

This page is about cloud-images on Azure. To learn more about Release vs Daily cloud-images in general, see this page: :ref:`all-clouds/all-clouds-explanations/release-types`.

On Azure, Daily and Release images for a given release of Ubuntu are published under two distinct offers. To avoid any confusion, only Release images of Ubuntu can be found on the Azure Marketplace while Daily images are "hidden".

In order to find Daily cloud-images, one can run the following command using the Azure CLI:

  az vm image list -p Canonical --offer 'daily' --all

Retention Policies
==================

Canonical uses different retention policies for Daily and Release images. As safety precaution users should always try to use the `latest` tag where possible. For example, use `Canonical:0001-com-ubuntu-server-jammy:22_04-lts-gen2:latest` instead of `Canonical:0001-com-ubuntu-server-jammy:22_04-lts-gen2:22.04.202311010`.

Release Images
--------------

On Azure, do to a limitation of the Marketplace, Canonical only keeps 90 Release images per plan/sku. For example, the image described by this URN `Canonical:0001-com-ubuntu-server-jammy:22_04-lts-arm64:22.04.202206220` will be available until 90 new images have been published under this plan `Canonical:0001-com-ubuntu-server-jammy:22_04-lts-arm64` (which should take approximately 2 years).

Daily Images
------------

Since Daily images are only meant for testing, Canonical only keeps 10 images per plan/sku.
