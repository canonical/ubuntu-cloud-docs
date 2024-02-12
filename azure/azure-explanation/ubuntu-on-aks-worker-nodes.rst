Ubuntu on AKS worker nodes
==========================

Overview
--------

Ubuntu 22.04 LTS is the default operating system for worker nodes in the Azure Kubernetes Service (AKS), encompassing both system node pools and user node pools. With the `end of standard support for Ubuntu 18.04 LTS`_, which no longer receives security fixes, AKS deployments on older Kubernetes versions must upgrade node pools to maintain security compliance.

Image customisation
-------------------

* AKS worker nodes use Ubuntu images provided by Canonical and customised by the Azure AKS team.
* Customisation is performed using the open-source tool `AgentBaker`_.
* Canonical closely collaborates with the AKS team to ensure that the images are appropriately configured for optimal performance on the Azure platform and all updates are tested by AKS to reduce the risks of regressions.

Auto-upgrade channels
---------------------

AKS has instituted several auto-upgrade channels to provide timely OS-level security updates to worker nodes. It is important to note that these updates operate independently of `Kubernetes cluster version upgrades`_.

Users can select from the following auto-upgrade channel options: ``None``, ``Unmanaged``, ``SecurityPatch``, ``NodeImage``. For detailed descriptions and implications of each auto-upgrade channel, please consult the `official AKS documentation for auto-upgrade`_.


.. note::

     Clusters without a specified auto-upgrade channel automatically fall under the ``None`` category, disabling 'unattended-upgrades'. Administrators are encouraged to modify this setting to an option that aligns with their security needs and maintenance preferences.


.. _`end of standard support for Ubuntu 18.04 LTS`: https://ubuntu.com/blog/18-04-end-of-standard-support
.. _`AgentBaker`: https://github.com/Azure/AgentBaker
.. _`Kubernetes cluster version upgrades`: https://learn.microsoft.com/en-us/azure/aks/auto-upgrade-cluster
.. _`official AKS documentation for auto-upgrade`: https://learn.microsoft.com/en-us/azure/aks/auto-upgrade-node-os-image  