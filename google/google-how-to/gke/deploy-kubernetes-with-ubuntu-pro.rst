Deploy Kubernetes with Ubuntu Pro on GCE
========================================


Limitations - Why not use Pro on GKE?
-------------------------------------

Google does not have Ubuntu Pro image offerings for GKE (`Google Kubernetes Engine`_) nodes as yet, i.e. you cannot choose Ubuntu Pro images for GKE nodes. GKE does not support custom images for the nodes and neither does it allow post-deployment customization of node VMs.

	"Modifications on the boot disk of a node VM do not persist across node re-creations. Nodes are re-created during manual upgrade, auto-upgrade, auto-repair, and auto-scaling. In addition, nodes are re-created when you enable a feature that requires node re-creation, such as GKE Sandbox, intranode visibility, and shielded nodes."

	-- `GKE docs`_

Since there's no mechanism to enable Ubuntu Pro or pre-bake the UA token in a specific cluster, a managed Pro Kubernetes cluster in GKE is not currently possible.

So one option to get an Ubuntu Pro based Kubernetes cluster is to manually deploy and manage Kubernetes on Ubuntu Pro VMs in GCE.

Create Ubuntu Pro VMs 
---------------------

Create a few Ubuntu Pro VMs for your Kubernetes cluster - say ``k8s-worker-1`` and ``k8s-worker-2`` to act as worker nodes and ``k8s-main`` for the control plane. 

If you want to create them from the google console, refer to :ref:`create-pro-on-gcp`. Or you can also use the `gcloud CLI tool`_ to create the VMs:

.. code::

	gcloud compute instances create <instance-name> <options..>

To access the VMs via SSH use:

.. code::

	gcloud compute ssh --zone <instance-zone> <instance-name> --project <project-name>


Install Kubernetes
------------------

You can use `MicroK8s`_ to meet your Kubernetes needs. SSH into each node and install the snap:

.. code::

	# repeat for each node
	sudo snap install microk8s --classic


Create a cluster
----------------

Use the ``microk8s add-node`` command to create a cluster out of two or more MicroK8s instances. The instance on which this command is run will be the cluster's manager and will host the Kubernetes control plane. For further details, refer to the `MicroK8s clustering doc`_. 

1. On ``k8s-main`` run:

.. code::
 
	sudo microk8s add-node

On completion, it'll give instructions for adding another node to the cluster:

.. code::

	From the node you wish to join to this cluster, run the following:
	microk8s join 10.128.0.24:25000/bde599439dc4182f54fc39f1c444edf3/9713e9c1c063

	Use the '--worker' flag to join a node as a worker not running the control plane, eg:
	microk8s join 10.128.0.24:25000/bde599439dc4182f54fc39f1c444edf3/9713e9c1c063 --worker

	[...]
	

2. On ``k8s-worker-1`` (based on the instructions received) run:

.. code::

	sudo microk8s join 10.128.0.24:25000/bde599439dc4182f54fc39f1c444edf3/9713e9c1c063 --worker

This will add ``k8s-worker-1`` to the cluster as a worker node. Now, repeat these two steps for each worker node, i.e. run ``microk8s add-node`` on ``k8s-main`` and use the new token that is generated to add ``k8s-worker-2`` to the cluster.

Use the ``kubetl get nodes`` command in the control plane VM (``k8s-main``) to check that the nodes have joined the cluster:

.. code::

	sudo microk8s kubectl get nodes --output=wide

.. code::

	NAME           STATUS   ROLES    AGE   VERSION   INTERNAL-IP   EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION   CONTAINER-RUNTIME
	k8s-worker-1   Ready    <none>   13m   v1.27.5   10.128.0.25   <none>        Ubuntu 22.04.3 LTS   6.2.0-1014-gcp   containerd://1.6.15
	k8s-worker-2   Ready    <none>   28m   v1.27.5   10.128.0.26   <none>        Ubuntu 22.04.3 LTS   6.2.0-1014-gcp   containerd://1.6.15
	k8s-main       Ready    <none>   49m   v1.27.5   10.128.0.24   <none>        Ubuntu 22.04.3 LTS   6.2.0-1014-gcp   containerd://1.6.15



