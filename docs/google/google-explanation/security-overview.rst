Security features with Ubuntu on GCP
====================================

Ubuntu images on Google Cloud include the security features provided by both Ubuntu and GCP. Some of these features might need to be specifically enabled. This explanation provides pointers to these features and to the specific how-to guides that help you enable them.


Ubuntu security features
------------------------

Ubuntu on GCP provides all the security features available on Ubuntu Server. A detailed description of these features can be found on the `Ubuntu security page`_ and in our explanation about :doc:`Security in the Ubuntu cloud images <all-clouds:all-clouds-explanation/security-overview>`. For further guidance on usage refer to  Ubuntu server's `Introductory page on security`_. 


GCP security features
---------------------

GCP offers comprehensive security and data protection in the cloud. `Security in Google Cloud`_ explains how users can benefit from GCP security features.


Confidential computing on GCP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To create and launch confidential compute enabled instances on GCE, refer to:

* :ref:`create-intel-tdx-conf-compute-on-gcp`
* :ref:`create-amd-sev-conf-compute-on-gcp`


Enhanced security using Ubuntu Pro
----------------------------------

Apart from the Ubuntu Server images, GCP also has images for `Ubuntu Pro`_, which come with enhanced security features:

* Expanded Security Maintenance (ESM): Provides 10 years of security patching for packages in the Ubuntu (main and universe) repositories.
* Live kernel updates: These reduce downtime and unplanned reboots in case of kernel vulnerabilities.
* FIPS compliance: Includes FIPS-certified modules to enable the use of Ubuntu in highly regulated environments.

To find Ubuntu Pro images on GCE, refer to :ref:`create-pro-on-gcp` and :ref:`create-pro-fips-on-gcp` and to enable the different Pro features refer to :doc:`../google-how-to/gce/enable-pro-features`.


.. _`Ubuntu security page`: https://ubuntu.com/security
.. _`Introductory page on security`: https://documentation.ubuntu.com/server/explanation/intro-to/security/
.. _`Security in Google Cloud`: https://cloud.google.com/docs/security
.. _`Ubuntu Pro`: https://ubuntu.com/aws/pro

