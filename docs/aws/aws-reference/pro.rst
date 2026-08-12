.. meta::
   :description: Learn about Ubuntu Pro on AWS, including ESM, Livepatch, compliance, and Pro image availability for cloud workloads.

.. _pro:

Ubuntu Pro on AWS
=================

`Ubuntu Pro`_ is a subscription that provides expanded security coverage,
enhanced kernel patching, and hardening options for compliance frameworks.

Ubuntu Pro availability on AWS
------------------------------

Ubuntu Pro on AWS is available through different methods:

:ref:`Launch new Amazon Images (AMIs) <launch-ubuntu-ec2-instance>`,
covering the following products:

* Ubuntu Pro server images: EC2, Marketplace
* Ubuntu Pro FIPS server images: Marketplace
* CIS-hardened Minimal Ubuntu Pro: Marketplace
* Minimal Ubuntu Pro images: EC2, Marketplace
* EKS worker-nodes images: EC2, Marketplace and ``eksctl``
* Ubuntu Pro Desktop: Available on `Amazon WorkSpaces`_

In-place upgrade of existing Ubuntu LTS instances to Ubuntu Pro:

* :ref:`Using AWS License Manager <upgrade-in-place-from-lts-to-pro>`: EC2, Marketplace (coming soon)
* Using Canonical Tokens: Marketplace (contact us)

Build custom AMIs using EC2 Image Builder:

* Starting from any base Ubuntu Pro image: EC2, Marketplace
* Using the :ref:`Upgrade to Ubuntu Pro component <build-ubuntu-pro-image-with-ec2-image-builder>`: Marketplace

Ubuntu Pro features overview
----------------------------

Expanded Security Maintenance (ESM)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
`ESM`_ extends the security patching of the main archive to 10 years through
the ``esm-infra`` entitlement. In addition to patching the core of Ubuntu
(i.e. the Ubuntu main repository), Pro also offers security maintenance for
high and critical vulnerabilities affecting any of the Ubuntu Universe
repository packages through ``esm-apps``, which contains thousands of 3rd party
open source apps. The Legacy add-on extends ESM by an additional 5 years, for a
total of 15 years.

Livepatch
~~~~~~~~~
`Livepatch`_ applies high and critical security updates to the kernel in
memory, allowing system administrators to minimize downtime between scheduled
maintenance windows. This is particularly advantageous for long-running
workloads such as big data, machine learning training, agentic AI, and
Kubernetes, where node reboots require a pod migration strategy.

Compliance
~~~~~~~~~~
Ubuntu Pro offers options for FedRAMP compliance, providing FIPS-certified
components for the Linux kernel and other cryptographic modules, and assisted
hardening against industry-standard benchmarks such as the Center for Internet
Security (CIS) and the Defense Information Systems Agency's Security Technical
Implementation Guide (DISA-STIG).

Learn more in our `security standards`_ page.

Canonical Landscape
~~~~~~~~~~~~~~~~~~~~
Every Ubuntu Pro customer is entitled to using `Landscape`_, Canonical's
endpoint management solution, in either the self-hosted or SaaS version. This
includes fleet patch management, alerting for security vulnerabilities,
configuration status, managing repository mirrors, and more.

Landscape also supports managing Amazon WorkSpaces desktop instances. Learn
more in our `how-to guide about setting up WorkSpaces in Landscape`_.

To sign up for Landscape SaaS see the `sign up page`_.

Verify your subscription
------------------------
To verify that you have successfully activated your Ubuntu Pro subscription,
open a terminal session (either using SSH, EC2 Instance Connect or SSM's
terminal session) and run the following command: ``sudo pro status``. You
should get an output similar to:

.. code-block:: text

   ubuntu@ip-172-31-82-190:~$ sudo pro status
   SERVICE          ENTITLED  STATUS       DESCRIPTION
   anbox-cloud      yes       disabled     Scalable Android in the cloud
   esm-apps         yes       enabled      Expanded Security Maintenance for Applications
   esm-infra        yes       enabled      Expanded Security Maintenance for Infrastructure
   fips-preview     yes       disabled     Preview of FIPS crypto packages undergoing certification with NIST
   fips-updates     yes       disabled     FIPS compliant crypto packages with stable security updates
   livepatch        yes       enabled      Canonical Livepatch service
   usg              yes       disabled     Security compliance and audit tools

   For a list of all Ubuntu Pro services and variants, run 'pro status --all'
   Enable services with: pro enable <service>

                   Account: <REDACTED>
              Subscription: <REDACTED>
               Valid until: Fri Dec 31 00:00:00 9999 UTC
   Technical support level: essential

To enable Ubuntu Pro services, you can use ``sudo pro enable <service name>``.
Learn more about the Pro client and its features in our
`documentation for Ubuntu Pro Client`_.

.. _`Ubuntu Pro`: https://ubuntu.com/aws/pro
.. _`ESM`: https://ubuntu.com/security/esm
.. _`Livepatch`: https://ubuntu.com/security/livepatch
.. _`security standards`: https://ubuntu.com/security/security-standards
.. _`Landscape`: https://ubuntu.com/landscape
.. _`how-to guide about setting up WorkSpaces in Landscape`: https://ubuntu.com/landscape/docs/how-to-guides/landscape-installation-and-set-up/cloud-providers/get-started-ubuntu-amazon-workspaces/
.. _`sign up page`: https://landscape.canonical.com/signup
.. _`documentation for Ubuntu Pro Client`: https://documentation.ubuntu.com/pro-client/en/latest/
.. _`Amazon WorkSpaces`: https://aws.amazon.com/workspaces/
