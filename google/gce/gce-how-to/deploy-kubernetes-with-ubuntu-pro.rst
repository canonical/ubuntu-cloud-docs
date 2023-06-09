Deploy Kubernetes with Ubuntu Pro on GCE
========================================


Limitations - Why not GKE?
--------------------------

As yet, Google does not have Ubuntu Pro image offerings for the GKE
(`Google Kubernetes Engine <https://cloud.google.com/kubernetes-engine>`_)
nodes, i.e. you cannot choose Ubuntu Pro images for the GKE nodes. GKE does not
support custom images for the nodes either. Additionally, GKE does not allow
post-deployment customisation of node VMs.

	"Modifications on the boot disk of a node VM do not persist across node re-creations.
	Nodes are re-created during manual upgrade, auto-upgrade, auto-repair, and auto-scaling.
	In addition, nodes are re-created when you enable a feature that requires node re-creation,
	such as GKE Sandbox, intranode visibility, and shielded nodes."

	-- `GKE docs <https://cloud.google.com/kubernetes-engine/docs/concepts/node-images#modifications>`_

Given that, currently, there's no mechanism to either enable Ubuntu Pro or pre-bake the UA token
in a specific cluster. So the managed Pro Kubernetes cluster is not applicable in GKE.


Deploy Kubernetes manually on Ubuntu Pro VMs
--------------------------------------------

One solution to have an Ubuntu Pro cluster is to deploy and manage Kubernetes manually on
Ubuntu Pro VMs available in GCE.

Create Ubuntu Pro VMs for the control plane and worker nodes
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a few Ubuntu Pro VMs for the worker nodes and control plane from the
`GCE VM instances <https://console.cloud.google.com/compute/instances>`_ page.
Use the `CREATE INSTANCE <https://console.cloud.google.com/compute/instancesAdd>`_ button
which takes you to the configuration details before creating the VM.

Make sure to change the boot disk configuration so that the operating system
is "Ubuntu Pro". There are a few versions to choose from, such as:

- Ubuntu 16.04 LTS Pro Server
- Ubuntu 18.04 LTS Pro Server
- Ubuntu 20.04 LTS Pro Server
- Ubuntu 22.04 LTS Pro Server
- Ubuntu 18.04 LTS Pro FIPS Server
- Ubuntu 20.04 LTS Pro FIPS Server

Choose the version suitable for your needs, and create the VMs.

As an example, you can create three "Ubuntu 20.04 LTS Pro FIPS Server" VMs for the Kubernetes cluster:

- ``k8s-worker-1`` and ``k8s-worker-2`` as worker nodes, and
- ``k8s-main`` as the control plane.

You can also utilise the `gcloud CLI tool <https://cloud.google.com/sdk/gcloud>`_ to deploy the VMs
with the following command.

::

	gcloud compute instances create <instance-name> <options..>

You can access the VMs via SSH with the following command.

::

	gcloud compute ssh --zone <instance-zone> <instance-name> --project <project-name>

Install Kubernetes and create a cluster
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can use `MicroK8s <https://microk8s.io/>`_ to meet your Kubernetes needs.
Install the snap on each node:

::

	# repeat for each node
	sudo snap install microk8s --classic

To create a cluster out of two or more already-running MicroK8s instances, use the
``microk8s add-node`` command. The MicroK8s instance on which this command is run
will be the cluster's manager and will host the Kubernetes control plane.

Considering the example VMs from above, run the following command in ``k8s-main``::
 
	root@k8s-main:~$ microk8s add-node
	
Then, SSH into each of the worker nodes and execute the following command to join the cluster as a worker::

	# repeat for each worker node
	root@k8s-worker-1:~$ microk8s join 10.128.0.7:25000/3a9547446eae54765ecc0bc522321968/079215076aa1 --worker
	Contacting cluster at 10.128.0.7

	The node has joined the cluster and will appear in the nodes list in a few seconds.

	This worker node gets automatically configured with the API server endpoints.
	If the API servers are behind a loadbalancer please set the '--refresh-interval' to '0s' in:
		/var/snap/microk8s/current/args/apiserver-proxy
	and replace the API server endpoints with the one provided by the loadbalancer in:
		/var/snap/microk8s/current/args/traefik/provider.yaml

Note that the IP address, port, and token used here are project specific and 
you may not have the same values. You can find more info in the 
`MicroK8s clustering doc <https://microk8s.io/docs/clustering>`_.

In the control plane VM, you should be able to see that the nodes have joined the cluster using
the ``kubetl get nodes`` command.

