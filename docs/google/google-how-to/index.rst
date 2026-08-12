.. meta::
   :description: List of how-to guides for launching, managing, and upgrading Ubuntu on Google Cloud, including image selection and solution deployment.
   
.. _google-how-to-index:

How-to guides
=============

These guides provide instructions for performing different operations related to our products on Google Cloud.

GCE - Launching and using Ubuntu instances
------------------------------------------

While using Ubuntu on GCP, you'll need to perform tasks such as finding the right image to use, launching different instance types, creating golden images and containers, using Ubuntu Pro and doing upgrades.

* :ref:`Find images <find-ubuntu-images>`
* :ref:`Create instances <create-different-instance-types>`
* :ref:`Launch a desktop <launch-ubuntu-desktop>`
* :ref:`Build a Pro golden image <build-ubuntu-pro-golden-image>`
* :ref:`Create customized docker containers <create-customized-docker-container>`
* :ref:`Change license between LTS and Pro <upgrade-in-place-from-lts-to-pro>`
* :ref:`Enable Pro features <enable-pro-features>`
* :ref:`Upgrade from Focal to Jammy <upgrade-from-focal-to-jammy>`
* :ref:`Set hostname <set-hostname-using-cloudinit>`
* :ref:`Use 64K page kernel on ARM64 instances <arm64-on-google-cloud>`

GKE and Kubernetes
------------------

If you want to create a GKE cluster with Ubuntu nodes, use Ubuntu Pro on your Kubernetes cluster, or install Charmed Kubeflow on GKE, you can use these instructions.

* :ref:`Create a GKE cluster with Ubuntu nodes <create-gke-cluster-with-ubuntu-nodes>`
* :ref:`Deploy Ubuntu Pro based k8s on GCE <deploy-kubernetes-with-ubuntu-pro>`
* `Install Charmed Kubeflow on GKE`_

   
.. toctree::
   :hidden:
   :maxdepth: 1
   
   gce/index    
   gke/index
 
  
.. _Install Charmed Kubeflow on GKE: https://documentation.ubuntu.com/charmed-kubeflow/latest/how-to/install/install-gke/