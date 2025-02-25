Deploy self-managed Ubuntu nodes
================================

Amazon provides a good baseline for `launch self-managed node groups`_. 
Minor modifications to eksctl can enable the same functionality for Ubuntu nodes.

To specify Ubuntu nodes, in the ``eksctl create nodegroup`` command, supply the `--node-ami-family argument` with one of
the following supported Node AMI families:

* Ubuntu2004
* Ubuntu2204
* UbuntuPro2204
* Ubuntu2404
* UbuntuPro2404

The `--node-ami` flag can be used to specify a specific AMI. By default, this
uses SSM parameters to select the latest available version for the given Node AMI
family. To look up the AMI ID for the region you wish to deploy to please reference
the :doc:`find ubuntu images <../instances/find-ubuntu-images>` page. 



.. _`launch self-managed node groups`: https://docs.aws.amazon.com/eks/latest/userguide/launch-workers.html
.. _`find ubuntu images`: "../instances/find-ubuntu-images.rst"
