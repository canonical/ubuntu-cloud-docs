Ubuntu Security on Azure
========================

Ubuntu images on Azure include the security features provided by both Ubuntu and Azure. Some of these features might need to be specifically enabled. This explanation provides pointers to these features and to the specific how-to guides that help you enable them.

Ubuntu security features
------------------------

Ubuntu on Azure inherits and benefits from all of the security features available to Ubuntu Server. A detailed description of these features can be found on the `Ubuntu security page`_ and in our explanation about :doc:`Security in the Ubuntu cloud images <all-clouds:all-clouds-explanation/security-overview>`. For further guidance on usage refer to  Ubuntu server's `Introductory page on security`_. 

Azure security features
-----------------------

Azure provides two main types of security features.

Trusted Launch
~~~~~~~~~~~~~~

`Trusted Launch`_ is now available by default when you launch an Ubuntu image on Azure. It comes with support for `secure boot`_ and includes a virtual Trusted Platform Module (vTPM). All Ubuntu images from 20.04 LTS (Focal Fossa) support trusted launch and secure boot on Hyper-V Gen2 instances.

Confidential Virtual Machines (CVMs)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

`CVMs`_ powered by Ubuntu and AMD's SEV-SNP technology as the underlying hardware are currently available. Ubuntu LTS images starting from 20.04 support AMD SEV-SNP, while from 22.04 onwards the images support both AMD SEV-SNP and Intel TDX. The Intel TDX option is still in public preview and is not yet generally available.

Apart from the trusted execution environments (TEE) provided by these specialized hardware components, these CVMS also support `measured boot`_ using a vTPM.

For confidential AI workloads, the security model also extends to GPU processing through the NVIDIA H100 Tensor Core GPU, which implements its own TEE with encrypted data transfer between the CPU and GPU.

To launch Ubuntu Confidential VMs, refer to :doc:`../azure-how-to/instances/launch-ubuntu-images`. It's important to note that though memory encryption is always enabled (via the TEE) with a confidential VM, full-disk encryption (FDE) is optional, and it requires explicit activation after the VM is provisioned.

To better understand the concepts of secure boot, measured boot, FDE and CVMs, refer to the relevant sections in our `generic cloud security overview page`_.


Enhanced security using Ubuntu Pro
----------------------------------

Apart from the Ubuntu Server images, Azure also has images for `Ubuntu Pro`_, which come with enhanced security features:

* Expanded Security Maintenance (ESM): Provides 10 years of security patching for packages in the Ubuntu (main and universe) repositories.
* Live kernel updates: These reduce downtime and unplanned reboots in case of kernel vulnerabilities.
* FIPS compliance: Includes FIPS-certified modules to enable the use of Ubuntu in highly regulated environments.

To find Ubuntu Pro images on Azure, refer to :doc:`../azure-how-to/instances/find-ubuntu-images`. 


.. _`Ubuntu security page`: https://ubuntu.com/security
.. _`Introductory page on security`: https://documentation.ubuntu.com/server/explanation/intro-to/security/
.. _`Trusted Launch`: https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch
.. _`secure boot`: https://wiki.ubuntu.com/UEFI/SecureBoot
.. _`CVMs`: https://learn.microsoft.com/en-us/azure/confidential-computing/confidential-vm-overview
.. _`measured boot`: https://learn.microsoft.com/en-us/azure/security/fundamentals/measured-boot-host-attestation
.. _`generic cloud security overview page`: https://documentation.ubuntu.com/public-cloud/all-clouds-explanation/security-overview/#verified-boot-tpm-fde
.. _`Ubuntu Pro`: https://ubuntu.com/azure/pro
