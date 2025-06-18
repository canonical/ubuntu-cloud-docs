Deploy OKE nodes using Ubuntu images
====================================

Ubuntu images are available for worker nodes on Oracle Kubernetes Engine (OKE) in Oracle Cloud. Currently there are only a select number of suites and Kubernetes versions supported due to this being a Limited Availability release. For a list of supported OKE configurations, see our :doc:`Ubuntu availability on OKE </oracle-reference/ubuntu-availability-on-oke>` page.

For node stability, the ``unattended-upgrades`` package has been removed from the Ubuntu image for OKE. Should your nodes need updates or security patches then refer to the Oracle documentation on `node cycling for managed nodes`_ and `node cycling for self-managed nodes`_.

Prerequisites
-------------

You'll need:

- Oracle Cloud compartment to create the nodes.

- Oracle's ``oci`` CLI installed.

- ``kubectl`` installed.

- `Domain <https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-create-new-identity-domain.htm>`_, `Dynamic Group and Policy <https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdynamicgrouppolicyforselfmanagednodes.htm#contengprereqsforselfmanagednodes-accessreqs>`_ configured (Self-Managed only). 


Find an Ubuntu image
-----------------------

Select a version from the `available releases </oracle-reference/ubuntu-availability-on-oke>`_. The images are listed as JSON in ascending order, therefore the latest image will be at the bottom. Make note of the image path for the image you choose. The image path conforms to the following format:

.. code:: bash
  
  <suite>/oke-<version>/<serial>/<image-name>.img

If you wish to get the latest image path, use the following command:

.. code:: bash
  
  curl <available-releases-location-link> | jq ".[][-2] | .name"

Register an Ubuntu image
------------------------

Images must be registered to be used with Oracle Cloud services. To learn more, refer to the Oracle Cloud documentation for `managing custom images`_.

When registering images, the :guilabel:`Launch mode` is an option to configure. The suggested configurations are :guilabel:`PARAVIRTUALIZED` for virtual nodes and :guilabel:`NATIVE` for bare-metal nodes.

.. tabs::

    .. group-tab:: Using console
    
        Start the registration process in Oracle Cloud by navigating to :guilabel:`Compute` > :guilabel:`Custom Images` and select :guilabel:`Import Image`. Select :guilabel:`Import from an Object Storage URL`, then paste the `available releases <#available-releases>`_ location link with your concatenated image path into the :guilabel:`Object Storage URL` field. The URL format pasted should conform to the following:

        .. code:: bash
         
          <available-releases-location-link>/<image-path>
    
        In the rest of the form, you must provide your :guilabel:`Compartment`, :guilabel:`Image name`, and :guilabel:`Launch mode`. Additionally the fields :guilabel:`Operating System` and :guilabel:`Image type` must be provided and use ``Ubuntu`` and ``QCOW2``, respectively.

        Lastly, select :guilabel:`Import image` and wait for the registration to complete. This process is expected to take a while.

    .. group-tab:: Using CLI
    
        The following command will directly import your image from a provided URI. You'll have to provide the values below with the exception of ``operating-system`` and ``source-image-type`` which are already provided.
        
        For more information on this command, refer to the ``oci`` docs for `import from-object-uri`_.

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

Create OKE Cluster with Ubuntu Images
-------------------------------------

Create OKE Cluster using web console
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Since this is a Limited Availability release of Ubuntu images for OKE, you can only create managed nodes through the Oracle Cloud API (``oci`` CLI or SDK). The ability to create managed nodes from the Oracle Cloud UI will be added later.


Create OKE Cluster using OCI CLI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create managed OKE nodes with Ubuntu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
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
      
      Then, create a placement configuration file to specify where in Oracle Cloud the managed node pool should be created and save the file as ``placement-config.json``.
      
      .. code:: json 
      
         [{
           "compartmentId":"<compartment-id>",
           "availabilityDomain":"<availability-domain>",
           "subnetId":"<subnet-id>"
         }]
      
      
      Lastly, replace the values and run the following command to create the managed node pool:
      
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


View the node pool status in Oracle Cloud by navigating to :guilabel:`Kubernetes Clusters (OKE)` and choosing your cluster, then select :guilabel:`Resources` > :guilabel:`Node pools` and select the latest node pool.

