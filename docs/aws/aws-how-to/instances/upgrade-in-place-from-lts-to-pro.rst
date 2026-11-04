.. meta::
   :description: Learn how to upgrade from Ubuntu LTS to Ubuntu Pro in-place. Step-by-step guide for using AWS License Manager to perform the upgrade, including requirements and verification steps.

.. _upgrade-in-place-from-lts-to-pro:

Upgrade from Ubuntu LTS to Ubuntu Pro using AWS License Manager
===============================================================

Overview
--------

`Ubuntu Pro`_ expands Ubuntu LTS’ standard security maintenance from 5 to 10 years, with an additional 5 years available through the Legacy add-on. It also expands security coverage beyond the main repository to thousand of packages in the Universe repository.

There are three ways to get Ubuntu Pro on AWS:

1. Launch a fresh instance of Ubuntu Pro from the AWS Marketplace or EC2 console, ready to use with a pay-as-you-go pricing model.
2. Upgrade an existing instance to Ubuntu Pro using AWS License Manager.
3. Attach an Ubuntu Pro token to any running Ubuntu LTS instance.

This how-to covers the second option: Upgrading to Ubuntu Pro using `AWS License Manager`_.


Requirements
------------

* The EC2 instances to be upgraded have to be Ubuntu 16.04 LTS or later
* The instances must be managed by `AWS Systems Manager`_ (SSM)
    * To check if your instances are managed by SSM, in the `SSM console`_, check if they appear as managed nodes under :guilabel:`Systems Manager` > :guilabel:`Node Management` > :guilabel:`Fleet Manager` > :guilabel:`Managed nodes`
    * If they don't, follow the `AWS instructions for configuring your instance permissions`_ or refer to this tutorial on `enabling AWS SSM`_ to create an IAM role and access your instances with SSM
    * If the role has been recently enabled, you may need to either restart the instance or the SSM agent by running:

    .. code::
        
        sudo snap restart amazon-ssm-agent

* You'll need the latest pro client tool, install it by running:

.. code::
    
    sudo apt install ubuntu-advantage-tools

* If you have a custom LTS image which hasn't run ``cloud-init`` for the first time in AWS, you'll need to run ``sudo cloud-init clean`` and reboot for the Pro commands to work correctly.

* To give the required network access to your instances, refer to the Ubuntu Pro related `network requirements`_ and `proxy configuration`_



Upgrade to Ubuntu Pro
---------------------

Once you have checked all the requirements from the previous section, go to the `EC2 dashboard`_ and **stop all the instances** that you would like to upgrade. Running instances cannot be selected for an upgrade in the `AWS License Manager`.

* Go to :guilabel:`AWS License Manager` > :guilabel:`License type conversion` and select :guilabel:`Create license type conversion` on the right corner.

* Select :guilabel:`Ubuntu LTS` as the source operating system and from the list of available instances, select all the instances that you want to upgrade.


* Choose :guilabel:`Ubuntu Pro License Manager Upgrade (x86/Arm)` as the target :guilabel:`License type destination` (Note: This option upgrades you to Ubuntu Pro as a Marketplace subscription, so you can opt-in later to volume discount and Private Offers. Selecting :guilabel:`Ubuntu Pro` as a destination license will also upgrade you to Ubuntu Pro, but as an EC2 license.

* Select :guilabel:`Convert` after reviewing the selected instances and license type.

The conversion can take a few minutes. Once done the conversion status will show ``Success`` in the `AWS License Manager`_ console. You can also verify the upgrade by logging into one of the instances and running:

.. code::
    
    pro status



.. _`Ubuntu Pro`: https://ubuntu.com/pro
.. _`AWS License Manager`: https://aws.amazon.com/license-manager/
.. _`AWS Systems Manager`: https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html
.. _`SSM console`: https://console.aws.amazon.com/systems-manager/
.. _`AWS instructions for configuring your instance permissions`: https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-instance-permissions.html
.. _`enabling AWS SSM`: https://ubuntu.com/tutorials/how-to-use-aws-ssm-session-manager-for-accessing-ubuntu-pro-instances
.. _`network requirements`: https://documentation.ubuntu.com/pro-client/en/latest/references/network_requirements/
.. _`proxy configuration`: https://documentation.ubuntu.com/pro-client/en/latest/howtoguides/configure_proxies/
.. _`EC2 dashboard`: https://console.aws.amazon.com/ec2/

