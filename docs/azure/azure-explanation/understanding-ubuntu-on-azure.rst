Understanding Ubuntu on Azure
=============================
-----------------------------
Is Ubuntu available on Azure?
-----------------------------

Yes, all the supported versions of Ubuntu are available for free on Azure. See: :doc:`../azure-how-to/instances/find-ubuntu-images`.

------------------------------------------------------
Why are there multiple offers from Canonical on Azure?
------------------------------------------------------

For technical reasons related to the publication process, Canonical publishes different versions of Ubuntu under dedicated offers. This is to ensure that the publication of a given version of Ubuntu cannot block or impact the publication of another version.

--------------------------------------
How often are Ubuntu images refreshed?
--------------------------------------

Canonical publishes a new version of an image every time the kernel for this image is updated. On an average, this happens once every three weeks. Important security or bug fixes might also trigger an image refresh. However, running virtual machines (VMs) are not affected by these changes. Use ``apt`` to keep your VM up to date and reboot your VM regularly to update the running kernel. If you are using Ubuntu Pro, Canonical's livepatch service will automatically apply kernel updates without the immediate need for a reboot, thereby allowing you to stick to your own restart schedule.

When using the CLI or any automated process, use the keyword `latest` in place of the image version. This ensures that you will always launch the latest image available for the given offer/SKU.

--------------------------------
How often are images deprecated?
--------------------------------

Microsoft Azure Partner Center has a hard limit of 100 images. To comply with this policy, Canonical has the following deprecation policy

* No more than 90 active images will be kept for a publication
* When the limit of 90 images is reached, Canonical will deprecate the oldest version to allow publishing of the latest version
* Images will have a 90 day deprecation time. During this time, users will receive warnings from Microsoft about the deprecation
* After 90 days, the deprecated images will be fully removed, and users will no longer have access.

---------------------------------------------------------
Is Ubuntu on Azure different from Ubuntu on other clouds?
---------------------------------------------------------

Yes, Ubuntu on Azure is customized to make it better for Azure. This customization includes:
 * A custom kernel ``linux-azure`` developed by Canonical for Azure
 * Extra configuration files that allow packages to work better with the platform
 * A few extra pre-installed packages that ensure built-in support for all features of Azure


----------------------------------------------------
Why are there so many publishers of Ubuntu on Azure?
----------------------------------------------------

Ubuntu is a collection of free and open source software, and redistribution is permitted in accordance with `Ubuntu's intellectual property policy`_. 

We do, however, advise caution when installing third-party Ubuntu images. You need to ensure that you trust the third party and the security of their image building pipeline. If you are paying for a third-party Ubuntu image, make sure that you not only trust it, but that you are receiving value beyond what you could obtain for free from Canonical or as part of Ubuntu Pro.


.. _`Ubuntu's intellectual property policy`: https://canonical.com/legal/intellectual-property-policy
