Ubuntu on OCI Registries
========================

The Open Container Initiative (OCI) establishes standards for constructing container 
images that can be reliably installed across a variety of compliant host environments.

Ubuntu’s `LTS Docker Image Portfolio <https://ubuntu.com/security/docker-images>`_ 
provides OCI-compliant images that receive stable security updates and predictable 
software updates, thus ensuring consistency in both maintenance schedule and operational 
interfaces for the underlying software your software builds on.

Ubuntu OCI tarball is a minimal rootfs tarball ready for use to build OCI/Docker 
container base images. It is similar to `Ubuntu Base <https://wiki.ubuntu.com/Base>`_ 
but already contains the modifications needed to make the rootfs suitable for 
building OCI/Docker container images. It is available for the amd64, armhf, arm64, 
powerpc and ppc64el architectures. The rootfs tarballs are published under 
`OCI partner images <https://partner-images.canonical.com/oci/>`_. 

Canonical publishes official Docker images to Docker Hub based on OCI images that are 
built from the Ubuntu OCI rootfs tarballs. Images are also published to AWS ECR 
(Elastic Container Registry) gallery (in `ubuntu <https://gallery.ecr.aws/ubuntu/ubuntu>`_
and `lts <https://gallery.ecr.aws/lts/ubuntu>`_ namespaces), ACR (Azure Container Registry),
OCIR (Oracle Container Infrastructure Registry), and there are plans to publish to more
registries in the future.


----------

.. _building_ubuntu_pro_oci_images:

Building Ubuntu Pro OCI images
------------------------------

Similar to the `Ubuntu Pro images in public clouds <https://canonical-ubuntu-pro-client.readthedocs-hosted.com/en/latest/explanations/what_are_ubuntu_pro_cloud_instances/>`_, one can build an Ubuntu Pro OCI image to leverage services like ESM (Extended Security Maintenance) and FIPS.

The easiest way to build an Ubuntu Pro container image is to make use of existing container management tools (like Docker) and enable the Pro services on top of an existing Ubuntu container image (e.g. `ubuntu:focal <https://hub.docker.com/layers/library/ubuntu/focal/images/sha256-b39db7fc56971aac21dee02187e898db759c4f26b9b27b1d80b6ad32ff330c76?context=explore>`_).

.. note::
   It is highly recommended that Ubuntu Pro container images should be built on hosts that are already covered by an Ubuntu Pro subscription.

This process is described in detail in the `pro client documentation <https://canonical-ubuntu-pro-client.readthedocs-hosted.com/en/latest/howtoguides/enable_in_dockerfile/>`_. The resulting Ubuntu Pro container image can then be loaded into your local Docker daemon (by using ``--load`` when running ``docker build``) and can be deployed/published normally as any other container image.


----------

How-to guides
-------------

Instructions for deploying Ubuntu Pro containers on Kubernetes and for creating a 'chiselled' Ubuntu base image are linked below:

* :doc:`./oci-how-to/deploy-pro-container-on-pro-kubernetes-cluster`
* :doc:`./oci-how-to/create-chiselled-ubuntu-image`


---------

Project and community
---------------------

Ubuntu on OCI registries is a member of the Ubuntu family and the project warmly welcomes 
community projects, contributions, suggestions, fixes and constructive feedback.

* `Code of conduct`_
* `Get support`_
* `Join our online chat`_
* :doc:`oci-how-to/contribute-to-these-docs`

.. toctree::
   :hidden:
   :maxdepth: 2

   oci-how-to/deploy-pro-container-on-pro-kubernetes-cluster
   oci-how-to/create-chiselled-ubuntu-image
   oci-how-to/contribute-to-these-docs

  
.. _Code of conduct: https://ubuntu.com/community/ethos/code-of-conduct
.. _Get support: https://ubuntu.com/cloud/public-cloud
.. _Join our online chat: https://discourse.ubuntu.com
