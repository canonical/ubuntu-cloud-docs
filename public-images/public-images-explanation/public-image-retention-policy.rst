Public images retention policies
================================

All Ubuntu images on `cloud-images.ubuntu.com`_ go through a life-cycle of: *release* > *deprecation* > *deletion*. 

Whenever a new daily image is built and released, all the previous serials for that image are deprecated except for the last 6. This policy determines when an image will be deleted, at which point it is no longer available for use.


Image retention policy
----------------------

.. include:: ../../reuse/common-intro.txt
   :start-after: Start: Daily vs release images
   :end-before: End: Daily vs release images

For more details about these image types, check out our documentation of :doc:`image release types <all-clouds:all-clouds-explanation/release-types>`.

The retention policy can be summarized as follows:

.. list-table::
   :header-rows: 1

   * - **Ubuntu suite**
     -
     - **Daily Images**
     - **Release Images**
   * - Interim Release
     - Active
     - Delete all *but* the last 6 serials
     - No images are deleted
   * -
     - EOL*
     - Delete all serials
     - Delete all *but* the latest serial
   * - LTS Release
     - Active
     - Delete all *but* the last 6 serials
     - No images are deleted
   * -
     - EOSS**
     - Delete all *but* the last 6 serials
     - No images are deleted

where:
  - **EOL** refers to when an interim Ubuntu release (for example, Lunar Lobster 23.04) has reached end-of-life, `and will no longer enjoy support <https://ubuntu.com/about/release-cycle/>`_
  - **EOSS** refers to when an LTS Ubuntu release (for example, Bionic Beaver 18.04 LTS) has reached "End of Standard Support"

.. Links
.. _cloud-images.ubuntu.com: https://cloud-images.ubuntu.com/