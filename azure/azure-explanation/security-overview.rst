Ubuntu Security on Azure
========================

Ubuntu security features
------------------------

Ubuntu on Azure inherits and benefits from all of the security features available to Ubuntu Server. Learn more about
Ubuntu Server security features and security-related topics with `Introduction to Security <https://documentation.ubuntu.com/server/explanation/intro-to/security/>`_.

Azure security features
-----------------------

By default, all Ubuntu X64 Hyper-V Gen2 images on Azure support `Trusted Launch for Azure Virtual Machines <https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch>`_.
Ubuntu also produces images which support `Azure Confidential Virtual Machines <https://learn.microsoft.com/en-us/azure/confidential-computing/confidential-vm-overview>`_.

See :doc:`confidential-computing`.

Choosing the right image
------------------------

Ubuntu offers a range of image types on Azure to meet security requirements. The security features and capabilities
of each image can be further enhanced with `Ubuntu Pro`_.

Server
~~~~~~

Optimised for general server use cases, Ubuntu Server is ideal for users seeking a stable and secure OS foundation to
support server workloads.

Minimal
~~~~~~~

By providing a greatly reduced package set to minimise the security cross-section of the image, Ubuntu Minimal requires
fewer security updates over time.

CIS
~~~

A hardened Ubuntu image (see `Image Hardening`_), pre-configured to align with industry best practices and guidelines
set by the Center for Internet Security (CIS). Ubuntu CIS images on Azure use custom tailoring files to meet both CIS
benchmarks as well as ensure the image remains functional in Azure cloud environments.

FIPS
~~~~

The Ubuntu FIPS image contains a Ubuntu kernel and security components which have been certified by the National
Institute of Standards and Technology (NIST), making it a compelling choice for users operating in regulated
environments such as FedRAMP, HIPAA, or PCI.

Confidential VM
~~~~~~~~~~~~~~~

Supports Azure Confidential Virtual Machines, providing enhanced security features to protect data at rest, in use, and
during boot.

Ubuntu Pro
----------

Ubuntu Pro extends the capabilities of Ubuntu Server by incorporating advanced security, compliance features, and
systems management tooling. It is designed for production environments where additional security layers and
compliance with regulatory standards are paramount. Ubuntu Pro includes:

* Expanded Security Maintenance: Security updates and patches for a wide array of applications and packages beyond the
  standard offerings.
* Kernel Livepatch: Minimises downtime and disruption by providing kernel updates that can be applied without rebooting
  the system.
* Up to 12 years of support: Long-term support that ensures your systems are secure and stable for more than a decade,
  with a guaranteed upgrade path.

To learn more about how to get Ubuntu Pro, see :doc:`../azure-how-to/instances/get-ubuntu-pro`.

Image Hardening
---------------

The security profile for Ubuntu images on Azure can be further enhanced with `hardening <https://ubuntu.com/blog/what-is-system-hardening-definition-and-best-practices>`_
by applying CIS hardening profiles from the `Ubuntu Security Guide (USG) <https://ubuntu.com/security/certifications/docs/usg>`_.

Updates
-------

Latest Images
~~~~~~~~~~~~~

Ubuntu images for a given Azure Marketplace offer (see :doc:`../azure-how-to/instances/find-ubuntu-images`) are
regularly published to deliver:

* The latest kernel available for the image type.
* Security patches to address CVEs.
* The latest stable package set from the Ubuntu archives.

Existing Workloads
~~~~~~~~~~~~~~~~~~

Deployments based off older image versions can receive the same security updates as the latest images by:

* Keeping installed packages up to date with :code:`apt`.
* Restarting the virtual machine to update the kernel, or leverage `Livepatch with Ubuntu Pro <https://ubuntu.com/security/livepatch>`_
  to automatically update the kernel while the system is running.
* Using :code:`unattended-upgrades` to automatically install security updates. It is strongly recommended users stage
  and test the updates (see the section on `updating packages automatically with unattended-upgrades <https://ubuntu.com/blog/ubuntu-updates-best-practices-for-updating-your-instance>`_.)
* Using the `Ubuntu Snapshot Service <https://snapshot.ubuntu.com/>`_ to install a snapshot of the Ubuntu archive for
  any available date and time after 1 March 2023.

Additional Information
----------------------

* `Ubuntu Security and Compliance Certifications <https://ubuntu.com/security/certifications/docs>`_
* `Introduction to Azure security <https://learn.microsoft.com/en-us/azure/security/fundamentals/overview>`_
* `Azure Update Manager <https://learn.microsoft.com/en-us/azure/update-manager/overview>`_
