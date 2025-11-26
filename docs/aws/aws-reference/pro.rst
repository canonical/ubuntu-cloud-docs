Ubuntu Pro on AWS
=================

`Ubuntu Pro`_ is a paid offering that 
provides expanded security coverage, enhanced kernel patching, and 
hardening options for compliance frameworks.

Pro product availability on AWS
-------------------------------
Ubuntu Pro images are available for the following products.

* Base server products
* EKS worker images 
* `Amazon WorkSpaces`_

For launching server and EKS pro products, refer to 
:doc:`../aws-how-to/instances/launch-ubuntu-ec2-instance`

Pro feature overview
--------------------

Expanded Security Maintenance (ESM)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
`ESM`_ extends the security patching of
the main archive to 10 years through the ``esm-infra`` entitlement. In addition
to patching the core of Ubuntu (i.e. the `Ubuntu main` repository), Pro also offers security maintenance of the 
`Ubuntu universe` repository. This security coverage is considered best effort
without Ubuntu Pro.

Livepatch
~~~~~~~~~
`Livepatch`_ applies security updates
to the kernel for critical and high security vulnerabilities in a live system.
This allows system administrators to minimize downtime between
scheduled maintenance windows. This is particularly helpful for workloads
that are expensive to migrate, such as kubernetes workers for EKS.

Compliance
~~~~~~~~~~
Ubuntu Pro offers compliance options via support for different `security standards`_ such as  
CIS (level 1 and 2) and FIPS. FIPS 140-2 is currently supported
on Ubuntu 18.04 and 20.04, while FIPS 140-3 is supported on Ubuntu 22.04. For Ubuntu 24.04, 
FIPS 140-3 is available through the `fips-updates` repository, while the modules await NIST
certification.

Ubuntu Landscape
~~~~~~~~~~~~~~~~
All Ubuntu Pro customers are entitled to the usage of 
`Landscape`_ self-hosted and SaaS solutions.
Landscape is an endpoint management solution for monitoring your Ubuntu
estate. This includes alerting for security vulnerabilities, patching status,
managing repository mirrors, and more. To sign up for Landscape SaaS see
the `sign up page`_.

.. _`Ubuntu Pro`: https://ubuntu.com/aws/pro
.. _`ESM`: https://ubuntu.com/security/esm
.. _`Livepatch`: https://ubuntu.com/security/livepatch
.. _`security standards`: https://ubuntu.com/security/security-standards
.. _`Landscape`: https://ubuntu.com/landscape
.. _`sign up page`: https://landscape.canonical.com/signup
.. _`Amazon WorkSpaces`: https://aws.amazon.com/workspaces-family/