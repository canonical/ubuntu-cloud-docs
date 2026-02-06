Canonical's offerings on GCP
============================

Canonical works closely with Google to ensure Ubuntu images support the latest GCP features. An optimized Ubuntu GCP kernel, built in collaboration with Google, delivers the very
best performance for scale-out, optimized workloads on the Google Cloud hypervisor. This makes Ubuntu a popular choice for both virtual machines 
and container workloads.

The optimized ``linux-gcp`` kernel enables accelerated networking with the Compute Engine Virtual Ethernet device and support for the latest Google ARM Tau VM. These advantages contribute to Ubuntu being the default host images for Anthos Multi-cloud.

The Ubuntu images support secure boot, with signed NVIDIA drivers available for workloads requiring access to vGPU compute acceleration. For instances that require confidential compute, Ubuntu images have been SEV-capable since 18.04 with `SEV-SNP`_ and `Intel TDX`_ support currently in private preview.

Ubuntu images are updated regularly with fixes that address the latest CVEs to ensure applications remain free from vulnerabilities.

Another useful feature is the native integration of Ubuntu images with the Administrator console, enabling patch management and :doc:`in-place upgrade of Ubuntu LTS images to Ubuntu Pro <../google-how-to/gce/upgrade-in-place-from-lts-to-pro>` without the need for workload redeployment.



Kernel optimizations
--------------------

Ubuntu images available on GCP use optimized kernels tailored for different workload types. GCE images run the ``linux-gcp`` kernel, while GKE node images use the ``linux-gke`` kernel optimized specifically for Kubernetes workloads. Anthos on VMware images use the ``linux-gkeop`` kernel designed for on-premises Kubernetes deployments.

By default, Ubuntu images use a **rolling kernel model**, which provides the latest upstream bug fixes and performance improvements around task scheduling, I/O scheduling, networking, hypervisor guests and containers. A rolling kernel model transitions the default kernel from one base version to the next as part of its regular patching cycle. That new kernel, called the HWE Kernel (Hardware Enablement Kernel) is the kernel of the latest Ubuntu release.

For example, users running Ubuntu 24.04 LTS instances launched in early 2024 would start with the 6.8 kernel by default. However, as new Ubuntu interim versions are released, the linux-gcp kernel "rolls" forward to the next release's kernel version. Consequently, an Ubuntu 24.04 LTS instance launched at a later point in time—such as in 2025 or 2026—would include a different kernel version depending on when it was launched; for instance, it might feature version 6.11 or 6.14.

Furthermore, all running instances that use the rolling linux-gcp package have their kernels automatically updated to the latest version in the track upon reboot. This means that even instances originally launched with the 6.8 kernel will eventually transition to these newer versions, ensuring they benefit from the latest Google Cloud hardware support and performance optimizations.

For more details about the rolling kernel model, refer to the `Ubuntu kernel release cycle`_ and the relevant `installation options`_.

If you do not want to roll to a new kernel, and want to stay on the base kernel provided by the LTS release (which continues to get support and receive updates for the length of the LTS), you need to install a specific corresponding kernel variant: ``linux-gcp-lts-<release>`` for GCE or ``linux-gke-lts-<release>`` for GKE. (Refer to the next section for an example.)


Kernel variants
~~~~~~~~~~~~~~~

Canonical provides different kernel variants, all optimized for GCP. They are available in the APT archives, and can be installed with the ``apt install`` command.

**For GCE (Compute Engine) instances:**

For x86_64 instances:

* ``linux-gcp-lts-<release>``: Where <release> is replaced by an LTS Ubuntu version, such as 18.04, 20.04, 22.04 or 24.04. This kernel does not roll and sticks to the original kernel present in the Ubuntu release, for the life of the release (e.g.: linux-gcp-lts-24.04 will always point to a 6.8 kernel for the life of Ubuntu 24.04 LTS).
* ``linux-gcp-edge``: The -edge kernel provides early access to the next HWE kernel. It is fully supported, but is less exposed to real world use cases since it is relatively new. It eventually transitions to the linux-gcp kernel. It can for instance be used for testing the upcoming kernels in your specific environment.

For ARM64 instances, we have four variants - the two mentioned above for x86_64 instances and two more:

* ``linux-gcp-64k``: This variant uses 64k memory pages by default (instead of the standard 4k). It is optimized for high-performance networking and memory-intensive workloads on ARM-based infrastructure.

* ``linux-gcp-64k-edge``: This variant provides early access to the next HWE kernel that is configured to use 64k memory pages by default.

**For GKE (Kubernetes Engine) node images:**

* ``linux-gke``: The default kernel for GKE node images, optimized for Kubernetes workloads.
* ``linux-gke-64k``: For ARM64 GKE nodes, a 64k page size variant is available for improved performance in high-memory scenarios. This is available starting from GKE version 1.34.
* ``linux-gke-lts-<release>``: Non-rolling kernel variant that stays on the original LTS kernel version.



GCE Images
~~~~~~~~~~

For each active Ubuntu release, at least two image variants are created for GCE: 

* **Base** images that contain a full Ubuntu development environment
* **Minimal** images that have a smaller footprint than base images, and are designed for production instances that will never be accessed by a human

For the LTS releases from 22.04 onwards, we also have:

* **Accelerator** images that contain the packages needed to run accelerator workloads on advanced GPUs and include pre-tested NVIDIA driver stacks for faster provisioning. These images are intended for machine learning, HPC, and graphics workloads where GPU readiness is required at boot.

For the Ubuntu Pro offering, we have: 

* **Ubuntu Pro** images created for 16.04, 18.04, 20.04, 22.04, and 24.04 
* **Ubuntu Pro FIPS** images created for 18.04, 20.04, and 22.04


GKE images
~~~~~~~~~~

GKE is Google Cloud's Kubernetes offering. Canonical produces node images for GKE that act as a base for running end user pods. These node images include a kernel that is optimized for use in the GKE environment ``linux-gke``, as well as custom NVIDIA drivers for workloads that wish to leverage GPU acceleration. Further details of the node images available for GKE can be found in Google's documentation about `GKE node images`_.



Anthos - Google's multi-cloud GKE strategy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Google provides a multi-cloud GKE strategy through a variety of Anthos product offerings, with an Ubuntu foundation providing the cross-platform support:

* `GKE Anthos on AWS`_ 
* `GKE Anthos on Azure`_ 
* `GKE Anthos on VMware`_ 

.. _`Ubuntu kernel release cycle`: https://ubuntu.com/about/release-cycle#ubuntu-kernel-release-cycle
.. _`installation options`: https://ubuntu.com/kernel/lifecycle
.. _`SEV-SNP`: https://www.amd.com/en/developer/sev.html
.. _`Intel TDX`: https://www.intel.com/content/www/us/en/developer/tools/trust-domain-extensions/overview.html
.. _`GKE node images`: https://cloud.google.com/kubernetes-engine/docs/concepts/node-images
.. _`GKE Anthos on AWS`: https://cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/os-details
.. _`GKE Anthos on Azure`: https://cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/os-details
.. _`GKE Anthos on VMware`: https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/node-image
