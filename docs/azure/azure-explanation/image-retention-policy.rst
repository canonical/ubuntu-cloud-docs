.. meta::
   :description: Understand the Ubuntu image retention policy on Azure, including release and daily image lifecycles and marketplace availability.

.. _image-retention-policy:

Image retention policy
======================

.. include:: ../../reuse/common-intro.txt
   :start-after: Start: Daily vs release images
   :end-before: End: Daily vs release images

Refer to :ref:`image release types <all-clouds:release-types>` and :ref:`Understanding Ubuntu cloud images <all-clouds:understanding-ubuntu-cloud-images>` for further explanation of cloud images and image types.

On Azure, *release* and *daily* images for a given Ubuntu release are published under two distinct offers. To avoid confusion, only *release* images of Ubuntu are displayed on the Azure Marketplace and *daily* images are 'hidden'.

To find the *daily* images, use the Azure CLI and run: 

.. code::

    az vm image list -p Canonical --offer 'daily' --all


Retention policies
------------------

The images published on Azure are not retained forever. Whenever possible, it is safer to use the ``latest`` tag while selecting images. For example, use ``Canonical:0001-com-ubuntu-server-jammy:22_04-lts-gen2:latest`` instead of ``Canonical:0001-com-ubuntu-server-jammy:22_04-lts-gen2:22.04.202311010``. 

Deprecation lifecycle
~~~~~~~~~~~~~~~~~~~~~

Once an image version falls outside the retention limits described below, it is deprecated rather than removed immediately:

1. The image enters a 90-day deprecation period. During this time, users receive warnings from Azure.
2. After the 90-day period expires, the deprecated image version is permanently removed from the marketplace and cannot be used to launch new virtual machines.

This lifecycle applies uniformly to both *release* and *daily* images. There are different retention policies for *release* and *daily* images, which determine when an image becomes eligible for deprecation:

*release* images
~~~~~~~~~~~~~~~~

The retention policy for *release* images depends on the status of the plan:

* **Active release plans.** The last 20 *release* image versions per plan/SKU are retained. No image version less than six months old will be removed, ensuring recent builds remain available regardless of the 20-image threshold.
* **Plans past standard maintenance.** For SKUs under plans that no longer receive active image updates (such as free public plans for releases that have transitioned out of their standard five-year window), only a single, final image version is retained.

For example, the image described by the URN ``Canonical:0001-com-ubuntu-server-jammy:22_04-lts-arm64:22.04.202206220`` will be available until 20 newer images have been published under the ``Canonical:0001-com-ubuntu-server-jammy:22_04-lts-arm64`` plan, or until the image is more than six months old (whichever comes later).

*daily* images
~~~~~~~~~~~~~~

Since the *daily* images are only meant for testing, 10 images per plan/SKU are kept alive.
