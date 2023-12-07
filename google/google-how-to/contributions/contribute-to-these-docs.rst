Contribute to these docs
========================

.. include:: ../../../reuse/contribute-to-docs.txt
   :start-after: Start: How to contribute
   :end-before: End: How to contribute

.. code::

	PROJECT=google make run

Setting the `PROJECT` parameter to ``google`` ensures that the documentation set for `Ubuntu on GCP` gets built. This parameter is needed to distinguish between the different documentation sets present in the repository.


Perform checks and submit PR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before opening a PR, run the following checks and also ensure that the documentation builds without any warnings (warnings are treated as errors in the publishing process):

.. code::

	PROJECT=google make spelling
	PROJECT=google make linkcheck
	PROJECT=google make woke

If you need to add new words to the allowed list of words, include them in ``.wordlist.txt``.

Once all the edits are done, commit the changes and push it to your fork. From the GitHub GUI of your fork, select the commit and open a PR for it.

.. include:: ../../../reuse/contribute-to-docs.txt
   :start-after: Start: How to contribute links
   :end-before: End: How to contribute links
