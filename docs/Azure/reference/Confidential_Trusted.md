# Trusted Launch and Confidential VM

Azure provides two *security types*:

* [Trusted Launch](https://docs.microsoft.com/en-us/azure/virtual-machines/trusted-launch) which is a set of features including vTPM and [Secure Boot](https://wiki.ubuntu.com/UEFI/SecureBoot)
* [Confidential VM](https://docs.microsoft.com/en-us/azure/confidential-computing/confidential-vm-overview) with support for [AMD SEV-SNP](https://www.amd.com/system/files/TechDocs/SEV-SNP-strengthening-vm-isolation-with-integrity-protection-and-more.pdf), along with [measured boot](https://docs.microsoft.com/en-us/azure/security/fundamentals/measured-boot-host-attestation) using a vTPM

## Trusted Launch

All Ubuntu images from 20.04 (Focal Fossa) support Trusted Launch and secure boot on Hyper-V Gen2 instances. One can start an instance of Ubuntu with secure boot enabled and a vTPM with the Azure CLI by using the following flags: `--security-type TrustedLaunch --enable-secure-boot true --enable-vtpm`.

##  Confidential VM

### Use Confidential VM on Ubuntu

Confidential VM require the use a special instance sizes and a special version of Ubuntu.

* the list of instance sizes that can be used with Confidential VM can be found in [Azure's documentation](https://docs.microsoft.com/en-us/azure/confidential-computing/confidential-vm-overview)
* only [this specific offer of Ubuntu](https://azuremarketplace.microsoft.com/en-gb/marketplace/apps/canonical.0001-com-ubuntu-confidential-vm-focal) supports Confidential VM

### What is it?

See [our techincal blog post about Confidential VM](https://canonical.com/blog/lets-get-confidential-canonical-ubuntu-confidential-vms-are-now-generally-available-on-microsoft-azure).

In short, Confidential VM is the combination of two features:

* Memory encryption: the memory of the virtual machine is encrypted and decrypted on the fly by the CPU. This is done using AMD SEV-SNP technology. This ensures that the host machine cannot read the memory of the guest since the encryption is done at the hardware level
* (v)TPM backed Full-disk encryption (FDE): not only the file system of the guest OS is encrypted at rest but the keys are stored in an enclave and cannot be retrieved unless the boot process stayed untouched since the key was sealed. Re-sealing happen when a new kernel is installed as replacing the kernel binary changes the boot sequence. The vTPM is part of the guest VM and its address space. As such, it benefits from the same run-time security guarantees as the guest VM memory.

It's important to note that memory encryption is always enabled with Confidential VM, but FDE is optional and require explicit activation on VM provisioning.
