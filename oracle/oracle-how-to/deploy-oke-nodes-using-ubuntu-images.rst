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

- `Domain`_, `Dynamic Group and Policy`_ configured (Self-Managed only). 


Find an Ubuntu image
-----------------------

Select a version from the :doc:`available releases </oracle-reference/ubuntu-availability-on-oke>`. The images are listed as JSON in ascending order, therefore the latest image will be at the bottom. Make note of the image path for the image you choose. The image path conforms to the following format:

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
    
        Start the registration process in Oracle Cloud by navigating to :guilabel:`Compute` > :guilabel:`Custom Images` and select :guilabel:`Import Image`. Select :guilabel:`Import from an Object Storage URL`, then paste the :doc:`available releases </oracle-reference/ubuntu-availability-on-oke>` location link with your concatenated image path into the :guilabel:`Object Storage URL` field. The URL format pasted should conform to the following:

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

Deploy OKE Cluster with Ubuntu using OCI Web Console
-----------------------------------------------------

Since this is a Limited Availability release of Ubuntu images for OKE, you can only create managed nodes through the Oracle Cloud API (``oci`` CLI, SDK, or Terraform). The ability to create managed nodes from the Oracle Cloud UI will be added later.

Deploy OKE Cluster with Ubuntu using CLI
-----------------------------------------

Deploying an OKE cluster with Ubuntu using the ``oci`` CLI involves three main steps:

* Create the required network resources for the cluster.
* Create the OKE cluster.
* Create a `managed node pool <cli-managed-nodes_>`_ or `self-managed nodes <cli-self-managed-nodes_>`_ with Ubuntu images.

If you already have a cluster, you can skip directly to `creating a managed node pool <cli-managed-nodes_>`_ or `self-managed nodes <cli-self-managed-nodes_>`_.

Create network resources for cluster deployment
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Before you can create and deploy an OKE cluster, you need to create the necessary network resources. This includes a Virtual Cloud Network (VCN), subnets, internet gateway, route table, and more. For a complete guide on how to set up the network resources, refer to the Oracle documentation on `cluster networking <cluster-networking_>`_.

Setting up a VCN typically involves the following (this is not an exhaustive list):

* A CIDR block (range of IP addresses) for the cluster nodes.
* An internet gateway (if using public subnets).
* A NAT gateway and a service gateway (if using private subnets).
* A route table (required if using gateways).
* Subnets for worker nodes, control plane, and load balancers.
* Security rules defined in security lists to control traffic between nodes and the control plane.

For a full working example, please refer to our `GitHub example repository <cli-example-repo_>`_.

The following command can be used to create a VCN using the ``oci`` CLI. Replace the placeholders with your own values.

.. code:: bash
  
  oci network vcn create \
  --compartment-id <compartment-id> \
  --display-name <vcn-name> \
  --cidr-block <vcn-cidr-block>
  
The next step is to create an internet gateway, a NAT gateway and/or a service gateway. To determine which of them are needed for your cluster, refer to the Oracle documentation for `network configuration <cluster-networking_>`_.
      
.. code:: bash
  
  # Create internet gateway
  oci network internet-gateway create \
    --compartment-id <compartment-id> \
    --vcn-id <vcn-id> \
    --is-enabled true

Next up, refer to the Oracle documentation for `security lists`_ for information on creating security rules for the nodes, control plane, and service load balancer. You can create a security list using the following command:

.. code:: bash
  
  oci network security-list create \
  --compartment-id <compartment-id> \
  --vcn-id <vcn-id> \
  --display-name <security-list-name> \
  --egress-security-rules <rules> \
  --ingress-security-rules <rules>
                
Now that you have the VCN, gateways, and security lists, you can create the route table and the subnets. The subnets will be used for the worker nodes, control plane, and load balancers.

You can create a route table and a subnet using the following commands.
      
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
      
  # Optionally, create a control plane subnet
  # and a service load balancer subnet

Create the OKE cluster
~~~~~~~~~~~~~~~~~~~~~~~

To create the OKE cluster, you will need to provide the compartment ID, the VCN OCID, and optionally, the subnets for the control plane and service load balancer. For more details on cluster creation, please refer to the Oracle documentation on `creating a cluster`_.

