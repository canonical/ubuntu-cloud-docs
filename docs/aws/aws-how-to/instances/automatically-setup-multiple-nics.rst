.. meta::
   :description: Learn how to automatically configure multiple network interfaces on EC2. Includes steps for enabling configuration during instance creation and on running instances.

.. _automatically-setup-multiple-nics:

Automatically configure multiple NICs on EC2 instances
======================================================

Ubuntu instances running on AWS can be set up to automatically configure source routing on multiple NICs via cloud-init (starting with `cloud-init v24.1`_). The configuration can be set up to occur on different events, such as:

* First boot (enabled by default)
* Subsequent boots
* Hotplug NIC additions and removals

.. note::

   On Ubuntu 24.04 LTS and newer, hot-plugged NICs are configured by default.


Enable configuration during instance creation
---------------------------------------------

To enable network configuration on additional `events`_, you can add supplemental cloud-init user-data at instance creation time. For example, the following command applies network configuration on every hotplug event:

..  code-block:: yaml

    updates:
      network:
        when: ['hotplug']

You can also specify multiple events to configure at once. For example, the following command applies network configuration on every boot and hotplug event:

..  code-block:: yaml

    #cloud-config
    # apply network config on every boot and hotplug event
    updates:
      network:
        when: ['boot', 'hotplug']

To learn more about configuring instances using cloud-init, refer to `cloud-init datasources`_ and `EC2 as a cloud-init datasource`_.


Enable configuration on running instances
-----------------------------------------

To enable network configuration on hotplug events for already running instances, execute the following command on the instance:

.. code-block::

    cloud-init devel hotplug-hook -s net enable

This is a last resort command for administrators to enable hotplug on running instances.
The recommended method to enable this is using user-data while creating the instance as described in the previous section. For more information about this command, see `cloud-init's CLI documentation`_.


.. _`cloud-init v24.1`: https://github.com/canonical/cloud-init/releases/tag/24.1
.. _`events`: https://docs.cloud-init.io/en/latest/explanation/events.html
.. _`cloud-init datasources`: https://docs.cloud-init.io/en/latest/reference/datasources.html
.. _`EC2 as a cloud-init datasource`: https://docs.cloud-init.io/en/latest/reference/datasources/ec2.html
.. _`cloud-init's CLI documentation`: https://docs.cloud-init.io/en/latest/reference/cli.html
