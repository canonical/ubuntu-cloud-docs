Ubuntu on Azure
===============

**Ubuntu on Azure is a set of customised Ubuntu images** that allow easy access to a wide range 
of products and services - offered by both Microsoft Azure and Canonical.

**These images provide a foundation for deploying cloud-based software solutions,** specifically
for softwares built on Ubuntu and running on Azure. They focus on providing the optimal tools 
and features needed to run specific workloads.

**The images create a stable and secure cloud platform** that is ideal for scaling development work
done on Ubuntu-based systems. Since Ubuntu is one of the most favoured operating systems amongst
developers, using an Ubuntu-based image for the corresponding cloud deployment becomes the simplest
option.

**Everyone from individual developers to large enterprises use these images** for developing and deploying
their softwares. For highly regulated industries from the government, medical and finance sectors, 
various security-certified images are also available.


---------

Understanding Ubuntu on Azure
-----------------------------


**Is Ubuntu available on Azure?**                             

Yes, all the supported versions of Ubuntu are available for free on Azure. See: :doc:`./azure-how-to/find-ubuntu-images`.


**Why are there multiple offers from Canonical on Azure?**                                                      

For technical reasons related to the publication process, Canonical publishes different versions of Ubuntu under dedicated offers. This is to ensure that the publication of a given version of Ubuntu cannot block or impact the publication of another version.


**How often are Ubuntu images refreshed?**                                     

Canonical publishes a new version of an image every time the kernel for this image is updated. On an average, this happens once every three weeks. Important security or bug fixes might also trigger an image refresh. However, running VMs are not affected by these changes. Use ``apt`` to keep your VM up to date and reboot your VM regularly to update the running kernel.

When using the CLI or any automated process, use the keyword `latest` in place of the image version. This ensures that you will always launch the latest image available for the given offer/SKU.


**Is Ubuntu on Azure different from Ubuntu on other clouds?**

Yes, Ubuntu on Azure is customised to make it better for Azure. This customisation includes:
 * A custom kernel ``linux-azure`` developed by Canonical for Azure
 * Extra configuration files that allow packages to work better with the platform
 * A few extra pre-installed packages that ensure built-in support for all features of Azure


**Why are there so many publishers of Ubuntu on Azure?**
                                                    
Ubuntu is a distribution of free software. Anyone is free to re-publish the OS. You are free to build your own software on top of Ubuntu and to sell it as a paid product. This is what makes Ubuntu so great. However, be very careful when downloading or using Ubuntu from an untrusted source. At best you will pay for the same product that you could get for free from Canonical. At worst, those offers could contain spyware or other malware programs that could put you and your business at risk.

*Always use Canonical's offers for running Ubuntu* except if you trust the other publisher.


---------

Canonical's offerings on Azure
------------------------------

1. Ubuntu server and Ubuntu Pro for all supported LTSes across all Azure architectures, including ARM
#. Minimal Ubuntu images for Independent Software Vendors and others who want to build on Azure
#. Ubuntu Pro FIPS images that allow US government Ubuntu users to easily move their workloads to Azure
#. Pre-hardened (CIS) Ubuntu minimal images, for those who want best security practices for Ubuntu out of the box
#. The only commercial Linux launch partner for Azure's Confidential Computing platform (both AMD SEV-SNP and TDX)
#. SQL Server on Ubuntu Pro images that include specific SQL-related OS optimisations and joint support from Canonical and Microsoft
#. Anbox on Azure, that allows users to run Android apps on Azure at scale
#. Collaboration with Azure's AKS team to support the Azure Kubernetes worker node image, as these worker nodes nearly always run Ubuntu
#. Collaboration with the Azure Guest Patching Service and Update Manager teams to ensure simple security patch management for users
#. Collaboration with the .Net team on `Chiselled .Net images`_ that have a smaller size and security cross-section 


---------

About security on Azure
-----------------------

Azure provides two types of *security*:

