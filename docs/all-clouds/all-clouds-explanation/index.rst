.. meta::
   :description: Understand key concepts for Ubuntu public cloud images, including release types, security, base images, and confidential computing.

Explanation
===========

Some key topics needed to understand the public cloud images are discussed here. They are common across all public clouds. Details that vary across the individual clouds, are discussed and clarified in their respective documentation sets.

Ubuntu image specifics
-----------------------

Understand some of the fundamental variants of Ubuntu cloud images - different release types, base vs minimal images, and architecture variants.

* :doc:`Cloud image release types <release-types>` 
* :doc:`Ubuntu base and minimal images <ubuntu-base-and-minimal-images>` 
* :doc:`Architecture variants support <architecture-variants>`


Security aspects
-----------------

Learn about the security practices and features built into Ubuntu cloud images. They include things like CVE handling, Kernel Livepatch, Hardening (DISA STIG, CIS), FIPS, AppArmor, and more.

* :doc:`Security in Ubuntu cloud images <security-overview>`


Customizations
---------------

Some specific customizations available in our cloud images are described here - confidential computing using trusted execution environments (Intel TDX and AMD SEV-SNP) and cloud-init metapackages.

* :doc:`Confidential computing <confidential-computing>` 
* :doc:`Cloud-init metapackages <cloud-init-metapackages>` 


.. toctree::
   :maxdepth: 1
   :hidden:
   
   Cloud image release types <release-types>
   Ubuntu base and minimal images <ubuntu-base-and-minimal-images>
   Security overview <security-overview>
   Confidential computing <confidential-computing>
   Cloud-init metapackages <cloud-init-metapackages>
   Architecture Variants <architecture-variants>
   Kernels on the cloud <kernels-on-the-cloud>
