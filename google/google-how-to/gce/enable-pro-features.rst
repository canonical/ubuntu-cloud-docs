Enable Ubuntu Pro features
==========================

Not all Pro features are automatically enabled when you create your Ubuntu Pro VM. They can be enabled individually as per your requirements.

.. Note::

    If you don't have an Ubuntu Pro VM already, you can either create a new instance (refer: :ref:`create-pro-on-gcp`) or do an in-place upgrade of your LTS VM to Pro (refer: :doc:`upgrade-in-place-from-lts-to-pro`).


To check the current status of different Pro services on your VM, SSH into it and run:

.. code::

    pro status

Use the appropriate section below to enable the service that you need.


ESM
---

Extended Security Maintenance (ESM) guarantees a security coverage of 10 years for your Pro VM. So e.g. Ubuntu 22.04 will get security updates till 2032. This feature is automatically enabled with Pro and on running ``pro status``, you should see something like:

.. code::

    SERVICE          ENTITLED  STATUS    DESCRIPTION
    esm-apps         yes       enabled   Expanded Security Maintenance for Applications
    esm-infra        yes       enabled   Expanded Security Maintenance for Infrastructure
    [...]


``esm-infra`` guarantees 10-year security coverage for packages in the "main" repository, which includes Canonical-supported free and open-source software.

``esm-apps`` further extends this coverage to the "universe" repository, which includes community-maintained free and open-source software.



CIS hardening
-------------

`CIS Benchmarks`_ are best practices for the secure configuration of a system. Ubuntu Pro includes CIS tooling packages and your Pro VM can be made CIS compliant by enabling the CIS service and then hardening the instance. Enable CIS using:

.. code::

    sudo ua enable cis

With the tooling packages now installed, you can for instance, harden your Ubuntu 20.04 Pro system with CIS level 1 server profile, by running:

.. code::

    sudo /usr/share/ubuntu-scap-security-guides/cis-hardening/Canonical_Ubuntu_20.04_CIS-harden.sh lvl1_server

In a few minutes, the hardening process will complete to give you a CIS level 1 compliant environment. To audit the system, run:

.. code::

    sudo cis-audit level1_server

The output should be similar to:

.. code::

    Title   Ensure mounting of cramfs filesystems is disabled
    Rule    xccdf_com.ubuntu.focal.cis_rule_CIS-1.1.1.1
    Result  pass
    […]

    CIS audit scan completed. The scan results are available in /usr/share/ubuntu-scap-security-guides/cis-20.04-report.html report.

The HTML report mentioned above will show you your CIS score. For comprehensive CIS hardening instructions, refer to the `Ubuntu CIS Compliance documentation`_.


FIPS compliance
---------------

`Federal Information Processing Standards (FIPS)`_ are standards and guidelines for federal computer systems developed by National Institute of Standards and Technology (NIST). To enable FIPS on your Pro VM, run:

.. code::

    sudo ua enable fips

The output will be similar to:

.. code::

    One moment, checking your subscription first
    This will install the FIPS core packages.
    Are you sure? (y/N) y
    Updating package lists
    Installing FIPS packages
    FIPS enabled
    A reboot is required to complete install.

Reboot the instance by running ``sudo reboot`` or through the Google Cloud console. Once the machine restarts, you can SSH into it again and run ``pro status`` to verify that the ``fips`` service is enabled.


Livepatch
---------

With livepatch enabled, high and critical CVEs are patched in place on a running kernel, without the need for a reboot. This means that you don't have to worry about kernel related security vulnerabilities. You can avoid unexpected downtime and delay your reboot until the next scheduled maintenance window.

To enable livepatch, run:

.. code::

    sudo ua enable livepatch

Run ``pro status`` to verify that the ``livepatch`` service is enabled.


.. _`CIS Benchmarks`: https://www.cisecurity.org/cis-benchmarks
.. _`Ubuntu CIS Compliance documentation`: https://ubuntu.com/security/certifications/docs/usg/cis#manual-installation
.. _`Federal Information Processing Standards (FIPS)`: https://www.nist.gov/standardsgov/compliance-faqs-federal-information-processing-standards-fips