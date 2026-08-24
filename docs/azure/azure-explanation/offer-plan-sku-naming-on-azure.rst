.. meta::
   :description: Explanations of how and why Canonical names its offers, plans, and SKUs on the Azure Marketplace.

.. _offer-plan-sku-naming-on-azure:

Offer, plan, and SKU naming on Azure
====================================

On Azure, each Canonical image is assigned a unique `Uniform Resource Name (URN)`_.
URNs are how Azure determines exactly what image to launch when using the Azure CLI. For example:

``Publisher:Offer:SKU:Version`` or ``Canonical:ubuntu-26_04-lts:server:latest``

To find Canonical's official Ubuntu images on Azure and the available URNs, refer to :ref:`find-ubuntu-images`. Alternatively, to learn how to launch an image with a URN, refer to :ref:`launch-ubuntu-images`. 

.. note:: ``Canonical`` is the only ``Publisher`` name that Canonical uses to distribute Ubuntu images on Azure.

Ubuntu offers on Azure
++++++++++++++++++++++

There are generally two types of offers that Canonical supports on the Azure Marketplace: unified offers and single-plan offers.

Unified offers
--------------

With Ubuntu 22.04 LTS, Canonical began deploying a unified offer structure such that all available Ubuntu images for a given release can be found under the same offer. Under this paradigm, the offer name is more generic to the release, but contains multiple plans. For example, `Ubuntu 26.04 LTS`_ contains all available 26.04 LTS image types.

Single-plan offers
------------------

Previously, Canonical created one plan per offer as seen with `Ubuntu Pro Server 20.04 LTS`_ and `Ubuntu Pro Minimal 20.04 LTS`_.

Canonical's public offers prefixed with ``0001-com-ubuntu`` all fall under this legacy format that maps one offer to a single product.

SKU naming conventions
++++++++++++++++++++++

An offer is composed of one or more underlying plans. Each plan represents a specific :ref:`product <canonical-offerings>`, but that plan may have a subset of SKUs to differentiate architecture and Hyper-V generation.

Canonical generally produces three SKUs per plan:

- AMD64 architecture with Hyper-V Generation 2
- AMD64 architecture with Hyper-V Generation 1
- ARM64 architecture with Hyper-V Generation 2

The default SKU under a plan **uses the plan name** and it describes the product type (e.g. ``pro-server``, ``server``, ``pro-20_04-lts``).

Upon Microsoft's introduction of `Hyper-V Generation 2`_, Canonical retroactively added ``-gen2`` suffixed SKUs to each plan in order to support the new functionality.

All unified offers default to Hyper-V Generation 2. There are ``-gen1`` SKUs in these offers to support backwards-compatibility.

Images are also available with the ARM64 architecture. Those images strictly utilize Hyper-V Generation 2 and contain a ``-arm64`` suffix.

.. list-table:: SKU Meaning by Offer Type
   :widths: 25 37 38
   :header-rows: 1

   * - SKU Name
     - Single-plan Offer
     - Unified Offer
   * - ``<plan>``
     - AMD64 (Gen1)
     - AMD64 (Gen2)
   * - ``<plan>-gen1``
     - 
     - AMD64 (Gen1)
   * - ``<plan>-gen2``
     - AMD64 (Gen2)
     - 
   * - ``<plan>-arm64``
     - ARM64 (Gen2)
     - ARM64 (Gen2)


.. _`Hyper-V Generation 2`: https://learn.microsoft.com/en-us/azure/virtual-machines/generation-2
.. _`Uniform Resource Name (URN)`: https://learn.microsoft.com/en-us/azure/virtual-machines/linux/cli-ps-findimage#terminology
.. _`Ubuntu Pro Server 20.04 LTS`: https://marketplace.microsoft.com/en-us/product/canonical.0001-com-ubuntu-pro-focal?tab=PlansAndPrice
.. _`Ubuntu Pro Minimal 20.04 LTS`: https://marketplace.microsoft.com/en-us/product/canonical.0001-com-ubuntu-pro-minimal-focal?tab=PlansAndPrice
.. _`Ubuntu 26.04 LTS`: https://marketplace.microsoft.com/en-us/product/canonical.ubuntu-26_04-lts?tab=PlansAndPrice
