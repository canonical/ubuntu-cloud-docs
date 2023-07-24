Ubuntu on GCP
=============

**Ubuntu on Google Cloud Platform (GCP) is a set of customised Ubuntu images** that allow easy access 
to a wide range of products and services - offered by both Google Cloud and Canonical.

**These images provide a foundation for deploying cloud-based software solutions,** specifically
for softwares built on Ubuntu and running on Google cloud. They focus on providing the optimal tools 
and features needed to run specific workloads.

**The images create a stable and secure cloud platform** that is ideal for scaling development work
done on Ubuntu-based systems. Since Ubuntu is one of the most favoured operating systems amongst
developers, using an Ubuntu-based image for the corresponding cloud deployment becomes the simplest
option.

**Everyone from individual developers to large enterprises use these images** for developing and deploying
their softwares. For highly regulated industries from the government, medical and finance sectors, 
various security-certified images are also available.



---------

Canonical's Offerings on Google Cloud
-------------------------------------

With an optimised Ubuntu GCP kernel built in collaboration between Google and Canonical to deliver the very
best performance on the Google Cloud hypervisor, Ubuntu is a popular Linux OS on GCP for both virtual machines 
and container workloads - i.e. for both Google Cloud Engine (GCE) and Google Kubernetes Engine (GKE).


GCE Images
~~~~~~~~~~

For each active Ubuntu release, at least two image variants are created for GCE: 

* **Base** images that contain a full Ubuntu development environment
* **Minimal** images that have a smaller footprint than base images, and are designed for production instances that will never be accessed by a human

Apart from these, 

* **Ubuntu Pro** images are created for 16.04, 18.04, 20.04, 22.04 and 
* **Ubuntu Pro FIPS** images are created for 18.04 and 20.04

Finally, there's a special sub-family of Google images:

* **Guest** images that are built with the Google guest agent and
* **Kernel** images that are built with the Google kernel

These are used by Google to do automated testing of new kernels and/or guests.


GKE images
~~~~~~~~~~

GKE is Google Cloud's Kubernetes offering. Canonical produces host images for GKE that act as a base for running end user containers. These images include GKE's own custom cloud ``gke`` kernel and custom NVIDIA drivers for use with the custom kernel.



Anthos - Google's multi-cloud GKE strategy
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

For the various Anthos versions available for different clouds, Canonical provides the following:

* **Anthos on AWS** - Consultation support
* **Anthos on Azure** - Consultation support
* **Anthos on bare metal** - Ubuntu images based on a DISA STIG hardened 20.04 FIPS compliant version.
* **Anthos on VMware** - A series of CIS hardened and unhardened Ubuntu images in the form of OVAs to be used with VMware


----------

How-to guides
-------------

Linked below are step-by-step guides for some key operations: deploying Kubernetes with Ubuntu Pro on GCE and upgrading from Ubuntu 20.04 to 22.04.

* :doc:`./google-how-to/deploy-kubernetes-with-ubuntu-pro`
* :doc:`./google-how-to/upgrade-from-focal-to-jammy`

---------

Project and community
---------------------

Ubuntu on GCP is a member of the Ubuntu family and the project warmly welcomes community projects, contributions, 
suggestions, fixes and constructive feedback.

	
* `Code of conduct`_
* `Get support`_
* `Join our online chat`_
* `Talk to us about Ubuntu on Google cloud`_

.. toctree::
   :hidden:
   :maxdepth: 2

   google-how-to/deploy-kubernetes-with-ubuntu-pro
   google-how-to/upgrade-from-focal-to-jammy
   
.. _Code of conduct: https://ubuntu.com/community/governance/code-of-conduct
.. _Get support: https://ubuntu.com/cloud/public-cloud
.. _Join our online chat: https://discourse.ubuntu.com
.. _Talk to us about Ubuntu on Google cloud: https://ubuntu.com/gcp#get-in-touch
