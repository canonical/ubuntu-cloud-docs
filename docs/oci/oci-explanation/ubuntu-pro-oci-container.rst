.. _ubuntu-pro-oci-container-images:

Ubuntu Pro OCI container images
===============================


As with the `Ubuntu Pro images in public clouds
<https://documentation.ubuntu.com/pro-client/en/latest/explanations/what_are_ubuntu_pro_cloud_instances/>`_, one can build an Ubuntu Pro container image to leverage services like
`Expanded Security Maintenance (ESM) <https://ubuntu.com/security/esm>`_ and `FIPS <https://ubuntu.com/security/fips>`_.

The easiest way to build an Ubuntu Pro container image is to make use of existing container management tools (like Docker) and enable the Pro services on top of an existing Ubuntu container image (e.g. `ubuntu:focal <https://hub.docker.com/_/ubuntu/tags?page=&page_size=&ordering=&name=focal>`_).

.. note::
   Ubuntu Pro container images should be run on hosts that are already covered by an Ubuntu Pro subscription.
   Please consult the `Ubuntu Pro service description <https://ubuntu.com/legal/ubuntu-pro>`_ for more details.

Find out how to enable `Ubuntu Pro services in a Dockerfile <https://documentation.ubuntu.com/pro-client/en/latest/howtoguides/enable_in_dockerfile/>`_. The resulting Ubuntu Pro container image can then be loaded into your local Docker daemon and/or can be deployed normally as any other container image.


