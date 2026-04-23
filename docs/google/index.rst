.. meta::
   :description: Discover Ubuntu on Google Cloud Platform (GCP), including optimized images, deployment guides, and best practices for cloud workloads.

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
      - :doc:`GCP optimizations <google-explanation/canonical-offerings>` • :doc:`Packaged Google agents <google-explanation/guest-agents>` •  
      
    * - **Finding and launching images**
      - :doc:`Find images <google-how-to/gce/find-ubuntu-images>` • :doc:`Create instances <google-how-to/gce/create-different-instance-types>` • :doc:`Launch a desktop <google-how-to/gce/launch-ubuntu-desktop>` • :doc:`ARM64 on Google Cloud <google-how-to/gce/arm64-on-google-cloud>`
      
    * - **Upgrades and maintenance**
      - :doc:`Switch between LTS and Pro <google-how-to/gce/upgrade-in-place-from-lts-to-pro>` • :doc:`Enable Ubuntu Pro features <google-how-to/gce/enable-pro-features>` • :doc:`Upgrade from Focal to Jammy <google-how-to/gce/upgrade-from-focal-to-jammy>` 

    * - **Creating golden images**
      - :doc:`Build a Pro golden image <google-how-to/gce/build-ubuntu-pro-golden-image>` •
            
    * - **Custom deployments**
      - :doc:`Deploy Kubernetes with Ubuntu Pro on GCE <google-how-to/gke/deploy-kubernetes-with-ubuntu-pro>` • :doc:`Create customized docker containers <google-how-to/gce/create-customized-docker-container>` • :doc:`Set hostname <google-how-to/gce/set-hostname-using-cloudinit>` 
      
    * - **Policies**
      - :doc:`Security aspects <google-explanation/security-overview>` • :doc:`Image retention policy <google-explanation/gce-image-retention-policy>` 



How this documentation is organized
------------------------------------


This documentation uses the `Diátaxis documentation structure <https://diataxis.fr/>`__.

* :doc:`How-to guides  <google-how-to/index>` assume you have basic familiarity with Ubuntu images on GCP and want to achieve specific goals. They are instructions covering key operations and common tasks involving the use of Ubuntu on GCP.

* :doc:`Explanation <google-explanation/index>` includes topic overviews, background and context and detailed discussion. These include key topics, such as our offerings, security features, Google's 'guest agents' on Ubuntu and our image retention policy.

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
* :doc:`google-how-to/contribute-to-these-docs`

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