* `Trusted launch <https://docs.microsoft.com/en-us/azure/virtual-machines/trusted-launch>`_ which is a set of features including vTPM and `secure boot <https://wiki.ubuntu.com/UEFI/SecureBoot>`_
* `Confidential VM <https://docs.microsoft.com/en-us/azure/confidential-computing/confidential-vm-overview>`_ with support for `AMD SEV-SNP <https://www.amd.com/system/files/TechDocs/SEV-SNP-strengthening-vm-isolation-with-integrity-protection-and-more.pdf>`_, along with `measured boot <https://docs.microsoft.com/en-us/azure/security/fundamentals/measured-boot-host-attestation>`_ using a vTPM


Trusted launch
~~~~~~~~~~~~~~

All Ubuntu images from 20.04 (Focal Fossa) support trusted launch and secure boot on Hyper-V Gen2 instances. 
To start an Ubuntu instance with vTPM and secure boot enabled, use the following flags from the Azure CLI::
        
   --security-type TrustedLaunch --enable-secure-boot true --enable-vtpm

Confidential VM
~~~~~~~~~~~~~~~

What are confidential VMs?
^^^^^^^^^^^^^^^^^^^^^^^^^^

Check out our `technical blog post about Confidential VMs on Azure <https://canonical.com/blog/lets-get-confidential-canonical-ubuntu-confidential-vms-are-now-generally-available-on-microsoft-azure>`_.

In short, a confidential VM is a combination of two features:

* *Memory encryption:* The virtual machine's memory is encrypted and decrypted on the fly by the CPU. This is done using AMD SEV-SNP technology. This ensures that the host machine cannot read the memory of the guest since the encryption is done at the hardware level
* *vTPM backed full-disk encryption (FDE):* The file system of the guest OS is encrypted at rest and the key is stored in an enclave. The key cannot be retrieved unless the boot process has stayed untouched since the last sealing of the key. Re-sealing happens when a new kernel is installed as replacing the kernel binary changes the boot sequence. The vTPM is part of the guest VM and its address space. So it benefits from the same run-time security guarantees as the guest VM memory.

It's important to note that memory encryption is always enabled with a confidential VM, but FDE is optional and requires explicit activation after the VM is provisioned.


Using Ubuntu on confidential VMs
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Confidential VMs require the use of special instance sizes and a special version of Ubuntu.

* A list of instance sizes that can be used for confidential VMs is given in `Azure's documentation <https://docs.microsoft.com/en-us/azure/confidential-computing/confidential-vm-overview>`_ 
* Only `this specific offer of Ubuntu <https://azuremarketplace.microsoft.com/en-gb/marketplace/apps/canonical.0001-com-ubuntu-confidential-vm-focal>`_ supports confidential VMs.


----------

How-to guides
--------------------------------

Step-by-step guides for some of the common tasks related to Ubuntu on Azure are available here:

* :doc:`./azure-how-to/install-azure-cli`
* :doc:`./azure-how-to/find-ubuntu-images`
* :doc:`./azure-how-to/get-ubuntu-pro`
* :doc:`./azure-how-to/upgrade-from-focal-to-jammy`

   
---------

Project and community
---------------------

Ubuntu on Azure is a member of the Ubuntu family and the project warmly welcomes community projects, 
contributions, suggestions, fixes and constructive feedback.

* `Code of conduct`_
* `Get support`_
* `Join our online chat`_
* `Talk to us about Ubuntu on Azure`_


.. toctree::
   :hidden:
   :maxdepth: 2

   azure-how-to/install-azure-cli
   azure-how-to/find-ubuntu-images
   azure-how-to/get-ubuntu-pro
   azure-how-to/upgrade-from-focal-to-jammy

.. _Code of conduct: https://ubuntu.com/community/governance/code-of-conduct
.. _Get support: https://ubuntu.com/cloud/public-cloud
.. _Join our online chat: https://discourse.ubuntu.com
.. _Talk to us about Ubuntu on Azure: https://ubuntu.com/azure#get-in-touch
.. _Chiselled .Net images: https://devblogs.microsoft.com/dotnet/dotnet-6-is-now-in-ubuntu-2204
