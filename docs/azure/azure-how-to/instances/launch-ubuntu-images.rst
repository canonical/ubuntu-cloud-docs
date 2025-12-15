Launch Ubuntu images on Azure
=============================

This guide is based on the `official Azure documentation`_ for creating Linux virtual machines using the
`Azure Command-Line Interface`_ (Azure CLI).


Prerequisites
-------------

- Microsoft Azure account
- Azure CLI
- Uniform Resource Name (URN) for an Ubuntu image (see :doc:`find-ubuntu-images`)

Azure CLI commands in this guide share some declared variables:

.. code::

    # The resource group to create the virtual machine in. this can either be
    # an existing resource group, or one created as part of the guide.
    RESOURCE_GROUP_NAME="..."

    # The Azure location to create the virtual machine in. Valid locations can
    # be listed with the `az account list-locations --output table` command.
    LOCATION="..."

    # The named identifier for the virtual machine.
    VIRTUAL_MACHINE_NAME="..."

    # The Ubuntu image URN to launch. The value of this variable will change
    # between commands as certain Azure features are only supported by specific
    # Ubuntu image lines.
    UBUNTU_IMAGE_URN="..."

Create a resource group
-----------------------

Azure virtual machines must be created in a resource group. This step can be skipped if using an existing resource group.

Create a resource group using the `group create`_ command:

.. code::

    az group create \
        --name "$RESOURCE_GROUP_NAME" \
        --location "$LOCATION"


Create a virtual machine
------------------------

Create a virtual machine using the `vm create`_ command. Virtual machines on Azure are created with `Trusted Launch`_
enabled by default. All Hyper-V Gen2 x86 Ubuntu images from 20.04 LTS forward support Trusted Launch and can be created
using the command defaults:

.. code::

    az vm create \
        --resource-group "$RESOURCE_GROUP_NAME" \
        --location "$LOCATION" \
        --name "$VIRTUAL_MACHINE_NAME" \
        --image "$UBUNTU_IMAGE_URN" \
        --generate-ssh-keys

ARM64 images
~~~~~~~~~~~~

ARM64 images must be launched with an ARM64-compatible virtual machine size. Furthermore, ARM64 images do not support
Trusted Launch and must instead use the **Standard** security type. You may also need to register usage of the security
type for your Azure subscription:

.. code::

    az feature register \
        --namespace "Microsoft.Compute" \
        --name "UseStandardSecurityType"

    # Required to propagate the changes.
    az provider register --name "Microsoft.Compute"

    # VM size should contain the "p" additive feature denoting an ARM64 processor.
    VIRTUAL_MACHINE_SIZE="Standard_D2ps_v5"
    SECURITY_TYPE="Standard"

    az vm create \
        --resource-group "$RESOURCE_GROUP_NAME" \
        --location "$LOCATION" \
        --name "$VIRTUAL_MACHINE_NAME" \
        --image "$UBUNTU_IMAGE_URN" \
        --security-type "$SECURITY_TYPE" \
        --size "$VIRTUAL_MACHINE_SIZE" \
        --generate-ssh-keys


Confidential Virtual Machines (CVM)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ubuntu CVM images must be launched with `specialized hardware`_ and configure `Confidential OS disk encryption`_ for
the deployment - either with or without Trusted Platform Module (TPM)-backed Full Disk Encryption (FDE).

.. code::

    # With TPM-backed FDE
    OS_ENCRYPTION_TYPE="DiskWithVMGuestState"

    # Without TPM-backed FDE
    OS_ENCRYPTION_TYPE="VMGuestStateOnly"

    # VM size should belong to the "C" subfamily denoting support for Azure
    # Confidential compute.
    VIRTUAL_MACHINE_SIZE="Standard_DC2as_v5"
    SECURITY_TYPE="ConfidentialVM"

    az vm create \
        --resource-group "$RESOURCE_GROUP_NAME" \
        --location "$LOCATION" \
        --name "$VIRTUAL_MACHINE_NAME" \
        --image "$UBUNTU_IMAGE_URN" \
        --security-type "$SECURITY_TYPE" \
        --os-disk-security-encryption-type "$OS_ENCRYPTION_TYPE" \
        --size "$VIRTUAL_MACHINE_SIZE" \
        --generate-ssh-keys


.. _`official Azure documentation`: https://learn.microsoft.com/en-us/azure/virtual-machines/linux/quick-create-cli
.. _`Azure Command-Line Interface`: https://learn.microsoft.com/en-us/cli/azure/?view=azure-cli-latest
.. _`group create`: https://learn.microsoft.com/en-us/cli/azure/group?view=azure-cli-latest#az-group-create
.. _`vm create`: https://learn.microsoft.com/en-us/cli/azure/vm?view=azure-cli-latest#az-vm-create
.. _`supports CVM on Azure`: https://learn.microsoft.com/en-us/azure/confidential-computing/virtual-machine-solutions#sizes
.. _`Trusted Launch`: https://learn.microsoft.com/en-us/azure/virtual-machines/trusted-launch
.. _`specialized hardware`: https://learn.microsoft.com/en-us/azure/confidential-computing/confidential-vm-overview#size-support
.. _`Confidential OS disk encryption`: https://learn.microsoft.com/en-us/azure/confidential-computing/confidential-vm-overview#confidential-os-disk-encryption
