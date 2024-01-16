Set ``hostname`` using cloud-init
=================================

One way of setting your VM's ``hostname`` is to use a set-up tool like cloud-init. The process for setting it involves `using the gcloud add-metadata command`_ to program the cloud-init metadata. Use:

.. code::

    gcloud compute instances add-metadata INSTANCE_NAME --metadata-from-file=KEY=VALUE

where INSTANCE_NAME is your VM name and the metadata is specified using a KEY=VALUE pair, e.g. user-data=FILENAME. Here FILENAME is the local path to a file that contains the desired cloud-init configurations, including the hostname:

.. code:: 

    hostname: test123

Refer to the `cloud-init documentation`_ for more details. 

This process of setting ``hostname`` using cloud-init requires slight changes based on the version of Ubuntu that your GCE image is using. Starting from Ubuntu 24.04, ``/etc/hostname`` is no longer present by default and the cloud-init key ``create_hostname_file`` is set to false. This means that the process mentioned above will not work as is and needs some tweaking. 


Set ``hostname`` in Ubuntu 24.04 and later
------------------------------------------

Using cloud-init
~~~~~~~~~~~~~~~~

To set ``hostname`` using cloud-init in 24.04+, apart from specifying the name you'll also need to set ``create_hostname_file`` to true in the user-data file:

.. code::

    hostname: test123
    create_hostname_file: true

This ensures that cloud-init will create the ``/etc/hostname`` file on boot if it does not already exist; and that the hostname will be statically set to the one specified in the user-data file.

However, this method of using cloud-init is not Google's preferred method for setting ``hostname`` in its VMs.

Using DHCP
~~~~~~~~~~

Google's preferred method for setting ``hostname`` is through its DHCP service. By default GCP sets ``hostname`` using an automatically created internal DNS name. But it is also possible for a user to specify a custom hostname. If that is done, then the DHCP service will additionally provide that custom name and will prioritise it to be the default ``hostname``.

The instructions for doing this are given in Google's documentation for `creating a VM with a custom hostname`_. The custom hostname in this case needs to be a fully qualified DNS name (FQDN), e.g. something like ``test123.test.com``, and you also need to create a corresponding DNS record for it.


Set ``hostname`` in earlier Ubuntu releases
-------------------------------------------

In Ubuntu 23.10 and earlier, if you want to set ``hostname`` using cloud-init, just specifying the desired hostname in the user-data file is enough: 

.. code:: 

    hostname: test123

The ``/etc/hostname`` file exists by default and even if it doesn't, cloud-init when run, will create it. 

However, if you want to use Google's preferred method of setting ``hostname`` through its DHCP service, just following the earlier mentioned instructions (`creating a VM with a custom hostname`_) is not enough. You'll also have to remove the ``/etc/hostname`` file and set ``create_hostname_file`` to false using the cloud-init metadata. So your user-data will now look like:  

.. code::

    hostname: test123
    create_hostname_file: false

and you'll have to ensure that ``/etc/hostname`` is deleted during or after first boot. 



.. _`using the gcloud add-metadata command`: https://cloud.google.com/sdk/gcloud/reference/compute/instances/add-metadata
.. _`cloud-init documentation`: https://cloudinit.readthedocs.io/en/latest/reference/modules.html#set-hostname
.. _`creating a VM with a custom hostname`: https://cloud.google.com/compute/docs/instances/custom-hostname-vm
