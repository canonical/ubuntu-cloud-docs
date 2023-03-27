Ubuntu cloud documentation
==========================

Documentation for Ubuntu on public clouds.

The documentation is currently published to: https://canonical-public-cloud.readthedocs-hosted.com


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

Start the ``sphinx-autobuild`` documentation server::

	make run

The documentation will be available at `127.0.0.1:8000 <http://127.0.0.1:8000>`_.

The command:

* activates the virtual environment and start serving the documentation
* rebuilds the documentation each time you save a file
* sends a reload page signal to the browser when the documentation is rebuilt

(This is the most convenient way to work on the documentation, but you can still use
the more standard ``make html``.)


Check spelling
~~~~~~~~~~~~~~

Run a spell check::

	make spelling

If new words are to be added to the allowed list, update ``.wordlist.txt`` accordingly.
