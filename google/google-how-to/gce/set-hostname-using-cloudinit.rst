Set hostname of GCE instances
=============================

The hostname of GCE instances can be set using multiple methods. Google's preferred method is to use its DHCP service, which requires you to choose a fully qualified DNS name (FQDN), e.g. something like test123.test.com. If you don't want an FQDN or if you want to use a consistent method for assigning hostnames across clouds, you can use a set-up tool like cloud-init to set your hostname.

Both these methods are described here. Also, due to a recent hostname-related update on GCP, you might have to make some additional changes for GCE images that use Ubuntu 24.04 LTS and later. These are explained at the end.


Using DHCP (Google's preferred method)
--------------------------------------

By default, Google's DHCP service sets the hostname to an automatically generated internal DNS name. 

To set your own custom name, follow the instructions given in `Create a VM instance with a custom hostname`_. In this case, the DHCP service will additionally provide the custom name and will prioritize it to be the default hostname. However, as mentioned earlier, the custom name needs to be an FQDN.


Using cloud-init
----------------

cloud-init uses the ``hostname`` command to programmatically set the hostname. You need to configure its metadata with the required hostname and use the `gcloud compute instances add-metadata`_ command:

.. code::

    gcloud compute instances add-metadata INSTANCE_NAME --metadata-from-file=KEY=VALUE

Here INSTANCE_NAME is your VM name and the metadata is specified using a KEY=VALUE pair. For instance, the metadata could be specified as 'user-data=FILENAME', where FILENAME is the local path to a file that contains the desired cloud-init configurations. Include the desired hostname in that user-data file:

.. code:: 

    #cloud-config

    hostname: test123

For more details about this, see `Set Hostname`_ in the cloud-init documentation. 


Changes based on new defaults (Ubuntu 24.04+)
---------------------------------------------

In GCE images that use Ubuntu 24.04 LTS or later, the ``/etc/hostname`` file is no longer present by default, and the cloud-init key ``create_hostname_file`` is set to false. 

Implications for using cloud-init
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Due to the way the underlying ``hostname`` command works, whenever a user or tool (such as cloud-init) tries to set the hostname on a system without ``/etc/hostname``, it will only be set transiently and will be overwritten by Google's DHCP service. To avoid this, you'll need to set ``create_hostname_file`` to true in the user-data file:

.. code::

    #cloud-config

    hostname: test123
    create_hostname_file: true

By setting ``create_hostname_file`` to true, you ensure two things: 

#. cloud-init will create the ``/etc/hostname`` file on boot (if it does not already exist) 
#. hostname will be statically set to the one specified in the user-data file


Creating consistent multi-VM environments across releases
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Another scenario where this new default can create inconsistencies is in the case of a server farm with images spanning the Ubuntu 24.04 LTS boundary (i.e. both 24.04+ and 23.10-). In this case, if you want a consistent file system layout and hostname style across all images, then you'll have to either remove the ``/etc/hostname`` file from the earlier versions or add it to the later versions.


Remove ``/etc/hostname`` from Ubuntu 23.10 and earlier
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set the cloud-init key ``create_hostname_file`` to false and ensure that ``/etc/hostname`` is deleted during or after first boot. So the user-data file will need:  

.. code::

    #cloud-config

    create_hostname_file: false


Add ``/etc/hostname`` to Ubuntu 24.04 LTS and later
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Set the cloud-init key ``create_hostname_file`` to true in the user-data file:  

.. code::

    #cloud-config

    hostname: test123
    create_hostname_file: true


.. _`Create a VM instance with a custom hostname`: https://cloud.google.com/compute/docs/instances/custom-hostname-vm
.. _`gcloud compute instances add-metadata`: https://cloud.google.com/sdk/gcloud/reference/compute/instances/add-metadata
.. _`Set Hostname`: https://cloudinit.readthedocs.io/en/latest/reference/modules.html#set-hostname
