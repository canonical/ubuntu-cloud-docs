Deploy Ubuntu OKE nodes using Terraform
=======================================

.. include:: ../../reuse/OKE-nodes.txt
   :start-after: Start: Intro and prereqs
   :end-before: End: Intro and prereqs

.. include:: ../../reuse/OKE-nodes.txt
   :start-after: Start: Get Ubuntu image access
   :end-before: End: Get Ubuntu image access

.. include:: ../../reuse/OKE-nodes.txt
   :start-after: Start: Find an image
   :end-before: End: Find an image
  

Deploy an OKE cluster using Terraform
--------------------------------------

Before getting started, note the architecture of the image you have selected, either ``AMD64`` or ``ARM64``, as you want to ensure that nodes are launched with the correct instance shapes.

For this guide we'll use our `GitHub example repository <terraform-example-repo_>`_ as a base. It contains all of the HCL to launch the networking, cluster and nodes using the `OCI Terraform Provider <gh-oci-terraform-provider_>`_ and `OKE Terraform Module <gh-oke-terraform-module_>`_. 

Set up the Terraform project
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clone the `GitHub example repository <gh-example-repo_>`_ and change directory to the Terraform example:

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

Before deploying the OKE resources you must initialize the Terraform project. This will download all of the required providers and modules to launch the configuration.

.. code:: bash

    terraform init

The Terraform example includes a template to create your ``terraform.tfvars`` file. This file contains all of the cluster and image configurations including the Kubernetes version and image OCID.

.. code:: bash
    
    cp terraform.tfvars.example terraform.tfvars

Create an OKE cluster
~~~~~~~~~~~~~~~~~~~~~

Now the ``terraform.tfvars`` file should contain the following Terraform variable assignments.

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
    
    To be clear, you `cannot use any` Ubuntu ``image_id``, but only Ubuntu OKE specific images that have been listed from the CLI or images that you can find through the ``oci_core_images`` Terraform API. If you do find them through the Terraform API, they must be specifically denoted as Ubuntu OKE.

After configuring your ``terraform.tfvars``, deploy a cluster using:

.. code:: bash
   
    terraform apply

Terraform will then provide a permission prompt for creating all the required OKE cluster resources:

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


After agreeing, the required cluster resources will be created, but by default you will not have access to the cluster. The Terraform example does provide the cluster's ``kubeconfig`` via an ``output`` though. The following command will create the ``~/.kube/`` directory and write the ``kubeconfig`` to ``~/.kube/config``.

.. code:: bash
    
    mkdir -p ~/.kube/
    terraform output -json cluster_kubeconfig | yq -p json | tee ~/.kube/config

This will allow you to verify cluster connectivity, using:

.. code:: bash
    
    kubectl cluster-info

The output should indicate that you are connected to the cluster:

.. code:: console

    Kubernetes control plane is running at https://<public-ip>:6443
    CoreDNS is running at https://<public-ip>:6443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

Add OKE nodes
~~~~~~~~~~~~~

You now have a cluster at your disposal but there aren't any nodes added yet. You can view the node status with:

.. code:: bash

    kubectl get nodes

to get as output:

.. code:: console

    No resources found


OKE offers two different node types to add to the cluster, `Managed <managed-nodes-docs_>`_ and `Self-Managed <self-managed-nodes-docs_>`_. From an Ubuntu OKE node perspective, the differences are regarding the ``user-data`` that is provided to the nodes through ``cloud-init`` and how the nodes are provisioned -- node pools for Managed and instances for Self-Managed.

These differences are illustrated in the two ``.yaml`` files present in the ``user-data`` folder of the Terraform example.

The Managed nodes ``user-data`` is quite simple:

.. code:: yaml
   
    #cloud-config

    runcmd:
    - oke bootstrap

While the Self-Managed ``user-data`` requires variable substitution from Terraform for the cluster certificate and private control plane IP:

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


To launch Ubuntu OKE nodes of these types, in ``terraform.tfvars``, set the variables ``add_managed_nodes`` or ``add_self_managed_nodes`` to ``true``:

.. code:: terraform

    # Optional
    public_nodes           = false
    architecture           = "amd64"
    add_managed_nodes      = true
    add_self_managed_nodes = true

.. note::

    Both node types can be enabled independently, therefore you could have just Self-Managed, Managed or both.

Once these variables are set, the next time you run ``terraform apply``, Terraform will attempt to update the state and create the nodes.

Alternatively, you can override these variables directly from the command line and they will override the ``terraform.tfvars`` file:

.. code:: bash

    terraform apply -var="add_managed_nodes=true" -var="add_self_managed_nodes=true"

After executing ``terraform apply`` with one of the methods above, Terraform will begin updating the state and creating the appropriate nodes. You can watch the nodes register in the cluster with:

.. code:: bash

    kubectl get nodes --watch

Which should provide output similar to:

.. code:: none

    NAME           STATUS   ROLES    AGE   VERSION
    10.0.101.01    Ready    node     2m    v1.32.1
    10.0.102.02    Ready    node     2m    v1.32.1
    10.0.103.03    Ready    node     2m    v1.32.1


Delete the OKE cluster
----------------------

If you wish to delete the nodes but maintain the cluster then disable the node variables using:

.. code:: bash
   
    terraform apply -var="add_managed_nodes=false"
    
Alternatively, you can tear down the nodes and all other resources deployed by Terraform using:

.. code:: bash
    
    terraform destroy

.. include:: ../../reuse/OKE-nodes.txt
   :start-after: Start: References and links
   :end-before: End: References and links
