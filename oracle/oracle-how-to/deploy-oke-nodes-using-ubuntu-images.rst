Deploy OKE Nodes using Ubuntu Images
====================================

Ubuntu images are available for worker nodes on Oracle Kubernetes Engine (OKE) in Oracle Cloud. Currently there are only a select number of suites and Kubernetes versions supported due to this being a Limited Availability release. 

Available Releases
------------------

.. list-table::
   :header-rows: 1

   * - Ubuntu Release
     - OKE Version
     - Location
   * - 22.04 (Jammy Jellyfish)
     - 1.29
     - `Link <https://intcanonical.objectstorage.us-phoenix-1.oci.customer-oci.com/p/vpqQtYASl8IooEZ_sxfKDnzUkF1b-3lQmXPC_rXf4zARQYoW7ncE8BGGxNqdUuGa/n/intcanonical/b/oke-shared/o/>`_


Networking Plugin Availability
------------------------------

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
     - No


Prerequisites
-------------

You'll need:

- Oracle Cloud compartment to create the nodes.

- Configured and running OKE cluster on Oracle Cloud.

- Oracle's ``oci`` CLI installed.

- ``kubectl`` installed (Self-Managed only).


Download an Ubuntu image
------------------------


To download an image, select a version from the `available releases <#available-releases>`_ and make note of the image path for the image you choose. The image path conforms to the following format:

.. code:: bash
  
  <suite>/oke-<version>/<serial>/<image-name>.img


Then, from the browser you can paste the image path after the link to begin downloading the image. 

Alternatively, you can use ``curl`` to achieve the same result by using the following command.

.. code:: bash
   
  curl -O <available-releases-link>/<image-path>

Upload the Ubuntu image to a bucket
-----------------------------------

The image must be uploaded to a bucket for image registration later on. Do this in Oracle Cloud by navigating to :guilabel:`Buckets` and selecting your bucket then click :guilabel:`Upload`.

Alternately, the following oci command will upload the object too.

.. code:: bash
  
  oci os object put --bucket-name <bucket-name> --file <file-path>


Register the Ubuntu image
-------------------------

Images must be registered to be used by Oracle Cloud services. To register an image in Oracle Cloud, navigate to :guilabel:`Compute` > :guilabel:`Custom Images` and select :guilabel:`Import Image`. 

In the form you must provide your :guilabel:`Compartment`, :guilabel:`Image name`, :guilabel:`Object name` and :guilabel:`Launch mode`. Additionally the fields :guilabel:`Operating System` and :guilabel:`Image type` must be provided and use ``Ubuntu`` and ``QCOW2``, respectively. 

Optionally, this process can be done with the following command:

.. code:: bash

  oci compute image import from-object \
    --compartment-id <compartment-id> \
    --display-name <image-name> \
    --launch-mode <launch-mode> \
    --image-source-object-name <object-name> \
    --bucket-name <bucket-name> \
    --operating-system "Ubuntu" \
    --operating-system-version <ubuntu-version-number> \
    --source-image-type QCOW2 \
    --wait-for-state AVAILABLE


Creating OKE Nodes with Ubuntu Images
-------------------------------------

The following steps on creating nodes assumes you have an existing OKE cluster on Oracle Cloud, but it is not required to have existing nodes. If you don't have an OKE cluster prepared then Oracle's documentation for `creating a cluster`_ is a good place to start.

Creating Managed OKE nodes with Ubuntu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Managed nodes are node instances whose lifecycle is managed by the OKE service. Since this is a Limited Availability release of Ubuntu images for OKE, you can only create managed nodes through the Oracle Cloud API (``oci`` CLI or SDK). The ability to create managed from nodes from the Oracle Cloud UI will be added at a later.

To create a managed node, start by copying the following cloud-init script into a file called ``user-data.yaml``.

.. code:: yaml

   #cloud-config
   
   runcmd:
     - oke bootstrap

Then, create a placement configuration file to specify where in Oracle Cloud the Managed node pool should be created and save the file as ``placement-config.json``.

.. code:: json 

   [{
     "compartmentId":"<compartment-id>",
     "availabilityDomain":"<availability-domain>",
     "subnetId":"<subnet-id>"
   }]


Lastly, replace the values and run the following command to create the Managed node pool:

.. code:: bash
   
  oci ce node-pool create \
    --cluster-id=<cluster-id> \
    --compartment-id=<compartment-id> \
    --name=<pool-name> \
    --node-shape=<node-shape> \
    --size=<pool-count> \
    --kubernetes-version="1.29.1" \
    --node-image-id=<ubuntu-image-id> \
    --placement-configs="$(cat placement-config.json)" \
    --node-metadata='{"user_data": "'"$(base64 user-data.yaml)"'"}'