::

	root@k8s-main:~$ microk8s kubectl get nodes --output=wide
	NAME           STATUS   ROLES    AGE     VERSION   INTERNAL-IP   EXTERNAL-IP   OS-IMAGE             KERNEL-VERSION        CONTAINER-RUNTIME
	k8s-worker-2   Ready    <none>   2m13s   v1.26.1   10.128.0.10   <none>        Ubuntu 20.04.5 LTS   5.4.0-1021-gcp-fips   containerd://1.6.8
	k8s-main       Ready    <none>   78m     v1.26.1   10.128.0.7    <none>        Ubuntu 20.04.5 LTS   5.4.0-1021-gcp-fips   containerd://1.6.8
	k8s-worker-1   Ready    <none>   16m     v1.26.1   10.128.0.8    <none>        Ubuntu 20.04.5 LTS   5.4.0-1021-gcp-fips   containerd://1.6.8

You can also check the cluster-info using the ``kubectl cluster-info`` command.

::

	root@k8s-main:~$ microk8s kubectl cluster-info
	Kubernetes control plane is running at https://127.0.0.1:16443

	To further debug and diagnose cluster problems, use 'kubectl cluster-info dump'.


Access the Pro Kubernetes cluster
---------------------------------

You can access your Pro Kubernetes cluster from any working environment with a Kubernetes
client.

Update firewall to allow HTTPS traffic
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On the control plane VM, during creation if you haven't allowed HTTPS traffic in the firewall, 
you can allow it by editing the configuration on the `GCE VM Instances`_ page. Select the VM 
name to access the instance details page and use the "Edit" button to change the configuration.
In the "Networking" section, you'll find a header named "Firewall". Check the "Allow
HTTPS traffic" box there and save. This should add a network tag ``https-server`` to your VM.

.. image:: deploy-kubernetes-with-ubuntu-pro-images/0_allow_https_traffic.png
   :align: center

You also need to allow access to the port on which your control plane is running. 
You can find this port number using the ``kubectl cluster-info``
command as demonstrated at the end of the `previous section <#install-kubernetes-and-create-a-cluster>`_.
Allow this port for your control plane VM by creating a firewall rule in
`VPC firewall rules <https://console.cloud.google.com/networking/firewalls/list>`_.
You can follow the `Google Cloud VPC docs <https://cloud.google.com/vpc/docs/using-firewalls>`_
to do so.

Manage cluster access with the kubeconfig file
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You will finally need the
`kubeconfig <https://kubernetes.io/docs/concepts/configuration/organize-cluster-access-kubeconfig/>`_
file to access the cluster from your local workstation. Running the ``microk8s config`` command in
your control plane VM will output the kubeconfig file from MicroK8s.

::

	root@k8s-main:~$ microk8s config
	apiVersion: v1
	clusters:
	- cluster:
	    certificate-authority-data: <certificate>
	    server: https://10.128.0.7:16443
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

Copy and save this as ``${HOME}/.kube/config`` on your local workstation. Notice that the server
IP address in the cluster is a private one. Replace that IP address with your control plane VM's "External IP"
which you can find on the `GCE VM Instances`_ page. This alone would not work however, since the
<certificate> for the cluster is not valid for the External IP address.

In your control plane VM, edit the ``/var/snap/microk8s/current/certs/csr.conf.template`` file,
and add the External IP address in the "alt_names" section to issue the certificate for the External
IP address as well.

::

	/var/snap/microk8s/current/certs/csr.conf.template
	...
	...
	[ alt_names ]
	DNS.1 = kubernetes
	DNS.2 = kubernetes.default
	IP.1 = 127.0.0.1
	IP.2 = 10.152.183.1
	#MOREIPS
	IP.100 = <External-IP>
	...
	...

Run the following command to refresh the certificates by using the latest version of
``csr.conf.template``.
`Learn more <https://github.com/canonical/microk8s/issues/421#issuecomment-1420387408>`_.

::
	
	sudo snap set microk8s test="$(date)"

Now, create the kubeconfig file again using the ``microk8s config`` command. Copy and save it
to the ``${HOME}/.kube/config`` file in your local workstation. Replace the server's private IP
address with the External IP address and save. You should now be able to access the cluster from your local
workstation. Run the following command on your local workstation to check.

::

	kubectl get nodes --output=wide


Verify Pro subscription
-----------------------

You now have an Ubuntu Pro Kubernetes cluster running in GCE. Your Pro subscription can be
verified on each of the provisioned nodes by running:

::

	pro status


