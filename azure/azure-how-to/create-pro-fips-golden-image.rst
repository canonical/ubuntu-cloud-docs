Create Ubuntu Pro FIPS golden image with Azure Image Builder
============================================================

This guide will provide instructions for using the Azure Image Builder (AIB) to create an Ubuntu Pro 20.04 FIPS “golden” image in an Azure Compute Gallery, (formerly Shared Image Gallery). In the process, you'll:

- Set up an environment with an Azure Compute Gallery (ACG) and the necessary resources to distribute an image from it
- Create an image definition for Ubuntu Pro 20.04 FIPS
- Create a build configuration template to add optional applications
- Create the golden image using the AIB service
- Create a VM from the golden image in the ACG

.. note::
    We are using a pre-enabled FIPS image, but you can also use the standard Ubuntu Pro if it better suits your needs.


What you'll need
----------------

- A Microsoft Azure account
- `Azure Command-Line Interface`_ 


Set up your Azure Compute Gallery
---------------------------------

To set up the compute gallery, you'll need to create a resource group, a user-identity, a gallery and finally the image definition itself. To simplify the process, we start by creating some variables for values that'll be used repeatedly.


Set up variables 
~~~~~~~~~~~~~~~~

A new resource group with an unused name will have to be created. It can be deleted after use.

.. note::
    To create a custom image, the AIB must be in the same resource group as the source-managed image.

.. code::

    # Resource group name
    sigResourceGroup=ibUbuntuFIPSGalleryRG
    # Datacenter location 
    location=westus2
    # Additional region for image replication
    additionalregion=eastus

Create variables for gallery name and image definition name. The image will be displayed in the Azure Portal as ``sigName/imageDefName``.

.. code::

    # Name of the ACG
    sigName=myIbGallery
    # Name of the image definition to be created
    imageDefName=myIbImageDef
    # Image distribution metadata reference name
    runOutputName=aibUbuntuSIG

Create a variable for your subscription ID:

.. code::

    subscriptionID=$(az account show --query id --output tsv)

Set up variables for the Ubuntu Pro plan to be used. If you have an Ubuntu Pro private offer with Canonical that includes 24x7 technical support with SLAs, you'll have a custom offer and ``sku``, which can be used here. If not, as seen in the example below, you can use the details from the Ubuntu Pro 20.04 FIPS image that is publicly available at the Azure Marketplace.

.. code::

    # Set the 'Publisher' field 
    ProPlanPublisher=canonical
    # Set the 'Offer' field 
    ProPlanOffer=0001-com-ubuntu-pro-focal-fips
    # ProPlanSku the 'Sku' 
    ProPlanSku=pro-fips-20_04-gen2
    

Create required resources, identities and permissions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Create the resource group:

.. code::

    az group create -n $sigResourceGroup -l $location --subscription $subscriptionID

AIB needs a user-identity to inject an image into ACG. So first create an Azure role definition with actions needed to distribute an image to ACG, and then assign that role definition to the user-identity.

.. code::

    # Create a user-identity
    identityName=aibBuiUserId$(date +'%s')
    az identity create -g $sigResourceGroup -n $identityName --subscription $subscriptionID

    # Get the user-identity ID
    imgBuilderCliId=$(az identity show -g $sigResourceGroup -n $identityName --subscription $subscriptionID -o json | grep "clientId" | cut -c16- | tr -d '",')

    # Get the user-identity URI
    imgBuilderId=/subscriptions/$subscriptionID/resourcegroups/$sigResourceGroup/providers/Microsoft.ManagedIdentity/userAssignedIdentities/$identityName

    # Download an Azure role definition template
    curl https://raw.githubusercontent.com/Azure/azvmimagebuilder/master/solutions/12_Creating_AIB_Security_Roles/aibRoleImageCreation.json -o aibRoleImageCreation.json

    imageRoleDefName="Azure Image Builder Image Def"$(date +'%s')

    # Update the role definition template with the correct subscription ID, resource group and role definition name
    sed -i -e "s/<subscriptionID>/$subscriptionID/g" aibRoleImageCreation.json
    sed -i -e "s/<rgName>/$sigResourceGroup/g" aibRoleImageCreation.json
    sed -i -e "s/Azure Image Builder Service Image Creation Role/$imageRoleDefName/g" aibRoleImageCreation.json

    # Create a role definition
    az role definition create --role-definition ./aibRoleImageCreation.json

    # Assign the role definition to the user-identity created earlier
    # If this gives an error, wait a bit and try again
    az role assignment create \
        --assignee $imgBuilderCliId \
        --role "$imageRoleDefName" \
        --scope /subscriptions/$subscriptionID/resourceGroups/$sigResourceGroup


Create an image definition and gallery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To use AIB with ACG, you'll need to have an existing gallery and an image definition.

First, create a gallery:

.. code::

    az sig create \
        -g $sigResourceGroup \
        --gallery-name $sigName \
        --subscription $subscriptionID

