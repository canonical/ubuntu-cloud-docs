CIS harden your Ubuntu Pro
==========================

`CIS Benchmarks`_ are best practices for the secure configuration of a system. Ubuntu Pro includes CIS tooling packages and can be made CIS compliant.

If you don't have an Ubuntu Pro VM, you can either create a new instance with Ubuntu Pro on it (as described in :doc:`create-different-instance-types`) or you can do an in-place upgrade of your Ubuntu LTS VM to Ubuntu Pro (as explained in :doc:`upgrade-in-place-from-lts-to-pro`).

SSH into your Ubuntu Pro VM and run:

.. code::

    ua status

You'll see that the CIS service is disabled. To enable it, run:

.. code::

    sudo ua enable cis

Once the command is completed, if you run ``ua status`` again, you'll see that CIS service is enabled.

Now with the tooling packages installed, you can harden your Ubuntu 16.04 Pro system with CIS level 1 server profile, by running:

.. code::

    sudo /usr/share/ubuntu-scap-security-guides/cis-hardening/Canonical_Ubuntu_16.04_CIS_v1.1.0-harden.sh level1_server

In a few minutes, the hardening process will complete to give you a CIS level 1 compliant environment. To audit the system, run:

.. code::

    sudo cis-audit level1_server

The output should be similar to:

.. code::

    Title   Ensure mounting of cramfs filesystems is disabled
    Rule    xccdf_com.ubuntu.xenial.cis_rule_CIS-1.1.1.1
    Result  pass
    […]
    CIS audit scan completed. The scan results are available in /usr/share/ubuntu-scap-security-guides/cis-16.04-report.html report.

The HTML report mentioned above will show you your CIS score. For comprehensive CIS hardening instructions, refer to the `Ubuntu CIS Compliance documentation`_.

.. _`CIS Benchmarks`: https://www.cisecurity.org/cis-benchmarks
.. _`Ubuntu CIS Compliance documentation`: https://ubuntu.com/security/certifications/docs/usg/cis#manual-installation
