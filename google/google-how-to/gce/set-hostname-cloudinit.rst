Set hostname with cloud-init on GCE
===================================

Hostnames can be set in many ways, including a user manually configuring the hostname, DHCP, and using a set-up tool like cloud-init.  On Ubuntu, most of these methods use the underlying ``hostname`` command, which sets the hostname statically if the ``/etc/hostname`` file exists and transiently if it does not.

Historically, all Ubuntu images have an ``/etc/hostname`` file and cloud-init, when run, would create an ``/etc/hostname`` file if it did not already exist.  Starting in 24.04 GCE images, the ``/etc/hostname`` file is no longer present by default and the cloud-init key ``create_hostname_file`` set to false.  This means that when a user or tool uses ``hostname`` to set the hostname, it is set transiently and trying to set the instance hostname using solely user-supplied metadata to cloud-init or manually from the command line will be overwritten by Google's DHCP service.  It is possible to set up a GCE instance with a user defined hostname which ensures Google's DHCP-supplied hostname matches the desired hostname but if that is not done, the DHCP hostname will be a random string such as ``[INTANCE-ID].c.[PROJECT].internal``.  A common programmatic way to set hostnames for machines is to use cloud-init metadata through the gcloud flag ``--metadata-from-file user-data=[FILENAME]``, where ``[FILENAME]`` contains the cloud-init configurations desired on the VMs including the hostname.  Starting in 24.04 GCE images, only passing the ``hostname`` key to cloud-init will no longer statically set the instance hostname.


To set the hostname using DHCP
------------------------------

To align the DHCP-provided hostname with the user-data provided hostname, follow Google's documentation to `Create a VM instance with a custom hostname`_.  If the hostname provided via the ``--hostname`` flag matches the hostname provided via ``--metadata-from-file user-data`` then the instance will have the correct hostname set both before and after 24.04.  This is Google's preferred method for setting hostnames.


To set the hostname using user-data in GCE images 24.04 and later
-----------------------------------------------------------------

To continue the historical behaviour (allowing the user-data provided hostname to be set statically), append the cloud-init key ``create_hostname_file`` set to true to the user-data that contains the hostname.  This ensures that cloud-init will write the ``/etc/hostname`` file on boot if it does not exist and all subsequent hostname setting will be static, ensuring random DHCP names do not overwrite the user-configured hostname.

Where previously the following user-data:

.. code::

  hostname: test123

would successfully set the hostname, after 24.04 and later images require:

.. code::

  hostname: test123
  create_hostname_file: true


To use a DHCP-supplied hostname on GCE images 23.10 and earlier
---------------------------------------------------------------

To ensure an image earlier than 24.04 follows the new GCE default of only setting hostnames transiently, ``/etc/hostname`` must be removed from the machine and the cloud-init key ``create_hostname_file`` must be set to false.

To create the 24.04+ behaviour on earlier images, change user-data of:

.. code::

  hostname: test123

to:

.. code::

  hostname: test123
  create_hostname_file: false

and ensure the ``/etc/hostname`` file is deleted on the instance during or after first boot.


.. _`Create a VM instance with a custom hostname`: https://cloud.google.com/compute/docs/instances/custom-hostname-vm