The following command will create the OKE cluster.

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
      
Once the cluster is created, you can create a kubeconfig file to access the cluster through `kubectl`. The following command will generate the kubeconfig file:

.. code:: bash
  
  oci ce cluster create-kubeconfig \
      --cluster-id <cluster-id> \
      --file <path-to-kube-config> \
      --kube-endpoint PUBLIC_ENDPOINT

.. _cli-managed-nodes:

Create managed OKE nodes with Ubuntu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Managed nodes are node instances whose lifecycle is managed by the OKE service. 
      
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
      "subnetId":"<nodes-subnet-ocid>"
    }]


Lastly, replace the values and run the following command to create the managed node pool:

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

To view the node pool status, use ``kubectl`` with the previously created ``kubeconfig``.

.. code:: bash

  kubectl get nodes --kubeconfig <config-path> --watch

All the nodes should show :guilabel:`STATUS` as :guilabel:`Ready` once everything is running as expected.  

.. _cli-self-managed-nodes:

Create self-managed OKE nodes with Ubuntu
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The following instructions assume that you have configured the domain, dynamic group, and policy as mentioned in the `prerequisites <Prerequisites_>`_. If you have not done this, refer to the Oracle documentation for `working with self-managed nodes`_

Next, the self-managed node will need a custom `cloud-init` script which needs some specific values, namely a Kubernetes certificate from the OKE cluster and the Kubernetes API private endpoint.

Obtain the Kubernetes certificate for the current context with the following command:

.. code:: bash

   kubectl config view --minify --raw -o json | jq -r '.clusters[].cluster."certificate-authority-data"'

Then obtain the ``Kubernetes API private endpoint`` using the following ``oci`` command:

.. code:: bash

   oci ce cluster get --cluster-id <cluster-id> | jq -r '.data.endpoints.private-endpoint' | cut -d ":" -f1

Use these obtained values (``certificate-data`` and ``private-endpoint``) in the following example and save it as ``user-data.yaml``.

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

The following command will create a self-managed instance with your previously created ``user-data.yaml``. The value for ``subnet-id`` should correspond with the subnet used for the nodes in your OKE cluster.
    
.. code:: bash

  oci compute instance launch \
    --compartment-id <compartment-id> \
    --availability-domain <availability-domain> \
    --shape <instance-shape> \
    --image-id <ubuntu-image-id> \
    --subnet-id <nodes-subnet-ocid> \
    --user-data-file user-data.yaml \
    --display-name <instance-name>

You can poll the status of the self-managed nodes with the following command:

.. code:: bash

  kubectl get nodes --kubeconfig <config-path> --watch

Your self-managed node is ready to accept pods when its :guilabel:`STATUS` is :guilabel:`Ready`, indicating that everything is running as expected.

Deploy OKE Cluster with Ubuntu using Terraform
-----------------------------------------------

Before getting started, confirm that you have all of the `Prerequisites <#prerequisites>`_ and ensure that you have an `Ubuntu OKE image registered <#register-an-ubuntu-image>`_. Make note of the architecture for the registered image, either ``amd64`` or ``arm64``, as you want ensure nodes are launched with the correct instance shapes.

For this guide we'll use our `GitHub example repository <terraform-example-repo_>`_ as a base. It contains all of the HCL to launch the networking, cluster and nodes using the `OCI Terraform Provider <gh-oci-terraform-provider_>`_ and `OKE Terraform Module <gh-oke-terraform-module_>`_. 

Setting up the Terraform Project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get started by cloning the `GitHub example repository <terraform-example-repo_>`_ and change directory to the Terraform example.

.. code:: bash

    git clone https://github.com/canonical/oracle-doc-examples
    cd oracle-doc-examples/deploy-oke-using-ubuntu/terraform

The Terraform example directory should look like the following.

.. code:: console
    
    .
    ├── data.tf
    ├── locals.tf
    ├── modules.tf
    ├── outputs.tf
    ├── providers.tf
    ├── README.md
    ├── self_managed.tf
    ├── terraform.tfvars.example
    ├── user-data
    │   ├── managed.yaml
    │   └── self-managed.yaml
    └── variables.tf

Before deploying the OKE resources you must initialize the Terraform project with the following command. This will download all of the required providers and modules to launch the configuration.

