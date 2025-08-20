Deploy Ubuntu OKE nodes using CLI
=================================

.. include:: ../../reuse/OKE-nodes.txt
   :start-after: Start: Intro and prereqs
   :end-before: End: Intro and prereqs

.. include:: ../../reuse/OKE-nodes.txt
   :start-after: Start: Get Ubuntu image access
   :end-before: End: Get Ubuntu image access

.. include:: ../../reuse/OKE-nodes.txt
   :start-after: Start: Find an image
   :end-before: End: Find an image


Deploy an OKE cluster using CLI
-------------------------------

Before getting started, note the architecture of the image you have selected, either ``amd64`` or ``arm64``, as you want to ensure that nodes are launched with the correct instance shapes.

Deploying an OKE cluster with Ubuntu images using the ``oci`` CLI involves three main steps:

* Create the required network resources for the cluster.
* Create the OKE cluster.
* Create a `managed node pool <cli-managed-nodes_>`_ or `self-managed nodes <cli-self-managed-nodes_>`_ with Ubuntu images.

The following sections provide a general guide for each of the steps outlined above. For a full working example, please refer to our `GitHub example repository <cli-example-repo_>`_.

If you already have a cluster, you can skip directly to `creating a managed node pool <cli-managed-nodes_>`_ or `creating self-managed nodes <cli-self-managed-nodes_>`_.


Create network resources
~~~~~~~~~~~~~~~~~~~~~~~~

Before you can create and deploy an OKE cluster, you need to create the necessary network resources. This includes a Virtual Cloud Network (VCN), subnets, internet gateway, route table, and more. For a complete guide on how to set up the network resources, refer to the Oracle documentation on `cluster networking <cluster-networking_>`_.

Setting up a VCN typically requires (this is not an exhaustive list):

* A CIDR block (range of IP addresses) for the cluster nodes.
* An internet gateway (if using public subnets).
* A NAT gateway and a service gateway (if using private subnets).
* A route table (required if using gateways).
* Subnets for worker nodes, control plane, and load balancers.
* Security rules defined in security lists to control traffic between nodes and the control plane.

To create a VCN using the ``oci`` CLI, use:

.. code:: bash
  
  oci network vcn create \
  --compartment-id <compartment-id> \
  --display-name <vcn-name> \
  --cidr-block <vcn-cidr-block>
  
Replace the placeholders with your own values.

The next step is to create an internet gateway, a NAT gateway and/or a service gateway. To determine which of them are needed for your cluster, refer to the same Oracle documentation on `cluster networking <cluster-networking_>`_.
      
.. code:: bash
  
  # Create internet gateway
  oci network internet-gateway create \
    --compartment-id <compartment-id> \
    --vcn-id <vcn-id> \
    --is-enabled true

Next up, refer to the Oracle documentation for `security lists`_ for information on creating security rules for the nodes, control plane, and service load balancer. You can create a security list using:

.. code:: bash
  
  oci network security-list create \
  --compartment-id <compartment-id> \
  --vcn-id <vcn-id> \
  --display-name <security-list-name> \
  --egress-security-rules <rules> \
  --ingress-security-rules <rules>
                
Now that you have the VCN, gateways, and security lists, you can create the route table and the subnets. Typically, you will need a nodes subnet, a control plane subnet, and a service load balancer subnet.

You can create a route table and a subnet using:
      
.. code:: bash
  
  # Create public route
  oci network route-table create \
      --compartment-id <compartment-id>\
      --vcn-id <vcn-id> \
      --display-name <route-table-name> \
      --route-rules <route-rules-with-internet-gateway>

  # Create nodes subnet                
  oci network subnet create \
      --compartment-id <compartment-id>\
      --vcn-id <vcn-id> \
      --display-name <nodes-subnet-name> \
      --cidr-block <subnet-cidr-block> \
      --route-table-id <route-table-ocid> \
      --security-list-ids <nodes-seclist-ocid>
      ...
      
Similarly, create a control plane subnet and a service load balancer subnet.

Create the OKE cluster
~~~~~~~~~~~~~~~~~~~~~~~

To create the OKE cluster, you will need to provide the compartment ID, the VCN OCID, and the subnets for the control plane and service load balancer. For more details on cluster creation, please refer to the Oracle documentation on `creating a cluster`_.

