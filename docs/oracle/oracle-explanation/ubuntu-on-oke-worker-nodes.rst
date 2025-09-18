Ubuntu on OKE worker nodes
==========================

Ubuntu images are now available for worker nodes on Oracle Kubernetes Engine (OKE). 


Supported OKE configurations
----------------------------

Currently there are only a select number of suites and Kubernetes versions supported due to this being a Limited Availability release. For a list of supported OKE configurations, see our :doc:`Ubuntu availability on OKE </oracle-reference/ubuntu-availability-on-oke>` page.


Deployment options
------------------

To deploy an Ubuntu worker node on OKE, you can use the Oracle Cloud Console, Oracle CLI (``oci``), or Terraform. For detailed instructions, refer to:

- :doc:`Deploying Ubuntu worker nodes using the Oracle Cloud Console </oracle-how-to/deploy-ubuntu-oke-nodes-using-console>`
- :doc:`Deploying Ubuntu worker nodes using the CLI </oracle-how-to/deploy-ubuntu-oke-nodes-using-cli>`
- :doc:`Deploying Ubuntu worker nodes using Terraform </oracle-how-to/deploy-ubuntu-oke-nodes-using-terraform>`


Updates and security patches
----------------------------

For node stability, the ``unattended-upgrades`` package has been removed from the Ubuntu image for OKE. Should your nodes need updates or security patches then refer to the Oracle documentation on `node cycling for managed nodes`_ and `node cycling for self-managed nodes`_.


.. _`node cycling for managed nodes`: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8sworkernode.htm
.. _`node cycling for self-managed nodes`: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingselfmanagednodes.htm#contengupgradingselfmanagednodes