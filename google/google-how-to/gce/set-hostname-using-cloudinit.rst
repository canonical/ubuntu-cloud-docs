Set ``hostname`` using cloud-init
=================================

One way of setting your VM's ``hostname`` is to use a set-up tool like cloud-init. The process for setting it involves `using the gcloud add-metadata command`_ to program the cloud-init metadata. Use:

.. code::

    gcloud compute instances add-metadata INSTANCE_NAME --metadata-from-file=KEY=VALUE

where INSTANCE_NAME is your VM name and the metadata is specified using a KEY=VALUE pair, e.g. user-data=FILENAME. Here FILENAME is the local path to a file that contains the desired cloud-init configurations, including the hostname:

.. code:: 

    hostname: test123

This process of setting ``hostname`` using cloud-init requires slight changes based on the version of Ubuntu that your GCE image is using. Starting from Ubuntu 24.04, ``/etc/hostname`` is no longer present by default and the cloud-init key ``create_hostname_file`` is set to false. This means that the process mentioned above will not work as is and needs some tweaking. 


Set ``hostname`` in Ubuntu 24.04 and later
------------------------------------------

Using cloud-init (24.04+)
~~~~~~~~~~~~~~~~~~~~~~~~~

To set ``hostname`` using cloud-init in 24.04+, apart from specifying the name you'll also need to set ``create_hostname_file`` to true in the user-data file:

.. code::

    hostname: test123
    create_hostname_file: true

This ensures that cloud-init will create the ``/etc/hostname`` file on boot if it does not already exist; and that the hostname will be statically set to the one specified in the user-data file.

However, this method of using cloud-init is not Google's preferred method for setting ``hostname`` in its VMs.

Using DHCP (24.04+)
~~~~~~~~~~~~~~~~~~~

Google's preferred method for setting ``hostname`` is through its DHCP service. By default GCP sets ``hostname`` using an automatically created internal DNS name. But it is also possible for a user to specify a custom hostname. If that is done, then the DHCP service will additionally provide that custom name and will prioritise it to be the default ``hostname``.

The instructions for doing this are given in Google's documentation for `creating a VM with a custom hostname`_. The custom hostname in this case needs to be a fully qualified DNS name (FQDN), e.g. something like ``test123.test.com``, and you also need to create a corresponding DNS record for it.

In Ubuntu 24.04 and later, this method of using DHCP to set ``hostname`` works by default. This is because ``/etc/hostname`` is not present and Google's DHCP service takes precedence.


Set ``hostname`` in earlier Ubuntu releases
-------------------------------------------

Using cloud-init (23.10-)
~~~~~~~~~~~~~~~~~~~~~~~~~

In Ubuntu 23.10 and earlier, ``/etc/hostname`` exists by default and even if it doesn't, cloud-init when run, will create it. So just specifying the desired hostname in the user-data file is enough to set ``hostname``:

.. code:: 

    hostname: test123


Using DHCP (23.10-)
~~~~~~~~~~~~~~~~~~~

If you have VMs with Ubuntu versions that span the 24.04 boundary, then having a single consistent behaviour across all of them would be useful. In the earlier versions you can emulate the default behaviour of 24.04+ by ensuring that the DHCP service takes precedence.

To do this, you'll have to remove the ``/etc/hostname`` file from the VM and set ``create_hostname_file`` to false. Set user-data to: 

.. code::

    hostname: test123
    create_hostname_file: false

.. [[[Question for Catherine: Do we still need to specify the hostname in this case? Or can we delete that line?]]]

and ensure that ``/etc/hostname`` is deleted during or after first boot.


.. _`using the gcloud add-metadata command`: https://cloud.google.com/sdk/gcloud/reference/compute/instances/add-metadata
.. _`creating a VM with a custom hostname`: https://cloud.google.com/compute/docs/instances/custom-hostname-vm