.. code:: bash

    terraform init

The Terraform example includes a template to create your ``terraform.tfvars`` file. This file contains all of the cluster and image configurations including the Kubernetes version and image OCID.

.. code:: bash
    
    cp terraform.tfvars.example terraform.tfvars

Creating the OKE Cluster
~~~~~~~~~~~~~~~~~~~~~~~~

Once you completed the `Setting up the Terraform Project <#setting-up-the-terraform-project>`_ section, the contents of ``terraform.tfvars`` should contain the following Terraform variable assignments.

.. code:: terraform
    
    # Required
    tenancy_ocid         = "ocid1.tenancy.oc1..xxxxxxxxxxx"
    user_ocid            = "ocid1.user.oc1..xxxxxxxxxxx"
    compartment_ocid     = "ocid1.compartment.oc1..xxxxxxxxxxx"
    fingerprint          = "xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx:xx"
    private_key_path     = "~/.oci/oci.pem"
    region               = "us-phoenix-1"
    kubernetes_version   = "v1.32.1"
    image_id             = "ocid1.image.oc1.phx.xxxxxxxxxxx"
    ssh_public_key_path  = "~/.ssh/id_rsa.pub"
    ssh_private_key_path = "~/.ssh/id_rsa"
    
    # Optional
    public_nodes           = false
    architecture           = "amd64"  # or "arm64"
    add_managed_nodes      = false
    add_self_managed_nodes = false

Most of the values for the ``terraform.tfvars`` can be found in your ``~/.oci/config`` file or by searching for each service in the OCI Web Console. 

.. note:: 
    
    To be clear, you `cannot use any` Ubuntu ``image_id``, but only Ubuntu OKE specific images that have been `downloaded <ubuntu-oke-availability_>`_ and `registered <#register-an-ubuntu-image>`_ or images that you can found through the ``oci_core_images`` Terraform API. If you do find them through the Terraform API, they must be denoted as specifically Ubuntu OKE.

After configuring your ``terraform.tfvars`` then you are able to deploy a cluster with the following command.

.. code:: bash
   
    terraform apply

Terraform will then provide the following permission prompt for creating all the required OKE cluster resources.

.. code:: console

    Plan: 61 to add, 0 to change, 0 to destroy.
    
    Changes to Outputs:
      + apiserver_private_host = (known after apply)
      + cluster_ca_cert        = (known after apply)
      + cluster_endpoints      = (known after apply)
      + cluster_id             = (known after apply)
      + cluster_kubeconfig     = (known after apply)
      + vcn_id                 = (known after apply)
      + worker_subnet_id       = (known after apply)
    
    Do you want to perform these actions?
      Terraform will perform the actions described above.
      Only 'yes' will be accepted to approve.
    
      Enter a value:  yes


After agreeing, the required cluster resources will be created but by default you will not have access to the cluster. The Terraform example does provide the cluster's ``kubeconfig`` via an ``output`` though. The following command will create the ``~/.kube/`` directory and write the ``kubeconfig`` to ``~/.kube/config``.

.. code:: bash
    
    mkdir -p ~/.kube/
    terraform output -json cluster_kubeconfig | yq -p json | tee ~/.kube/config

Which should allow you to verify cluster connectivity.

.. code:: bash
    
    kubectl cluster-info

The following indicates you connected to the cluster.

.. code:: console

    Kubernetes control plane is running at https://<public-ip>:6443
    CoreDNS is running at https://<public-ip>:6443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

Adding OKE Nodes with Ubuntu 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

After completing the `Creating the OKE Cluster <#creating-the-oke-cluster>`_ section, you will now have a cluster at your disposal but there aren't any nodes added yet. You can view the node status with the following command.

.. code:: bash

    kubectl get nodes

This output verifies there aren't any nodes in the cluster.

.. code:: console

    No resources found


To clarify, OKE offers 2 different node types to add to the cluster, `Managed <managed-nodes-docs_>`_ and `Self-Managed <self-managed-nodes-docs_>`_. From an Ubuntu OKE node perspective, the differences are regarding the ``user-data`` that is provided to the nodes through ``cloud-init`` and how the nodes are provisioned, Node Pools for Managed and Instances for Self-Managed.

