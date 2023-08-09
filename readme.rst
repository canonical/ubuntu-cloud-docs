Ubuntu cloud documentation
==========================

Documentation for Ubuntu on public clouds. This documentation is composed of six related documentation sets. Five of them pertain to different cloud partners (AWS, Azure, IBM, Google cloud and Oracle cloud), while the sixth one is for OCI registries.

The documentation is currently published to six different locations:

* https://canonical-aws.readthedocs-hosted.com/
* https://canonical-azure.readthedocs-hosted.com/
* https://canonical-gcp.readthedocs-hosted.com/
* https://canonical-ibm.readthedocs-hosted.com/
* https://canonical-oci.readthedocs-hosted.com/
* https://canonical-oracle.readthedocs-hosted.com/


How to work with this documentation
-----------------------------------

Download and install
~~~~~~~~~~~~~~~~~~~~
Fork and clone this repository.

Once cloned, run::

	make install

This invokes the ``install`` command in the ``Makefile``, and creates a
virtual environment (``.sphinx/venv``) and installs dependencies in
``.sphinx/requirements.txt``.

A complete set of pinned, known-working dependencies is included in
``.sphinx/pinned-requirements.txt``.


Build and serve the documentation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The ``make run`` command can be used to start the ``sphinx-autobuild`` documentation server.
Since each cloud has it's own separate documentation set, you have to specify the required cloud name as a command line parameter. For example the command below will build and serve the documentation for AWS cloud::

	PROJECT=aws make run

The different projects that can be specfied are 'aws', 'azure', 'google', 'ibm', 'oracle' and 'oci'.

The documentation will be available at `127.0.0.1:8000 <http://127.0.0.1:8000>`_ or equivalently at `localhost:8000 <http://localhost:8000>`_.

The command:

* activates the virtual environment and start serving the documentation
* rebuilds the documentation each time you save a file
* sends a reload page signal to the browser when the documentation is rebuilt

(This is the most convenient way to work on the documentation, but you can still use
the more standard ``make html``. For instance, ``PROJECT=azure make html`` will create the 
azure related html pages in _build/azure.)


Check spelling
~~~~~~~~~~~~~~

Run a spell check::

	PROJECT=azure make spelling

If new words are to be added to the allowed list, update ``.wordlist.txt`` accordingly.


Check links
~~~~~~~~~~~

Run a check for broken links::

	PROJECT=google make linkcheck


