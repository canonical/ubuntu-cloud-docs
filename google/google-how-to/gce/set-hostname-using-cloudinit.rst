Set hostname of GCE instances
=================================

The hostname of GCE instances can be set using multiple methods. Apart from setting it manually, one option is to use a set-up tool like cloud-init, while Google's preferred method is to use its DHCP service. Both these options are considered here.

.. _use_cloud-init:

Option 1: Use cloud-init
------------------------

You can set the required hostname by programming the cloud-init metadata. For this, use the `gcloud compute instances add-metadata`_ command:

.. code::

    gcloud compute instances add-metadata INSTANCE_NAME --metadata-from-file=KEY=VALUE

Here INSTANCE_NAME is your VM name and the metadata is specified using a KEY=VALUE pair, e.g. user-data=FILENAME, where FILENAME is the local path to a file that contains the desired cloud-init configurations (including the hostname). Specify the required hostname in the user-data file:

.. code:: 

    hostname: test123

For more details about this, see `Set Hostname`_ in the cloud-init documentation. 


Additional change needed for Ubuntu 24.04 and later
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In GCE images that use Ubuntu 24.04 (or later), the ``/etc/hostname`` file is no longer present by default, and the cloud-init key ``create_hostname_file`` is set to false. This implies that whenever a user or tool (such as cloud-init) tries to set the hostname using the underlying ``hostname`` command, it will fail and the hostname will be overwritten by Google's DHCP service. 

To avoid this failure, you'll need to set ``create_hostname_file`` to true in the user-data file (apart from specifying the required hostname):

.. code::

    hostname: test123
    create_hostname_file: true

By setting ``create_hostname_file`` to true, you ensure that cloud-init will create the ``/etc/hostname`` file on boot if it does not already exist; and that the hostname will be statically set to the one specified in the user-data file.


Option 2: Use DHCP (Google's preferred method)
----------------------------------------------

Google's preferred method of setting hostname is through its DHCP service. The hostname is set to an automatically generated internal DNS name by default. 

If you want your own custom name, you can follow the instructions given in `Create a VM instance with a custom hostname`_. In this case, the DHCP service will additionally provide the custom name and will prioritise it to be the default hostname. However, the custom name needs to be a fully qualified DNS name, e.g. something like test123.test.com, and you also need to create a corresponding DNS record for it. 

If you need the hostname to be in a different format, you can use cloud-init for setting it, as described in the :ref:`previous section <use_cloud-init>`.


Additional change needed for Ubuntu 23.10 and earlier
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to ensure that GCE images that use Ubuntu 23.10 (or earlier) follow the new GCE default of only setting hostnames through DHCP, then the existing ``/etc/hostname`` must be removed and the cloud-init key ``create_hostname_file`` must be set to false. So your user-data file will now need:  

.. code::

    create_hostname_file: false

and you'll have to ensure that ``/etc/hostname`` is deleted during or after first boot. 

.. _`gcloud compute instances add-metadata`: https://cloud.google.com/sdk/gcloud/reference/compute/instances/add-metadata
.. _`Set Hostname`: https://cloudinit.readthedocs.io/en/latest/reference/modules.html#set-hostname
.. _`Create a VM instance with a custom hostname`: https://cloud.google.com/compute/docs/instances/custom-hostname-vm