View the node pool status in Oracle Cloud by navigating to :guilabel:`Kubernetes Clusters (OKE)` and click on your cluster, then select :guilabel:`Resources` > :guilabel:`Node pools` and click on the latest node pool.

Everything will be running as expected when the :guilabel:`Kubernetes node condition` and :guilabel:`Node state` of all the nodes are labelled :guilabel:`Ready`.

Creating Self-Managed OKE nodes with Ubuntu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following instructions assumes that you have configured your OKE cluster to work with self-managed nodes. If you have not done this, refer to the Oracle documentation for `working with self-managed nodes`_

Before adding a self-managed node, ensure you have configured ``kubectl`` to your OKE cluster with the following command. This process will be easier if ``kubectl`` is configured for a single OKE cluster.

.. code:: bash
  
  kubectl cluster-info

Next, the self-managed node will need a custom cloud-init script which needs some specific values, namely a Kubernetes certificate from the OKE cluster and the Kubernetes API private endpoint.

Obtain the Kubernetes certificate using ``kubectl`` with the following command and note that ``[0]`` is the index of the cluster if only one is configured:

.. code:: bash

   kubectl config view --raw -o json | jq -r '.clusters[0].cluster.certificate-authority-data'

Then obtain the ``Kubernetes API private endpoint`` from Oracle Cloud by navigating to :guilabel:`Kubernetes Cluster (OKE)` then select your cluster. Be sure to copy only the IP, not the port.

Alternately, use the following ``oci`` command to obtain the ``Kubernetes API private endpoint``:

.. code:: bash

   oci ce cluster get --cluster-id <cluster-id> | jq -r '.data.endpoints.private-endpoint' | cut -d ":" -f1

Using your previously obtained values, insert them in the following example and save it with the name ``user-data.yaml``.

.. code:: yaml

   #cloud-config
   runcmd:
     - oke bootstrap --ca <certificate-data> --apiserver-host <private-endpoint>
   
   write_files:
   - path: /etc/oke/oke-apiserver
     permissions: '0644'
     content: <private-endpoint>
   - encoding: b64
     path: /etc/kubernetes/ca.crt
     permissions: '0644'
     content: <certificate-data>


Now, create the instance behind the self-managed node in Oracle Cloud by navigating to :guilabel:`Compute` > :guilabel:`Instance` and click :guilabel:`Create Instance`. Next, click :guilabel:`Change Image` and select :guilabel:`My Images` then click the Ubuntu image recently registered. 

Setup the cloud-init for the instance by clicking :guilabel:`Show advanced options` then select :guilabel:`Paste cloud-init script`, where you should be able to paste your completed cloud-init script (the one saved in ``user-data.yaml``).

Lastly, click :guilabel:`Create` and wait for your instance to be provisioned.

Optionally, you can this ``oci`` command to create the self-managed node:

.. code:: bash

  oci compute instance launch \
    --compartment-id <compartment-ocid> \
    --availability-domain <availability-domain> \
    --shape <instance-shape> \
    --image-id <ubuntu-image-ocid> \
    --subnet-id <subnet-ocid> \
    --user-data-file user-data.yaml \
    --display-name <instance-name>


Self-managed nodes cannot be viewed from Oracle Cloud so you can poll their status with the following command. The process for nodes joining the cluster will take several minutes.

.. code:: bash

   watch 'kubectl get nodes'

Once your nodes are in :guilabel:`Ready` state, then everything is running as expected and you're self-managed node is ready to accept pods. 

Further references
------------------

For more information about oci CLI and managing self-managed nodes on your cluster, refer to the Oracle Documentation:

* `oci CLI Documentation`_
* `Creating and Managing Kubernetes Clusters`_
* `Creating a Dynamic Group and a Policy for Self-Managed Nodes`_
* `Creating Cloud-init scripts for Self-Managed Nodes`_

.. _`working with self-managed nodes`: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithselfmanagednodes.htm
.. _`creating a cluster`: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-cluster.htm
.. _`OCI CLI Documentation`: https://docs.oracle.com/en-us/iaas/tools/oci-cli/3.46.0/oci_cli_docs/
.. _`Creating and Managing Kubernetes CLusters`: https://docs.public.oneportal.content.oci.oraclecloud.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-and-managing-kubernetes-clusters.htm
.. _`Creating a Dynamic Group and a Policy for Self-Managed Nodes`: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdynamicgrouppolicyforselfmanagednodes.htm
.. _`Creating Cloud-init scripts for Self-Managed Nodes`: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcloudinitforselfmanagednodes.htm

