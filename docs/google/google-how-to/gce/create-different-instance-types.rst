Create different instance types on GCP
======================================

The procedure for creating different instance types on GCP basically boils down to choosing the correct options on your google console. Some specific examples are given below.


.. _create-lts-on-gcp:

Create an Ubuntu LTS instance
-----------------------------

On your Google Cloud console, while creating a new instance from :guilabel:`Compute Engine` > :guilabel:`VM instances`> :guilabel:`CREATE INSTANCE`:

* in the :guilabel:`OS and storage` tab, select ``Ubuntu`` and ``Ubuntu 24.04 LTS`` in :guilabel:`Operating system and storage` > :guilabel:`CHANGE` > :guilabel:`Operating system` and :guilabel:`Version`


.. _create-pro-on-gcp:

Create an Ubuntu Pro instance
-----------------------------

On your Google Cloud console, while creating a new instance from :guilabel:`Compute Engine` > :guilabel:`VM instances`> :guilabel:`CREATE INSTANCE`:

* in the :guilabel:`OS and storage` tab, select ``Ubuntu Pro`` and ``Ubuntu 24.04 LTS Pro Server`` in :guilabel:`Operating system and storage` > :guilabel:`CHANGE` > :guilabel:`Operating system` and :guilabel:`Version`

Once the instance is up, ssh into it and run

.. code::

   pro status

to check that ``livepatch``, ``esm-apps`` and ``esm-infra`` are enabled.


.. _create-pro-fips-on-gcp:

Create an Ubuntu Pro FIPS instance
----------------------------------

On your Google Cloud console, while creating a new instance from :guilabel:`Compute Engine` > :guilabel:`VM instances`> :guilabel:`CREATE INSTANCE`:

* in the :guilabel:`OS and storage` tab, select ``Ubuntu Pro`` and ``Ubuntu 20.04 LTS Pro FIPS Updates Server`` in :guilabel:`Operating system and storage` > :guilabel:`CHANGE` > :guilabel:`Operating system` and :guilabel:`Version`

Once the instance is up, ssh into it and run

.. code::

   uname -r

The kernel version will include ``fips`` in the name. To check the FIPS packages, run:

.. code::

   dpkg-query -l | grep fips

It should show you a long list of packages with ``fips`` in the name or version.


.. _create-arm-on-gcp:

Create an ARM-based instance
----------------------------

On your Google Cloud console, while creating a new instance from :guilabel:`Compute Engine` > :guilabel:`VM instances`> :guilabel:`CREATE INSTANCE`:

* choose the ARM CPU platform ``T2A`` in :guilabel:`Machine configuration` > :guilabel:`Series`
* choose an ARM compatible OS and version, say ``Ubuntu`` and ``Ubuntu 24.04 LTS Minimal`` in :guilabel:`OS and storage` > :guilabel:`Operating system and storage` > :guilabel:`CHANGE` > :guilabel:`Operating system` and :guilabel:`Version` 


.. _create-amd-sev-conf-compute-on-gcp:

Create an AMD SEV based confidential computing VM 
--------------------------------------------------

On your Google Cloud console, while creating a new instance from :guilabel:`Compute Engine` > :guilabel:`VM instances`> :guilabel:`CREATE INSTANCE`:

* In the :guilabel:`Security` section, select :guilabel:`Confidential VM service` > :guilabel:`ENABLE`

Choose one of ``AMD SEV`` or ``AMD SEV-SNP`` in the service type and confirm the selection. The latest compatible Ubuntu LTS image will be selected automatically.



.. _create-intel-tdx-conf-compute-on-gcp:

Create an Intel® TDX based confidential computing VM 
-----------------------------------------------------

On your Google Cloud console, while creating a new instance from :guilabel:`Compute Engine` > :guilabel:`VM instances`> :guilabel:`CREATE INSTANCE`:

* In the :guilabel:`Security` section, select :guilabel:`Confidential VM service` > :guilabel:`ENABLE`

Choose one of ``Intel TDX`` in the service type and confirm the selection. The latest compatible Ubuntu LTS image will be selected automatically.

Optionally, you can also use the Google Cloud CLI to create the VM. Use the ``instances create`` command with ``confidential-compute-type=TDX`` and a machine type chosen from the `C3 machine series`_ since they use the 4th Gen Intel® Xeon CPUs.

.. code::

   gcloud compute instances create INSTANCE_NAME \
    --machine-type=c3-standard-4 \
    --zone=us-central1-a \
    --confidential-compute-type=TDX \
    --maintenance-policy=TERMINATE \
    --image-family=ubuntu-2404-lts-amd64 \
    --image-project=ubuntu-os-cloud

where:

* INSTANCE_NAME: is the name of the instance to create and
* ``image-family`` can be set to a supported image family, such as ``ubuntu-2204-lts`` or ``ubuntu-2404-lts-amd64``.

.. _create-accelerator-on-gcp:

Create an Accelerator (GPU) instance
------------------------------------

On your Google Cloud console, while creating a new instance from :guilabel:`Compute Engine` > :guilabel:`VM instances` > :guilabel:`CREATE INSTANCE`:

* select a GPU type and the number of GPUs that match your workload in :guilabel:`GPUs` tab
* select a machine type that matches your vCPUs and memory needs, or choose :guilabel:`Custom` to set them manually
* go to :guilabel:`OS and storage` > :guilabel:`Change`, then in :guilabel:`Public images` select the **Ubuntu Accelerator Optimized** operating system and choose an image such as ``Ubuntu 24.04 LTS NVIDIA 580``

Optionally, you can also use the Google Cloud CLI to create a GPU-enabled VM. Use the ``instances create`` command with the ``--accelerator`` flag and a compatible machine type.

.. code::
   
   gcloud compute instances create INSTANCE_NAME \
    --zone=ZONE \
    --machine-type=n1-standard-4 \
    --accelerator=type=nvidia-tesla-t4,count=1 \
    --maintenance-policy=TERMINATE \
    --image=ubuntu-accelerator-2404-amd64-with-nvidia-580-vYYYYMMDD \
    --image-project=ubuntu-os-accelerator-images

where:

* INSTANCE_NAME: is the name of the instance to create and
* ``--accelerator`` specifies the GPU type and count for the instance.

For details on supported GPU types and host machine series, see `Accelerator-optimized machine types`_.

.. _`C3 machine series`: https://cloud.google.com/compute/docs/general-purpose-machines#c3_series
.. _`Accelerator-optimized machine types`: https://cloud.google.com/compute/docs/accelerator-optimized-machines
