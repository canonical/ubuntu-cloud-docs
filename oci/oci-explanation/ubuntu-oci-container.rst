.. _ubuntu-oci-container-images:

Ubuntu OCI container images
===========================

The `Open Container Initiative (OCI) <https://opencontainers.org/>`_ establishes standards for constructing container 
images that can be reliably installed across a variety of compliant host environments.

Ubuntu’s `LTS Docker Image Portfolio <https://ubuntu.com/security/docker-images>`_ 
provides OCI-compliant images that receive stable security updates and predictable 
software updates, ensuring consistency in both maintenance schedule and operational 
interfaces for the underlying foundation your software builds on.

Moreover, all `Ubuntu-based containers <https://ubuntu.com/containers>`_ (like
`chiseled container images <https://documentation.ubuntu.com/rockcraft/en/latest/explanation/chisel/>`_)


leverage the Ubuntu container image as their
starting point, and so also benefit from its
`support and security commitments <https://ubuntu.com/security/docker-images>`_.

The Ubuntu container image is built from a minimal rootfs tarball. This tarball
already contains the modifications needed to make the rootfs suitable for 
building OCI/Docker container images. The Ubuntu OCI rootfs tarballs are published
in `OCI partner images <https://partner-images.canonical.com/oci/>`_. 
