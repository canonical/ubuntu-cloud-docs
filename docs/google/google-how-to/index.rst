How-to guides
=============

These guides provide instructions for performing different operations related to our products on Google Cloud.

GCE - Launching and using Ubuntu instances
------------------------------------------

While using Ubuntu on GCP, you'll need to perform tasks such as finding the right image to use, launching different instance types, creating golden images and containers, using Ubuntu Pro and doing upgrades.

* :doc:`Find images <gce/find-ubuntu-images>`
* :doc:`Create instances <gce/create-different-instance-types>`
* :doc:`Launch a desktop <gce/launch-ubuntu-desktop>`
* :doc:`Build a Pro golden image <gce/build-ubuntu-pro-golden-image>`
* :doc:`Create customized docker containers <gce/create-customized-docker-container>`
* :doc:`Upgrade to Pro <gce/upgrade-in-place-from-lts-to-pro>`
* :doc:`Enable Pro features <gce/enable-pro-features>`
* :doc:`Upgrade from Focal to Jammy <gce/upgrade-from-focal-to-jammy>`
* :doc:`Set hostname <gce/set-hostname-using-cloudinit>`

GKE and Kubernetes
------------------

If you want to use Ubuntu Pro on your Kubernetes cluster, or install Charmed Kubeflow on GKE, you can use these instructions.

* :doc:`Deploy Ubuntu Pro based k8s on GCE <gke/deploy-kubernetes-with-ubuntu-pro>`
* `Install Charmed Kubeflow on GKE`_

   
.. toctree::
   :hidden:
   :maxdepth: 1
   
   gce/index    
   gke/index
 
  
.. _Install Charmed Kubeflow on GKE: https://documentation.ubuntu.com/charmed-kubeflow/how-to/install/install-gke/