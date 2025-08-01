Ubuntu on AKS worker nodes
==========================

Overview
--------

Ubuntu is the default operating system for worker nodes in the Azure Kubernetes Service (AKS). It is used in both system node pools and user node pools. The Ubuntu images are provided by Canonical and customized by Microsoft to ensure enhanced compatibility within the AKS environment. Specific methods are available to ensure timely security updates for these images.


Image customization
-------------------

Canonical closely collaborates with the Azure AKS team to ensure that the Ubuntu images are appropriately configured for optimal performance. The customization is done using `AgentBaker`_, an open-source tool.


Security updates
----------------

For automatic security updates, traditional Ubuntu systems use `unattended-upgrades`_. However, AKS offers a node update method for doing that. The method deploys new images with pre-tested updates. This allows Azure to collectively test the updates and tailor them for AKS before their rollout, thereby ensuring safer integration into the clusters. The key benefit is improved stability and compatibility, albeit with a potential delay in applying the security updates.

.. note::
     
     With Ubuntu 20.04 LTS reaching the end of standard support, AKS users are urged to upgrade their node pools to Ubuntu 22.04 LTS to ensure continued security compliance and access to the latest features.


Auto-upgrade channels
---------------------

AKS has also instituted several auto-upgrade channels to provide timely OS-level security updates to worker nodes. It is important to note that these updates operate independently of `Kubernetes cluster version upgrades`_.

Users can select from the following auto-upgrade channel options: ``None``, ``Unmanaged``, ``SecurityPatch``, ``NodeImage``. For detailed descriptions and implications of each auto-upgrade channel, please consult the `official AKS documentation for auto-upgrade`_.


.. note::

     New clusters default to the ``NodeImage`` channel, which updates nodes weekly with a new virtual hard disk containing security and bug fixes, thereby following defined maintenance windows. 
     
     Legacy clusters may default to ``None``, thereby disabling automatic updates. Administrators should adjust their cluster's setting according to their security and maintenance preferences.


.. _`end of standard support for Ubuntu 18.04 LTS`: https://ubuntu.com/blog/18-04-end-of-standard-support
.. _`AgentBaker`: https://github.com/Azure/AgentBaker
.. _`unattended-upgrades`: https://ubuntu.com/blog/ubuntu-updates-best-practices-for-updating-your-instance#updating-automatically-with-unattended-upgrades
.. _`Kubernetes cluster version upgrades`: https://learn.microsoft.com/en-us/azure/aks/auto-upgrade-cluster
.. _`official AKS documentation for auto-upgrade`: https://learn.microsoft.com/en-us/azure/aks/auto-upgrade-node-os-image  