Then, create an image definition. Ensure that the “hyper-v-generation” flag is set to the same generation as the base image that you plan to use.

.. code::

    az sig image-definition create \
        -g $sigResourceGroup \
        --gallery-name $sigName \
        --gallery-image-definition $imageDefName \
        --publisher $ProPlanPublisher \
        --offer $ProPlanOffer \
        --sku $ProPlanSku \
        --os-type Linux \
        --plan-name $ProPlanSku \
        --plan-product $ProPlanOffer \
        --plan-publisher $ProPlanPublisher \
        --hyper-v-generation V2 \
        --subscription $subscriptionID
        

Create a configuration template
-------------------------------

We'll be using a sample JSON template to configure the image. It can be customised to include build instructions that are specifically needed for your golden image. Download a template:

.. code::

    curl https://pastebin.com/raw/fCkQAgAc -o UbuntuProFips2004SIGTemplate.json

Customise it to use the values set above:

.. code::

    sed -i -e "s/<subscriptionID>/$subscriptionID/g" UbuntuProFips2004SIGTemplate.json
    sed -i -e "s/<rgName>/$sigResourceGroup/g" UbuntuProFips2004SIGTemplate.json
    sed -i -e "s/<imageDefName>/$imageDefName/g" UbuntuProFips2004SIGTemplate.json
    sed -i -e "s/<sharedImageGalName>/$sigName/g" UbuntuProFips2004SIGTemplate.json
    sed -i -e "s/<region1>/$location/g" UbuntuProFips2004SIGTemplate.json
    sed -i -e "s/<region2>/$additionalregion/g" UbuntuProFips2004SIGTemplate.json
    sed -i -e "s/<runOutputName>/$runOutputName/g" UbuntuProFips2004SIGTemplate.json
    sed -i -e "s%<imgBuilderId>%$imgBuilderId%g" UbuntuProFips2004SIGTemplate.json
    sed -i -e "s/<ProPlanPublisher>/$ProPlanPublisher/g" UbuntuProFips2004SIGTemplate.json
    sed -i -e "s/<ProPlanOffer>/$ProPlanOffer/g" UbuntuProFips2004SIGTemplate.json
    sed -i -e "s/<ProPlanSku>/$ProPlanSku/g" UbuntuProFips2004SIGTemplate.json


Review the template content
---------------------------

In case you want to change something or add your own actions, some of the following sections might help. The plan details of the VM image being used as a starting point for your golden image are under 'source':

.. code::

    "source": {
        "type": "PlatformImage",
            "publisher": "canonical",
            "offer": "0001-com-ubuntu-pro-focal-fips",
            "sku": "pro-fips-20_04-gen2",
            "version": "latest",
    "planInfo": {
                "planName": "pro-fips-20_04-gen2",
                "planProduct": "0001-com-ubuntu-pro-focal-fips",
                "planPublisher": "canonical"
            }
    },

The ``customize`` section allows you to run commands as part of the image building process. The command seen here is used to include a wait until Ubuntu’s ``ua`` client is attached to its subscription.

