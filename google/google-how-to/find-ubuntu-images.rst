Find Ubuntu images on GCE
=========================

On your Google Cloud console, you can find the latest Ubuntu images by selecting ``Ubuntu`` as the Operating System under :guilabel:`Compute Engine` > :guilabel:`VM instances`> :guilabel:`CREATE INSTANCE` > :guilabel:`Boot disk` > :guilabel:`CHANGE`. 


For a programmatic method, you can use the gcloud command:

.. code::

  gcloud compute images list --filter ubuntu-os

Daily, untested images are found under the ``ubuntu-os-cloud-devel`` project:

.. code::

  gcloud compute images --project ubuntu-os-cloud-devel list --filter ubuntu-os-cloud-devel


Image locator
-------------

Canonical also produces an `Ubuntu cloud image finder`_ where users can filter based on a variety of criteria, such as region or release, etc.


.. _`Ubuntu cloud image finder`: https://cloud-images.ubuntu.com/locator/
