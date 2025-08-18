Ubuntu on AWS
=============


**Ubuntu on AWS is a set of customized Ubuntu images** that allow easy access to a wide range 
of products and services - offered by both Amazon Web Services (AWS) and Canonical. These images 
have an optimized kernel that boots faster, has a smaller footprint and includes AWS-specific drivers.

**These images provide a foundation for deploying cloud-based software solutions,** specifically
for software built on Ubuntu and running on AWS. They focus on providing the optimal tools 
and features needed to run specific workloads.

.. include:: ../reuse/common-intro.txt
   :start-after: Start: Product need and user
   :end-before: End: Product need and user


---------

In this documentation
---------------------

..  grid:: 1 1 1 1
   :padding: 0

   ..  grid-item:: :doc:`How-to guides <aws-how-to/index>`

      **Step-by-step guides** covering key operations and common tasks involving the use of Ubuntu on EC2 and EKS.

.. grid:: 1 1 2 2
   :padding: 0
   :reverse:

   .. grid-item:: :doc:`Reference <aws-reference/index>`

      **Technical information** about things like EC2 credentials, EKS snaps, Ubuntu Pro and the support options available on AWS.

   .. grid-item:: :doc:`Explanation <aws-explanation/index>`

      **Discussion and clarification** of key topics, such as our offerings, our image retention policy and the usage of snaps in our EKS images.


----------

Customized Ubuntu images
------------------------

For each Ubuntu release, we deliver multiple customized images to AWS. These images are based on the - AWS service being used, underlying architectures, required features, storage types and virtualization types:

* **AWS services** - EC2, EKS
* **architectures** - AMD64, ARM64 (Graviton)
* **Ubuntu image types** - server, minimal
* **storage types** - instance store, Elastic Block Store (EBS)
* **virtualization types** - Paravirtual (PV), Hardware Virtual Machine (HVM)
* **support/security compliance levels** - standard, Ubuntu Pro, Ubuntu Pro FIPS

More details are available in our explanation about :doc:`aws-explanation/canonical-offerings`

---------

Project and community
---------------------

Ubuntu on AWS is a member of the Ubuntu family and the project warmly welcomes community projects, contributions, 
suggestions, fixes and constructive feedback.


* `Get support`_
* `Join our online chat`_
* `Discuss on Matrix`_
* `Talk to us about Ubuntu on AWS`_
* :doc:`aws-how-to/contribute-to-these-docs`
* `Code of conduct`_

If none of the above options are suitable for you, and you still want to get in touch, send us an email: aws@canonical.com.

.. toctree::
   :hidden:
   :maxdepth: 1

   aws-how-to/index
   aws-explanation/index
   aws-reference/index
   aws-how-to/contribute-to-these-docs


.. _Get support: https://ubuntu.com/cloud/public-cloud
.. _Join our online chat: https://discourse.ubuntu.com/c/project/aws/177
.. _`Discuss on Matrix`: https://matrix.to/#/#ubuntu-cloud:ubuntu.com
.. _Talk to us about Ubuntu on AWS: https://ubuntu.com/aws#get-in-touch
.. _Code of conduct: https://ubuntu.com/community/docs/ethos/code-of-conduct
