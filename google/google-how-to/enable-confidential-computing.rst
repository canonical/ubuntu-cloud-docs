Enable confidential computing
=============================

What is confidential computing?
-------------------------------

.. include:: ../../reuse/common-intro.txt
   :start-after: Start: Confidential computing
   :end-before: End: Confidential computing


Create a confidential compute enabled VM
----------------------------------------

To enable confidential computing on google cloud:

#. Log in to Google console and select :guilabel:`CREATE INSTANCE`
#. Scroll down and select :guilabel:`ENABLE` under the *Confidential VM service* option. It'll show you the machine type and OS details - an ``N2d-standard-2`` CPU and an Ubuntu 20.04 LTS Pro FIPS image. On selecting :guilabel:`ENABLE` again, the changes should be reflected under the *Machine configuration* section and the *Boot disk* section.


Verify the confidential compute features
----------------------------------------

After creation of the instance (which might take a few minutes), ssh into it and run:

.. code::

   dmesg | grep SEV | head

It should display a statement containing: ``AMD Secure Encryption Virtulization (SEV) active``.

Next, select the instance on the google console and open :guilabel:`Cloud Logging` under *Logs*. From the list of logs, expand the one for ``sevLaunchAttestationReportEvent`` and check that the field ``integrityEvaluationPassed`` is set to ``true``.

