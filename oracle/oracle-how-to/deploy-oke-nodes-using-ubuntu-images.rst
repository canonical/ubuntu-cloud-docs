Deploy OKE nodes using Ubuntu images
====================================

Ubuntu images are available for worker nodes on Oracle Kubernetes Engine (OKE) in Oracle Cloud. Currently there are only a select number of suites and Kubernetes versions supported due to this being a Limited Availability release. 

Available releases
------------------

.. list-table::
   :header-rows: 1

   * - Ubuntu Release
     - OKE Version
     - Location
   * - 22.04 (Jammy Jellyfish)
     - 1.29
     - `List of Images <https://intcanonical.objectstorage.us-phoenix-1.oci.customer-oci.com/p/vpqQtYASl8IooEZ_sxfKDnzUkF1b-3lQmXPC_rXf4zARQYoW7ncE8BGGxNqdUuGa/n/intcanonical/b/oke-shared/o/>`_

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
     - No


Prerequisites
-------------

You'll need:

- Oracle Cloud compartment to create the nodes.

- Configured and running OKE cluster on Oracle Cloud.

- Oracle's ``oci`` CLI installed.

- ``kubectl`` installed (Self-Managed only).


Finding an Ubuntu image
-----------------------

Select a version from the `available releases <#available-releases>`_. The images are listed as JSON in ascending order, therefore the latest image will be at the bottom. After viewing the `available releases <#available-releases>`_, make note of the image path for the image you choose. The image path conforms to the following format:

.. code:: bash
  
  <suite>/oke-<version>/<serial>/<image-name>.img

If you wish to get the latest image path, use the following command:

.. code:: bash
  
  curl <available-releases-location-link> | jq ".[][-2] | .name"

Register an Ubuntu image
------------------------

Images must be registered to be used with Oracle Cloud services. To learn more, refer to the Oracle Cloud documentation for `managing custom images`_.

.. tabs::

    .. group-tab:: Using console
    
        Start the registration process Oracle Cloud by navigating to :guilabel:`Compute` > :guilabel:`Custom Images` and select :guilabel:`Import Image`. Select :guilabel:`Import from an Object Storage URL`, then paste the `available releases <#available-releases>`_ location link with your concatenated image path into the :guilabel:`Object Storage URL` field. The URL format pasted should conform to the following:

        .. code:: bash
         
          <available-releases-location-link>/<image-path>
    
        In the rest of the form, you must provide your :guilabel:`Compartment`, :guilabel:`Image name`, and :guilabel:`Launch mode`. Additionally the fields :guilabel:`Operating System` and :guilabel:`Image type` must be provided and use ``Ubuntu`` and ``QCOW2``, respectively.

        Lastly, select :guilabel:`Import image` and wait for the registration to complete. This process is expected to take a while.

    .. group-tab:: Using CLI
    
        The ``oci`` CLI offers the convenience of registering an image without having to upload it directly. For more information refer to the ``oci`` docs for `import from-object-uri`_. If you wish to separate these steps refer to the ``oci`` docs for `object upload`_ and `image import from object`_.

        .. code:: bash
    
            oci compute image import from-object-uri \
                --compartment-id <compartment-id> \
                --uri <available-release-location-link>/<image-path> \
                --display-name <image-name> \
                --launch-mode <launch-mode> \
                --image-source-object-name <object-name> \
                --operating-system "Ubuntu" \
                --operating-system-version <ubuntu-version-number> \
                --source-image-type QCOW2

Create OKE nodes with Ubuntu Images
-------------------------------------

The following steps on creating nodes assumes you have an existing OKE cluster on Oracle Cloud, but it is not required to have existing nodes. If you don't have an OKE cluster prepared then Oracle's documentation for `creating a cluster`_ is a good place to start.

When creating nodes, the :guilabel:`Launch mode` is an option to configure. The suggested configurations are :guilabel:`PARAVIRTUALIZED` for virtual nodes and :guilabel:`NATIVE` for bare-metal nodes.

Create managed OKE nodes with Ubuntu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Managed nodes are node instances whose lifecycle is managed by the OKE service. 

.. tabs::

  .. group-tab:: Using console

      Since this is a Limited Availability release of Ubuntu images for OKE, you can only create managed nodes through the Oracle Cloud API (``oci`` CLI or SDK). The ability to create managed nodes from the Oracle Cloud UI will be added later.

  
  .. group-tab:: Using CLI
      
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


