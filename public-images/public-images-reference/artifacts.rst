Ubuntu cloud image artifacts
============================
This document provides detailed information on various Ubuntu cloud image artifacts available on `cloud-images.ubuntu.com <http://cloud-images.ubuntu.com/>`_.

Images
------
This section contains information on all of the Ubuntu cloud images available for download. These images are pre-configured and ready for deployment in cloud environments, supporting multiple architectures and configurations.

Architectures supported
~~~~~~~~~~~~~~~~~~~~~~~
-  **amd64:** Standard 64-bit PC architecture.
-  **arm64:** 64-bit ARM architecture.
-  **armhf:** Hard-float 32-bit ARM architecture.
-  **ppc64el:** 64-bit PowerPC little-endian architecture.
-  **riscv64:** 64-bit RISC-V architecture.
-  **s390x:** IBM System z (s390x) architecture.

Initial ramdisk (initrd)
~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 1 2
   :header-rows: 0

   * - Extension
     - ``<artifact>-initrd-generic``
   * - Example filename
     - ``noble-server-cloudimg-amd70-initrd-generic``
   * - Format description
     - An initial ramdisk is a temporary root file system loaded into memory during the boot process to initialise the system before the real root file system is mounted.
   * - Use cases
     - Initrds are used to ensure the kernel can boot by loading necessary drivers and modules before the root filesystem is mounted. This allows the support of diverse hardware and virtual environments, making them essential for cloud instance startup. To facilitate this, initrds can include custom initialisation scripts and they offer modular kernel support.

Linux kernel image
~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 1 2
   :header-rows: 0

   * - Extension
     - ``<artifact>-vmlinuz-generic``
   * - Example filename
     - ``noble-server-cloudimg-amd64-vmlinuz-generic``
   * - Format description
     - The vmlinuz image contains a compressed image of the Linux kernel.
   * - Use cases
     - The Linux kernel is the core component of the operating system. It handles essential functions such as process management, memory management and system calls. Kernel images may be customised for specific hardware configurations, leading to offerings for each supported architecture.

LXD tarball
~~~~~~~~~~~
.. list-table::
   :widths: 1 2
   :header-rows: 0

   * - Extension
     - ``<artifact>.lxd.tar.xz``
   * - Example filename
     - ``noble-server-cloudimg-amd64-lxd.tar.xz``
   * - Format description
     - Tar archive compressed with ``xz`` (LZMA2) containing an image suitable for LXD container deployment.
   * - Use cases
     - These files are specifically formatted for LXD, a system container manager. They contain complete file system images that can be used to instantiate LXD containers. You can use ``.lxd.tar.xz`` files to create isolated environments with specific configurations and applications, ensuring consistent container deployments across LXD hosts.

Open Virtual Appliance (OVA)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 1 2
   :header-rows: 0

   * - Extension
     - ``.ova``
   * - Example filename
     - ``noble-server-cloudimg-amd64.ova``
   * - Format description
     - An OVA is a single file distribution of an Open Virtualisation Format (OVF) package.
   * - Use cases
     - OVA files encapsulate an entire virtual machine setup including configuration, disk images and other metadata. They are used for easy deployment of virtual appliances across different virtualisation providers such as VirtualBox or VMware. You can import an ``.ova`` file into VirtualBox to quickly deploy a pre-configured virtual machine.

QEMU Copy On Write (QCOW)
~~~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 1 2
   :header-rows: 0

   * - Extension
     - ``.img``
   * - Example filename
     - ``noble-server-cloudimg-amd64.img``
   * - Format description
     - QCOW image files are disk image files containing raw sector-by-sector copies of a storage device.
   * - Use cases
     - QCOW images are used for creating bootable disks and virtual machines in virtualisation environments. Some of the primary features that make QCOW images attractive are their support for dynamic disk sizing, snapshot support and copy-on-write. You can use a ``.img`` file to create a bootable USB drive or a virtual machine disk in QEMU or VirtualBox.

Root tarball
~~~~~~~~~~~~
.. list-table::
   :widths: 1 2
   :header-rows: 0

   * - Extension
     - ``<artifact>-root.tar.xz``
   * - Example filename
     - ``noble-server-cloudimg-amd64-root.tar.xz``
   * - Format description
     - Tar archive compressed with XZ (LZMA2) containing a root file system for various architectures.
   * - Use cases
     - These files are used for deploying base system images in virtual machines and containers. You can use ``.root.tar.xz`` files to distribute pre-configured root file systems that can be deployed directly into virtual machines or container runtimes like Docker or Kubernetes.

SquashFS
~~~~~~~~
.. list-table::
   :widths: 1 2
   :header-rows: 0

   * - Extension
     - ``.squashfs``
   * - Example filename
     - ``noble-server-cloudimg-amd64.squashfs``
   * - Format description
     - SquashFS is a compressed read-only file system format.
   * - Use cases
     - SquashFS files are used for embedding file systems in read-only environments, often in embedded systems or live CDs. In cloud environments, they are used for distributing lightweight operating system images that are ready to use. You can use a ``.squashfs`` file containing a minimal Linux distribution to create container images that boot quickly and require minimal storage space.

Tarball (gzip)
~~~~~~~~~~~~~~
.. list-table::
   :widths: 1 2
   :header-rows: 0

   * - Extension
     - ``<artifact>.tar.gz``
   * - Example filename
     - ``noble-server-cloudimg-amd64.tar.gz``
   * - Format description
     - ``.tar.gz`` is an archive format, often called a tarball, that combines files into a single file and compresses it using ``gzip`` compression.
   * - Use cases
     - Our ``.tar.gz`` archives are used to distribute complete file system images along with the kernel for various operating systems and virtualisation platforms. They allow extraction and booting of the entire system on compatible hardware or virtual machines.

Vagrant Box
~~~~~~~~~~~
.. list-table::
   :widths: 1 2
   :header-rows: 0

   * - Extension
     - ``.box``
   * - Example filename
     - ``jammy-server-cloudimg-amd64-vagrant.box``
   * - Format description
     - The Vagrant Box format is used to package and distribute virtual machine environments managed by Vagrant.
   * - Use cases
     - These files contain a virtual machine image along with metadata required for Vagrant. Vagrant simplifies the creation and provisioning of virtual environments, making it easier to manage and share development environments across different systems. You can use a ``.box`` file along with a supported provider to quickly set up environments with specific configurations, tools and dependencies. All of Vagrant Boxes are provider specific, with our Boxes having been built for VirtualBox.

Virtual Hard Disk (VHD)
~~~~~~~~~~~~~~~~~~~~~~~
.. list-table::
   :widths: 1 2
   :header-rows: 0

   * - Extension
     - ``.vhd.tar.gz``
   * - Example filename
     - ``noble-server-cloudimg-amd64-azure.vhd.tar.gz``
   * - Format description
     - A VHD is a file format used by virtualisation software to store virtual hard disk images.
   * - Use cases
     - VHD files are used in cloud environments for storing VM disk images. They allow easy deployment and scaling of virtual machines. You can use a ``.vhd`` file to create an instance based on a pre-configured image, ensuring consistency across multiple deployments.

Other files
-----------
This section includes information on checksums, GPG signatures, changelogs and manifest files. These files help verify the integrity and authenticity of the images, provide details on changes between versions and list all included packages.

Changelogs
~~~~~~~~~~
.. list-table::
   :widths: 1 2
   :header-rows: 0

   * - Extension
     - ``.image_changelog.json``
   * - Example filename
     - ``noble-server-cloudimg-amd64.daily.20240612.20240622.image_changelog.json``
   * - Format description
     - JSON-formatted changelogs detailing the changes in the respective image builds.
   * - Data format
     -
      | - **summary:**
      |   - **snap:**
      |     - **added:** Lists newly added snap packages.
      |     - **removed:** Lists removed snap packages.
      |     - **diff:** Lists snap packages that have changed.
      |   - **deb:**
      |     - **added:** Lists newly added deb packages.
      |     - **removed:** Lists removed deb packages.
      |     - **diff:** Lists deb packages that have changed.
      | - **diff:**
      |   - **deb:** Detailed information on changed deb packages:
      |     - **name:** The name of the package.
      |     - **from_version:** Previous version details, including the source package name and version.
      |     - **to_version:** New version details, including the source package name and version.
      |     - **cves:** Common Vulnerabilities and Exposures fixed.
      |     - **launchpad_bugs_fixed:** IDs of fixed Launchpad bugs.
      |     - **changes:** A list of changes with details like CVEs, change logs, package name, version,
      |       urgency, distributions, author and date.
      |     - **notes:** Additional notes, if any.
      |   - **snap:** Detailed information on changed snap packages (same structure as deb).
      | - **added:** Lists newly added deb and snap packages.
      | - **removed:** Lists removed deb and snap packages.
      | - **notes:** General notes regarding the changelog.
      | - **from_series:** The starting series name.
      | - **to_series:** The target series name.
      | - **from_serial:** The starting serial number.
      | - **to_serial:** The target serial number.
      | - **from_manifest_filename:** Filename of the previous manifest.
      | - **to_manifest_filename:** Filename of the current manifest.
   * - Example
     - 
        .. dropdown::
            
            .. code-block:: json
                
                {
                    "summary": {
                        "snap": {
                            "added": [],
                            "removed": [],
                            "diff": []
                        },
                        "deb": {
                            "added": [
                                "linux-headers-6.8.0-36",
                                "linux-headers-6.8.0-36-generic",
                                "linux-image-6.8.0-36-generic",
                                "linux-modules-6.8.0-36-generic",
                                "linux-tools-6.8.0-36",
                                "linux-tools-6.8.0-36-generic"
                            ],
                            "removed": [
                                "linux-headers-6.8.0-35",
                                "linux-headers-6.8.0-35-generic",
                                "linux-image-6.8.0-35-generic",
                                "linux-modules-6.8.0-35-generic",
                                "linux-tools-6.8.0-35",
                                "linux-tools-6.8.0-35-generic"
                            ],
                            "diff": [
                                "dracut-install",
                                "libnetplan1",
                                "linux-headers-generic",
                                "linux-headers-virtual",
                                "linux-image-virtual",
                                "linux-libc-dev",
                                "linux-tools-common",
                                "linux-virtual",
                                "netplan-generator",
                                "netplan.io",
                                "python3-distupgrade",
                                "python3-netplan",
                                "ubuntu-release-upgrader-core",
                                "wget"
                            ]
                        }
                    },
                    "diff": {
                        "deb": [
                            {
                                "name": "dracut-install",
                                "from_version": {
                                    "source_package_name": "dracut",
                                    "source_package_version": "060+5-1ubuntu3",
                                    "version": "060+5-1ubuntu3"
                                },
                                "to_version": {
                                    "source_package_name": "dracut",
                                    "source_package_version": "060+5-1ubuntu3.1",
                                    "version": "060+5-1ubuntu3.1"
                                },
                                "cves": [],
                                "launchpad_bugs_fixed": [
                                    2065180
                                ],
                                "changes": [
                                    {
                                        "cves": [],
                                        "log": [
                                            "",
                                            "  * perf(dracut-install): preload kmod resources for quicker module lookup",
                                            "    (LP: #2065180)",
                                            ""
                                        ],
                                        "package": "dracut",
                                        "version": "060+5-1ubuntu3.1",
                                        "urgency": "medium",
                                        "distributions": "noble",
                                        "launchpad_bugs_fixed": [
                                            2065180
                                        ],
                                        "author": "Benjamin Drung <bdrung@ubuntu.com>",
                                        "date": "Tue, 04 Jun 2024 17:21:56 +0200"
                                    }
                                ],
                                "notes": null
                            },
                            {
                                "name": "libnetplan1",
                                "from_version": {
                                    "source_package_name": "netplan.io",
                                    "source_package_version": "1.0-2ubuntu1",
                                    "version": "1.0-2ubuntu1"
                                },
                                "to_version": {
                                    "source_package_name": "netplan.io",
                                    "source_package_version": "1.0-2ubuntu1.1",
                                    "version": "1.0-2ubuntu1.1"
                                },
                                "cves": [
                                    {
                                        "cve": "CVE-2022-4968",
                                        "url": "https://ubuntu.com/security/CVE-2022-4968",
                                        "cve_description": "netplan leaks the private key of wireguard to local users. A security fix will be released soon.",
                                        "cve_priority": "medium",
                                        "cve_public_date": "2024-06-07 01:15:00 UTC"
                                    }
                                ],
                                "launchpad_bugs_fixed": [
                                    2065738,
                                    1987842,
                                    2066258
                                ],
                                "changes": [
                                    {
                                        "cves": [
                                            {
                                                "cve": "CVE-2022-4968",
                                                "url": "https://ubuntu.com/security/CVE-2022-4968",
                                                "cve_description": "netplan leaks the private key of wireguard to local users. A security fix will be released soon.",
                                                "cve_priority": "medium",
                                                "cve_public_date": "2024-06-07 01:15:00 UTC"
                                            }
                                        ],
                                        "log": [
                                            "",
                                            "  * SECURITY UPDATE: weak permissions on secret files, command injection",
                                            "    - d/p/lp2065738/0014-libnetplan-use-more-restrictive-file-permissions.patch:",
                                            "      Use more restrictive file permissions to prevent unprivileged users to",
                                            "      read sensitive data from back end files (LP: #2065738, #1987842)",
                                            "    - CVE-2022-4968",
                                            "    - d/p/lp2066258/0015-libnetplan-escape-control-characters.patch:",
                                            "      Escape control characters in the parser and double quotes in backend",
                                            "      files.",
                                            "    - d/p/lp2066258/0016-backends-escape-file-paths.patch:",
                                            "      Escape special characters in file paths.",
                                            "    - d/p/lp2066258/0017-backends-escape-semicolons-in-service-units.patch:",
                                            "      Escape isolated semicolons in systemd service units. (LP: #2066258)",
                                            "  * debian/netplan-generator.postinst: Add a postinst maintainer script to call",
                                            "    the generator. It's needed so the file permissions fixes will be applied",
                                            "    automatically, thanks to danilogondolfo ",
                                            ""
                                        ],
                                        "package": "netplan.io",
                                        "version": "1.0-2ubuntu1.1",
                                        "urgency": "medium",
                                        "distributions": "noble-security",
                                        "launchpad_bugs_fixed": [
                                            2065738,
                                            1987842,
                                            2066258
                                        ],
                                        "author": "Sudhakar Verma <sudhakar.verma@canonical.com>",
                                        "date": "Tue, 25 Jun 2024 00:13:00 +0530"
                                    }
                                ],
                                "notes": null
                            },
                            {
                                "name": "linux-headers-generic",
                                "from_version": {
                                    "source_package_name": "linux-meta",
                                    "source_package_version": "6.8.0-35.35",
                                    "version": "6.8.0-35.35"
                                },
                                "to_version": {
                                    "source_package_name": "linux-meta",
                                    "source_package_version": "6.8.0-36.36",
                                    "version": "6.8.0-36.36"
                                },
                                "cves": [],
                                "launchpad_bugs_fixed": [],
                                "changes": [
                                    {
                                        "cves": [],
                                        "log": [
                                            "",
                                            "  * Main version: 6.8.0-36.36",
                                            ""
                                        ],
                                        "package": "linux-meta",
                                        "version": "6.8.0-36.36",
                                        "urgency": "medium",
                                        "distributions": "noble",
                                        "launchpad_bugs_fixed": [],
                                        "author": "Roxana Nicolescu <roxana.nicolescu@canonical.com>",
                                        "date": "Mon, 10 Jun 2024 11:29:30 +0200"
                                    }
                                ],
                                "notes": null
                            },
                            {
                                "name": "linux-headers-virtual",
                                "from_version": {
                                    "source_package_name": "linux-meta",
                                    "source_package_version": "6.8.0-35.35",
                                    "version": "6.8.0-35.35"
                                },
                                "to_version": {
                                    "source_package_name": "linux-meta",
                                    "source_package_version": "6.8.0-36.36",
                                    "version": "6.8.0-36.36"
                                },
                                "cves": [],
                                "launchpad_bugs_fixed": [],
                                "changes": [
                                    {
                                        "cves": [],
                                        "log": [
                                            "",
                                            "  * Main version: 6.8.0-36.36",
                                            ""
                                        ],
                                        "package": "linux-meta",
                                        "version": "6.8.0-36.36",
                                        "urgency": "medium",
                                        "distributions": "noble",
                                        "launchpad_bugs_fixed": [],
                                        "author": "Roxana Nicolescu <roxana.nicolescu@canonical.com>",
                                        "date": "Mon, 10 Jun 2024 11:29:30 +0200"
                                    }
                                ],
                                "notes": null
                            },
                            {
                                "name": "linux-image-virtual",
                                "from_version": {
                                    "source_package_name": "linux-meta",
                                    "source_package_version": "6.8.0-35.35",
                                    "version": "6.8.0-35.35"
                                },
                                "to_version": {
                                    "source_package_name": "linux-meta",
                                    "source_package_version": "6.8.0-36.36",
                                    "version": "6.8.0-36.36"
                                },
                                "cves": [],
                                "launchpad_bugs_fixed": [],
                                "changes": [
                                    {
                                        "cves": [],
                                        "log": [
                                            "",
                                            "  * Main version: 6.8.0-36.36",
                                            ""
                                        ],
                                        "package": "linux-meta",
                                        "version": "6.8.0-36.36",
                                        "urgency": "medium",
                                        "distributions": "noble",
                                        "launchpad_bugs_fixed": [],
                                        "author": "Roxana Nicolescu <roxana.nicolescu@canonical.com>",
                                        "date": "Mon, 10 Jun 2024 11:29:30 +0200"
                                    }
                                ],
                                "notes": null
                            },
                            {
                                "name": "linux-libc-dev",
                                "from_version": {
                                    "source_package_name": "linux",
                                    "source_package_version": "6.8.0-35.35",
                                    "version": "6.8.0-35.35"
                                },
                                "to_version": {
                                    "source_package_name": "linux",
                                    "source_package_version": "6.8.0-36.36",
                                    "version": "6.8.0-36.36"
                                },
                                "cves": [
                                    {
                                        "cve": "CVE-2024-26924",
                                        "url": "https://ubuntu.com/security/CVE-2024-26924",
                                        "cve_description": "In the Linux kernel, the following vulnerability has been resolved: netfilter: nft_set_pipapo: do not free live element Pablo reports a crash with large batches of elements with a back-to-back add/remove pattern. Quoting Pablo: add_elem(\"00000000\") timeout 100 ms ... add_elem(\"0000000X\") timeout 100 ms del_elem(\"0000000X\") <---------------- delete one that was just added ... add_elem(\"00005000\") timeout 100 ms 1) nft_pipapo_remove() removes element 0000000X Then, KASAN shows a splat. Looking at the remove function there is a chance that we will drop a rule that maps to a non-deactivated element. Removal happens in two steps, first we do a lookup for key k and return the to-be-removed element and mark it as inactive in the next generation. Then, in a second step, the element gets removed from the set/map. The _remove function does not work correctly if we have more than one element that share the same key. This can happen if we insert an element into a set when the set already holds an element with same key, but the element mapping to the existing key has timed out or is not active in the next generation. In such case its possible that removal will unmap the wrong element. If this happens, we will leak the non-deactivated element, it becomes unreachable. The element that got deactivated (and will be freed later) will remain reachable in the set data structure, this can result in a crash when such an element is retrieved during lookup (stale pointer). Add a check that the fully matching key does in fact map to the element that we have marked as inactive in the deactivation step. If not, we need to continue searching. Add a bug/warn trap at the end of the function as well, the remove function must not ever be called with an invisible/unreachable/non-existent element. v2: avoid uneeded temporary variable (Stefano)",
                                        "cve_priority": "high",
                                        "cve_public_date": "2024-04-25 06:15:00 UTC"
                                    }
                                ],
                                "launchpad_bugs_fixed": [
                                    2068150
                                ],
                                "changes": [
                                    {
                                        "cves": [
                                            {
                                                "cve": "CVE-2024-26924",
                                                "url": "https://ubuntu.com/security/CVE-2024-26924",
                                                "cve_description": "In the Linux kernel, the following vulnerability has been resolved: netfilter: nft_set_pipapo: do not free live element Pablo reports a crash with large batches of elements with a back-to-back add/remove pattern. Quoting Pablo: add_elem(\"00000000\") timeout 100 ms ... add_elem(\"0000000X\") timeout 100 ms del_elem(\"0000000X\") <---------------- delete one that was just added ... add_elem(\"00005000\") timeout 100 ms 1) nft_pipapo_remove() removes element 0000000X Then, KASAN shows a splat. Looking at the remove function there is a chance that we will drop a rule that maps to a non-deactivated element. Removal happens in two steps, first we do a lookup for key k and return the to-be-removed element and mark it as inactive in the next generation. Then, in a second step, the element gets removed from the set/map. The _remove function does not work correctly if we have more than one element that share the same key. This can happen if we insert an element into a set when the set already holds an element with same key, but the element mapping to the existing key has timed out or is not active in the next generation. In such case its possible that removal will unmap the wrong element. If this happens, we will leak the non-deactivated element, it becomes unreachable. The element that got deactivated (and will be freed later) will remain reachable in the set data structure, this can result in a crash when such an element is retrieved during lookup (stale pointer). Add a check that the fully matching key does in fact map to the element that we have marked as inactive in the deactivation step. If not, we need to continue searching. Add a bug/warn trap at the end of the function as well, the remove function must not ever be called with an invisible/unreachable/non-existent element. v2: avoid uneeded temporary variable (Stefano)",
                                                "cve_priority": "high",
                                                "cve_public_date": "2024-04-25 06:15:00 UTC"
                                            }
                                        ],
                                        "log": [
                                            "",
                                            "  * noble/linux: 6.8.0-36.36 -proposed tracker (LP: #2068150)",
                                            "",
                                            "  * CVE-2024-26924",
                                            "    - netfilter: nft_set_pipapo: do not free live element",
                                            ""
                                        ],
                                        "package": "linux",
                                        "version": "6.8.0-36.36",
                                        "urgency": "medium",
                                        "distributions": "noble",
                                        "launchpad_bugs_fixed": [
                                            2068150
                                        ],
                                        "author": "Roxana Nicolescu <roxana.nicolescu@canonical.com>",
                                        "date": "Mon, 10 Jun 2024 11:26:41 +0200"
                                    }
                                ],
                                "notes": null
                            },
                            {
                                "name": "linux-tools-common",
                                "from_version": {
                                    "source_package_name": "linux",
                                    "source_package_version": "6.8.0-35.35",
                                    "version": "6.8.0-35.35"
                                },
                                "to_version": {
                                    "source_package_name": "linux",
                                    "source_package_version": "6.8.0-36.36",
                                    "version": "6.8.0-36.36"
                                },
                                "cves": [
                                    {
                                        "cve": "CVE-2024-26924",
                                        "url": "https://ubuntu.com/security/CVE-2024-26924",
                                        "cve_description": "In the Linux kernel, the following vulnerability has been resolved: netfilter: nft_set_pipapo: do not free live element Pablo reports a crash with large batches of elements with a back-to-back add/remove pattern. Quoting Pablo: add_elem(\"00000000\") timeout 100 ms ... add_elem(\"0000000X\") timeout 100 ms del_elem(\"0000000X\") <---------------- delete one that was just added ... add_elem(\"00005000\") timeout 100 ms 1) nft_pipapo_remove() removes element 0000000X Then, KASAN shows a splat. Looking at the remove function there is a chance that we will drop a rule that maps to a non-deactivated element. Removal happens in two steps, first we do a lookup for key k and return the to-be-removed element and mark it as inactive in the next generation. Then, in a second step, the element gets removed from the set/map. The _remove function does not work correctly if we have more than one element that share the same key. This can happen if we insert an element into a set when the set already holds an element with same key, but the element mapping to the existing key has timed out or is not active in the next generation. In such case its possible that removal will unmap the wrong element. If this happens, we will leak the non-deactivated element, it becomes unreachable. The element that got deactivated (and will be freed later) will remain reachable in the set data structure, this can result in a crash when such an element is retrieved during lookup (stale pointer). Add a check that the fully matching key does in fact map to the element that we have marked as inactive in the deactivation step. If not, we need to continue searching. Add a bug/warn trap at the end of the function as well, the remove function must not ever be called with an invisible/unreachable/non-existent element. v2: avoid uneeded temporary variable (Stefano)",
                                        "cve_priority": "high",
                                        "cve_public_date": "2024-04-25 06:15:00 UTC"
                                    }
                                ],
                                "launchpad_bugs_fixed": [
                                    2068150
                                ],
                                "changes": [
                                    {
                                        "cves": [
                                            {
                                                "cve": "CVE-2024-26924",
                                                "url": "https://ubuntu.com/security/CVE-2024-26924",
                                                "cve_description": "In the Linux kernel, the following vulnerability has been resolved: netfilter: nft_set_pipapo: do not free live element Pablo reports a crash with large batches of elements with a back-to-back add/remove pattern. Quoting Pablo: add_elem(\"00000000\") timeout 100 ms ... add_elem(\"0000000X\") timeout 100 ms del_elem(\"0000000X\") <---------------- delete one that was just added ... add_elem(\"00005000\") timeout 100 ms 1) nft_pipapo_remove() removes element 0000000X Then, KASAN shows a splat. Looking at the remove function there is a chance that we will drop a rule that maps to a non-deactivated element. Removal happens in two steps, first we do a lookup for key k and return the to-be-removed element and mark it as inactive in the next generation. Then, in a second step, the element gets removed from the set/map. The _remove function does not work correctly if we have more than one element that share the same key. This can happen if we insert an element into a set when the set already holds an element with same key, but the element mapping to the existing key has timed out or is not active in the next generation. In such case its possible that removal will unmap the wrong element. If this happens, we will leak the non-deactivated element, it becomes unreachable. The element that got deactivated (and will be freed later) will remain reachable in the set data structure, this can result in a crash when such an element is retrieved during lookup (stale pointer). Add a check that the fully matching key does in fact map to the element that we have marked as inactive in the deactivation step. If not, we need to continue searching. Add a bug/warn trap at the end of the function as well, the remove function must not ever be called with an invisible/unreachable/non-existent element. v2: avoid uneeded temporary variable (Stefano)",
                                                "cve_priority": "high",
                                                "cve_public_date": "2024-04-25 06:15:00 UTC"
                                            }
                                        ],
                                        "log": [
                                            "",
                                            "  * noble/linux: 6.8.0-36.36 -proposed tracker (LP: #2068150)",
                                            "",
                                            "  * CVE-2024-26924",
                                            "    - netfilter: nft_set_pipapo: do not free live element",
                                            ""
                                        ],
                                        "package": "linux",
                                        "version": "6.8.0-36.36",
                                        "urgency": "medium",
                                        "distributions": "noble",
                                        "launchpad_bugs_fixed": [
                                            2068150
                                        ],
                                        "author": "Roxana Nicolescu <roxana.nicolescu@canonical.com>",
                                        "date": "Mon, 10 Jun 2024 11:26:41 +0200"
                                    }
                                ],
                                "notes": null
                            },
                            {
                                "name": "linux-virtual",
                                "from_version": {
                                    "source_package_name": "linux-meta",
                                    "source_package_version": "6.8.0-35.35",
                                    "version": "6.8.0-35.35"
                                },
                                "to_version": {
                                    "source_package_name": "linux-meta",
                                    "source_package_version": "6.8.0-36.36",
                                    "version": "6.8.0-36.36"
                                },
                                "cves": [],
                                "launchpad_bugs_fixed": [],
                                "changes": [
                                    {
                                        "cves": [],
                                        "log": [
                                            "",
                                            "  * Main version: 6.8.0-36.36",
                                            ""
                                        ],
                                        "package": "linux-meta",
                                        "version": "6.8.0-36.36",
                                        "urgency": "medium",
                                        "distributions": "noble",
                                        "launchpad_bugs_fixed": [],
                                        "author": "Roxana Nicolescu <roxana.nicolescu@canonical.com>",
                                        "date": "Mon, 10 Jun 2024 11:29:30 +0200"
                                    }
                                ],
                                "notes": null
                            },
                            {
                                "name": "netplan-generator",
                                "from_version": {
                                    "source_package_name": "netplan.io",
                                    "source_package_version": "1.0-2ubuntu1",
                                    "version": "1.0-2ubuntu1"
                                },
                                "to_version": {
                                    "source_package_name": "netplan.io",
                                    "source_package_version": "1.0-2ubuntu1.1",
                                    "version": "1.0-2ubuntu1.1"
                                },
                                "cves": [
                                    {
                                        "cve": "CVE-2022-4968",
                                        "url": "https://ubuntu.com/security/CVE-2022-4968",
                                        "cve_description": "netplan leaks the private key of wireguard to local users. A security fix will be released soon.",
                                        "cve_priority": "medium",
                                        "cve_public_date": "2024-06-07 01:15:00 UTC"
                                    }
                                ],
                                "launchpad_bugs_fixed": [
                                    2065738,
                                    1987842,
                                    2066258
                                ],
                                "changes": [
                                    {
                                        "cves": [
                                            {
                                                "cve": "CVE-2022-4968",
                                                "url": "https://ubuntu.com/security/CVE-2022-4968",
                                                "cve_description": "netplan leaks the private key of wireguard to local users. A security fix will be released soon.",
                                                "cve_priority": "medium",
                                                "cve_public_date": "2024-06-07 01:15:00 UTC"
                                            }
                                        ],
                                        "log": [
                                            "",
                                            "  * SECURITY UPDATE: weak permissions on secret files, command injection",
                                            "    - d/p/lp2065738/0014-libnetplan-use-more-restrictive-file-permissions.patch:",
                                            "      Use more restrictive file permissions to prevent unprivileged users to",
                                            "      read sensitive data from back end files (LP: #2065738, #1987842)",
                                            "    - CVE-2022-4968",
                                            "    - d/p/lp2066258/0015-libnetplan-escape-control-characters.patch:",
                                            "      Escape control characters in the parser and double quotes in backend",
                                            "      files.",
                                            "    - d/p/lp2066258/0016-backends-escape-file-paths.patch:",
                                            "      Escape special characters in file paths.",
                                            "    - d/p/lp2066258/0017-backends-escape-semicolons-in-service-units.patch:",
                                            "      Escape isolated semicolons in systemd service units. (LP: #2066258)",
                                            "  * debian/netplan-generator.postinst: Add a postinst maintainer script to call",
                                            "    the generator. It's needed so the file permissions fixes will be applied",
                                            "    automatically, thanks to danilogondolfo ",
                                            ""
                                        ],
                                        "package": "netplan.io",
                                        "version": "1.0-2ubuntu1.1",
                                        "urgency": "medium",
                                        "distributions": "noble-security",
                                        "launchpad_bugs_fixed": [
                                            2065738,
                                            1987842,
                                            2066258
                                        ],
                                        "author": "Sudhakar Verma <sudhakar.verma@canonical.com>",
                                        "date": "Tue, 25 Jun 2024 00:13:00 +0530"
                                    }
                                ],
                                "notes": null
                            },
                            {
                                "name": "netplan.io",
                                "from_version": {
                                    "source_package_name": "netplan.io",
                                    "source_package_version": "1.0-2ubuntu1",
                                    "version": "1.0-2ubuntu1"
                                },
                                "to_version": {
                                    "source_package_name": "netplan.io",
                                    "source_package_version": "1.0-2ubuntu1.1",
                                    "version": "1.0-2ubuntu1.1"
                                },
                                "cves": [
                                    {
                                        "cve": "CVE-2022-4968",
                                        "url": "https://ubuntu.com/security/CVE-2022-4968",
                                        "cve_description": "netplan leaks the private key of wireguard to local users. A security fix will be released soon.",
                                        "cve_priority": "medium",
                                        "cve_public_date": "2024-06-07 01:15:00 UTC"
                                    }
                                ],
                                "launchpad_bugs_fixed": [
                                    2065738,
                                    1987842,
                                    2066258
                                ],
                                "changes": [
                                    {
                                        "cves": [
                                            {
                                                "cve": "CVE-2022-4968",
                                                "url": "https://ubuntu.com/security/CVE-2022-4968",
                                                "cve_description": "netplan leaks the private key of wireguard to local users. A security fix will be released soon.",
                                                "cve_priority": "medium",
                                                "cve_public_date": "2024-06-07 01:15:00 UTC"
                                            }
                                        ],
                                        "log": [
                                            "",
                                            "  * SECURITY UPDATE: weak permissions on secret files, command injection",
                                            "    - d/p/lp2065738/0014-libnetplan-use-more-restrictive-file-permissions.patch:",
                                            "      Use more restrictive file permissions to prevent unprivileged users to",
                                            "      read sensitive data from back end files (LP: #2065738, #1987842)",
                                            "    - CVE-2022-4968",
                                            "    - d/p/lp2066258/0015-libnetplan-escape-control-characters.patch:",
                                            "      Escape control characters in the parser and double quotes in backend",
                                            "      files.",
                                            "    - d/p/lp2066258/0016-backends-escape-file-paths.patch:",
                                            "      Escape special characters in file paths.",
                                            "    - d/p/lp2066258/0017-backends-escape-semicolons-in-service-units.patch:",
                                            "      Escape isolated semicolons in systemd service units. (LP: #2066258)",
                                            "  * debian/netplan-generator.postinst: Add a postinst maintainer script to call",
                                            "    the generator. It's needed so the file permissions fixes will be applied",
                                            "    automatically, thanks to danilogondolfo ",
                                            ""
                                        ],
                                        "package": "netplan.io",
                                        "version": "1.0-2ubuntu1.1",
                                        "urgency": "medium",
                                        "distributions": "noble-security",
                                        "launchpad_bugs_fixed": [
                                            2065738,
                                            1987842,
                                            2066258
                                        ],
                                        "author": "Sudhakar Verma <sudhakar.verma@canonical.com>",
                                        "date": "Tue, 25 Jun 2024 00:13:00 +0530"
                                    }
                                ],
                                "notes": null
                            },
                            {
                                "name": "python3-distupgrade",
                                "from_version": {
                                    "source_package_name": "ubuntu-release-upgrader",
                                    "source_package_version": "1:24.04.18",
                                    "version": "1:24.04.18"
                                },
                                "to_version": {
                                    "source_package_name": "ubuntu-release-upgrader",
                                    "source_package_version": "1:24.04.19",
                                    "version": "1:24.04.19"
                                },
                                "cves": [],
                                "launchpad_bugs_fixed": [
                                    2067886,
                                    2067071,
                                    2067585
                                ],
                                "changes": [
                                    {
                                        "cves": [],
                                        "log": [
                                            "",
                                            "  * DistUpgrade: drop quirk for systems with BIOS and XFS /boot (LP: #2067886)",
                                            "  * DistUpgradeQuirks: make sure replacement.candidate is not None",
                                            "    (LP: #2067071)",
                                            "  * DistUpgrade: use tempfile for apt extended_states during simulation",
                                            "    (LP: #2067585)",
                                            "  * Run pre-build.sh: updating mirrors, demotions and translations.",
                                            ""
                                        ],
                                        "package": "ubuntu-release-upgrader",
                                        "version": "1:24.04.19",
                                        "urgency": "medium",
                                        "distributions": "noble",
                                        "launchpad_bugs_fixed": [
                                            2067886,
                                            2067071,
                                            2067585
                                        ],
                                        "author": "Nick Rosbrook <enr0n@ubuntu.com>",
                                        "date": "Tue, 04 Jun 2024 11:55:51 -0400"
                                    }
                                ],
                                "notes": null
                            },
                            {
                                "name": "python3-netplan",
                                "from_version": {
                                    "source_package_name": "netplan.io",
                                    "source_package_version": "1.0-2ubuntu1",
                                    "version": "1.0-2ubuntu1"
                                },
                                "to_version": {
                                    "source_package_name": "netplan.io",
                                    "source_package_version": "1.0-2ubuntu1.1",
                                    "version": "1.0-2ubuntu1.1"
                                },
                                "cves": [
                                    {
                                        "cve": "CVE-2022-4968",
                                        "url": "https://ubuntu.com/security/CVE-2022-4968",
                                        "cve_description": "netplan leaks the private key of wireguard to local users. A security fix will be released soon.",
                                        "cve_priority": "medium",
                                        "cve_public_date": "2024-06-07 01:15:00 UTC"
                                    }
                                ],
                                "launchpad_bugs_fixed": [
                                    2065738,
                                    1987842,
                                    2066258
                                ],
                                "changes": [
                                    {
                                        "cves": [
                                            {
                                                "cve": "CVE-2022-4968",
                                                "url": "https://ubuntu.com/security/CVE-2022-4968",
                                                "cve_description": "netplan leaks the private key of wireguard to local users. A security fix will be released soon.",
                                                "cve_priority": "medium",
                                                "cve_public_date": "2024-06-07 01:15:00 UTC"
                                            }
                                        ],
                                        "log": [
                                            "",
                                            "  * SECURITY UPDATE: weak permissions on secret files, command injection",
                                            "    - d/p/lp2065738/0014-libnetplan-use-more-restrictive-file-permissions.patch:",
                                            "      Use more restrictive file permissions to prevent unprivileged users to",
                                            "      read sensitive data from back end files (LP: #2065738, #1987842)",
                                            "    - CVE-2022-4968",
                                            "    - d/p/lp2066258/0015-libnetplan-escape-control-characters.patch:",
                                            "      Escape control characters in the parser and double quotes in backend",
                                            "      files.",
                                            "    - d/p/lp2066258/0016-backends-escape-file-paths.patch:",
                                            "      Escape special characters in file paths.",
                                            "    - d/p/lp2066258/0017-backends-escape-semicolons-in-service-units.patch:",
                                            "      Escape isolated semicolons in systemd service units. (LP: #2066258)",
                                            "  * debian/netplan-generator.postinst: Add a postinst maintainer script to call",
                                            "    the generator. It's needed so the file permissions fixes will be applied",
                                            "    automatically, thanks to danilogondolfo ",
                                            ""
                                        ],
                                        "package": "netplan.io",
                                        "version": "1.0-2ubuntu1.1",
                                        "urgency": "medium",
                                        "distributions": "noble-security",
                                        "launchpad_bugs_fixed": [
                                            2065738,
                                            1987842,
                                            2066258
                                        ],
                                        "author": "Sudhakar Verma <sudhakar.verma@canonical.com>",
                                        "date": "Tue, 25 Jun 2024 00:13:00 +0530"
                                    }
                                ],
                                "notes": null
                            },
                            {
                                "name": "ubuntu-release-upgrader-core",
                                "from_version": {
                                    "source_package_name": "ubuntu-release-upgrader",
                                    "source_package_version": "1:24.04.18",
                                    "version": "1:24.04.18"
                                },
                                "to_version": {
                                    "source_package_name": "ubuntu-release-upgrader",
                                    "source_package_version": "1:24.04.19",
                                    "version": "1:24.04.19"
                                },
                                "cves": [],
                                "launchpad_bugs_fixed": [
                                    2067886,
                                    2067071,
                                    2067585
                                ],
                                "changes": [
                                    {
                                        "cves": [],
                                        "log": [
                                            "",
                                            "  * DistUpgrade: drop quirk for systems with BIOS and XFS /boot (LP: #2067886)",
                                            "  * DistUpgradeQuirks: make sure replacement.candidate is not None",
                                            "    (LP: #2067071)",
                                            "  * DistUpgrade: use tempfile for apt extended_states during simulation",
                                            "    (LP: #2067585)",
                                            "  * Run pre-build.sh: updating mirrors, demotions and translations.",
                                            ""
                                        ],
                                        "package": "ubuntu-release-upgrader",
                                        "version": "1:24.04.19",
                                        "urgency": "medium",
                                        "distributions": "noble",
                                        "launchpad_bugs_fixed": [
                                            2067886,
                                            2067071,
                                            2067585
                                        ],
                                        "author": "Nick Rosbrook <enr0n@ubuntu.com>",
                                        "date": "Tue, 04 Jun 2024 11:55:51 -0400"
                                    }
                                ],
                                "notes": null
                            },
                            {
                                "name": "wget",
                                "from_version": {
                                    "source_package_name": "wget",
                                    "source_package_version": "1.21.4-1ubuntu4",
                                    "version": "1.21.4-1ubuntu4"
                                },
                                "to_version": {
                                    "source_package_name": "wget",
                                    "source_package_version": "1.21.4-1ubuntu4.1",
                                    "version": "1.21.4-1ubuntu4.1"
                                },
                                "cves": [
                                    {
                                        "cve": "CVE-2024-38428",
                                        "url": "https://ubuntu.com/security/CVE-2024-38428",
                                        "cve_description": "url.c in GNU Wget through 1.24.5 mishandles semicolons in the userinfo subcomponent of a URI and thus there may be insecure behavior in which data that was supposed to be in the userinfo subcomponent is misinterpreted to be part of the host subcomponent.",
                                        "cve_priority": "medium",
                                        "cve_public_date": "2024-06-16 03:15:00 UTC"
                                    }
                                ],
                                "launchpad_bugs_fixed": [],
                                "changes": [
                                    {
                                        "cves": [
                                            {
                                                "cve": "CVE-2024-38428",
                                                "url": "https://ubuntu.com/security/CVE-2024-38428",
                                                "cve_description": "url.c in GNU Wget through 1.24.5 mishandles semicolons in the userinfo subcomponent of a URI and thus there may be insecure behavior in which data that was supposed to be in the userinfo subcomponent is misinterpreted to be part of the host subcomponent.",
                                                "cve_priority": "medium",
                                                "cve_public_date": "2024-06-16 03:15:00 UTC"
                                            }
                                        ],
                                        "log": [
                                            "",
                                            "  * SECURITY UPDATE: mishandling of semicolons in userinfo",
                                            "    - debian/patches/CVE-2024-38428.patch: properly re-implement userinfo",
                                            "      parsing in src/url.c.",
                                            "    - CVE-2024-38428",
                                            ""
                                        ],
                                        "package": "wget",
                                        "version": "1.21.4-1ubuntu4.1",
                                        "urgency": "medium",
                                        "distributions": "noble-security",
                                        "launchpad_bugs_fixed": [],
                                        "author": "Marc Deslauriers <marc.deslauriers@ubuntu.com>",
                                        "date": "Wed, 19 Jun 2024 08:14:03 -0400"
                                    }
                                ],
                                "notes": null
                            }
                        ],
                        "snap": []
                    },
                    "added": {
                        "deb": [
                            {
                                "name": "linux-headers-6.8.0-36",
                                "from_version": {
                                    "source_package_name": "linux",
                                    "source_package_version": "6.8.0-35.35",
                                    "version": null
                                },
                                "to_version": {
                                    "source_package_name": "linux",
                                    "source_package_version": "6.8.0-36.36",
                                    "version": "6.8.0-36.36"
                                },
                                "cves": [
                                    {
                                        "cve": "CVE-2024-26924",
                                        "url": "https://ubuntu.com/security/CVE-2024-26924",
                                        "cve_description": "In the Linux kernel, the following vulnerability has been resolved: netfilter: nft_set_pipapo: do not free live element Pablo reports a crash with large batches of elements with a back-to-back add/remove pattern. Quoting Pablo: add_elem(\"00000000\") timeout 100 ms ... add_elem(\"0000000X\") timeout 100 ms del_elem(\"0000000X\") <---------------- delete one that was just added ... add_elem(\"00005000\") timeout 100 ms 1) nft_pipapo_remove() removes element 0000000X Then, KASAN shows a splat. Looking at the remove function there is a chance that we will drop a rule that maps to a non-deactivated element. Removal happens in two steps, first we do a lookup for key k and return the to-be-removed element and mark it as inactive in the next generation. Then, in a second step, the element gets removed from the set/map. The _remove function does not work correctly if we have more than one element that share the same key. This can happen if we insert an element into a set when the set already holds an element with same key, but the element mapping to the existing key has timed out or is not active in the next generation. In such case its possible that removal will unmap the wrong element. If this happens, we will leak the non-deactivated element, it becomes unreachable. The element that got deactivated (and will be freed later) will remain reachable in the set data structure, this can result in a crash when such an element is retrieved during lookup (stale pointer). Add a check that the fully matching key does in fact map to the element that we have marked as inactive in the deactivation step. If not, we need to continue searching. Add a bug/warn trap at the end of the function as well, the remove function must not ever be called with an invisible/unreachable/non-existent element. v2: avoid uneeded temporary variable (Stefano)",
                                        "cve_priority": "high",
                                        "cve_public_date": "2024-04-25 06:15:00 UTC"
                                    }
                                ],
                                "launchpad_bugs_fixed": [
                                    2068150
                                ],
                                "changes": [
                                    {
                                        "cves": [
                                            {
                                                "cve": "CVE-2024-26924",
                                                "url": "https://ubuntu.com/security/CVE-2024-26924",
                                                "cve_description": "In the Linux kernel, the following vulnerability has been resolved: netfilter: nft_set_pipapo: do not free live element Pablo reports a crash with large batches of elements with a back-to-back add/remove pattern. Quoting Pablo: add_elem(\"00000000\") timeout 100 ms ... add_elem(\"0000000X\") timeout 100 ms del_elem(\"0000000X\") <---------------- delete one that was just added ... add_elem(\"00005000\") timeout 100 ms 1) nft_pipapo_remove() removes element 0000000X Then, KASAN shows a splat. Looking at the remove function there is a chance that we will drop a rule that maps to a non-deactivated element. Removal happens in two steps, first we do a lookup for key k and return the to-be-removed element and mark it as inactive in the next generation. Then, in a second step, the element gets removed from the set/map. The _remove function does not work correctly if we have more than one element that share the same key. This can happen if we insert an element into a set when the set already holds an element with same key, but the element mapping to the existing key has timed out or is not active in the next generation. In such case its possible that removal will unmap the wrong element. If this happens, we will leak the non-deactivated element, it becomes unreachable. The element that got deactivated (and will be freed later) will remain reachable in the set data structure, this can result in a crash when such an element is retrieved during lookup (stale pointer). Add a check that the fully matching key does in fact map to the element that we have marked as inactive in the deactivation step. If not, we need to continue searching. Add a bug/warn trap at the end of the function as well, the remove function must not ever be called with an invisible/unreachable/non-existent element. v2: avoid uneeded temporary variable (Stefano)",
                                                "cve_priority": "high",
                                                "cve_public_date": "2024-04-25 06:15:00 UTC"
                                            }
                                        ],
                                        "log": [
                                            "",
                                            "  * noble/linux: 6.8.0-36.36 -proposed tracker (LP: #2068150)",
                                            "",
                                            "  * CVE-2024-26924",
                                            "    - netfilter: nft_set_pipapo: do not free live element",
                                            ""
                                        ],
                                        "package": "linux",
                                        "version": "6.8.0-36.36",
                                        "urgency": "medium",
                                        "distributions": "noble",
                                        "launchpad_bugs_fixed": [
                                            2068150
                                        ],
                                        "author": "Roxana Nicolescu <roxana.nicolescu@canonical.com>",
                                        "date": "Mon, 10 Jun 2024 11:26:41 +0200"
                                    }
                                ],
                                "notes": "linux-headers-6.8.0-36 version '6.8.0-36.36' (source package linux version '6.8.0-36.36') was added. linux-headers-6.8.0-36 version '6.8.0-36.36' has the same source package name, linux, as removed package linux-headers-6.8.0-35. As such we can use the source package version of the removed package, '6.8.0-35.35', as the starting point in our changelog diff. Kernel packages are an example of where the binary package name changes for the same source package. Using the removed package source package version as our starting point means we can still get meaningful changelog diffs even for what appears to be a new package."
                            },
                            {
                                "name": "linux-headers-6.8.0-36-generic",
                                "from_version": {
                                    "source_package_name": "linux",
                                    "source_package_version": "6.8.0-35.35",
                                    "version": null
                                },
                                "to_version": {
                                    "source_package_name": "linux",
                                    "source_package_version": "6.8.0-36.36",
                                    "version": "6.8.0-36.36"
                                },
                                "cves": [
                                    {
                                        "cve": "CVE-2024-26924",
                                        "url": "https://ubuntu.com/security/CVE-2024-26924",
                                        "cve_description": "In the Linux kernel, the following vulnerability has been resolved: netfilter: nft_set_pipapo: do not free live element Pablo reports a crash with large batches of elements with a back-to-back add/remove pattern. Quoting Pablo: add_elem(\"00000000\") timeout 100 ms ... add_elem(\"0000000X\") timeout 100 ms del_elem(\"0000000X\") <---------------- delete one that was just added ... add_elem(\"00005000\") timeout 100 ms 1) nft_pipapo_remove() removes element 0000000X Then, KASAN shows a splat. Looking at the remove function there is a chance that we will drop a rule that maps to a non-deactivated element. Removal happens in two steps, first we do a lookup for key k and return the to-be-removed element and mark it as inactive in the next generation. Then, in a second step, the element gets removed from the set/map. The _remove function does not work correctly if we have more than one element that share the same key. This can happen if we insert an element into a set when the set already holds an element with same key, but the element mapping to the existing key has timed out or is not active in the next generation. In such case its possible that removal will unmap the wrong element. If this happens, we will leak the non-deactivated element, it becomes unreachable. The element that got deactivated (and will be freed later) will remain reachable in the set data structure, this can result in a crash when such an element is retrieved during lookup (stale pointer). Add a check that the fully matching key does in fact map to the element that we have marked as inactive in the deactivation step. If not, we need to continue searching. Add a bug/warn trap at the end of the function as well, the remove function must not ever be called with an invisible/unreachable/non-existent element. v2: avoid uneeded temporary variable (Stefano)",
                                        "cve_priority": "high",
                                        "cve_public_date": "2024-04-25 06:15:00 UTC"
                                    }
                                ],
                                "launchpad_bugs_fixed": [
                                    2068150
                                ],
                                "changes": [
                                    {
                                        "cves": [
                                            {
                                                "cve": "CVE-2024-26924",
                                                "url": "https://ubuntu.com/security/CVE-2024-26924",
                                                "cve_description": "In the Linux kernel, the following vulnerability has been resolved: netfilter: nft_set_pipapo: do not free live element Pablo reports a crash with large batches of elements with a back-to-back add/remove pattern. Quoting Pablo: add_elem(\"00000000\") timeout 100 ms ... add_elem(\"0000000X\") timeout 100 ms del_elem(\"0000000X\") <---------------- delete one that was just added ... add_elem(\"00005000\") timeout 100 ms 1) nft_pipapo_remove() removes element 0000000X Then, KASAN shows a splat. Looking at the remove function there is a chance that we will drop a rule that maps to a non-deactivated element. Removal happens in two steps, first we do a lookup for key k and return the to-be-removed element and mark it as inactive in the next generation. Then, in a second step, the element gets removed from the set/map. The _remove function does not work correctly if we have more than one element that share the same key. This can happen if we insert an element into a set when the set already holds an element with same key, but the element mapping to the existing key has timed out or is not active in the next generation. In such case its possible that removal will unmap the wrong element. If this happens, we will leak the non-deactivated element, it becomes unreachable. The element that got deactivated (and will be freed later) will remain reachable in the set data structure, this can result in a crash when such an element is retrieved during lookup (stale pointer). Add a check that the fully matching key does in fact map to the element that we have marked as inactive in the deactivation step. If not, we need to continue searching. Add a bug/warn trap at the end of the function as well, the remove function must not ever be called with an invisible/unreachable/non-existent element. v2: avoid uneeded temporary variable (Stefano)",
                                                "cve_priority": "high",
                                                "cve_public_date": "2024-04-25 06:15:00 UTC"
                                            }
                                        ],
                                        "log": [
                                            "",
                                            "  * noble/linux: 6.8.0-36.36 -proposed tracker (LP: #2068150)",
                                            "",
                                            "  * CVE-2024-26924",
                                            "    - netfilter: nft_set_pipapo: do not free live element",
                                            ""
                                        ],
                                        "package": "linux",
                                        "version": "6.8.0-36.36",
                                        "urgency": "medium",
                                        "distributions": "noble",
                                        "launchpad_bugs_fixed": [
                                            2068150
                                        ],
                                        "author": "Roxana Nicolescu <roxana.nicolescu@canonical.com>",
                                        "date": "Mon, 10 Jun 2024 11:26:41 +0200"
                                    }
                                ],
                                "notes": "linux-headers-6.8.0-36-generic version '6.8.0-36.36' (source package linux version '6.8.0-36.36') was added. linux-headers-6.8.0-36-generic version '6.8.0-36.36' has the same source package name, linux, as removed package linux-headers-6.8.0-35. As such we can use the source package version of the removed package, '6.8.0-35.35', as the starting point in our changelog diff. Kernel packages are an example of where the binary package name changes for the same source package. Using the removed package source package version as our starting point means we can still get meaningful changelog diffs even for what appears to be a new package."
                            },
                            {
                                "name": "linux-image-6.8.0-36-generic",
                                "from_version": {
                                    "source_package_name": "linux-signed",
                                    "source_package_version": "6.8.0-35.35+1",
                                    "version": null
                                },
                                "to_version": {
                                    "source_package_name": "linux-signed",
                                    "source_package_version": "6.8.0-36.36",
                                    "version": "6.8.0-36.36"
                                },
                                "cves": [],
                                "launchpad_bugs_fixed": [
                                    1786013
                                ],
                                "changes": [
                                    {
                                        "cves": [],
                                        "log": [
                                            "",
                                            "  * Main version: 6.8.0-36.36",
                                            "",
                                            "  * Packaging resync (LP: #1786013)",
                                            "    - [Packaging] debian/tracking-bug -- resync from main package",
                                            ""
                                        ],
                                        "package": "linux-signed",
                                        "version": "6.8.0-36.36",
                                        "urgency": "medium",
                                        "distributions": "noble",
                                        "launchpad_bugs_fixed": [
                                            1786013
                                        ],
                                        "author": "Roxana Nicolescu <roxana.nicolescu@canonical.com>",
                                        "date": "Mon, 10 Jun 2024 11:29:38 +0200"
                                    }
                                ],
                                "notes": "linux-image-6.8.0-36-generic version '6.8.0-36.36' (source package linux-signed version '6.8.0-36.36') was added. linux-image-6.8.0-36-generic version '6.8.0-36.36' has the same source package name, linux-signed, as removed package linux-image-6.8.0-35-generic. As such we can use the source package version of the removed package, '6.8.0-35.35+1', as the starting point in our changelog diff. Kernel packages are an example of where the binary package name changes for the same source package. Using the removed package source package version as our starting point means we can still get meaningful changelog diffs even for what appears to be a new package."
                            },
                            {
                                "name": "linux-modules-6.8.0-36-generic",
                                "from_version": {
                                    "source_package_name": "linux",
                                    "source_package_version": "6.8.0-35.35",
                                    "version": null
                                },
                                "to_version": {
                                    "source_package_name": "linux",
                                    "source_package_version": "6.8.0-36.36",
                                    "version": "6.8.0-36.36"
                                },
                                "cves": [
                                    {
                                        "cve": "CVE-2024-26924",
                                        "url": "https://ubuntu.com/security/CVE-2024-26924",
                                        "cve_description": "In the Linux kernel, the following vulnerability has been resolved: netfilter: nft_set_pipapo: do not free live element Pablo reports a crash with large batches of elements with a back-to-back add/remove pattern. Quoting Pablo: add_elem(\"00000000\") timeout 100 ms ... add_elem(\"0000000X\") timeout 100 ms del_elem(\"0000000X\") <---------------- delete one that was just added ... add_elem(\"00005000\") timeout 100 ms 1) nft_pipapo_remove() removes element 0000000X Then, KASAN shows a splat. Looking at the remove function there is a chance that we will drop a rule that maps to a non-deactivated element. Removal happens in two steps, first we do a lookup for key k and return the to-be-removed element and mark it as inactive in the next generation. Then, in a second step, the element gets removed from the set/map. The _remove function does not work correctly if we have more than one element that share the same key. This can happen if we insert an element into a set when the set already holds an element with same key, but the element mapping to the existing key has timed out or is not active in the next generation. In such case its possible that removal will unmap the wrong element. If this happens, we will leak the non-deactivated element, it becomes unreachable. The element that got deactivated (and will be freed later) will remain reachable in the set data structure, this can result in a crash when such an element is retrieved during lookup (stale pointer). Add a check that the fully matching key does in fact map to the element that we have marked as inactive in the deactivation step. If not, we need to continue searching. Add a bug/warn trap at the end of the function as well, the remove function must not ever be called with an invisible/unreachable/non-existent element. v2: avoid uneeded temporary variable (Stefano)",
                                        "cve_priority": "high",
                                        "cve_public_date": "2024-04-25 06:15:00 UTC"
                                    }
                                ],
                                "launchpad_bugs_fixed": [
                                    2068150
                                ],
                                "changes": [
                                    {
                                        "cves": [
                                            {
                                                "cve": "CVE-2024-26924",
                                                "url": "https://ubuntu.com/security/CVE-2024-26924",
                                                "cve_description": "In the Linux kernel, the following vulnerability has been resolved: netfilter: nft_set_pipapo: do not free live element Pablo reports a crash with large batches of elements with a back-to-back add/remove pattern. Quoting Pablo: add_elem(\"00000000\") timeout 100 ms ... add_elem(\"0000000X\") timeout 100 ms del_elem(\"0000000X\") <---------------- delete one that was just added ... add_elem(\"00005000\") timeout 100 ms 1) nft_pipapo_remove() removes element 0000000X Then, KASAN shows a splat. Looking at the remove function there is a chance that we will drop a rule that maps to a non-deactivated element. Removal happens in two steps, first we do a lookup for key k and return the to-be-removed element and mark it as inactive in the next generation. Then, in a second step, the element gets removed from the set/map. The _remove function does not work correctly if we have more than one element that share the same key. This can happen if we insert an element into a set when the set already holds an element with same key, but the element mapping to the existing key has timed out or is not active in the next generation. In such case its possible that removal will unmap the wrong element. If this happens, we will leak the non-deactivated element, it becomes unreachable. The element that got deactivated (and will be freed later) will remain reachable in the set data structure, this can result in a crash when such an element is retrieved during lookup (stale pointer). Add a check that the fully matching key does in fact map to the element that we have marked as inactive in the deactivation step. If not, we need to continue searching. Add a bug/warn trap at the end of the function as well, the remove function must not ever be called with an invisible/unreachable/non-existent element. v2: avoid uneeded temporary variable (Stefano)",
                                                "cve_priority": "high",
                                                "cve_public_date": "2024-04-25 06:15:00 UTC"
                                            }
                                        ],
                                        "log": [
                                            "",
                                            "  * noble/linux: 6.8.0-36.36 -proposed tracker (LP: #2068150)",
                                            "",
                                            "  * CVE-2024-26924",
                                            "    - netfilter: nft_set_pipapo: do not free live element",
                                            ""
                                        ],
                                        "package": "linux",
                                        "version": "6.8.0-36.36",
                                        "urgency": "medium",
                                        "distributions": "noble",
                                        "launchpad_bugs_fixed": [
                                            2068150
                                        ],
                                        "author": "Roxana Nicolescu <roxana.nicolescu@canonical.com>",
                                        "date": "Mon, 10 Jun 2024 11:26:41 +0200"
                                    }
                                ],
                                "notes": "linux-modules-6.8.0-36-generic version '6.8.0-36.36' (source package linux version '6.8.0-36.36') was added. linux-modules-6.8.0-36-generic version '6.8.0-36.36' has the same source package name, linux, as removed package linux-headers-6.8.0-35. As such we can use the source package version of the removed package, '6.8.0-35.35', as the starting point in our changelog diff. Kernel packages are an example of where the binary package name changes for the same source package. Using the removed package source package version as our starting point means we can still get meaningful changelog diffs even for what appears to be a new package."
                            },
                            {
                                "name": "linux-tools-6.8.0-36",
                                "from_version": {
                                    "source_package_name": "linux",
                                    "source_package_version": "6.8.0-35.35",
                                    "version": null
                                },
                                "to_version": {
                                    "source_package_name": "linux",
                                    "source_package_version": "6.8.0-36.36",
                                    "version": "6.8.0-36.36"
                                },
                                "cves": [
                                    {
                                        "cve": "CVE-2024-26924",
                                        "url": "https://ubuntu.com/security/CVE-2024-26924",
                                        "cve_description": "In the Linux kernel, the following vulnerability has been resolved: netfilter: nft_set_pipapo: do not free live element Pablo reports a crash with large batches of elements with a back-to-back add/remove pattern. Quoting Pablo: add_elem(\"00000000\") timeout 100 ms ... add_elem(\"0000000X\") timeout 100 ms del_elem(\"0000000X\") <---------------- delete one that was just added ... add_elem(\"00005000\") timeout 100 ms 1) nft_pipapo_remove() removes element 0000000X Then, KASAN shows a splat. Looking at the remove function there is a chance that we will drop a rule that maps to a non-deactivated element. Removal happens in two steps, first we do a lookup for key k and return the to-be-removed element and mark it as inactive in the next generation. Then, in a second step, the element gets removed from the set/map. The _remove function does not work correctly if we have more than one element that share the same key. This can happen if we insert an element into a set when the set already holds an element with same key, but the element mapping to the existing key has timed out or is not active in the next generation. In such case its possible that removal will unmap the wrong element. If this happens, we will leak the non-deactivated element, it becomes unreachable. The element that got deactivated (and will be freed later) will remain reachable in the set data structure, this can result in a crash when such an element is retrieved during lookup (stale pointer). Add a check that the fully matching key does in fact map to the element that we have marked as inactive in the deactivation step. If not, we need to continue searching. Add a bug/warn trap at the end of the function as well, the remove function must not ever be called with an invisible/unreachable/non-existent element. v2: avoid uneeded temporary variable (Stefano)",
                                        "cve_priority": "high",
                                        "cve_public_date": "2024-04-25 06:15:00 UTC"
                                    }
                                ],
                                "launchpad_bugs_fixed": [
                                    2068150
                                ],
                                "changes": [
                                    {
                                        "cves": [
                                            {
                                                "cve": "CVE-2024-26924",
                                                "url": "https://ubuntu.com/security/CVE-2024-26924",
                                                "cve_description": "In the Linux kernel, the following vulnerability has been resolved: netfilter: nft_set_pipapo: do not free live element Pablo reports a crash with large batches of elements with a back-to-back add/remove pattern. Quoting Pablo: add_elem(\"00000000\") timeout 100 ms ... add_elem(\"0000000X\") timeout 100 ms del_elem(\"0000000X\") <---------------- delete one that was just added ... add_elem(\"00005000\") timeout 100 ms 1) nft_pipapo_remove() removes element 0000000X Then, KASAN shows a splat. Looking at the remove function there is a chance that we will drop a rule that maps to a non-deactivated element. Removal happens in two steps, first we do a lookup for key k and return the to-be-removed element and mark it as inactive in the next generation. Then, in a second step, the element gets removed from the set/map. The _remove function does not work correctly if we have more than one element that share the same key. This can happen if we insert an element into a set when the set already holds an element with same key, but the element mapping to the existing key has timed out or is not active in the next generation. In such case its possible that removal will unmap the wrong element. If this happens, we will leak the non-deactivated element, it becomes unreachable. The element that got deactivated (and will be freed later) will remain reachable in the set data structure, this can result in a crash when such an element is retrieved during lookup (stale pointer). Add a check that the fully matching key does in fact map to the element that we have marked as inactive in the deactivation step. If not, we need to continue searching. Add a bug/warn trap at the end of the function as well, the remove function must not ever be called with an invisible/unreachable/non-existent element. v2: avoid uneeded temporary variable (Stefano)",
                                                "cve_priority": "high",
                                                "cve_public_date": "2024-04-25 06:15:00 UTC"
                                            }
                                        ],
                                        "log": [
                                            "",
                                            "  * noble/linux: 6.8.0-36.36 -proposed tracker (LP: #2068150)",
                                            "",
                                            "  * CVE-2024-26924",
                                            "    - netfilter: nft_set_pipapo: do not free live element",
                                            ""
                                        ],
                                        "package": "linux",
                                        "version": "6.8.0-36.36",
                                        "urgency": "medium",
                                        "distributions": "noble",
                                        "launchpad_bugs_fixed": [
                                            2068150
                                        ],
                                        "author": "Roxana Nicolescu <roxana.nicolescu@canonical.com>",
                                        "date": "Mon, 10 Jun 2024 11:26:41 +0200"
                                    }
                                ],
                                "notes": "linux-tools-6.8.0-36 version '6.8.0-36.36' (source package linux version '6.8.0-36.36') was added. linux-tools-6.8.0-36 version '6.8.0-36.36' has the same source package name, linux, as removed package linux-headers-6.8.0-35. As such we can use the source package version of the removed package, '6.8.0-35.35', as the starting point in our changelog diff. Kernel packages are an example of where the binary package name changes for the same source package. Using the removed package source package version as our starting point means we can still get meaningful changelog diffs even for what appears to be a new package."
                            },
                            {
                                "name": "linux-tools-6.8.0-36-generic",
                                "from_version": {
                                    "source_package_name": "linux",
                                    "source_package_version": "6.8.0-35.35",
                                    "version": null
                                },
                                "to_version": {
                                    "source_package_name": "linux",
                                    "source_package_version": "6.8.0-36.36",
                                    "version": "6.8.0-36.36"
                                },
                                "cves": [
                                    {
                                        "cve": "CVE-2024-26924",
                                        "url": "https://ubuntu.com/security/CVE-2024-26924",
                                        "cve_description": "In the Linux kernel, the following vulnerability has been resolved: netfilter: nft_set_pipapo: do not free live element Pablo reports a crash with large batches of elements with a back-to-back add/remove pattern. Quoting Pablo: add_elem(\"00000000\") timeout 100 ms ... add_elem(\"0000000X\") timeout 100 ms del_elem(\"0000000X\") <---------------- delete one that was just added ... add_elem(\"00005000\") timeout 100 ms 1) nft_pipapo_remove() removes element 0000000X Then, KASAN shows a splat. Looking at the remove function there is a chance that we will drop a rule that maps to a non-deactivated element. Removal happens in two steps, first we do a lookup for key k and return the to-be-removed element and mark it as inactive in the next generation. Then, in a second step, the element gets removed from the set/map. The _remove function does not work correctly if we have more than one element that share the same key. This can happen if we insert an element into a set when the set already holds an element with same key, but the element mapping to the existing key has timed out or is not active in the next generation. In such case its possible that removal will unmap the wrong element. If this happens, we will leak the non-deactivated element, it becomes unreachable. The element that got deactivated (and will be freed later) will remain reachable in the set data structure, this can result in a crash when such an element is retrieved during lookup (stale pointer). Add a check that the fully matching key does in fact map to the element that we have marked as inactive in the deactivation step. If not, we need to continue searching. Add a bug/warn trap at the end of the function as well, the remove function must not ever be called with an invisible/unreachable/non-existent element. v2: avoid uneeded temporary variable (Stefano)",
                                        "cve_priority": "high",
                                        "cve_public_date": "2024-04-25 06:15:00 UTC"
                                    }
                                ],
                                "launchpad_bugs_fixed": [
                                    2068150
                                ],
                                "changes": [
                                    {
                                        "cves": [
                                            {
                                                "cve": "CVE-2024-26924",
                                                "url": "https://ubuntu.com/security/CVE-2024-26924",
                                                "cve_description": "In the Linux kernel, the following vulnerability has been resolved: netfilter: nft_set_pipapo: do not free live element Pablo reports a crash with large batches of elements with a back-to-back add/remove pattern. Quoting Pablo: add_elem(\"00000000\") timeout 100 ms ... add_elem(\"0000000X\") timeout 100 ms del_elem(\"0000000X\") <---------------- delete one that was just added ... add_elem(\"00005000\") timeout 100 ms 1) nft_pipapo_remove() removes element 0000000X Then, KASAN shows a splat. Looking at the remove function there is a chance that we will drop a rule that maps to a non-deactivated element. Removal happens in two steps, first we do a lookup for key k and return the to-be-removed element and mark it as inactive in the next generation. Then, in a second step, the element gets removed from the set/map. The _remove function does not work correctly if we have more than one element that share the same key. This can happen if we insert an element into a set when the set already holds an element with same key, but the element mapping to the existing key has timed out or is not active in the next generation. In such case its possible that removal will unmap the wrong element. If this happens, we will leak the non-deactivated element, it becomes unreachable. The element that got deactivated (and will be freed later) will remain reachable in the set data structure, this can result in a crash when such an element is retrieved during lookup (stale pointer). Add a check that the fully matching key does in fact map to the element that we have marked as inactive in the deactivation step. If not, we need to continue searching. Add a bug/warn trap at the end of the function as well, the remove function must not ever be called with an invisible/unreachable/non-existent element. v2: avoid uneeded temporary variable (Stefano)",
                                                "cve_priority": "high",
                                                "cve_public_date": "2024-04-25 06:15:00 UTC"
                                            }
                                        ],
                                        "log": [
                                            "",
                                            "  * noble/linux: 6.8.0-36.36 -proposed tracker (LP: #2068150)",
                                            "",
                                            "  * CVE-2024-26924",
                                            "    - netfilter: nft_set_pipapo: do not free live element",
                                            ""
                                        ],
                                        "package": "linux",
                                        "version": "6.8.0-36.36",
                                        "urgency": "medium",
                                        "distributions": "noble",
                                        "launchpad_bugs_fixed": [
                                            2068150
                                        ],
                                        "author": "Roxana Nicolescu <roxana.nicolescu@canonical.com>",
                                        "date": "Mon, 10 Jun 2024 11:26:41 +0200"
                                    }
                                ],
                                "notes": "linux-tools-6.8.0-36-generic version '6.8.0-36.36' (source package linux version '6.8.0-36.36') was added. linux-tools-6.8.0-36-generic version '6.8.0-36.36' has the same source package name, linux, as removed package linux-headers-6.8.0-35. As such we can use the source package version of the removed package, '6.8.0-35.35', as the starting point in our changelog diff. Kernel packages are an example of where the binary package name changes for the same source package. Using the removed package source package version as our starting point means we can still get meaningful changelog diffs even for what appears to be a new package."
                            }
                        ],
                        "snap": []
                    },
                    "removed": {
                        "deb": [
                            {
                                "name": "linux-headers-6.8.0-35",
                                "from_version": {
                                    "source_package_name": "linux",
                                    "source_package_version": "6.8.0-35.35",
                                    "version": "6.8.0-35.35"
                                },
                                "to_version": {
                                    "source_package_name": null,
                                    "source_package_version": null,
                                    "version": null
                                },
                                "cves": [],
                                "launchpad_bugs_fixed": [],
                                "changes": [],
                                "notes": null
                            },
                            {
                                "name": "linux-headers-6.8.0-35-generic",
                                "from_version": {
                                    "source_package_name": "linux",
                                    "source_package_version": "6.8.0-35.35",
                                    "version": "6.8.0-35.35"
                                },
                                "to_version": {
                                    "source_package_name": null,
                                    "source_package_version": null,
                                    "version": null
                                },
                                "cves": [],
                                "launchpad_bugs_fixed": [],
                                "changes": [],
                                "notes": null
                            },
                            {
                                "name": "linux-image-6.8.0-35-generic",
                                "from_version": {
                                    "source_package_name": "linux-signed",
                                    "source_package_version": "6.8.0-35.35+1",
                                    "version": "6.8.0-35.35+1"
                                },
                                "to_version": {
                                    "source_package_name": null,
                                    "source_package_version": null,
                                    "version": null
                                },
                                "cves": [],
                                "launchpad_bugs_fixed": [],
                                "changes": [],
                                "notes": null
                            },
                            {
                                "name": "linux-modules-6.8.0-35-generic",
                                "from_version": {
                                    "source_package_name": "linux",
                                    "source_package_version": "6.8.0-35.35",
                                    "version": "6.8.0-35.35"
                                },
                                "to_version": {
                                    "source_package_name": null,
                                    "source_package_version": null,
                                    "version": null
                                },
                                "cves": [],
                                "launchpad_bugs_fixed": [],
                                "changes": [],
                                "notes": null
                            },
                            {
                                "name": "linux-tools-6.8.0-35",
                                "from_version": {
                                    "source_package_name": "linux",
                                    "source_package_version": "6.8.0-35.35",
                                    "version": "6.8.0-35.35"
                                },
                                "to_version": {
                                    "source_package_name": null,
                                    "source_package_version": null,
                                    "version": null
                                },
                                "cves": [],
                                "launchpad_bugs_fixed": [],
                                "changes": [],
                                "notes": null
                            },
                            {
                                "name": "linux-tools-6.8.0-35-generic",
                                "from_version": {
                                    "source_package_name": "linux",
                                    "source_package_version": "6.8.0-35.35",
                                    "version": "6.8.0-35.35"
                                },
                                "to_version": {
                                    "source_package_name": null,
                                    "source_package_version": null,
                                    "version": null
                                },
                                "cves": [],
                                "launchpad_bugs_fixed": [],
                                "changes": [],
                                "notes": null
                            }
                        ],
                        "snap": []
                    },
                    "notes": "Changelog diff for Ubuntu 24.04 noble image from daily image serial 20240622 to 20240628",
                    "from_series": "noble",
                    "to_series": "noble",
                    "from_serial": "20240622",
                    "to_serial": "20240628",
                    "from_manifest_filename": "daily_manifest.previous",
                    "to_manifest_filename": "manifest.current"
                }

