Deploy Kubernetes with Ubuntu Pro on OpenShift
==============================================


Prerequisites
~~~~~~~~~~~~~

You need to have an existing OpenShift Cluster.

Limitations
~~~~~~~~~~~

OpenShift does not have Ubuntu Pro image offerings for the nodes, i.e. you cannot choose Ubuntu Pro images for the nodes.

	"RHCOS is the only supported operating system for OpenShift Container Platform control plane, or master, machines. While RHCOS is the default operating system for all cluster machines, you can create compute machines, which are also known as worker machines, that use RHEL as their operating system."

	-- `OpenShift docs <https://docs.openshift.com/container-platform/4.8/architecture/architecture-rhcos.html#rhcos-about_architecture-rhcos>`_


Conclusion
~~~~~~~~~~

You can reach out to `here <https://ubuntu.com/support/contact-us?product=contextual-footer-ua>`_ for attaching the cluster nodes to an Ubuntu Pro subscription, or contact rocks@canonical.com if you need additional support.

