Ubuntu Security on Azure
########################

Ubuntu security features
************************

Ubuntu on Azure inherits and benefits from all of the security features available to Ubuntu Server. Learn more about
Ubuntu Server security features and security-related topics with `Introduction to Security <https://documentation.ubuntu.com/server/explanation/intro-to/security/>`_.

Azure security features
***********************

Azure provides two types of security features:

* `Trusted Launch`_ which is a set of features including virtual Trusted Platform Module (vTPM) and `secure boot`_
* `Confidential Virtual Machine`_ with support for AMD Secure Encrypted Virtualization-Secure Nested Paging (SEV-SNP), along with `measured boot`_ using a vTPM

To launch Ubuntu images with Trusted Launch and Confidential VM, refer to :doc:`../azure-how-to/instances/launch-ubuntu-images`.

Trusted launch
==============

All Ubuntu images from 20.04 LTS (Focal Fossa) support trusted launch and secure boot on Hyper-V Gen2 instances. 

Confidential VM
===============

What are confidential VMs?
--------------------------

Check out our `technical blog post about Confidential VMs on Azure`_.

In short, a confidential VM is a combination of two features:

* *Memory encryption:* The virtual machine's memory is encrypted and decrypted on the fly by the CPU. This is done using AMD SEV-SNP technology. This ensures that the host machine cannot read the memory of the guest since the encryption is done at the hardware level
* *vTPM backed full-disk encryption (FDE):* The file system of the guest OS is encrypted at rest and the key is stored in an enclave. The key cannot be retrieved unless the boot process has stayed untouched since the last sealing of the key. Re-sealing happens when a new kernel is installed as replacing the kernel binary changes the boot sequence. The vTPM is part of the guest VM and its address space. So it benefits from the same run-time security guarantees as the guest VM memory.

It's important to note that memory encryption is always enabled with a confidential VM, but FDE is optional and requires explicit activation after the VM is provisioned.

Using Ubuntu on confidential VMs
--------------------------------

Ubuntu LTS images starting from 20.04 support Confidential VMs. While 20.04 only supports AMD's SEV-SNP technology as the underlying hardware, from 22.04 onwards the images support both AMD SEV-SNP and Intel TDX. However, the Intel TDX option is still in Public Preview and has not yet reached General Availability. 


.. _`Trusted Launch`: https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch
.. _`secure boot`: https://wiki.ubuntu.com/UEFI/SecureBoot
.. _`Confidential Virtual Machine`: https://learn.microsoft.com/en-us/azure/confidential-computing/confidential-vm-overview
.. _`measured boot`: https://learn.microsoft.com/en-us/azure/security/fundamentals/measured-boot-host-attestation
.. _`technical blog post about Confidential VMs on Azure`: https://canonical.com/blog/lets-get-confidential-canonical-ubuntu-confidential-vms-are-now-generally-available-on-microsoft-azure