.. code::
    
    "customize": [
        {
        "type": "Shell",
        "name": "WaitForUAtokenAutoAttach",
        "inline": [
            "sudo ua status --wait"
        ]
    },

Within this section you can add your own actions, for say hardening the image or installing specific software.

.. code::

    {
        "type": "Shell",
        "name": "Placeholder for custom commands required in each Ubuntu VM",
        "inline": [
            "echo 'Replace me!'"
        ]
    },

The following commands deregister the golden image from Ubuntu Pro and remove the machine-id. This will ensure that VMs generated from the golden image will generate their own unique IDs.

.. code::

    {
        "type": "Shell",
        "name": "DetachUA -- images created from this will auto attach themselves with new credentials",
        "inline": [
            "sudo ua detach --assume-yes && sudo rm -rf /var/log/ubuntu-advantage.log"
        ]
    },

    {
        "type": "Shell",
        "name": "Replace /etc/machine-id with empty file to ensure UA client does not see clones as duplicates",
        "inline": [
            "sudo rm -f /etc/machine-id && sudo touch /etc/machine-id"
        ]
    }


Create the golden image 
-----------------------

To create the image in ACG, submit the image configuration to the AIB service:

.. code::

    az resource create \
        --resource-group $sigResourceGroup \
        --subscription $subscriptionID \
        --properties @UbuntuProFips2004SIGTemplate.json \
        --is-full-object \
        --resource-type Microsoft.VirtualMachineImages/imageTemplates \
        -n UbuntuProFips2004SIG01

Accept the legal terms of the image:

.. code::

    az vm image terms accept --plan $ProPlanSku --offer $ProPlanOffer --publisher $ProPlanPublisher --subscription $subscriptionID

Start the image build process:

.. code::

    az resource invoke-action \
        --resource-group $sigResourceGroup \
        --subscription $subscriptionID \
        --resource-type  Microsoft.VirtualMachineImages/imageTemplates \
        -n UbuntuProFips2004SIG01 \
        --action Run

This step can take some time (~25 minutes) as Azure will actually launch a VM and run the steps that you have defined. While you are waiting for the AIB build process to complete, you can view the corresponding logs by going to the storage account inside the resource group created by AIB. (i.e. Go to Azure Portal > Resource groups > ``IT_ibUbuntuFIPSGalleryRG_***`` > Random ID of the storage account > Containers > ``packerlogs`` > Random ID of the container > ``customization.log`` > Download)

Once the build process is completed, the status will change from “Running” to "Succeeded", to show something like:

.. code::

    {
        "endTime": "2022-09-10T23:13:25.9008064Z",
        "name": "37962BEF-34DC-45B1-A1C6-E827CE20F89B",
        "startTime": "2022-09-10T22:48:19.7520483Z",
        "status": "Succeeded"
    }


Create a VM - using the Portal
------------------------------

To create a VM based on the golden image, in the portal:

#. Go to *Azure services* > *Virtual Machines* > *Create* > *Virtual machine*
#. Open the *See all images* link located below the *Image* field drop down 
#. Select *Shared Images* from the column on the left
#. Choose your golden image and it should now be the selected image in the *Image* field 
#. Complete the remaining fields as per your requirements and select *Review + Create*


Create a VM - using the CLI
---------------------------

To create a VM from the command line, you'll need to use all the variables created earlier. If you already have an SSH key use the following commands to launch the VM:

.. code::

    SSHPublicKeyPath=<path to your id_rsa.pub>

.. code::

    az vm create \
        --resource-group $sigResourceGroup \
        --subscription $subscriptionID \
        --name myAibGalleryVM \
        --admin-username aibuser \
        --location $location \
        --image "/subscriptions/$subscriptionID/resourceGroups/$sigResourceGroup/providers/Microsoft.Compute/galleries/$sigName/images/$imageDefName/versions/latest" \
        --ssh-key-values $SSHPublicKeyPath \
        --plan-name $ProPlanSku \
        --plan-product $ProPlanOffer \
        --public-ip-sku Standard \
        --plan-publisher $ProPlanPublisher

Alternatively, if you do not have an SSH key, replace the ``--ssh-key-values $SSHPublicKeyPath`` with ``--generate-ssh-keys`` as shown below. However this may overwrite the ssh keypair ``id_rsa`` and ``id_rsa.pub`` located in .ssh in your home directory.

.. code::

    az vm create \
        --resource-group $sigResourceGroup \
        --subscription $subscriptionID \
        --name myAibGalleryVM \
        --admin-username aibuser \
        --location $location \
        --image "/subscriptions/$subscriptionID/resourceGroups/$sigResourceGroup/providers/Microsoft.Compute/galleries/$sigName/images/$imageDefName/versions/latest" \
        --generate-ssh-keys \
        --plan-name $ProPlanSku \
        --plan-product $ProPlanOffer \
        --public-ip-sku Standard \
        --plan-publisher $ProPlanPublisher


Once the command completes, you should see something like:

.. code::

    {
        "fqdns": "",
        "id": "/subscriptions/50a71625-6dba-43a2-87ad-9eb26e52c9c4/resourceGroups/ibUbuntuFIPSGalleryRG/providers/Microsoft.Compute/virtualMachines/myAibGalleryVM",
        "identity": {
            "principalId": "632b1fc9-9d93-46da-bbd1-3b32e85f96eb",
            "tenantId": "40a524d9-f848-46d4-a96f-be6df491fe15",
            "type": "SystemAssigned",
            "userAssignedIdentities": null
        },
        "location": "westus2",
        "macAddress": "00-0D-3A-F5-29-B8",
        "powerState": "VM running",
        "privateIpAddress": "10.0.0.4",
        "publicIpAddress": "51.143.126.x",
        "resourceGroup": "ibUbuntuFIPSGalleryRG",
        "zones": ""
    }

You can use the ``publicIpAddress`` (``51.143.126.x`` in this case) to ssh into the machine. To check that the VM is attached to an Ubuntu Pro subscription and is running a FIPS kernel, run:

.. code::

    sudo ua status --wait


Post creation cleanup
---------------------

You now have an Azure Compute Gallery with an Ubuntu Pro 20.04 FIPS image inside. You have also launched and tested a VM based on this golden image. So you can go ahead with the deletion of the resource groups that were created. You should be able to see the created resource groups with:

.. code::

    az group list --query [].name --output table --subscription $subscriptionID | grep $sigResourceGroup

This command returns something like:

.. code::

    ibUbuntuFIPSGalleryRG
    IT_ibUbuntuFIPSGalleryRG_UbuntuProFips2004S_02ecb26b-21f4-4450-b207-e86c7fd6853e

If you want to delete these resource groups, use the following command on each of them. You may find that deleting the first one automatically deletes the second.

.. code::

    az group delete --name [the name from above] --subscription $subscriptionID




.. _`Azure Command-Line Interface`: https://learn.microsoft.com/en-us/cli/azure/

