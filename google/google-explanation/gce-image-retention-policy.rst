GCE image retention policies
=============================

All Ubuntu images on GCE go through a life-cycle of: *release* > *deprecation* > *deletion*. 

Whenever a new image is built and released to GCE, the previous serial of the corresponding image is deprecated. A deprecated image is not visible on the google console, but it can still be listed, launched in GCP, etc. Our image retention policy determines when an image will be deleted. Once deleted, the images are no longer accessible for use.

At any give time, there will be only **one** active image per Ubuntu variant, with all the other images of that variant being either deprecated or deleted.


Image retention policy
----------------------

.. include:: ../../reuse/common-intro.txt
   :start-after: Start: Daily vs release images
   :end-before: End: Daily vs release images

For more details about these image types, check out our documentation of :doc:`image release types <all-clouds:all-clouds-explanation/release-types>`, and to get a list of these images on GCP, refer to: :doc:`../google-how-to/gce/find-ubuntu-images`.

The retention policy can be summarised as follows:

.. code::

  ┌─────────────────┬────────┬─────────────────────────────────────┬────────────────────────────────────┐
  │  Ubuntu suite   │        │ Daily Images                        │ Release Images                     │
  ├─────────────────┼────────┼─────────────────────────────────────┼────────────────────────────────────┤
  │ Interim Release │ Active │ Delete all *but* the last 5 serials │ No images are deleted              │
  │                 │--------│-------------------------------------│------------------------------------│
  │                 │ EOL*   │ Delete all *but* the latest serial  │ Delete all *but* the latest serial │
  │=================│========│=====================================│====================================│
  │ LTS Release     │ Active │ Delete all *but* the last 5 serials │ No images are deleted              │
  │                 │--------│-------------------------------------│------------------------------------│
  │                 │ EOSS** │ Delete all *but* the latest serial  │ No images are deleted              │
  └─────────────────┴────────┴─────────────────────────────────────┴────────────────────────────────────┘


where:
  - **EOL** refers to when an interim Ubuntu release (for example, Lunar Lobster 23.04) has reached end-of-life, `and will no longer enjoy support <https://ubuntu.com/about/release-cycle/>`_
  - **EOSS** refers to when an LTS Ubuntu release (for example, Jammy Jellyfish 22.04) has reached "End of Standard Support" but will remain supported under Ubuntu Pro
