.. meta::
   :description: Learn about Ubuntu container images on OCI registries, including security, multi-arch support, and trusted application base images.

Ubuntu on OCI container registries
==================================

**Ubuntu is one of the world's most popular container images,** a minimalistic Ubuntu image that offers the same security, versatility, and update cadence as other Ubuntu offerings. It is a developer favorite in container registries such as Docker Hub, with up to 30,000 pulls per week.

**Available in all major OCI container registries,** such as Microsoft's ACR, Amazon's ECR, and of course, Docker Hub, as an official image from a verified publisher - Canonical. 

**A base container for trusted application images.** Container image provenance is a key aspect of any supply chain. The Ubuntu container image offers the ideal starting point for your application images, both in utility and trustworthiness.

**Compatible with multiple platforms and available in different flavors.** The Ubuntu container image is published as a multi-arch Open Container Initiative (OCI) image, available for ``AMD64``, ``ARM``, ``ARM64``, ``ppc64le`` and ``s390x``. Ubuntu Pro is also available for containers, which means hardened and security-enhanced versions of the public Ubuntu container image are also available.



In this documentation
---------------------

.. list-table::
    :widths: 35 65
    :header-rows: 0

    * - **Canonical's offerings**
      - :doc:`Ubuntu OCI container images <oci-explanation/ubuntu-oci-container>` • :doc:`Ubuntu Pro OCI container images <oci-explanation/ubuntu-pro-oci-container>` • :doc:`OCI image configuration <oci-reference/oci-image-configuration>` 

    * - **Working with Ubuntu OCI containers**
      - :doc:`Find the Ubuntu container images <oci-how-to/getting-started>` • :doc:`Create an Ubuntu FIPS Docker image <oci-tutorials/fips-ubuntu-container>` • :doc:`Deploy Ubuntu Pro containers on Kubernetes <oci-how-to/deploy-pro-container-on-pro-kubernetes-cluster>`
      

How this documentation is organized
------------------------------------


This documentation uses the `Diátaxis documentation structure <https://diataxis.fr/>`__.

* The :doc:`Tutorial <oci-tutorials/fips-ubuntu-container>` takes you step-by-step through the basics of creating an Ubuntu FIPS Docker image.

* :doc:`How-to guides  <oci-how-to/index>` assume you have basic familiarity with Ubuntu images on OCI container registries and want to achieve specific goals. They are instructions for finding Ubuntu container images and deploying Ubuntu Pro containers on Kubernetes clusters.

* :doc:`Reference <oci-reference/index>` includes an in-depth description of the Ubuntu image's OCI configuration.

* :doc:`Explanation <oci-explanation/index>` includes definitions of the Ubuntu and Ubuntu Pro container images.

---------

Project and community
---------------------

This project is a member of the Ubuntu family and it warmly welcomes community
projects, contributions, suggestions, fixes, and constructive feedback.

Get involved
~~~~~~~~~~~~
	
* `Get support <https://ubuntu.com/cloud/public-cloud>`_
* `Join our online chat <https://discourse.ubuntu.com/c/project/public-cloud/176>`_
* `Discuss on Matrix <https://matrix.to/#/#ubuntu-cloud:ubuntu.com>`_

Resources
~~~~~~~~~

* `Ubuntu Docker Images on Launchpad <https://launchpad.net/ubuntu-docker-images>`_

Governance and policies
~~~~~~~~~~~~~~~~~~~~~~~

* `Ubuntu Code of Conduct <https://ubuntu.com/community/docs/ethos/code-of-conduct>`_
* `Canonical contributor license agreement
  <https://ubuntu.com/legal/contributors>`_


.. toctree::
   :maxdepth: 1
   :hidden:

   oci-tutorials/index
   oci-how-to/index
   oci-reference/index
   oci-explanation/index