View the node pool status in Oracle Cloud by navigating to :guilabel:`Kubernetes Clusters (OKE)` and choose on your cluster, then select :guilabel:`Resources` > :guilabel:`Node pools` and select the latest node pool.

Everything will be running as expected when the :guilabel:`Kubernetes node condition` and :guilabel:`Node state` of all the nodes are labelled :guilabel:`Ready`.

Create self-managed OKE nodes with Ubuntu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following instructions assume that you have configured your OKE cluster to work with self-managed nodes. If you have not done this, refer to the Oracle documentation for `working with self-managed nodes`_

Before adding a self-managed node, ensure you have configured ``kubectl`` for your OKE cluster with the following command. This process will be easier if ``kubectl`` is configured for a single OKE cluster.

.. code:: bash
  
  kubectl cluster-info

Next, the self-managed node will need a custom cloud-init script which needs some specific values, namely a Kubernetes certificate from the OKE cluster and the Kubernetes API private endpoint.

Obtain the Kubernetes certificate using ``kubectl`` with the following command and note that ``[0]`` is the index of the cluster if only one is configured:

.. code:: bash

   kubectl config view --raw -o json | jq -r '.clusters[0].cluster.certificate-authority-data'

Then obtain the ``Kubernetes API private endpoint`` from Oracle Cloud by navigating to :guilabel:`Kubernetes Cluster (OKE)` and selecting your cluster. Be sure to copy only the IP, not the port.

Alternately, use the following ``oci`` command to obtain the ``Kubernetes API private endpoint``:

.. code:: bash

   oci ce cluster get --cluster-id <cluster-id> | jq -r '.data.endpoints.private-endpoint' | cut -d ":" -f1

Use these obtained values (certificate-data and private-endpoint) in the following example and save it as ``user-data.yaml``.

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

.. tabs::

   .. group-tab:: Using console
  
    Now, create the self-managed node in Oracle Cloud by navigating to :guilabel:`Compute` > :guilabel:`Instance` and select :guilabel:`Create Instance`. Next, select :guilabel:`Change Image` and select :guilabel:`My Images`, then select the Ubuntu image you recently registered. 
    
    Setup the cloud-init for the instance by selecting :guilabel:`Show advanced options`, then select :guilabel:`Paste cloud-init script`, and then paste your completed cloud-init script (the one saved in ``user-data.yaml``).
    
    Lastly, select :guilabel:`Create` and wait for your instance to be provisioned.

   .. group-tab:: Using CLI

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

Once your node is in :guilabel:`Ready` state, then everything is running as expected and your self-managed node is ready to accept pods. 

Further references
------------------

For more information about oci CLI and managing self-managed nodes on your cluster, refer to the Oracle Documentation:

* `oci CLI documentation`_
* `Creating and managing kubernetes clusters`_
* `Creating a dynamic group and a policy for self-managed nodes`_
* `Creating cloud-init scripts for self-managed nodes`_

.. _`working with self-managed nodes`: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithselfmanagednodes.htm
.. _`creating a cluster`: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-cluster.htm
.. _`import from-object-uri`: https://docs.oracle.com/en-us/iaas/tools/oci-cli/3.45.2/oci_cli_docs/cmdref/compute/image/import/from-object-uri.html
.. _`object upload`: https://docs.oracle.com/en-us/iaas/tools/oci-cli/3.45.2/oci_cli_docs/cmdref/os/object/put.html
.. _`image import from object`: https://docs.oracle.com/en-us/iaas/tools/oci-cli/3.45.2/oci_cli_docs/cmdref/compute/image/import/from-object.html
.. _`managing custom images`: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingcustomimages.htm
.. _`OCI CLI documentation`: https://docs.oracle.com/en-us/iaas/tools/oci-cli/3.46.0/oci_cli_docs/
.. _`Creating and managing kubernetes clusters`: https://docs.public.oneportal.content.oci.oraclecloud.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-and-managing-kubernetes-clusters.htm
.. _`Creating a dynamic group and a policy for self-managed nodes`: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdynamicgrouppolicyforselfmanagednodes.htm
.. _`Creating cloud-init scripts for self-managed nodes`: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcloudinitforselfmanagednodes.htm

