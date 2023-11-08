# Ubuntu on Azure Kubernetes worker nodes

Ubuntu 22.04 LTS is the default operating system used by Azure Kubernetes Service (AKS) worker nodes. The use of 22.04 LTS is recent and previous worker nodes were running Ubuntu 18.04 LTS which is now out of standard support. If you still run old AKS worker nodes with old versions of Kubernetes, make sure to upgrade as 18.04 LTS no longer receives security fixes.

Please note that Canonical does not directly publish the images used by AKS worker nodes. The AKS team at Azure uses images produced by Canonical as a base and applies their own configuration layer before publishing images for their worker nodes. The customization tool is open source and can be found on Github: [AgentBacker](https://github.com/Azure/AgentBaker). Canonical is working closely with the AKS team to make Ubuntu the best OS for AKS worker nodes.

It is important to know that unattended-upgrade, the service used to automatically upgrade certain parts of Ubuntu in case of security fixes, is disabled on AKS worker nodes.
