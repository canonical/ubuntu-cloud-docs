.. meta::
   :description: Learn about Ubuntu cloud image architecture variants, starting with amd64v3 in Ubuntu 26.04, including supported variants, compatibility, and future plans.

Architecture Variants Support in Ubuntu Cloud Images
====================================================

Starting with 26.04 (Resolute Raccoon), Ubuntu cloud images will be built and published to support architecture variants.
This means that for a given base architecture (e.g. amd64), there may be multiple architecture variants (e.g. amd64v3)
built, published, and supported officially by Canonical.

Read on for more information about what architecture variants are, which ones are supported, and how they are supported
for various cloud platforms.

Supported Variants
------------------

The first architecture variant supported is amd64v3, which represents the latest x86_64 ABI and instruction set
extensions. This variant will be supported for Ubuntu 26.04 Resolute Raccoon and future releases. There are no plans to
build existing supported releases (e.g. 24.04 LTS Noble Numbat) for architecture variants.

See individual cloud docs pages for detailed information on how any given variant is delivered and supported. For
example, amd64v3 Ubuntu Download images (those found at https://cloud-images.ubuntu.com) will be made available
alongside legacy amd64
images, but for official Ubuntu images available to launch within public cloud platforms, only v3-enabled images will be
available (again, for 26.04 Resolute Raccoon and forward). These amd64v3-enabled images will be published and supported
under the "amd64" architecture name. Legacy amd64 images for public cloud platforms will not be published or supported
for 26.04 and forward.

Future Variants
---------------

New architecture variants are likely to be supported by Ubuntu cloud images in the future. However, no additional
variant support beyond amd64v3 is planned for the 26.04 release.

Canonical's release, publication, and support strategies for other/future variants are likely to be more nuanced, so
documentation for specific clouds and variants should be consulted whenever possible over general assumptions.

Compatibility
-------------

Generally, older architecture variants can run on new variant hardware, as the newer variants represent a superset of
older ABIs and new instructions; for example, legacy amd64 images can run on amd64v3 hardware, which comprises almost
all modern x86_64 hardware. However, the inverse is not true -- newer architecture variants cannot run without error on
older hardware. This is at least the case for amd64 and amd64v3, and is likely to be the case for future variants as
well.
