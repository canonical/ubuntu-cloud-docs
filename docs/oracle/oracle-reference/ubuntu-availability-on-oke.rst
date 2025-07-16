Ubuntu Availability on OKE
==========================


Available releases
------------------

The following Ubuntu images are available for worker nodes on Oracle Kubernetes Engine (OKE) in Oracle Cloud.

.. list-table::
   :header-rows: 1

   * - Ubuntu Release
     - OKE Version
     - End of Life
     - Location
   * - 22.04 (Jammy Jellyfish)
     - 1.31.1
     - 30 days after 1.34.1 OKE Release
     - `List of Images <https://objectstorage.us-phoenix-1.oraclecloud.com/p/lH_ztqUFhNMHzlMqe6CLUlM1TrAI4OzTjq1adtUD8pP6sIQ-iVOfBq7juf9iGVA8/n/intcanonical/b/oke-shared/o/>`__
   * -
     - 1.32.1
     - 30 days after 1.35.1 OKE Release
     - `List of Images <https://objectstorage.us-phoenix-1.oraclecloud.com/p/YfyIxRjIiLNUMd8sT70NOKODXeCXwoNv3EHLJF2uz5NH6uDP7p0S_DnT_a4i4BqX/n/intcanonical/b/oke-shared/o/>`__
   * - 24.04 (Noble Numbat)
     - 1.31.1
     - 30 days after 1.34.1 OKE Release
     - `List of Images <https://objectstorage.us-phoenix-1.oraclecloud.com/p/hloW9HxqKIwuanrFdPSTFpgEjNbdijtApD_GbwSXuIKg18J2G866NmPgTRa78M8v/n/intcanonical/b/oke-shared/o/>`__
   * -
     - 1.32.1
     - 30 days after 1.35.1 OKE Release
     - `List of Images <https://objectstorage.us-phoenix-1.oraclecloud.com/p/xIj-IH-CNygD9rGfB-oYTcJCu3ouGF5EVblFTKea9_x31eljhQN9akosZ6E49suY/n/intcanonical/b/oke-shared/o/>`__


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

