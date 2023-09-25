Create different instance types on GCP
======================================

The procedure for creating different instance types on GCP basically boils down to choosing the correct options on your google console. Some specific examples are given below.


Create and Ubuntu Pro 22.04 instance
------------------------------------

On your google console, while creating a new instance from :guilabel:`Compute Engine` > :guilabel:`VM instances`> :guilabel:`CREATE INSTANCE`:

* select ``Ubuntu Pro`` and ``Ubuntu 22.04 Pro Server`` in :guilabel:`Boot disk` > :guilabel:`CHANGE` > :guilabel:`Operating system` and :guilabel:`Version`

Once the instance is up, ssh into it and run

.. code::

   ua status

to check that ``livepatch``, ``esm-apps`` and ``esm-infra`` are enabled.



Create an ARM-based instance
----------------------------

On your google console, while creating a new instance from :guilabel:`Compute Engine` > :guilabel:`VM instances`> :guilabel:`CREATE INSTANCE`:

* choose the ARM CPU platform ``T2A`` in :guilabel:`Machine configuration` > :guilabel:`Series`
* choose an ARM compatible OS and version, say ``Ubuntu`` and ``Ubuntu 22.04 LTS Minimal`` in :guilabel:`Boot disk` > :guilabel:`CHANGE` > :guilabel:`Operating system` and :guilabel:`Version` 



Create a confidential compute enabled VM
----------------------------------------

On your google console, while creating a new instance from :guilabel:`Compute Engine` > :guilabel:`VM instances`> :guilabel:`CREATE INSTANCE`:

* select :guilabel:`Confidential VM service` > :guilabel:`ENABLE`

It'll show you the available machine type - ``N2d-standard-2`` and OS image - ``Ubuntu 20.04 LTS Pro FIPS Server``. On selecting :guilabel:`ENABLE` again, the changes will be reflected under the :guilabel:`Machine configuration` and :guilabel:`Boot disk` sections.

To check that confidential computing has been enabled correctly, once the instance is up, ssh into it and run

.. code::
   
   dmesg | grep SEV | head

A statement containing: ``AMD Secure Encryption Virtulization (SEV) active`` should be displayed. 

Back on the google console, select the instance and open :guilabel:`Logs` > :guilabel:`Cloud Logging`. From the list of logs, expand the one for ``sevLaunchAttestationReportEvent`` and check that the field ``integrityEvaluationPassed`` is set to ``true``.


