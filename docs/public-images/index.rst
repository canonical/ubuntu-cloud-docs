Ubuntu Public Images
====================

**Canonical produces generic (generic kernel) cloud images, LXD images (rootfs tarballs) and KVM optimized cloud images (KVM kernel)**. These images are public (unlike other cloud-specific images) and are available on `cloud-images.ubuntu.com`_.
Canonical also produces so-called Buildd images that are used primarily by `Launchpad <https://launchpad.net/builders>`_ to serve the purpose of building archive packages and Ubuntu images.

.. include:: ../reuse/common-intro.txt
   :start-after: Start: Product need and user
   :end-before: End: Product need and user


---------

In this documentation
---------------------

..  grid:: 1 1 1 1
   :padding: 0

   ..  grid-item:: :doc:`How-to guides <public-images-how-to/index>`

      **Step-by-step guides** covering key operations related to our Public Images offerings.

.. grid:: 1 1 2 2
   :padding: 0

   .. grid-item:: :doc:`Explanation <public-images-explanation/index>`

      **Discussion and clarification** of key topics such as the different types of images available, security aspects and our retention policy.

   .. grid-item:: :doc:`Cloud image artifacts - A reference <public-images-reference/artifacts>`

      **Reference guide** for the artifacts found on `cloud-images.ubuntu.com`_.



----------

Project and community
---------------------

Ubuntu Public Images is a member of the Ubuntu family and the project warmly welcomes community projects, contributions, 
suggestions, fixes and constructive feedback.


* `Get support`_
* `Discuss on Matrix`_
* :ref:`public-images-contribute`
* `Code of conduct`_

.. If none of the above options are suitable for you, and you still want to get in touch, send us an email: aws@canonical.com.

.. toctree::
   :hidden:
   :maxdepth: 1

   public-images-how-to/index
   public-images-explanation/index
   public-images-reference/artifacts
   public-images-how-to/contribute-to-these-docs

.. _Get support: https://ubuntu.com/cloud/public-cloud
.. _`Discuss on Matrix`: https://matrix.to/#/#ubuntu-cloud:ubuntu.com
.. _Code of conduct: https://ubuntu.com/community/docs/ethos/code-of-conduct
.. _cloud-images.ubuntu.com: https://cloud-images.ubuntu.com
