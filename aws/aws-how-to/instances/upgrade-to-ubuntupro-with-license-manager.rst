Upgrade Ubuntu instances to Ubuntu Pro with AWS License Manager
===============================================================


AWS released a functionality that allows users upgrade Ubuntu LTS instances to `Ubuntu Pro`_ with `AWS License Manager`_.


Requirements
------------

To upgrade to Ubuntu Pro, you will need

* Ubuntu LTS EC2 instances 16.04 or later LTS versions
* EC2 instances managed by `AWS Systems Manager`_ (SSM)
    * Follow `AWS Official SSM Manager document`_, `Enabling AWS SSM video tutorial`_ or `step-by-step tutorial`_ to create IAM role and access instances with SSM
    * To check if instances are managed by SSM, go to the `SSM console`_ and check if the instances to be upgraded appear in :guilabel:`Systems Manager` > :guilabel:`Fleet Manager` > :guilabel:`Managed nodes`.
    * You may need to either restart the instance or directly the SSM agent by running ``sudo snap restart amazon-ssm-agent`` to reactivate
* Install latest pro client tool by running ``sudo apt install ubuntu-advantage-tools``
* Check with `network requirements`_ and `proxy configuration`_ for Ubuntu Pro to give network access to instances.


Upgrade to Ubuntu Pro
---------------------

Once you checked all requirements in previous section, go to `EC2 dashboard`_ and stopped all the instances you would like to upgrade. Running instances are not able to be selected to upgrade in :guilabel:`AWS License Manager`.

* Go to :guilabel:`AWS License Manager` > :guilabel:`License type conversion` and click :guilabel:`Create license type conversion` on the right corner.

* Select :guilabel:`Ubuntu LTS` from drop-down menu and check instances you want to upgrade to Pro.

* Select Ubuntu Pro for :guilabel:`License type destination`.

* Review selected instances and license type and click :guilabel:`Convert`.

* Converting to Ubuntu Pro can take some time and you can check status `AWS License Manager`_ console. And conversion status will be changed to ``success``.

* You can also verify the upgrade by logging into one of the instances and run ``pro status``.


.. _`AWS License Manager`: https://aws.amazon.com/license-manager/
.. _`Ubuntu Pro`: https://ubuntu.com/pro
.. _`AWS Systems Manager`: https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html
.. _`AWS Official SSM Manager document`: https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-instance-permissions.html
.. _`Enabling AWS SSM video tutorial`: https://www.youtube.com/watch?v=3sjrJsT28Uw
.. _`step-by-step tutorial`: https://ubuntu.com/tutorials/how-to-use-aws-ssm-session-manager-for-accessing-ubuntu-pro-instances#1-overview
.. _`SSM console`: https://console.aws.amazon.com/systems-manager/
.. _`network requirements`: https://canonical-ubuntu-pro-client.readthedocs-hosted.com/en/latest/references/network_requirements/
.. _`proxy configuration`: https://canonical-ubuntu-pro-client.readthedocs-hosted.com/en/latest/howtoguides/configure_proxies/
.. _`EC2 dashboard`: https://console.aws.amazon.com/ec2/

