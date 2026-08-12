.. meta::
   :description: Discover Ubuntu on Google Cloud Platform (GCP), including optimized images, deployment guides, and best practices for cloud workloads.

.. _index:

Ubuntu on GCP
=============

**Ubuntu on Google Cloud Platform (GCP) is a set of customized Ubuntu images** that allow easy access 
to a wide range of products and services - offered by both Google Cloud and Canonical. These images 
have an optimized kernel that boots faster, has a smaller footprint and includes GCP-specific drivers.

**These images provide a foundation for deploying cloud-based software solutions,** specifically
for software built on Ubuntu and running on Google cloud. They focus on providing the optimal tools 
and features needed to run specific workloads.

.. include:: ../reuse/common-intro.txt
   :start-after: Start: Product need and user
   :end-before: End: Product need and user

---------

In this documentation
---------------------

.. list-table::
    :widths: 35 65
    :header-rows: 0

    * - **Canonical's offerings**
      - :ref:`GCP optimizations <canonical-offerings>` • :ref:`Packaged Google agents <guest-agents>` 
      
    * - **Finding and launching images**
      - :ref:`Find images <find-ubuntu-images>` • :ref:`Create instances <create-different-instance-types>` • :ref:`Launch a desktop <launch-ubuntu-desktop>` • :ref:`Use 64K page kernel on ARM64 instances <arm64-on-google-cloud>`
      
    * - **Upgrades and maintenance**
      - :ref:`Switch between LTS and Pro <upgrade-in-place-from-lts-to-pro>` • :ref:`Enable Ubuntu Pro features <enable-pro-features>` • :ref:`Upgrade from Focal to Jammy <upgrade-from-focal-to-jammy>` 

    * - **Creating golden images**
      - :ref:`Build a Pro golden image <build-ubuntu-pro-golden-image>`
            
    * - **Custom deployments**
      - :ref:`Create a GKE cluster with Ubuntu nodes <create-gke-cluster-with-ubuntu-nodes>` • :ref:`Deploy Kubernetes with Ubuntu Pro on GCE <deploy-kubernetes-with-ubuntu-pro>` • :ref:`Create customized docker containers <create-customized-docker-container>` • :ref:`Set hostname <set-hostname-using-cloudinit>` 
      
    * - **Quality and policies**
      - :ref:`Security aspects <security-overview>` • :ref:`Image testing <gce-image-testing>` • :ref:`Image retention policy <gce-image-retention-policy>`



How this documentation is organized
------------------------------------


This documentation uses the `Diátaxis documentation structure <https://diataxis.fr/>`__.

* :ref:`How-to guides <google-how-to-index>` assume you have basic familiarity with Ubuntu images on GCP and want to achieve specific goals. They are instructions covering key operations and common tasks involving the use of Ubuntu on GCP.

* :ref:`Explanation <google-explanation-index>` includes topic overviews, background and context and detailed discussion. These include key topics, such as our offerings, security features, Google's 'guest agents' on Ubuntu and our image retention policy.

---------

Project and community
---------------------

Ubuntu on GCP is a member of the Ubuntu family and the project warmly welcomes community projects, contributions, suggestions, fixes and constructive feedback.

Get involved
~~~~~~~~~~~~
	
* `Get support`_
* `Join our online chat`_
* `Discuss on Matrix`_
* `Talk to us about Ubuntu on Google cloud`_
* :ref:`contribute-to-these-docs`

Governance and policies
~~~~~~~~~~~~~~~~~~~~~~~

* `Code of conduct`_

.. toctree::
   :hidden:
   :maxdepth: 2

   google-how-to/index
   google-explanation/index
   google-how-to/contribute-to-these-docs

   
.. _Get support: https://ubuntu.com/cloud/public-cloud
.. _Join our online chat: https://discourse.ubuntu.com/c/project/gcp/179
.. _`Discuss on Matrix`: https://matrix.to/#/#ubuntu-cloud:ubuntu.com
.. _Talk to us about Ubuntu on Google cloud: https://ubuntu.com/gcp#get-in-touch
.. _Code of conduct: https://ubuntu.com/community/docs/ethos/code-of-conduct

