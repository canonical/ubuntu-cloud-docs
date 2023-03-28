=====================
Ubuntu on Azure - FAQ
=====================

Is Ubuntu available on Azure?
=============================

Yes, all the supported versions of Ubuntu are available for free on Azure. Here is how you can find them: :doc:`../azure-how-to/find-ubuntu-images`.

Why are there multiple offers from Canonical on Azure?
=============================================================

For technical reasons related to the publication process, Canonical publishes the different versions of Ubuntu under dedicated offers. This is to ensure that the publication of a given version of Ubuntu cannot block or impact the publication of another version.

How often are Ubuntu images refreshed?
======================================

Canonical publishes a new version of an image every time the kernel for this image is updated. On an average, this happens once every three weeks. Important security or bug fixes might also trigger an image refresh. Keep in mind that running VMs are not affected by these changes. Make sure to keep your VM up to date using ``apt`` and to reboot your VM regularly to update the running kernel.

When using the CLI or any automated process, make sure to use the keyword `latest` in place of the image version. Thus, you will always be launching the latest image available for the given offer/SKU.

Why are there so many publishers of Ubuntu on Azure?
====================================================

Ubuntu is a distribution of free software. Anyone is free to re-publish the OS. You are free to build your own software on top of Ubuntu and to sell it as a paid product. This is what makes Ubuntu so great. However, be very careful when downloading or using Ubuntu from an untrusted source. At best you will pay for the same product you could get for free from Canonical. At worst, those offers could contain spyware or other malware programs that could put you and your business at risk.

**Always use Canonical's offers for running Ubuntu** except if you trust the other publisher.

Is Ubuntu on Azure different from Ubuntu on other clouds?
=========================================================

Yes, Ubuntu on Azure is customised to make it better for Azure. This customisation includes:
 * A custom kernel ``linux-azure`` developed by Canonical for the Azure public cloud
 * Extra configuration files that allow packages to work better with the platform
 * A few extra pre-installed packages that ensure built-in support for all features of Azure
