Canonical's offerings on IBM Cloud
===================================

Canonical and the Ubuntu community work together with IBM to ensure that Ubuntu works seamlessly across IBM platforms, including IBM Z and LinuxONE, IBM Power Systems and the IBM Cloud.

Canonical provides optimized Ubuntu LTS images with a custom kernel, minimal size, livepatch and support.

These images are available on IBM Cloud for both the IBM VPC infrastructure and the IBM Classic infrastructure.



IBM VPC vs IBM Classic infrastructures
--------------------------------------

IBM Cloud offers two types of infrastructures: IBM VPC infrastructure and IBM Classic infrastructure (Legacy). For new users, IBM only offers the VPC infrastructure. However, some long term users may still have access to the legacy Classic infrastructure.

IBM VPC offers multiple advantages over the legacy infrastructure such as better performance, scalability, and ease of use.



Ubuntu Pro
----------

Ubuntu Pro is a comprehensive subscription for open-source software security and management running on Ubuntu LTS. It provides a suite of services, including advanced tooling and optional phone and ticket support, to give you confidence in the security of your Ubuntu infrastructure.

Ubuntu Pro can be enabled on any Ubuntu instance running in IBM Cloud. After `setting up an account <https://documentation.ubuntu.com/pro/account-setup/>`__, attach the machine to your Ubuntu Pro subscription `using the Pro client <https://documentation.ubuntu.com/pro-client/en/latest/howtoguides/how_to_attach/>`__. Once attached, run `pro status` to view available features:

.. code-block::

    SERVICE          ENTITLED  STATUS    DESCRIPTION
    cc-eal           yes       disabled  Common Criteria EAL2 Provisioning Packages
    cis              yes       disabled  Security compliance and audit tools
    esm-apps         yes       enabled   Expanded Security Maintenance for Applications
    esm-infra        yes       enabled   Expanded Security Maintenance for Infrastructure
    fips             yes       disabled  NIST-certified core packages
    fips-updates     yes       disabled  NIST-certified core packages with priority security updates
    livepatch        yes       enabled   Canonical Livepatch service
    ros              yes       disabled  Security Updates for the Robot Operating System
    ros-updates      yes       disabled  All Updates for the Robot Operating System
    
    Enable services with: pro enable <service>
    
            Account: USER ACCOUNT
            Subscription: USER SUBSCRIPTION
            Valid until: 9999-12-31 00:00:00+00:00
            Technical support level: essential




Canonical Support
-----------------

Ubuntu instances on IBM Cloud can receive 24/7 `enterprise support <https://ubuntu.com/support>`__ from Canonical. In addition to Ubuntu Pro services, a support contract enititles you to:

- Full access to our Knowledge Base
- Break-fix support
- Bug-fix support
- Phone and ticket communication channels

Flexible options allow for you to receive coverage on just the packages you need. Find additional details on our `pricing <https://ubuntu.com/pricing/pro>`__ page and in our `service description <https://ubuntu.com/legal/ubuntu-pro-description#ubuntu-pro-description>`__.



Community Support
-----------------

Ad-hoc assistance can also be found on our community platforms like `AskUbuntu <https://askubuntu.com/>`__ and `Matrix <https://documentation.ubuntu.com/project/community/contributors/matrix/onboarding/#matrix-onboarding>`__.
