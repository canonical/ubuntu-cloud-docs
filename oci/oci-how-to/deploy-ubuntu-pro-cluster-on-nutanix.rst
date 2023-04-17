Deploy Kubernetes with Ubuntu Pro on Nutanix
============================================


Prerequisites
~~~~~~~~~~~~~

You need to have an existing Nutanix Kubernetes cluster. See the
`Nutanix Karbon Guide <https://portal.nutanix.com/page/documents/details?targetId=Karbon-v2_4:kar-karbon-deploy-cluster-c.html>`_
to learn how to create a cluster.


Limitations
~~~~~~~~~~~

Nutanix does not have Ubuntu Pro offerings for the nodes, i.e. you cannot
choose Ubuntu Pro images for the nodes.

	"Deploying Kubernetes clusters in Karbon requires a **CentOS** image.
	You must choose from a CentOS version and download the image."

	-- `Nutanix docs: "Downloading Images" <https://portal.nutanix.com/page/documents/details?targetId=Karbon-v2_4:kar-karbon-upload-image-t.html>`_



Get an Ubuntu Pro subscription
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can reach out `here <https://ubuntu.com/support/contact-us?product=contextual-footer-ua>`_
to attach the cluster nodes to an Ubuntu Pro subscription, or contact
`rocks@canonical.com <mailto:rocks@canonical.com>`_ if you need additional support.


Conclusion
~~~~~~~~~~

After attaching your Ubuntu Pro subscription to the cluster nodes, you will have an
Ubuntu Pro Kubernetes cluster running on Nutanix.
