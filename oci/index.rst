Ubuntu on OCI Registries
======================================================

Ubuntu OCI tarballs are minimal rootfs ready for use to build OCI/Docker container base images.
It is similar to `Ubuntu Base <https://wiki.ubuntu.com/Base>`_ but contains already 
the modifications to make the rootfs suitable for building OCI/Docker container images.
It is available for the amd64, armhf, arm64, powerpc and ppc64el architectures. The 
rootfs tarballs are published under `<https://partner-images.canonical.com/oci/>`_. 

Canonical publishes official Docker images to Docker Hub based on OCI images that are 
built from the Ubuntu OCI rootfs tarballs. Images are also published to AWS ECR 
(Elastic Container Registry) gallery (in `ubuntu <https://gallery.ecr.aws/ubuntu/ubuntu>`_
and `lts <https://gallery.ecr.aws/lts/ubuntu>`_ namespace), ACR (Azure Container Registry),
OCIR (Oracle Container Infrastructure Registry), and there are plans to publish to more
registries in the future.

---------

In this documentation
---------------------

..  grid:: 1 1 2 2

   ..  grid-item:: :doc:`Tutorial <oci-tutorial/index>`

       **Start here**: a hands-on introduction to Ubuntu OCI images

   ..  grid-item:: :doc:`How-to guides <oci-how-to/index>`

      **Step-by-step guides** covering key operations and common tasks

.. grid:: 1 1 2 2
   :reverse:

   .. grid-item:: :doc:`Reference <oci-reference/index>`

      **Technical information** - services, features, pricing

   .. grid-item:: :doc:`Explanation <oci-explanation/index>`

      **Discussion and clarification** of key topics

---------

Project and community
---------------------

Ubuntu public cloud is open source project that warmly welcomes community projects, contributions, suggestions, fixes and constructive feedback.

* `Code of conduct <https://ubuntu.com/community/governance/code-of-conduct>`_
* `Get support <https://ubuntu.com/cloud/public-cloud>`_
* `Join our online chat <https://discourse.ubuntu.com/>`_	


.. toctree::
   :hidden:
   :maxdepth: 2

   oci-tutorial/index
   oci-how-to/index
   oci-reference/index
   oci-explanation/index

