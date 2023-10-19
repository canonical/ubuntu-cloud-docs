Security: Confidential computing
================================

.. include:: ../../reuse/common-intro.txt
   :start-after: Start: Confidential computing
   :end-before: End: Confidential computing


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



Confidential computing on GCP
-----------------------------

To create and launch confidential compute enabled instances on GCE, refer to:

* Intel® TDX - :ref:`create-intel-tdx-conf-compute-on-gcp`
* AMD SEV - :ref:`create-amd-sev-conf-compute-on-gcp`


.. _`Intel® Trust Domain Extensions`: https://www.intel.com/content/dam/develop/external/us/en/documents/tdx-whitepaper-v4.pdf
