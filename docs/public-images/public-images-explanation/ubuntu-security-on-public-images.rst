.. _ubuntu-security-on-public-images:

Ubuntu security on cloud images
===============================

Ubuntu security features
------------------------

Download images available at `Cloud images <https://cloud-images.ubuntu.com/>`_ (including OCI and LXD images) inherit all the security features available on Ubuntu Server. A detailed description of these features can be found on the `Ubuntu security page`_ and further guidance on usage is available from the `Ubuntu server's security overview page`_. 

Enhanced security using Ubuntu Pro
----------------------------------

Enhanced security features are available for Ubuntu via the Ubuntu Pro subscription:

* Expanded Security Maintenance (ESM): Provides up to 12 years of support for security updates as detailed in the `ESM <https://ubuntu.com/security/esm>`_ section.
* Kernel livepatching: Shrinks the exploit window for critical kernel vulnerabilities as detailed in the `Livepatch <https://ubuntu.com/security/livepatch>`_ section.
* Security compliance and certifications: Provides rigorous security certifications such as FIPS and CIS as detailed in the `Certifications <https://ubuntu.com/security/certifications/docs>`_ section.

Common Vulnerabilities and Exposures (CVE)
------------------------------------------

All CVEs affecting Ubuntu are tracked and reported on the `Ubuntu CVE <https://ubuntu.com/security/cves>`_ system. This system allows users to:

* Stay up to date with publicly disclosed security vulnerabilities.
* Find which releases are affected by a specific vulnerability.
* Track the status of CVEs and the patches released to address these CVEs.

Following the fix of security issues, notices are posted under `Security notices <https://ubuntu.com/security/notices>`_

Image signing and checksums
---------------------------

Each image published under `Cloud images <https://cloud-images.ubuntu.com/>`_ comes with a corresponding SHA256 checksum and GPG file that allows you to verify its authenticity and that
it has not been corrupted or tampered with. 

The Ubuntu tutorial `How to verify Ubuntu <https://ubuntu.com/tutorials/how-to-verify-ubuntu>`_ gives a detailed guide on how to
verify and validate the integrity of an image.

.. _`Ubuntu security page`: https://ubuntu.com/security
.. _`Ubuntu server's security overview page`: https://documentation.ubuntu.com/server/explanation/intro-to/security/
