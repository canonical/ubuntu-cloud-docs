.. meta::
   :description: Understand the Ubuntu and Oracle Cloud security features available while using Ubuntu on Oracle Cloud, including full-disk encryption.

Security features with Ubuntu on Oracle Cloud
=============================================

Ubuntu images on Oracle Cloud include the security features provided by both Ubuntu and Oracle Cloud. Some of these features might need to be specifically enabled. This explanation provides pointers to these features.

Ubuntu security features
------------------------

Ubuntu on Oracle provides all the security features available on Ubuntu Server. A detailed description of these features can be found on the `Ubuntu security page`_ and in our explanation about :doc:`Security in the Ubuntu cloud images <all-clouds:all-clouds-explanation/security-overview>`. For further guidance on usage refer to  Ubuntu server's `Introductory page on security`_. 


Oracle Cloud security features
------------------------------

Oracle Cloud offers comprehensive security and data protection in the cloud. This documentation about `Security in the Oracle Cloud Infrastructure`_ explains how users can benefit from their security features.


Full-disk encryption (FDE)
~~~~~~~~~~~~~~~~~~~~~~~~~~

FDE ensures that all data on the disk is inaccessible without an encryption key. To use FDE on Oracle Cloud, refer to :doc:`../oracle-how-to/use-fde`.


Confidential computing
~~~~~~~~~~~~~~~~~~~~~~

Confidential computing protects data in-use by performing computation in a hardware-based trusted execution environment. Oracle Cloud supports confidential computing on AMD EPYC™ processors using two technologies:

* **AMD SEV** (Secure Encrypted Virtualization) on VM shapes — encrypts VM memory with a unique key per VM, isolating guests from the hypervisor.
* **AMD TSME** (Transparent Secure Memory Encryption) on bare metal shapes — encrypts all system memory transparently.

These technologies are available on E3, E4, and E5 shapes across select regions. For further details about AMD SEV and TSME, see `AMD's description of SEV`_. To enable confidential computing on an Oracle Cloud instance, refer to :doc:`../oracle-how-to/enable-confidential-computing`.


.. _`Ubuntu security page`: https://ubuntu.com/security
.. _`Introductory page on security`: https://documentation.ubuntu.com/server/explanation/intro-to/security/
.. _`Security in the Oracle Cloud Infrastructure`: https://docs.oracle.com/en-us/iaas/Content/Security/Concepts/security.htm
.. _`AMD's description of SEV`: https://www.amd.com/en/developer/sev.html
