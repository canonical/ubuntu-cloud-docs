Automatically configure multiple NICs on EC2 instances
======================================================

Ubuntu instances running on AWS can be configured to automatically configure source routing on multiple NICs via cloud-init, starting with `v24.1`_, on different `events`_, as:

* First boot (enabled by default)
* Subsequent boots
* Hotplug NIC additions and removals

.. note::

   On Ubuntu Noble and newer, hot-plugged NICs are configured by default.

Enable network configuration events
-----------------------------------

To enable network configuration on additional `events`_, one can add supplemental cloud-init user-data at instance creation time:

..  code-block:: yaml

    #cloud-config
    # apply network config on every hotplug event
    updates:
      network:
        when: ['hotplug']

To specify multiple events use:

..  code-block:: yaml

    #cloud-config
    # apply network config on every boot and hotplug event
    updates:
      network:
        when: ['boot', 'hotplug']

To learn more about configuring instances using cloud-init, refer to `cloud-init documentation`_ and `EC2 datasource`_.

Enable hotplug network configuration on running instances
---------------------------------------------------------

To enable network configuration on hotplug events on already running instances, execute the following command in the instance:

.. code-block::

    $ cloud-init devel hotplug-hook -s net enable

This is a last resort command for administrators to enable hotplug in running instances.
The recommended method to enable this is using user-data while creating the instance as described previously.
For more information about this command, see `cloud-init's CLI documentation`_.

.. _`events`: https://cloudinit.readthedocs.io/en/latest/explanation/events.html
.. _`cloud-init's CLI documentation`: https://docs.cloud-init.io/en/latest/reference/cli.html
.. _`v24.1`: https://github.com/canonical/cloud-init/releases/tag/24.1
.. _`cloud-init documentation`: https://docs.cloud-init.io
.. _`EC2 datasource`: https://docs.cloud-init.io/en/latest/reference/datasources/ec2.html