Everything will be running as expected when the :guilabel:`Kubernetes node condition` and :guilabel:`Node state` of all the nodes are labeled :guilabel:`Ready`.

Create self-managed OKE nodes with Ubuntu
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The following instructions assume that you have configured your OKE cluster to work with self-managed nodes. If you have not done this, refer to the Oracle documentation for `working with self-managed nodes`_

Before adding a self-managed node, ensure that you have configured ``kubectl`` for your OKE cluster with the following command. This process will be easier if ``kubectl`` is configured for a single OKE cluster.

.. code:: bash
  
  kubectl cluster-info

Next, the self-managed node will need a custom cloud-init script which needs some specific values, namely a Kubernetes certificate from the OKE cluster and the Kubernetes API private endpoint.

Obtain the Kubernetes certificate for the current context with the following command:

.. code:: bash

   kubectl config view --minify --raw -o json | jq -r '.clusters[].cluster."certificate-authority-data"'

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
  
    Now, create the self-managed node in Oracle Cloud by navigating to :guilabel:`Compute` > :guilabel:`Instance` and select :guilabel:`Create Instance`. Next, select :guilabel:`Change Image` > :guilabel:`My Images`, and then select the Ubuntu image you recently registered. 
    
    Setup the cloud-init for the instance by selecting :guilabel:`Show advanced options` > :guilabel:`Paste cloud-init script`, and then paste your completed cloud-init script (the one saved in ``user-data.yaml``).
    
    Lastly, select :guilabel:`Create` and wait for your instance to be provisioned.

   .. group-tab:: Using CLI

    The following command will create an instance with your previously created ``user-data.yaml``. The value for ``subnet-id`` should correspond with the subnet used for the nodes in your OKE cluster.
    
    .. code:: bash
    
      oci compute instance launch \
        --compartment-id <compartment-id> \
        --availability-domain <availability-domain> \
        --shape <instance-shape> \
        --image-id <ubuntu-image-id> \
        --subnet-id <subnet-ocid> \
        --user-data-file user-data.yaml \
        --display-name <instance-name>


Self-managed nodes cannot be viewed from Oracle Cloud so you can poll their status with the following command. The process for nodes joining the cluster will take several minutes.

.. code:: bash

   watch 'kubectl get nodes'

Once your node is in :guilabel:`Ready` state, then everything is running as expected and your self-managed node is ready to accept pods. 

Create OKE Cluster using Terraform
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


Further references
------------------

For more information about ``oci`` CLI and managing self-managed nodes on your cluster, refer to the Oracle Documentation:

* `oci CLI documentation`_
* `Creating and managing kubernetes clusters`_
* `Creating a dynamic group and a policy for self-managed nodes`_
* `Creating cloud-init scripts for self-managed nodes`_

.. _`node cycling for managed nodes`: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingk8sworkernode.htm
.. _`node cycling for self-managed nodes`: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengupgradingselfmanagednodes.htm#contengupgradingselfmanagednodes
.. _`working with self-managed nodes`: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithselfmanagednodes.htm
.. _`creating a cluster`: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/create-cluster.htm
.. _`import from-object-uri`: https://docs.oracle.com/en-us/iaas/tools/oci-cli/3.54.3/oci_cli_docs/cmdref/compute/image/import/from-object-uri.html
.. _`object upload`: https://docs.oracle.com/en-us/iaas/tools/oci-cli/3.45.2/oci_cli_docs/cmdref/os/object/put.html
.. _`image import from object`: https://docs.oracle.com/en-us/iaas/tools/oci-cli/3.45.2/oci_cli_docs/cmdref/compute/image/import/from-object.html
.. _`managing custom images`: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingcustomimages.htm
.. _`OCI CLI documentation`: https://docs.oracle.com/en-us/iaas/tools/oci-cli/3.54.3/oci_cli_docs/
.. _`Creating and managing kubernetes clusters`: https://docs.public.oneportal.content.oci.oraclecloud.com/en-us/iaas/compute-cloud-at-customer/topics/oke/creating-and-managing-kubernetes-clusters.htm
.. _`Creating a dynamic group and a policy for self-managed nodes`: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdynamicgrouppolicyforselfmanagednodes.htm
.. _`Creating cloud-init scripts for self-managed nodes`: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcloudinitforselfmanagednodes.htm

