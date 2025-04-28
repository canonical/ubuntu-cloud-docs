Confidential computing
======================

Confidential computing addresses the question of trust between cloud providers and their users. The idea is to hide and protect sensitive workloads. Users should be allowed to run programs on untrusted systems with the technical assurance that the cloud provider cannot read nor modify the program's data and memory. While it might not be entirely possible to satisfy these requirements, the solutions at least ensure that modification of data is detected.

Data can be thought of as being in one of three states:  

* in-transit - being transmitted from one location to another
* at-rest - stored somewhere and
* in-use - being used by a CPU to perform some operation
  
Both data in-transit and data at-rest can be encrypted using well-known techniques, but securing data in-use needs confidential computing.

Confidential computing is the protection of data in-use by performing computation in a hardware-based trusted execution environment. These are secure and isolated environments that prevent unauthorized access or modification of applications and data while they are in use. In effect, they allow the encryption of data while it is in the system memory. This requires the support of both hardware and the OS. For example, your hardware could be based on Intel's TDX (Trust Domain Extensions) processors or AMD's SEV (Secure Encrypted Virtualization) architecture and the OS could be Ubuntu. 


Intel® Trust Domain Extensions (Intel® TDX)
-------------------------------------------

Intel introduced Intel® TDX to its confidential computing portfolio with the launch of its new 4th Gen Xeon enterprise processors in January, 2023. Intel® TDX is a combination of hardware and software features that provide isolation and security for virtual machines (VMs) running on Intel processors. It introduces architectural innovations to enable the deployment of hardware-isolated VMs, known as trust domains (TDs). The primary objective of Intel® TDX is to create a robust isolation layer between TDs and the virtual-machine manager (VMM)/hypervisor, as well as other non-TD software. This offers comprehensive protection against a wide spectrum of potential threats. 

These hardware-isolated TDs encompass several critical components, including the Secure Arbitration Mode (SEAM) module, an Intel-provided, digitally-signed security-services module. Additional features of TDX include:

* shared bit in the guest-physical address
* secure extended-page table for address-translation integrity
* physical-address-metadata table for page management
* multi-key total-memory-encryption engine for memory encryption and integrity
* remote attestation 

These features are integral to ensuring the security and trustworthiness of TD execution within the Intel® TDX system. For further details, check out this white paper on `Intel® Trust Domain Extensions`_.

In essence, Intel® TDX empowers you to execute your workloads within a logically isolated hardware-based execution environment. This is achieved by allocating a dedicated segment of system memory that undergoes real-time encryption using an advanced AES-128 encryption engine. TDX also introduces stringent access control measures that govern memory access. This prevents external access, including access from the cloud's privileged system software.


AMD SEV-SNP
-----------

Secure Encrypted Virtualization-Secure Nested Paging (SEV-SNP) is a security feature available on AMD's EPYC processors. It provides the following benefits for your VMs: 

* `Improved security` - it encrypts the memory pages that contain firmware code. This makes it much more difficult for attackers to gain access to the firmware and launch attacks.
* `Increased isolation` - it allows each VM to have its own secure memory space. This means that a VM cannot access the memory of another VM, even if the hypervisor is compromised.
* `Enhanced performance` - it can be used to improve the performance of virtualized applications. This is because SEV-SNP allows the hypervisor to offload some of the security processing to the processor.

SEV-SNP provides an extra layer of safeguard against malicious hypervisor-based attacks, such as data reply and memory re-mapping, by establishing a secure and isolated execution environment.

It also introduces several optional security enhancements, strengthens protection around interrupt behavior and bolsters defenses against side channel attacks.

For further details, check out this white paper on `AMD SEV-SNP - Strengthening VM Isolation with Integrity Protection and More`_.

.. _`Intel® Trust Domain Extensions`: https://cdrdv2-public.intel.com/690419/TDX-Whitepaper-February2022.pdf

.. _`AMD SEV-SNP - Strengthening VM Isolation with Integrity Protection and More`: https://www.amd.com/content/dam/amd/en/documents/epyc-business-docs/white-papers/SEV-SNP-strengthening-vm-isolation-with-integrity-protection-and-more.pdf