Create the OKE cluster using:

.. code:: bash
  
  oci ce cluster create \
      --compartment-id <compartment-id> \
      --name <cluster-name> \
      --kubernetes-version <kubernetes-version> \
      --vcn-id <vcn-ocid> \
      --cluster-pod-network-options <cluster-network-options> \
      --endpoint-subnet-id <control-plane-subnet-ocid> \
      --service-lb-subnet-ids "[<service-lb-subnet-ocid>]"
      ...
      
Once the cluster is created, you can create a kubeconfig file to access the cluster through ``kubectl``. Generate the kubeconfig file using:

.. code:: bash
  
  oci ce cluster create-kubeconfig \
      --cluster-id <cluster-id> \
      --file <path-to-kube-config> \
      --kube-endpoint PUBLIC_ENDPOINT


.. _cli-managed-nodes:

Create a managed node pool of Ubuntu OKE nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Managed nodes are node instances whose lifecycle is managed by the OKE service. 
      
To create a managed node, start by copying the following `cloud-init` script into a file called ``user-data.yaml``.
      
.. code:: yaml

    #cloud-config
    
    runcmd:
      - oke bootstrap

Then create a placement configuration file to specify where in Oracle Cloud the managed node pool should be created and save the file as ``placement-config.json``.

.. code:: json 

    [{
      "compartmentId":"<compartment-id>",
      "availabilityDomain":"<availability-domain>",
      "subnetId":"<nodes-subnet-ocid>"
    }]


Finally, to create the managed node pool, replace the placeholders and run:

.. code:: bash
    
  oci ce node-pool create \
    --cluster-id=<cluster-id> \
    --compartment-id=<compartment-id> \
    --name=<pool-name> \
    --node-shape=<node-shape> \
    --size=<pool-count> \
    --kubernetes-version=<kubernetes-version> \
    --node-image-id=<ubuntu-image-id> \
    --placement-configs="$(cat placement-config.json)" \
    --node-metadata='{"user_data": "'"$(base64 user-data.yaml)"'"}'

To view the node pool status, use ``kubectl`` with the previously created ``kubeconfig`` file: 

.. code:: bash

  kubectl get nodes --kubeconfig <config-path> --watch

All the nodes should show *STATUS* as *Ready* once everything is running as expected.  


.. _cli-self-managed-nodes:

Create self-managed Ubuntu OKE nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following instructions assume that you have configured the domain, dynamic group, and policy as mentioned in the `prerequisites <Prerequisites_>`_. If you have not done this, refer to the Oracle documentation for `working with self-managed nodes`_

The self-managed nodes will need a custom `cloud-init` script which needs some specific values, namely a Kubernetes certificate from the OKE cluster and the Kubernetes API private endpoint.

Obtain the Kubernetes certificate for the current context using:

.. code:: bash

   kubectl config view --minify --raw -o json | jq -r '.clusters[].cluster."certificate-authority-data"'

Then obtain the Kubernetes API private endpoint using:

.. code:: bash

   oci ce cluster get --cluster-id <cluster-id> | jq -r '.data.endpoints.private-endpoint' | cut -d ":" -f1

Use these obtained values (``certificate-data`` and ``private-endpoint``) below and save it as ``user-data.yaml``.

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

Next, create a self-managed instance with the ``user-data.yaml`` just created. The value for ``subnet-id`` should correspond with the subnet used for the nodes in your OKE cluster.
    
.. code:: bash

  oci compute instance launch \
    --compartment-id <compartment-id> \
    --availability-domain <availability-domain> \
    --shape <instance-shape> \
    --image-id <ubuntu-image-id> \
    --subnet-id <nodes-subnet-ocid> \
    --user-data-file user-data.yaml \
    --display-name <instance-name>

Since this command creates a single instance (node), you can rerun it multiple times to create the desired number of nodes.

You can poll the status of the self-managed nodes using:

.. code:: bash

  kubectl get nodes --kubeconfig <config-path> --watch

Your self-managed node is ready to accept pods when its `STATUS` is `Ready`, indicating that everything is running as expected.

.. include:: ../../reuse/OKE-nodes.txt
   :start-after: Start: References and links
   :end-before: End: References and links
