GCE image retention policies
=============================

GCE Ubuntu image deletion
~~~~~~~~~~~~~~~~~~~~~~~~~~

Ubuntu cloud images have a concept of "daily" and "release" images. In a nutshell, daily images are untested builds with cutting edge features and package versions.
Release images are tested and therefore benefit from Canonical's in-life support. See how to list both "daily" and "release" images here: :doc:`find-ubuntu-images`.

Older daily and release images are subject to a retention policy. The policy can be summarised as follows:

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

GCE Ubuntu image deprecation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Images are also subject to "deprecation". Image deletion and deprecation are not the same; a deprecated image can still be listed, launched in GCP, etc. unlike "deleted" images.
At any give time, there will only ever be **one** active image per suite and type (i.e. minimal, base, etc.) with all the other images subject to either deprecation or deletion.
When a new daily image is built and released to GCE, the previous daily serial is deprecated, with the same being true for release images.