To further illustrate these differences, the following ``user-data`` below is from the Terraform example.

The Managed nodes ``user-data`` is quite simple.

.. code:: yaml
   
    #cloud-config

    runcmd:
    - oke bootstrap

While the Self-Managed ``user-data`` requires variable substitution from Terraform for the cluster certificate and private control plane IP.

.. code:: yaml

   #cloud-config

    runcmd:
      - oke bootstrap --ca ${cluster_ca_cert} --apiserver-host ${api_server_endpoint}
    
    write_files:
      - path: /etc/oke/oke-apiserver
        permissions: '0644'
        content: ${api_server_endpoint}
      - encoding: b64
        path: /etc/kubernetes/ca.crt
        permissions: '0644'
        content: ${cluster_ca_cert}


Finally, to actually launch Ubuntu OKE nodes we can do this by configuring the variables assigned in ``terraform.tfvars`` or by command-line override.

Recall the contents of ``terraform.tfvars``.

.. code:: terraform

    # Optional
    public_nodes           = false
    architecture           = "amd64"
    add_managed_nodes      = false
    add_self_managed_nodes = false

If you set ``add_managed_nodes`` or ``add_self_managed_nodes`` to ``true``, then the next time you run ``terraform apply``, Terraform will attempt to update the state and create the nodes.

Alternatively, you can override these variables directly from the command line and they will override the ``terraform.tfvars`` file.

.. code:: bash

    terraform apply -var="add_managed_nodes=true" -var="add_self_managed_nodes=true"

.. note::

    Both node types can be enabled independently, therefore you could have just Self-Managed, Managed or both.

After executing ``terraform apply`` with one of the methods above then Terraform will begin updating the state and creating the appropriate nodes. You can watch the nodes register in the cluster with the following command.

.. code:: bash

    kubectl get nodes --watch

Which should provide output similar to:

.. code:: none

    NAME           STATUS   ROLES    AGE   VERSION
    10.0.101.01    Ready    node     2m    v1.32.1
    10.0.102.02    Ready    node     2m    v1.32.1
    10.0.103.03    Ready    node     2m    v1.32.1


If you wish to delete the nodes but maintain the cluster then all you need is disable the node variables like:

.. code:: bash
   
    terraform apply -var="add_managed_nodes=false"
    
Alternatively, you can tear down the nodes and all other resources deployed by Terraform with the following command.

.. code:: bash
    
    terraform destroy

Further references
------------------

For more information about ``oci`` CLI and managing self-managed nodes on your cluster, refer to the Oracle Documentation:

* `oci CLI documentation`_
* `Creating and managing kubernetes clusters`_
* `Creating a dynamic group and a policy for self-managed nodes <Dynamic Group and Policy_>`_
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
.. _`Dynamic Group and Policy`: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengdynamicgrouppolicyforselfmanagednodes.htm
.. _`Creating cloud-init scripts for self-managed nodes`: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengcloudinitforselfmanagednodes.htm
.. _`Domain`: https://docs.oracle.com/en-us/iaas/Content/Identity/domains/to-create-new-identity-domain.htm
.. _`cluster-networking`: https://docs.oracle.com/en-us/iaas/Content/ContEng/Concepts/contengnetworkconfig.htm
.. _`cli-example-repo`: https://github.com/canonical/oracle-doc-examples/tree/main/deploy-oke-using-ubuntu/cli
.. _`terraform-example-repo`: https://github.com/canonical/oracle-doc-examples/tree/main/deploy-oke-using-ubuntu/terraform
.. _`security lists`: https://docs.oracle.com/en-us/iaas/Content/Network/Tasks/managingsecuritylists.htm
.. _`ubuntu-oke-availability`: https://canonical-oracle.readthedocs-hosted.com/oracle-reference/ubuntu-availability-on-oke/
.. _`gh-oci-terraform-provider`: https://github.com/oracle/terraform-provider-oci
.. _`gh-oke-terraform-module`: https://github.com/oracle-terraform-modules/terraform-oci-oke
.. _`managed-nodes-docs`: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithmanagednodes.htm
.. _`self-managed-nodes-docs`: https://docs.oracle.com/en-us/iaas/Content/ContEng/Tasks/contengworkingwithselfmanagednodes.htm
