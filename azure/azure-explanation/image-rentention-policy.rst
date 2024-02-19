Image retention policy
======================

.. include:: ../../reuse/common-intro.txt
   :start-after: Start: Daily vs release images
   :end-before: End: Daily vs release images

For more details about these image types, check out our documentation of :doc:`image release types <all-clouds:all-clouds-explanation/release-types>`. 

On Azure, *release* and *daily* images for a given Ubuntu release are published under two distinct offers. To avoid confusion, only *release* images of Ubuntu are displayed on the Azure Marketplace and *daily* images are 'hidden'.

To find the *daily* images, use the Azure CLI and run: 

.. code::

    az vm image list -p Canonical --offer 'daily' --all


Retention policies
------------------

The images published on Azure are not retained forever. Whenever possible, it is safer to use the ``latest`` tag while selecting images. For example, use ``Canonical:0001-com-ubuntu-server-jammy:22_04-lts-gen2:latest`` instead of ``Canonical:0001-com-ubuntu-server-jammy:22_04-lts-gen2:22.04.202311010``. 

There are different retention policies for *release* and *daily* images:

*release* images
~~~~~~~~~~~~~~~~

Only 90 *release* images per plan/SKU are kept alive at any given time. This is due to a marketplace limit on the number of images. For example, the image described by the  URN ``Canonical:0001-com-ubuntu-server-jammy:22_04-lts-arm64:22.04.202206220`` will be available until 90 new images have been published under the ``Canonical:0001-com-ubuntu-server-jammy:22_04-lts-arm64`` plan. This translates into an approximate time period of two years.

*daily* images
~~~~~~~~~~~~~~

Since the *daily* images are only meant for testing, 10 images per plan/SKU are kept alive.
