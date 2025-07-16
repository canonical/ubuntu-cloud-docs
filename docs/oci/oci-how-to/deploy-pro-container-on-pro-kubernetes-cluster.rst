.. _how-to-deploy-pro-container-on-pro-cluster:

Deploy Ubuntu Pro containers on Kubernetes
******************************************

You can easily deploy your Ubuntu Pro container images on Kubernetes clusters, provided
that said clusters are composed of Ubuntu Pro nodes. Read more on the
`Ubuntu Pro <https://ubuntu.com/pro>`_ website.


Prerequisites
-------------

You will need

- an Ubuntu Pro container image on a private registry. This can be built using the procedure given at 
  :ref:`Building Ubuntu Pro OCI images <ubuntu-pro-oci-container-images>`. Since the image is attached to your Ubuntu Pro subscription, it should be kept private to avoid the sharing of your Ubuntu Pro subscription with unwanted users. 

- a Kubernetes cluster with an Ubuntu Pro subscription. To learn to deploy it for different clouds, refer to the options shown below: 

Deploying Pro Kubernetes clusters in various clouds
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. tabs::

	.. tab:: EKS

		Check out :doc:`aws:aws-how-to/kubernetes/deploy-ubuntu-pro-cluster` to learn
		how to deploy an Ubuntu Pro Kubernetes cluster on Elastic Kubernetes Service (EKS).

	.. tab:: GCE

		Check out :doc:`google:google-how-to/gke/deploy-kubernetes-with-ubuntu-pro` to learn
		how to deploy an Ubuntu Pro Kubernetes cluster on Google Compute Engine (GCE).

	.. tab:: OpenShift

		See the `OpenShift guide <https://docs.redhat.com/en/documentation/openshift_container_platform/4.8/html/installing/ocp-installation-overview>`_
		to learn how to create a cluster.


		**Limitations**

		Although OpenShift can be deployed on public clouds, it does not support
		having Ubuntu Pro instances as cluster nodes.

			"RHCOS is the only supported operating system for OpenShift Container Platform control plane, or master, machines. While RHCOS is the default operating system for all cluster machines, you can create compute machines, which are also known as worker machines, that use RHEL as their operating system."

			-- `OpenShift docs <https://docs.openshift.com/container-platform/4.8/architecture/architecture-rhcos.html#rhcos-about_architecture-rhcos>`_


		**Get an Ubuntu Pro subscription**

		You can `reach out to us <https://ubuntu.com/support/contact-us?product=contextual-footer-ua>`_
		to attach the cluster nodes to an Ubuntu Pro subscription, or contact
		`rocks@canonical.com <mailto:rocks@canonical.com>`_ if you need additional support.


		**Success**

		After attaching your Ubuntu Pro subscription to the cluster nodes, you will have an
		Ubuntu Pro Kubernetes cluster running on OpenShift.

	.. tab:: Tanzu

		See the `Tanzu guide <https://techdocs.broadcom.com/us/en/vmware-tanzu/standalone-components/tanzu-kubernetes-grid/2-5.html>`_
		to learn how to create a cluster.

		**Get an Ubuntu Pro subscription**

		If the resulting Kubernetes cluster is composed of Ubuntu nodes, you must attach them
		to a Pro subscription as described in `this tutorial <https://ubuntu.com/pro/tutorial>`_. Otherwise,
		if the Kubernetes cluster is not running on Ubuntu nodes, you can 
		`contact us <https://ubuntu.com/support/contact-us?product=contextual-footer-ua>`_
		to attach the nodes to an Ubuntu Pro subscription, or contact
		`rocks@canonical.com <mailto:rocks@canonical.com>`_ if you need additional support.

		**Success**

		After attaching your Ubuntu Pro subscription to the cluster nodes, you will have an
		Ubuntu Pro Kubernetes cluster running on Tanzu.

	.. tab:: Nutanix

		See the `Nutanix Karbon Guide <https://portal.nutanix.com/page/documents/details?targetId=Karbon-v2_4:kar-karbon-deploy-cluster-c.html>`_
		to learn how to create a cluster.


		**Limitations**

		Nutanix does not have Ubuntu Pro offerings for the nodes, i.e. you cannot
		choose Ubuntu Pro images for the nodes.

			"Deploying Kubernetes clusters in Karbon requires a **CentOS** image.
			You must choose from a CentOS version and download the image."

			-- `Nutanix docs: "Downloading Images" <https://portal.nutanix.com/page/documents/details?targetId=Karbon-v2_4:kar-karbon-upload-image-t.html>`_



		**Get an Ubuntu Pro subscription**

		You can `contact us <https://ubuntu.com/support/contact-us?product=contextual-footer-ua>`_
		to attach the cluster nodes to an Ubuntu Pro subscription, or contact
		`rocks@canonical.com <mailto:rocks@canonical.com>`_ if you need additional support.


		**Success**

		After attaching your Ubuntu Pro subscription to the cluster nodes, you will have an
		Ubuntu Pro Kubernetes cluster running on Nutanix.

.. _create-k8s-secret:

Create a Secret for Private Registry
------------------------------------

Since your Ubuntu Pro container image is in a private registry, you will need to create a
`secret <https://kubernetes.io/docs/concepts/configuration/secret/>`_ in Kubernetes
(For more details about pulling images from private registries, check out the `Kubernetes documentation <https://kubernetes.io/docs/tasks/configure-pod-container/pull-image-private-registry/>`_).

You can use the following example command to create a secret named ``regcred`` for
`Docker Hub <https://hub.docker.com>`_  (i.e. using ``https://index.docker.io/v1/``
as ``<your-registry-server>``).

::

	kubectl create secret docker-registry regcred \
	    --docker-server=<your-registry-server> \
	    --docker-username=<your-username> \
	    --docker-password=<your-password> \
	    --docker-email=<your-email>


Deploy Pro container image to Pro Kubernetes cluster
----------------------------------------------------

You can deploy your Pro container image in a `Pod`_, `Deployment`_, or as a `Service`_.
Make sure to include your created :ref:`secret <create-k8s-secret>` and your Pro container image correctly.

.. _Pod: https://kubernetes.io/docs/concepts/workloads/pods/
.. _Deployment: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
.. _Service: https://kubernetes.io/docs/concepts/services-networking/service/

Here is a manifest for a Pod that consists of a container running your
Ubuntu Pro image. It uses your secret ``regcred`` to pull the Pro container image
from your private registry.

::

	# pro-container-pod.yaml
	apiVersion: v1
	kind: Pod
	metadata:
	  name: pro-container-pod
	spec:
	  imagePullSecrets:
	  - name: regcred
	  containers:
	  - name: ubuntu-pro-container
	    image: <your-private-pro-image>
	  restartPolicy: OnFailure

Replace ``<your-private-pro-image>`` with your private Pro container image (something
similar to ``janedoe/jdoe-private:v1`` for Docker Hub).

Create the Pod, and verify that the Pod is running:

::

	kubectl apply -f pro-container-pod.yaml
	kubectl get pod pro-container-pod


Check pod logs
--------------

Your Pro container image is deployed in the Pro Kubernetes cluster and running inside
a Pod. You can check the logs by running:

::

	kubectl logs pod/pro-container-pod
