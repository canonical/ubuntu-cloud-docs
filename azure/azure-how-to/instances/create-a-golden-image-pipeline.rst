Create an Ubuntu golden image pipeline
======================================

This guide will provide instructions for using GitHub Actions to create a pipeline for building Ubuntu "golden" images with the Azure Image Builder (AIB). Creating an automated pipeline is a great way to ensure your golden image is kept up to date with the latest security and bug fixes. This guide focuses on automating the use of Azure Image Builder. If you want more information on how to use Azure Image Builder see the :doc:`Create a Pro golden image <create-pro-fips-golden-image>` guide which explains the individual steps.

What you'll need
----------------

- A Microsoft Azure account
- `Azure Command-Line Interface`_
- A GitHub account
- (Optional) Golang for local debugging/testing

Set up your Azure credentials
-----------------------------

This guide is based on a sample application which uses the Azure Go SDK to interact with Azure. To authenticate with the Azure Go SDK you are going to use an Azure service principal with a client secret.
For help creating an Azure service principal see `Create an Azure service principal`_. Make sure to assign this service principal the owner role if you don't want to manually create and setup the managed identity needed by Azure Image Builder.

You will need the following to authenticate with Azure in later steps:

- Your Azure subscription ID
- Your Azure tenant ID
- Your service principal client ID
- Your service principal client secret

Set up your GitHub repository
-----------------------------

To make use of GitHub Actions you will need to create a new repository. After creating the repository you'll need the URL of the form ``git@github.com:<username>/<repository-name>.git`` for SSH based authentication or ``https://github.com/<username>/<repo-name>.git`` for HTTPS authentication.

Clone the sample repository `azure-image-builder-pipeline-demo`_ and set the remote URL to your newly created repository.

.. code::

   git clone https://github.com/canonical/azure-image-builder-pipeline-demo.git
   git remote set-url origin <your Git repository URL>
   git push -u origin main

Main executables
~~~~~~~~~~~~~~~~

The sample repository uses the Azure Go SDK to allow programmatic access to Azure resources. This repository defines two executables: ``create_all_resources`` and ``run_image_builder``. 

create_all_resources
++++++++++++++++++++

``create_all_resources`` is a program which will create all the resources needed for Azure Image Builder. If a resource already exists it will not create a new one or update the existing resource. It will attempt to do the following:

- Create a resource group
- Create a managed identity
- Create a role for the managed identity
- Assign the role to the managed identity
- Create an image gallery
- Create an image definition
- Create an image template (this is what Azure Image Builder actually uses)

``create_all_resources`` does not expose all the configuration options for these various resources so you may prefer to do this manually. These steps only need to be done once to generate the final image template which is what you need to automate the building of your golden images.

run_image_builder
+++++++++++++++++

``run_image_builder`` is a program which calls Azure Image Builder with a given image template. Once you have an image template you can keep calling to this program to get updated versions of your golden image.

Local set up
~~~~~~~~~~~~
If you have Golang installed you can compile the project locally to debug and test. This is also helpful for seeing all the options that can be passed to the commands.

.. code::

   go mod tidy
   go build ./cmd/create_all_resources
   go build ./cmd/run_image_builder

   ./create_all_resources --help
   ./run_image_builder --help

Configure your golden image
---------------------------

Once you have your clone of the sample repository setup you can start to configure it to build your golden image. If you want to use an image template you've already created then you can skip ahead.

``create_all_resources`` provides the following flags to configure its behaviour:

.. code::

   --subscriptionID value, -s value                                   Azure subscription ID [$AZURE_SUBSCRIPTION_ID]
   --resourceGroup value, -g value                                    Azure resource group name
   --location value, -l value                                         Location in which to deploy resources
   --imageTemplateName value                                          Name of the image template to create
   --runOutputName value                                              The Azure Image Builder output name (default: "aibDemoOutput")
   --imageName value                                                  The name of the image definition to create (default: "aibDemoImage")
   --galleryName value                                                The name of the image gallery to create
   --targetRegion value, -r value [ --targetRegion value, -r value ]  A region to replicate the produced image to.
   --rolePermissions value                                            Path to the role permissions file (default: "./config/aibRolePermissions.json")
   --imageProperties value                                            Path to the image definitions properties file (default: "./config/imageDefinitionProperties.json")
   --customizations value                                             Path to the image template customizations file (default: "./config/customizations.json")
   --exportTemplate                                                   Whether the raw iamge template data should be exported (default: false)
   --exportPath value                                                 Path to export the image template to if enabled (default: "generatedTemplate.json")

Not all of these values need to be provided, any option which has a default can be omitted. Two important options to note are ``--imageProperties`` and ``--customizations``. These point to the following files in the config directory by default.

``./config/imageDefinitionProperties.json`` is where you define the base image to build your golden image from. The sample repository is using Ubuntu Pro 22.04 by default.

.. code::

   {
        "identifier": {
            "offer": "0001-com-ubuntu-pro-jammy",
            "publisher": "canonical",
            "sku": "pro-22_04-lts-gen2"
        },
        "osState": "Generalized",
        "osType": "Linux",
        "architecture": "x64",
        "hyperVGeneration": "V2"
    }

``.config/customizations.json`` is where you define the commands to modify your base image into your golden image.

