Ubuntu cloud documentation
==========================

Documentation for Ubuntu on public clouds. This documentation is composed of eight related documentation sets. The first one is for content related to public clouds in general and includes links to the remaining seven. Five of the remaining seven pertain to different cloud partners (AWS, Azure, IBM, Google cloud and Oracle cloud). The sixth one is about container (OCI) registries and the last one about the different types of publicly available Ubuntu images.

Each documentation set is currently published to a different location:

* https://documentation.ubuntu.com/public-cloud/
* https://documentation.ubuntu.com/aws/
* https://documentation.ubuntu.com/azure/
* https://documentation.ubuntu.com/gcp/
* https://canonical-ibm.readthedocs-hosted.com/
* https://documentation.ubuntu.com/oci-registries/
* https://canonical-oracle.readthedocs-hosted.com/
* https://documentation.ubuntu.com/public-images/


How to work with this documentation
-----------------------------------

Download and install
~~~~~~~~~~~~~~~~~~~~
Fork and clone this repository.

Once cloned, run::

	cd docs
	make install

This invokes the ``install`` command from the ``Makefile``, which creates a
virtual environment (``.sphinx/venv``) and installs all the dependencies specified in
``docs/requirements.txt``.


Build and serve the documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``make run`` command can be used to start the ``sphinx-autobuild`` documentation server.
Since each cloud has it's own separate documentation set, you have to specify the required cloud name as a command line parameter. For example the command below will build and serve the documentation for AWS cloud::

	PROJECT=aws make run

The different projects that can be specfied are 'all-clouds', 'aws', 'azure', 'google', 'ibm', 'oracle', 'oci' and 'public-images'.

The documentation will be available at `127.0.0.1:8000 <http://127.0.0.1:8000>`_ or equivalently at `localhost:8000 <http://localhost:8000>`_.

The command:

* activates the virtual environment and serves the documentation
* rebuilds the documentation each time you save a file
* sends a reload page signal to the browser when the documentation is rebuilt

(This is the most convenient way to work on the documentation, but you can still use
the more standard ``make html``. For instance, ``PROJECT=azure make html`` will create the 
azure related html pages in _build/azure.)


Check spelling
~~~~~~~~~~~~~~

Run a spell check::

	PROJECT=azure make spelling

If new words are to be added to the allowed list, update ``.custom_wordlist.txt`` accordingly.


Check links
~~~~~~~~~~~

Run a check for broken links::

	PROJECT=google make linkcheck


Per project contribution guidelines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each project has its own contribution guide: 
* `All-clouds <https://documentation.ubuntu.com/public-cloud/all-clouds-how-to/contribute-to-these-docs/>`_
* `AWS <https://documentation.ubuntu.com/aws/aws-how-to/contribute-to-these-docs/>`_
* `Azure <https://documentation.ubuntu.com/azure/azure-how-to/contribute-to-these-docs/>`_
* `Google <https://documentation.ubuntu.com/gcp/google-how-to/contribute-to-these-docs/>`_
* `IBM <https://canonical-ibm.readthedocs-hosted.com/ibm-how-to/contribute-to-these-docs/>`_
* `OCI container registries <https://documentation.ubuntu.com/oci-registries/oci-how-to/contribute-to-these-docs/>`_
* `Oracle <https://canonical-oracle.readthedocs-hosted.com/oracle-how-to/contribute-to-these-docs/>`_
* `Public Images <https://documentation.ubuntu.com/public-images/public-images-how-to/contribute-to-these-docs/>`_
