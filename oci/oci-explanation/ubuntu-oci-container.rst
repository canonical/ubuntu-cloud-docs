.. _ubuntu-oci-container-images:

Ubuntu OCI container images
===========================

The `Open Container Initiative (OCI) <https://opencontainers.org/>`_ establishes standards for constructing container 
images that can be reliably installed across a variety of compliant host environments.

Ubuntu’s `LTS Docker Image Portfolio <https://ubuntu.com/security/docker-images>`_ 
provides OCI-compliant images that receive stable security updates and predictable 
software updates, ensuring consistency in both maintenance schedule and operational 
interfaces for the underlying software your software builds on.

Moreover, `Ubuntu-based containers <https://ubuntu.com/containers>`_ (like
chiselled container images) all leverage the Ubuntu container image as their
starting point, and thus also profit from its support and security commitments.

The Ubuntu container image is built from a minimal rootfs tarball. This tarball
contains the modifications needed to make the rootfs suitable for 
building OCI/Docker container images. The Ubuntu OCI rootfs tarballs are published
in `OCI partner images <https://partner-images.canonical.com/oci/>`_. 
