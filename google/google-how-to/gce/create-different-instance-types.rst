Create different instance types on GCP
======================================

The procedure for creating different instance types on GCP basically boils down to choosing the correct options on your google console. Some specific examples are given below.


.. _create-lts-on-gcp:

Create an Ubuntu LTS instance
-----------------------------

On your Google Cloud console, while creating a new instance from :guilabel:`Compute Engine` > :guilabel:`VM instances`> :guilabel:`CREATE INSTANCE`:

* select ``Ubuntu`` and ``Ubuntu 22.04 LTS`` in :guilabel:`Boot disk` > :guilabel:`CHANGE` > :guilabel:`Operating system` and :guilabel:`Version`


.. _create-pro-on-gcp:

Create an Ubuntu Pro instance
-----------------------------

On your Google Cloud console, while creating a new instance from :guilabel:`Compute Engine` > :guilabel:`VM instances`> :guilabel:`CREATE INSTANCE`:

* select ``Ubuntu Pro`` and ``Ubuntu 22.04 LTS Pro Server`` in :guilabel:`Boot disk` > :guilabel:`CHANGE` > :guilabel:`Operating system` and :guilabel:`Version`

Once the instance is up, ssh into it and run

.. code::

   pro status

to check that ``livepatch``, ``esm-apps`` and ``esm-infra`` are enabled.


.. _create-pro-fips-on-gcp:

Create an Ubuntu Pro FIPS instance
----------------------------------

On your Google Cloud console, while creating a new instance from :guilabel:`Compute Engine` > :guilabel:`VM instances`> :guilabel:`CREATE INSTANCE`:

* select ``Ubuntu Pro`` and ``Ubuntu 20.04 LTS Pro FIPS Server`` in :guilabel:`Boot disk` > :guilabel:`CHANGE` > :guilabel:`Operating system` and :guilabel:`Version`

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
* choose an ARM compatible OS and version, say ``Ubuntu`` and ``Ubuntu 22.04 LTS Minimal`` in :guilabel:`Boot disk` > :guilabel:`CHANGE` > :guilabel:`Operating system` and :guilabel:`Version` 


.. _create-amd-sev-conf-compute-on-gcp:

Create an AMD SEV based confidential computing VM 
--------------------------------------------------

On your Google Cloud console, while creating a new instance from :guilabel:`Compute Engine` > :guilabel:`VM instances`> :guilabel:`CREATE INSTANCE`:

* select :guilabel:`Confidential VM service` > :guilabel:`ENABLE`

It'll show you the available machine type - ``n2d-standard-2`` and boot disk image - ``Ubuntu 20.04 LTS``. Select :guilabel:`ENABLE` again and the changes will be reflected under the :guilabel:`Machine configuration` and :guilabel:`Boot disk` sections. However, we need to change the disk image to one with Pro FIPS:

* Go to :guilabel:`Boot disk` > :guilabel:`CHANGE` > :guilabel:`Confidential Images` and filter using 'ubuntu' to select ``Ubuntu 20.04 LTS Pro FIPS Server``. Select that and create the instance.

To check that confidential computing has been enabled correctly, once the instance is up, ssh into it and run

.. code::
   
   dmesg | grep SEV

A statement containing: ``AMD Secure Encryption Virtulization (SEV) active`` should be displayed. 

Back on the google console, open the instance details and go to :guilabel:`Logs` > :guilabel:`Logging`. In the list of logs, look for one that mentions ``sevLaunchAttestationReportEvent`` and expand it. In the resulting JSON, check that the field ``integrityEvaluationPassed`` is set to ``true``, under ``sevLaunchAttestationReportEvent``, something like:

.. code::

   insertId: "0",
   jsonPayload: {
      @type: "type.googleapis.com/cloud_integrity.IntegrityEvent",
      bootCounter: "0",
      sevLaunchAttestationReportEvent: {
         integrityEvaluationPassed: true
         sevPolicy: {0}
         [...]         


.. _create-intel-tdx-conf-compute-on-gcp:

Create an Intel® TDX based confidential computing VM 
-----------------------------------------------------

In GCE, Intel® TDX is supported in the `C3 machine series`_ since they use the 4th Gen Intel® Xeon CPUs. To create the VM, in the Google Cloud CLI, use the ``instances create`` command with ``confidential-compute-type=TDX``:

.. code::

   gcloud alpha compute instances create INSTANCE_NAME \
      --machine-type MACHINE_TYPE --zone us-central1-a \
      --confidential-compute-type=TDX \
      --on-host-maintenance=TERMINATE \
      --image-family=IMAGE_FAMILY_NAME \
      --image-project=IMAGE_PROJECT \
      --project PROJECT_NAME

where:

* MACHINE_TYPE: is the C3 machine type to use and 
* IMAGE_FAMILY_NAME: is the name of the confidential VM supported image family to use, such as Ubuntu 22.04 LTS, Ubuntu 24.04 LTS or Ubuntu 24.04 LTS Pro Server


.. _`C3 machine series`: https://cloud.google.com/compute/docs/general-purpose-machines#c3_series
