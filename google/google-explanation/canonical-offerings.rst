Canonical's offerings on GCP
============================

Canonical works closely with Google to ensure Ubuntu images support the latest GCP features. An optimized Ubuntu GCP kernel, built in collaboration with Google, delivers the very
best performance for scale-out, optimized workloads on the Google Cloud hypervisor. This makes Ubuntu a popular choice for both virtual machines 
and container workloads.

The optimized ``linux-gcp`` kernel enables accelerated networking with the Compute Engine Virtual Ethernet device and support for the latest Google ARM Tau VM. These advantages contribute to Ubuntu being the default host images for Anthos Multi-cloud.

The Ubuntu images support secure boot, with signed NVIDIA drivers available for workloads requiring access to vGPU compute acceleration. For instances that require confidential compute, Ubuntu images have been SEV-capable since 18.04 with `SEV-SNP`_ and `Intel TDX`_ support currently in private preview.

Ubuntu images are updated regularly with fixes that address the latest CVEs to ensure applications remain free from vulnerabilities.

Another useful feature is the native integration of Ubuntu images with the Administrator console, enabling patch management and :doc:`in-place upgrade of Ubuntu LTS images to Ubuntu Pro <../google-how-to/gce/upgrade-in-place-from-lts-to-pro>` without the need for workload redeployment.



GCE Images
~~~~~~~~~~

For each active Ubuntu release, at least two image variants are created for GCE: 

* **Base** images that contain a full Ubuntu development environment
* **Minimal** images that have a smaller footprint than base images, and are designed for production instances that will never be accessed by a human

In addition, the following images are also available: 

* **Ubuntu Pro** images are created for 16.04, 18.04, 20.04, 22.04 and 
* **Ubuntu Pro FIPS** images are created for 18.04 and 20.04


GKE images
~~~~~~~~~~

GKE is Google Cloud's Kubernetes offering. Canonical produces node images for GKE that act as a base for running end user pods. These node images include a kernel that is optimized for use in the GKE environment ``linux-gke``, as well as custom NVIDIA drivers for workloads that wish to leverage GPU acceleration. Further details of the node images available for GKE can be found in Google's documentation about `GKE node images`_.



Anthos - Google's multi-cloud GKE strategy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Google provides a multi-cloud GKE strategy through a variety of Anthos product offerings, with an Ubuntu foundation providing the cross-platform support:

* `GKE Anthos on AWS`_ 
* `GKE Anthos on Azure`_ 
* `GKE Anthos on VMware`_ 

.. _`SEV-SNP`: https://www.amd.com/en/developer/sev.html
.. _`Intel TDX`: https://www.intel.com/content/www/us/en/developer/tools/trust-domain-extensions/overview.html
.. _`GKE node images`: https://cloud.google.com/kubernetes-engine/docs/concepts/node-images
.. _`GKE Anthos on AWS`: https://cloud.google.com/kubernetes-engine/multi-cloud/docs/aws/reference/os-details
.. _`GKE Anthos on Azure`: https://cloud.google.com/kubernetes-engine/multi-cloud/docs/azure/reference/os-details
.. _`GKE Anthos on VMware`: https://cloud.google.com/kubernetes-engine/distributed-cloud/vmware/docs/concepts/node-image
