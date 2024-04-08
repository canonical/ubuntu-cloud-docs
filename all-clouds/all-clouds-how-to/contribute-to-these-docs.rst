Contribute to these docs
========================

.. include:: ../../reuse/contribute-to-docs.txt
   :start-after: Start: How to contribute
   :end-before: End: How to contribute

.. include:: ../../reuse/contribute-to-docs.txt
   :start-after: Start: Build and serve the docs (part)
   :end-before: End: Build and serve the docs (part)

.. code::

	PROJECT=all-clouds make run

Setting the `PROJECT` parameter to ``all-clouds`` ensures that the documentation set for `Ubuntu on public cloud` gets built. This parameter is needed to distinguish between the different documentation sets present in the repository.

.. include:: ../../reuse/contribute-to-docs.txt
   :start-after: Start: How to contribute (continued)
   :end-before: End: How to contribute (continued)

Perform checks and submit a PR
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before opening a PR, run the following checks and also ensure that the documentation builds without any warnings (warnings are treated as errors in the publishing process):

.. code::

	PROJECT=all-clouds make spelling
	PROJECT=all-clouds make linkcheck
	PROJECT=all-clouds make woke

If you need to add new words to the allowed list of words, include them in ``.custom_wordlist.txt``.

Once all the edits are done, commit the changes and push it to your fork. From the GitHub GUI of your fork, select the commit and open a PR for it.

.. include:: ../../reuse/contribute-to-docs.txt
   :start-after: Start: How to contribute links
   :end-before: End: How to contribute links