You can also check the cluster-info using the ``kubectl cluster-info`` command on ``k8s-main``:

.. code::

	microk8s kubectl cluster-info

.. code::

	Kubernetes control plane is running at https://127.0.0.1:16443
	CoreDNS is running at https://127.0.0.1:16443/api/v1/namespaces/kube-system/services/kube-dns:dns/proxy

	To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.



Access the Pro Kubernetes cluster
---------------------------------

You can access your Pro Kubernetes cluster from any working environment with a Kubernetes client. For this you'll need to allow external access to the control plane VM and also get the relevant kubeconfig file.

Allow external access to control plane VM
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**HTTPS traffic access** - On your google console, select the ``k8s-main`` instance and in the details page, go to :guilabel:`Edit` > :guilabel:`Networking` > :guilabel:`Firewalls` and enable :guilabel:`Allow HTTPS traffic`.

**Kubernetes port access** - Allow access to the Kubernetes port (16443 - found in response to the ``kubectl cluster-info`` command above), by creating a firewall rule in the `VPC firewall rules`_. For instructions on how to do that, refer to the `Google Cloud VPC docs`_.


Get the kubeconfig file
~~~~~~~~~~~~~~~~~~~~~~~

To access the cluster from your local workstation, you'll need to copy the appropriate `kubeconfig`_ file from your control plane VM. But before doing that, since you'll be connecting to the VM using its external IP address, you'll also have to ensure that the file's certificate is valid for the external IP address.

**Update certificate** - In your control plane VM, edit the ``/var/snap/microk8s/current/certs/csr.conf.template`` file to add the VM's external IP address in the "alt_names" section. The external IP address can be obtained from the `GCE VM Instances`_ page.

.. code::

	...
	[ alt_names ]
	DNS.1 = kubernetes
	DNS.2 = kubernetes.default
	IP.1 = 127.0.0.1
	IP.2 = 10.152.183.1
	#MOREIPS
	IP.100 = <External-IP>
	...

To refresh the certificates with the latest version of ``csr.conf.template``, run: 

.. code::
	
	sudo snap set microk8s test="$(date)"

**Get config file** - In your control plane VM, run:

.. code::

	sudo microk8s config

The output will be the required kubeconfig file, something like:

.. code::

	apiVersion: v1
	clusters:
	- cluster:
	    certificate-authority-data: <certificate>
	    server: https://10.128.0.24:16443
	name: microk8s-cluster
	contexts:
	- context:
	    cluster: microk8s-cluster
	    user: <username>
	name: microk8s
	current-context: microk8s
	kind: Config
	preferences: {}
	users:
	- name: <username>
	user:
	    token: <token>

Copy this to your local workstation as ``${HOME}/.kube/config``. Replace the server's private IP address with the external IP address and save it. 

Access the cluster
~~~~~~~~~~~~~~~~~~

You now have an Ubuntu Pro Kubernetes cluster running in GCE. You should be able to access it from your local workstation, using a Kubernetes client. To check the access, run:

.. code::

	kubectl get nodes --output=wide

This will show you details about your cluster nodes. You can verify the Pro subscription on each of the provisioned nodes by running ``pro status`` on them.


.. _`Google Kubernetes Engine`: https://cloud.google.com/kubernetes-engine
.. _`GKE docs`: https://cloud.google.com/kubernetes-engine/docs/concepts/node-images#modifications
.. _`gcloud CLI tool`: https://cloud.google.com/sdk/gcloud
.. _`MicroK8s`: https://microk8s.io/
.. _`MicroK8s clustering doc`: https://microk8s.io/docs/clustering
.. _`GCE VM Instances`: https://console.cloud.google.com/compute/instances
.. _`VPC firewall rules`: https://console.cloud.google.com/networking/firewalls/list
.. _`Google Cloud VPC docs`: https://cloud.google.com/firewall/docs/using-firewalls
.. _`kubeconfig`: https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig