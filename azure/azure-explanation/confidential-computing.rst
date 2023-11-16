Confidential computing
======================

.. include:: ../../reuse/common-intro.txt
   :start-after: Start: Confidential computing
   :end-before: End: Confidential computing

Azure provides two types of *security*:

* `Trusted launch <https://docs.microsoft.com/en-us/azure/virtual-machines/trusted-launch>`_ which is a set of features including virtual Trusted Platform Module (vTPM) and `secure boot <https://wiki.ubuntu.com/UEFI/SecureBoot>`_
* `Confidential virtual machine <https://docs.microsoft.com/en-us/azure/confidential-computing/confidential-vm-overview>`_ with support for `AMD Secure Encrypted Virtualisation-Secure Nested Paging (SEV-SNP) <https://www.amd.com/system/files/TechDocs/SEV-SNP-strengthening-vm-isolation-with-integrity-protection-and-more.pdf>`_, along with `measured boot <https://docs.microsoft.com/en-us/azure/security/fundamentals/measured-boot-host-attestation>`_ using a vTPM


Trusted launch
--------------

All Ubuntu images from 20.04 (Focal Fossa) support trusted launch and secure boot on Hyper-V Gen2 instances. 
To start an Ubuntu instance with vTPM and secure boot enabled, use the following flags from the Azure CLI::
        
   --security-type TrustedLaunch --enable-secure-boot true --enable-vtpm

Confidential VM
---------------

What are confidential VMs?
~~~~~~~~~~~~~~~~~~~~~~~~~~

Check out our `technical blog post about Confidential VMs on Azure <https://canonical.com/blog/lets-get-confidential-canonical-ubuntu-confidential-vms-are-now-generally-available-on-microsoft-azure>`_.

In short, a confidential VM is a combination of two features:

* *Memory encryption:* The virtual machine's memory is encrypted and decrypted on the fly by the CPU. This is done using AMD SEV-SNP technology. This ensures that the host machine cannot read the memory of the guest since the encryption is done at the hardware level
* *vTPM backed full-disk encryption (FDE):* The file system of the guest OS is encrypted at rest and the key is stored in an enclave. The key cannot be retrieved unless the boot process has stayed untouched since the last sealing of the key. Re-sealing happens when a new kernel is installed as replacing the kernel binary changes the boot sequence. The vTPM is part of the guest VM and its address space. So it benefits from the same run-time security guarantees as the guest VM memory.

It's important to note that memory encryption is always enabled with a confidential VM, but FDE is optional and requires explicit activation after the VM is provisioned.


Using Ubuntu on confidential VMs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Confidential VMs require the use of special instance sizes and a special version of Ubuntu.

* A list of instance sizes that can be used for confidential VMs is given in `Azure's documentation <https://docs.microsoft.com/en-us/azure/confidential-computing/confidential-vm-overview>`_ 
* Only `this specific offer of Ubuntu <https://azuremarketplace.microsoft.com/en-gb/marketplace/apps/canonical.0001-com-ubuntu-confidential-vm-focal>`_ supports confidential VMs.


   