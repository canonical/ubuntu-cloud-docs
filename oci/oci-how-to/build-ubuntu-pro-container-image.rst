Build an Ubuntu Pro container image
============================
Similarly to the `Ubuntu Pro images in Public Clouds <https://canonical-ubuntu-pro-client.readthedocs-hosted.com/en/latest/explanations/what_are_ubuntu_pro_cloud_instances.html>`_, one can also build an Ubuntu Pro container image to leverage from familiar Ubuntu Pro services like ESM (Extended Security Maintenance) and FIPS.

.. note::
   It is highly recommended to build Ubuntu Pro container images on hosts which are already covered by an Ubuntu Pro
   subscription.

The easiest way to build an Ubuntu Pro container image is to make use of existing container management tools (like Docker) and enable the Pro services on top of an existing Ubuntu container image (like `ubuntu:focal <https://hub.docker.com/layers/library/ubuntu/focal/images/sha256-b39db7fc56971aac21dee02187e898db759c4f26b9b27b1d80b6ad32ff330c76?context=explore>`_).

This process is described in detail in `here <https://canonical-ubuntu-pro-client.readthedocs-hosted.com/en/latest/howtoguides/enable_in_dockerfile.html>`_. The resulting Ubuntu Pro container image can then be loaded into the local Docker daemon (by using ``--load`` when running the ``docker build``) and deployed/published normally as any other container image.