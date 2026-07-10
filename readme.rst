Ubuntu cloud documentation
==========================

Documentation for Ubuntu on public clouds. This documentation is composed of eight related documentation sets. The first one is for content related to public clouds in general and includes links to the remaining seven. Five of the remaining seven pertain to different cloud partners (AWS, Azure, IBM, Google cloud and Oracle cloud). The sixth one is about container (OCI) registries and the last one about the different types of publicly available Ubuntu images.

Each documentation set is currently published to a different location:

* https://ubuntu.com/cloud/public-cloud/docs/
* https://ubuntu.com/aws/docs/
* https://ubuntu.com/azure/docs/
* https://ubuntu.com/gcp/docs/
* https://ubuntu.com/docs/ibm/
* https://ubuntu.com/docs/oci-registries/
* https://ubuntu.com/docs/oracle/
* https://ubuntu.com/docs/public-images/
* https://documentation.ubuntu.com/vmware/


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

The different projects that can be specfied are 'all-clouds', 'aws', 'azure', 'google', 'ibm', 'oracle', 'oci', 'public-images' and 'vmware'.

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

	make spelling

If new words are to be added to the allowed list, update ``.custom_wordlist.txt`` accordingly.


Check links
~~~~~~~~~~~

Run a check for broken links::

	PROJECT=google make linkcheck


Per project contribution guidelines
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Each project has its own contribution guide: 
* `All-clouds <https://ubuntu.com/cloud/public-cloud/docs/all-clouds-how-to/contribute-to-these-docs/>`_
* `AWS <https://ubuntu.com/aws/docs/aws-how-to/contribute-to-these-docs/>`_
* `Azure <https://ubuntu.com/azure/docs/azure-how-to/contribute-to-these-docs/>`_
* `Google <https://ubuntu.com/gcp/docs/google-how-to/contribute-to-these-docs/>`_
* `IBM <https://ubuntu.com/docs/ibm/ibm-how-to/contribute-to-these-docs/>`_
* `OCI container registries <https://ubuntu.com/docs/oci-registries/oci-how-to/contribute-to-these-docs/>`_
* `Oracle <https://ubuntu.com/docs/oracle/oracle-how-to/contribute-to-these-docs/>`_
* `Public Images <https://ubuntu.com/docs/public-images/public-images-how-to/contribute-to-these-docs/>`_
* `VMware <https://documentation.ubuntu.com/vmware/vmware-how-to/contribute-to-these-docs/>`_
