Contribute to these docs
========================

.. include:: ../../../reuse/contribute-to-docs.txt
   :start-after: Start: How to contribute
   :end-before: End: How to contribute

.. code::

	PROJECT=aws make run

Setting the `PROJECT` parameter to ``aws`` ensures that the documentation set for `Ubuntu on AWS` gets built. This parameter is needed to distinguish between the different documentation sets present in the repository.

If you don't want to preview the changes continuously and only wish to build the docs once (e.g., to have a local copy on your machine), then run ``PROJECT=aws make html``. This will create the AWS related HTML pages in _build/aws. You can preview the site by opening ``index.html`` on your web browser. 


Perform checks and submit PR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before opening a PR, run the following checks and also ensure that the documentation builds without any warnings (warnings are treated as errors):

.. code::

	PROJECT=aws make spelling
	PROJECT=aws make linkcheck
	PROJECT=aws make woke

If you need to add new words to the allowed list of words, include them in ``.wordlist.txt``.

Once all the edits are done, commit the changes and push it to your fork. From the GitHub GUI of your fork, select the commit and open a PR for it.

.. _`ubuntu-cloud-docs`: https://github.com/canonical/ubuntu-cloud-docs
.. _`Diátaxis`: https://diataxis.fr/
.. _`reStructuredText`: https://docutils.sourceforge.io/rst.html
.. _`Canonical style guide`: https://docs.ubuntu.com/styleguide/en
.. _`Sphinx`: https://www.sphinx-doc.org/en/master/
.. _`Read the Docs`: https://readthedocs.com


