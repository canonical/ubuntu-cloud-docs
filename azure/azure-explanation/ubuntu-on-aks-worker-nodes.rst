Ubuntu on AKS worker nodes
==========================

Azure Kubernetes Service (AKS) worker nodes use Ubuntu 22.04 LTS as their default operating system. The use of 22.04 LTS is recent. The earlier default was Ubuntu 18.04 LTS which is now out of standard support. So if you still run old AKS worker nodes with old versions of Kubernetes, you need to upgrade as Ubuntu 18.04 LTS no longer receives security fixes.

The Ubuntu images used by the AKS worker nodes are not directly published by Canonical. They are published by the AKS team at Azure, after applying a configuration layer on a base image provided by Canonical. `AgentBaker`_ is the open source customisation tool used for doing this. Canonical works closely with the AKS team on this.

.. important::

    Unattended upgrades are disabled on AKS worker nodes. The service 'unattended-upgrades', that is used to automatically upgrade Ubuntu for security-related fixes, is disabled on AKS worker nodes.


.. _`AgentBaker`: https://github.com/Azure/AgentBaker