.. code::

   [
        {
            "type": "Shell",
            "name": "WaitForUAtokenAutoAttach",
            "inline": [
                "sudo ua status --wait"
            ]
        },
        {
            "type": "Shell",
            "name": "Placeholder for custom commands required in each Ubuntu VM",
            "inline": [
                "echo 'Replace me!'"
            ]
        },
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
    ]

Once you have made the necessary changes to these files make sure to commit the changes and push them to your GitHub repository.

.. code::

   git add ./config/
   git commit -m "Updated golden image configuration"
   git push -u origin main

Configure your GitHub Action
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The sample repository comes with the following GitHub Action predefined:

.. code::

   name: GitHub Actions Azure Image Builder Demo

    env:
      AZURE_SUBSCRIPTION_ID: ${{ secrets.AZURE_SUBSCRIPTION_ID }}
      AZURE_TENANT_ID: ${{ secrets.AZURE_TENANT_ID }}
      AZURE_CLIENT_ID: ${{ secrets.AZURE_CLIENT_ID }}
      AZURE_CLIENT_SECRET: ${{ secrets.AZURE_CLIENT_SECRET }}

    on:
      schedule:
        - cron: '0 0 * * 0' # run weekly

      workflow_dispatch: # adds the ability to manually trigger the action

    jobs:
      Run-Azure-Image-Builder-With-Bootstrap:
        runs-on: ubuntu-latest
        steps:
          - uses: actions/checkout@v4

          - name: Setup Go
            uses: actions/setup-go@v4
            with:
              go-version: '1.21.x'

          - name: Install dependencies
            run: go mod tidy

          - name: Build create_all_resources
            run: go build -v ./cmd/create_all_resources

          - name: Build run_image_builder
            run: go build -v ./cmd/run_image_builder

          - name: Create all resources needed for Azure Image Builder
            run: |
              ./create_all_resources \
                --resourceGroup "aib-pipeline" \
                --galleryName "aibGallery" \
                --imageTemplateName "ubuntu_22_04" \
                --location "eastus" \
                --targetRegion "eastus" --targetRegion "westus" \
                --exportTemplate true

          - name: Run Azure Image Builder
            run: |
              ./run_image_builder \
                --templateName "ubuntu_22_04" \
                --resourceGroupName "aib-pipeline"

If you're new to GitHub Actions it can be helpful to first read `Understanding GitHub Actions`_. There are several things you might want to modify in this workflow. The first is the ``on`` field which defines what triggers your workflow. In the sample it is set to run weekly based on a cron expression. It also sets ``workflow_dispatch`` to allow the workflow to be triggered manually in the UI.

By default the action is configured to ``runs-on: ubuntu-latest``, but if you are self-hosting your runners (see `Adding self-hosted runner`_) you should change this to ``runs-on: self-hosted``.

The next thing you might want to change is completely removing the two steps related to ``create_all_resources``. As mentioned before, if you've already manually created your image template you don't need to run this and can simply call ``run_image_builder``.

The final thing you will want to modify are the options passed to ``create_all_resources`` and ``run_image_builder``. This is where you can set all the options that are not defined separately in the /config directory.

Make sure to commit and push any changes you make to the workflow file.

.. code::

   git add .github/
   git commit -m "Updated GitHub Action"
   git push -u origin main

Accept the image terms
~~~~~~~~~~~~~~~~~~~~~~

To use Azure Image Builder you must accept the terms of the base image you choose. Unfortunately this is not a step that can be done with the SDK. Accepting the image terms is just one command with the Azure CLI.

.. code::

    az vm image terms accept --plan <sku> --offer <offer> --publisher <publisher> --subscription <subID>

Just make sure the values for sku, offer and publisher match what you set in ``config/imageDefinitionProperties.json``. For the default values in the sample repository this would be:

.. code::

    az vm image terms accept --plan pro-22_04-lts-gen2 --offer 0001-com-ubuntu-pro-jammy --publisher canonical --subscription <subID>


Run the GitHub Action
---------------------

Once you have all your configuration changes you are now ready to run the workflow. The first thing to do is setting the four secrets you see used in the workflow:

.. code::

    env:
        AZURE_SUBSCRIPTION_ID: ${{ secrets.AZURE_SUBSCRIPTION_ID }}
        AZURE_TENANT_ID: ${{ secrets.AZURE_TENANT_ID }}
        AZURE_CLIENT_ID: ${{ secrets.AZURE_CLIENT_ID }}
        AZURE_CLIENT_SECRET: ${{ secrets.AZURE_CLIENT_SECRET }}

If you need help adding secrets to your repository, you can follow the instructions in `Using secrets in GitHub Actions`_.

Now that your secrets are setup you have everything ready and can head to the Actions page on your GitHub repository and select your workflow. If you kept ``workflow_dispatch`` in your workflow you will have a button to run the workflow manually.

You have successfully created a GitHub Action which will automatically build your golden image.




.. _`azure-image-builder-pipeline-demo`: https://github.com/canonical/azure-image-builder-pipeline-demo
.. _`Understanding GitHub Actions`: https://docs.github.com/en/actions/learn-github-actions/understanding-github-actions
.. _`Create an Azure service principal`: https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal
.. _`Using secrets in GitHub Actions`: https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions
.. _`Adding self-hosted runner`: https://docs.github.com/en/actions/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners
.. _`Azure Command-Line Interface`: https://learn.microsoft.com/en-us/cli/azure/