Checksums
~~~~~~~~~
.. list-table::
   :widths: 1 2
   :header-rows: 0

   * - Extension
     - ``<artifact>SUMS``
   * - Example filename
     - MD5SUMS, SHA256SUMS
   * - Format description
     - Contains checksums (MD5 or SHA256) of files to verify integrity.
   * - Use Cases
     - Checksum files are used extensively in software distribution to verify file integrity after download or transfer.
   * - Example
     - 	
        .. code-block:: bash

            md5sum noble-server-cloudimg-amd64.img
            # Compare this checksum with the value in MD5SUMS.
            cat MD5SUMS | grep noble-server-cloudimg-amd64.img

GPG signatures
~~~~~~~~~~~~~~
.. list-table::
   :widths: 1 2
   :header-rows: 0

   * - Extension
     - ``.gpg``
   * - Example filename
     - MD5SUMS.gpg, SHA256SUMS.gpg
   * - Format description
     - GPG signatures for MD5SUMS and SHA256SUMS files, ensuring authenticity and integrity.
   * - Use Cases
     - GPG signatures are used in conjunction with checksum files to verify the authenticity of downloaded or transferred files securely. Verify the GPG signature of a checksum file before calculating and comparing the checksums.
   * - Example
     -
        .. code-block:: bash

            # Verify the GPG signature
            gpg ~~verify SHA256SUMS.gpg SHA256SUMS


        If there is no public key for Ubuntu present, you will get an error message with a ``key id``. Use that id to import the GPG key from the Ubuntu keyserver.

        .. code-block:: bash

            gpg --keyserver keyserver.ubuntu.com \
                --recv-keys <key id>

Manifests
~~~~~~~~~
.. list-table::
   :widths: 1 2
   :header-rows: 0

   * - Extension
     - .manifest
   * - Example filename
     - noble-server-cloudimg-amd64-root.manifest
   * - Format description
     - Lists of packages included in various images.
   * - Data format
     - ``<package_name> <version>``
   * - Example
     - 
        .. code-block:: text

            adduser    3.137ubuntu1
            apparmor    4.0.0-beta3-0ubuntu3
            apport    2.28.1-0ubuntu3
            apport-core-dump-handler    2.28.1-0ubuntu3
            apport-symptoms    0.25
            appstream    1.0.2-1build6
            apt    2.7.14build2
            ...
