Canonical's offerings on GCP
============================

With an optimised Ubuntu GCP kernel built in collaboration between Google and Canonical to deliver the very
best performance on the Google Cloud hypervisor, Ubuntu is a popular Linux OS on GCP for both virtual machines 
and container workloads - i.e. for both Google Cloud Engine (GCE) and Google Kubernetes Engine (GKE).

The ``linux-gcp`` kernel enables accelerated networking with the Compute Engine Virtual Ethernet device and supports the Google latest Tau VM, enabling scale-out optimised workloads. These advantages contribute to Ubuntu being the default host images for Anthos Multi-cloud.

Another useful feature is the native integration of Ubuntu images with the Administrator console. This enables things like patch management and in-place upgrade of Ubuntu LTS images to Ubuntu Pro without the need for workload redeployment.

GCE Images
~~~~~~~~~~

For each active Ubuntu release, at least two image variants are created for GCE: 

* **Base** images that contain a full Ubuntu development environment
* **Minimal** images that have a smaller footprint than base images, and are designed for production instances that will never be accessed by a human

Apart from these, 

* **Ubuntu Pro** images are created for 16.04, 18.04, 20.04, 22.04 and 
* **Ubuntu Pro FIPS** images are created for 18.04 and 20.04


GKE images
~~~~~~~~~~

GKE is Google Cloud's Kubernetes offering. Canonical produces host images for GKE that act as a base for running end user containers. These images include GKE's own custom cloud ``gke`` kernel and custom NVIDIA drivers for use with the custom kernel.



Anthos - Google's multi-cloud GKE strategy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For the various Anthos versions available for different clouds, Canonical provides the following:

* **Anthos on AWS** - Consultation support
* **Anthos on Azure** - Consultation support
* **Anthos on VMware** - A series of CIS hardened and unhardened Ubuntu images in the form of OVAs to be used with VMware

