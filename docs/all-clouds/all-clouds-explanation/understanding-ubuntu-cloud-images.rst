.. meta::
   :description: Understand Ubuntu cloud images across public clouds, including image availability, update cadence, platform optimizations, and marketplace publishers.

.. _understanding-ubuntu-cloud-images:

Understanding Ubuntu cloud images
=================================

Canonical provides officially certified and optimized Ubuntu images across all major public cloud platforms. These images take advantage of each platform's features, hardware optimizations, and security capabilities.


Image refresh cadence
---------------------

Canonical regularly builds and publishes refreshed image versions across all supported cloud platforms.

* **Kernel updates:** New image builds are published primarily in response to kernel updates.
* **Security and bug fixes:** Critical security updates or urgent bug fixes may also trigger intermediate image releases.

Running instances are not automatically altered or rebooted when new images are published. To keep running virtual machines secure and updated:

* Use standard package management tools (e.g. ``apt`` or ``unattended-upgrades``) to apply system and package updates.
* Reboot instances when required to load newly installed kernel updates, or use Canonical's `Livepatch service <https://ubuntu.com/security/livepatch>`_ (available with Ubuntu Pro) to apply kernel security patches without downtime.

When launching instances via the command-line interface (CLI), APIs, or infrastructure-as-code automation, reference the ``latest`` alias or dynamic image query for your target release and variant. This ensures newly deployed instances always launch from the most recent, fully patched image build.


Marketplace publishers and third-party images
---------------------------------------------

Ubuntu is a collection of open-source software, and redistribution is permitted in accordance with `Canonical's intellectual property policy`_. As a result, you may encounter third-party publishers offering Ubuntu-based images across various cloud marketplaces.

Refer to the platform-specific guides for the official Canonical images:

* :ref:`Find Ubuntu images on AWS <aws:find-ubuntu-images>`
* :ref:`Find Ubuntu images on Azure <azure:find-ubuntu-images>`
* :ref:`Find Ubuntu images on GCP <google:find-ubuntu-images>`
* :ref:`Find Ubuntu images on IBM Cloud <ibm:find-ubuntu-images>`
* :ref:`Find Ubuntu images on Oracle Cloud <oracle:find-ubuntu-images>`

.. _`Canonical's intellectual property policy`: https://canonical.com/legal/intellectual-property-policy
