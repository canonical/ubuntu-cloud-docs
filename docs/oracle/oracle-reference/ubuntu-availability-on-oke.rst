Ubuntu Availability on OKE
==========================

.. include:: ../../reuse/OKE-nodes.txt
   :start-after: Start: Get Ubuntu image access
   :end-before: End: Get Ubuntu image access


Available releases
------------------

The following Ubuntu images are available for worker nodes on Oracle Kubernetes Engine (OKE) in Oracle Cloud.

**Ubuntu images are available for both AMD64 and ARM64 architectures.**

.. list-table::
   :header-rows: 1

   * - Ubuntu Release
     - OKE Version
     - End of Life
   * - 22.04 (Jammy Jellyfish)
     - 1.31.1
     - 30 days after 1.34.1 OKE Release
   * -
     - 1.32.1
     - 30 days after 1.35.1 OKE Release
   * - 24.04 (Noble Numbat)
     - 1.31.1
     - 30 days after 1.34.1 OKE Release
   * -
     - 1.32.1
     - 30 days after 1.35.1 OKE Release


Networking plugin availability
------------------------------

The availability of networking plugins (Flannel / VCN Native) depends on the type of OKE node being used:

.. list-table::
   :header-rows: 1

   * - Node Type
     - Plugin
     - Supported
   * - Managed
     - Flannel
     - Yes
   * -
     - VCN Native
     - Yes
   * - Self-Managed
     - Flannel
     - Yes
   * -
     - VCN Native
     - Yes

Related how-to guides
---------------------

For step-by-step instructions on deploying Ubuntu nodes on OKE, see:

- :doc:`Deploy Ubuntu OKE nodes using Console <../oracle-how-to/deploy-ubuntu-oke-nodes-using-console>`
- :doc:`Deploy Ubuntu OKE nodes using CLI <../oracle-how-to/deploy-ubuntu-oke-nodes-using-cli>`
- :doc:`Deploy Ubuntu OKE nodes using Terraform <../oracle-how-to/deploy-ubuntu-oke-nodes-using-terraform>`

.. _`Policy`: https://cloud.oracle.com/identity/domains/policies
