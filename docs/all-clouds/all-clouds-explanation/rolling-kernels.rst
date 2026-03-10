.. _rolling-kernels:

Rolling kernel model
====================

By default, Ubuntu images use a **rolling kernel model**, which provides the latest upstream bug fixes and performance improvements around task scheduling, I/O scheduling, networking, hypervisor guests and containers. A rolling kernel model transitions the default kernel from one base version to the next as part of its regular patching cycle. That new kernel, called the `Hardware Enablement (HWE) Kernel`_ is the kernel of the latest Ubuntu release.

For example, users running Ubuntu 24.04 LTS instances launched in early 2024 started with the 6.8 kernel by default. However, as new Ubuntu interim versions are released and the kernel patching cycle continues, the kernel "rolls" forward to the next available kernel version. Consequently, an Ubuntu 24.04 LTS instance launched at a later point in time—such as in 2025 or 2026—will include a different kernel version depending on when it was launched; for instance, it might feature version 6.11 or 6.14.

For more details about the rolling kernel model, refer to the `Ubuntu kernel release cycle`_ and the relevant `installation options`_.


Change rolling kernel behavior
++++++++++++++++++++++++++++++

On each cloud, there is a default kernel variant (generally ``linux-<cloud-provider>``) with HWE activated. This is not the case for all Ubuntu products, but you may have the ability to modify the rolling kernel behavior by installing a different kernel package via the ``apt install`` command.


Early kernel rolling
--------------------

To receive early access to the HWE kernels, you can manually install a kernel with the ``-edge`` suffix. These kernels are still fully supported, but are less exposed to real world use cases since they are relatively new. This kernel will eventually transition into the default HWE-activated kernel. One use-case of ``-edge`` kernels is to allow you to test your deployment environment against upcoming kernel changes before your default deployment (without an ``-edge`` kernel) takes those updates.

To see the available ``-edge`` kernels for your current deployment, you can run the following command on your virtual machine:

.. code-block:: bash

   apt list linux-image-*-edge

Parse the output and pick the kernel associated to your cloud and product.

For example, if your base kernel on an Ubuntu 24.04 LTS deployment is ``linux-image-azure``, the ``-edge`` kernel is ``linux-image-azure-edge``.

.. note:: The bash command will return kernels associated to multiple products across multiple cloud partners. Selecting a kernel that is not associated to your selected cloud or product is not recommended as kernels may not be compatible with the image or hardware associated to your virtual machine.


Stop kernel rolling
-------------------

If you want to disable kernel rolling, and want to stay on the base kernel provided by the LTS release (which continues to get support and receive updates for the length of the LTS), you need to install a specific corresponding kernel variant. To find the available kernel packages, you can run the following command:

.. code-block:: bash

   apt list linux-image-*-lts-*

Parse the output and pick the kernel associated to your cloud, product, and release.

For example, if your base kernel on an Ubuntu 24.04 LTS deployment is ``linux-image-gcp`` the HWE-disabled kernel is ``linux-image-gcp-lts-24.04``

.. note:: The bash command will return kernels associated to multiple products across multiple cloud partners. Selecting a kernel that is not associated to your selected cloud or product is not recommended as kernels may not be compatible with the image or hardware associated to your virtual machine.

.. _`Hardware Enablement (HWE) Kernel`: https://canonical-kernel-docs.readthedocs-hosted.com/latest/reference/hwe-kernels/
.. _`Ubuntu kernel release cycle`: https://ubuntu.com/about/release-cycle#ubuntu-kernel-release-cycle
.. _`installation options`: https://ubuntu.com/kernel/lifecycle
