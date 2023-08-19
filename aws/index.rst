Ubuntu on AWS
=============


**Ubuntu on AWS is a set of customised Ubuntu images** that allow easy access to a wide range 
of products and services - offered by both Amazon Web Services (AWS) and Canonical. These images 
have an optimised kernel that boots faster, has a smaller footprint and includes AWS-specific drivers.

**These images provide a foundation for deploying cloud-based software solutions,** specifically
for softwares built on Ubuntu and running on AWS. They focus on providing the optimal tools 
and features needed to run specific workloads.

.. include:: ../reuse/common-intro.txt
   :start-after: Start: Product need and user
   :end-before: End: Product need and user


----------

Customised Ubuntu images
------------------------

For each Ubuntu release, we deliver multiple customised images to AWS. These images are based on the - AWS service being used, underlying architectures, required features, storage types and virtualisation types:

* **AWS services** - EC2, EKS
* **architectures** - AMD64, ARM64, Graviton
* **Ubuntu image types** - server, minimal
* **storage types** - instance store, Elastic Block Store (EBS)
* **virtualisation types** - Paravirtual (PV), Hardware Virtual Machine (HVM)
* **support/security compliance levels** - standard, Ubuntu Pro, Ubuntu Pro FIPS

For more details read about :doc:`canonical-offerings`

---------

Project and community
---------------------

Ubuntu on AWS is a member of the Ubuntu family and the project warmly welcomes community projects, contributions, 
suggestions, fixes and constructive feedback.

* `Code of conduct`_
* `Get support`_
* `Join our online chat`_
* `Talk to us about Ubuntu on AWS`_


.. toctree::
   :hidden:
   :maxdepth: 2

   canonical-offerings
   aws-how-to/index
   eks-image-retention-policy


.. _Code of conduct: https://ubuntu.com/community/governance/code-of-conduct
.. _Get support: https://ubuntu.com/cloud/public-cloud
.. _Join our online chat: https://discourse.ubuntu.com
.. _Talk to us about Ubuntu on AWS: https://ubuntu.com/aws#get-in-touch

