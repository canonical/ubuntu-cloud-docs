Launch Ubuntu Images on Azure
=============================

This documentation is based on the `official Azure documentation <https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-cli>`_
for creating Linux virtual machines with the Azure CLI.

Prerequisites
-------------

- A Microsoft Azure account
- `Azure Command-Line Interface <https://learn.microsoft.com/en-us/cli/azure/>`_
- The URN for a Ubuntu image on Azure to launch (see :ref:`Find Ubuntu images on Azure`)

Launch a Ubuntu Image
---------------------

To launch a Ubuntu Image, you will need to create a resource group and create a virtual machine using the Ubuntu image
you have selected.

Create the Resource Group
~~~~~~~~~~~~~~~~~~~~~~~~~

Define variables to select the resource group name and location to deploy:

.. code::

    RESOURCE_GROUP_NAME="ubuntu-vm-rg"
    LOCATION="eastus"

Create a resource group using the `az group create <https://learn.microsoft.com/en-us/cli/azure/group?view=azure-cli-latest#az-group-create>`_ command:

.. code::

    az group create \
        -n $RESOURCE_GROUP_NAME \
        -l $LOCATION

Create the Virtual Machine
~~~~~~~~~~~~~~~~~~~~~~~~~~

Create a virtual machine using the `az vm create <https://learn.microsoft.com/en-us/cli/azure/vm?view=azure-cli-latest#az-vm-create>`_ command.

Depending on the type of Ubuntu image you have selected, additional arguments may be required to correctly launch
the image. Most Ubuntu images can be launched with the default arguments:

.. code::

    az vm create \
        --name $VIRTUAL_MACHINE_NAME \
        --resource-group $RESOURCE_GROUP_NAME \
        --image $UBUNTU_IMAGE_URN \
        --generate-ssh-keys

Security Type - Trusted Launch
++++++++++++++++++++++++++++++

All Ubuntu images from Ubuntu 20.04 LTS (Focal Fossa) forward support Trusted Launch on Hyper-V Gen2 skus. Example
definitions of Ubuntu image URNs for Hyper-V Gen2 include:

.. code::

    UBUNTU_IMAGE_URN="Canonical:0001-com-ubuntu-server-jammy:22_04-lts-gen2:latest"
    # or
    UBUNTU_IMAGE_URN="Canonical:0001-com-ubuntu-server-focal:20_04-lts-gen2:latest"

Define the variables to select the security type:

.. code::

    SECURITY_TYPE=TrustedLaunch

Create the virtual machine:

.. code::

    az vm create \
        --name $VIRTUAL_MACHINE_NAME \
        --resource-group $RESOURCE_GROUP_NAME \
        --image $UBUNTU_IMAGE_URN \
        --security-type $SECURITY_TYPE \
        --generate-ssh-keys

Security Type - Confidential Virtual Machine
++++++++++++++++++++++++++++++++++++++++++++

Select one of the two URNs for Ubuntu images which support CVM on Azure:

.. code::

    UBUNTU_IMAGE_URN="Canonical:0001-com-ubuntu-confidential-vm-jammy:22_04-lts-cvm:latest"
    # or
    UBUNTU_IMAGE_URN="Canonical:0001-com-ubuntu-confidential-vm-focal:20_04-lts-cvm:latest"

Define variables to select the security type and encryption type:

.. code::

    SECURITY_TYPE=ConfidentialVm
    OS_ENCRYPTION_TYPE=DiskWithVMGuestState

Select a virtual machine size which `supports CVM on Azure <https://learn.microsoft.com/en-us/azure/confidential-computing/virtual-machine-solutions#sizes>`_.
Note that not all regions will contain the selected virtual machine size, and you may need to specify the region if
your default region does not have the selected size:

.. code::

    VM_SIZE=Standard_DC2as_v5

    # Standard_DC2as_v5 is available on eastus
    LOCATION=eastus

Create the virtual machine:

.. code::

    az vm create \
        --name $VIRTUAL_MACHINE_NAME \
        --resource-group $RESOURCE_GROUP_NAME \
        --image $UBUNTU_IMAGE_URN \
        --security-type $SECURITY_TYPE \
        --os-disk-security-encryption-type $OS_ENCRYPTION_TYPE \
        --size $VM_SIZE \
        --location $LOCATION \
        --generate-ssh-keys
