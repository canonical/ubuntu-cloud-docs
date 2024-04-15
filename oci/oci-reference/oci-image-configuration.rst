Ubuntu OCI image configuration
******************************

The definition of the Ubuntu container image follows the `OCI image format
specification <https://github.com/opencontainers/image-spec/blob/main/spec.md>`_.

Thus, as with any other container image, the Ubuntu image contains enough metadata
such that one can inspect the image without actually running the container.

Layers
------

As explained in :ref:`ubuntu-oci-container-images`, the Ubuntu container
images are built from a minimal rootfs tarball that is tailored for container
environments. For each Ubuntu release, you'll find a corresponding `release
branch in Launchpad <https://code.launchpad.net/~cloud-images-release-managers/cloud-images/+oci/ubuntu-base/+git/ubuntu-base>`_
(e.g. ``noble-24.04``) with the build recipe and a reference to the respective
architecture-specific rootfs tarballs.

Image index
-----------

The Ubuntu container image is published with a multi-architecture image index,
meaning that there will be a container image digest that will internally
resolve to multiple architecture-specific digests.

In other words, when pulling any Ubuntu container image by its OCI tag
(e.g. ``ubuntu:24.04``), your container runtime should automatically find and
pull the right container image for your host's architecture.

If however, you'd like to pin a specific Ubuntu container architecture, you can
pull the Ubuntu container image by its architecture-specific digest
(e.g. ``ubuntu@sha256:<arch-specific-digest>``).

Image configuration
-------------------

The Ubuntu container images are built and published with the following
configurations:

- no default OCI entrypoint,
- ``bash`` is the default OCI command,
- OCI labels to identify the image name (i.e. ``ubuntu``) and its release.

