Create an Ubuntu golden image pipeline
======================================

You can use GitHub Actions to create a pipeline for building Ubuntu "golden" images with the Azure Image Builder (AIB). Creating an automated pipeline is a great way to ensure that your golden image is kept up to date with the latest security and bug fixes. 

The focus here is on automating the use of AIB. If you want more information about how to use AIB see the :doc:`Create a Pro golden image <create-pro-fips-golden-image>` guide which explains the individual steps.


Prerequisites
--------------

- A Microsoft Azure account
- `Azure Command-Line Interface`_
- A GitHub account
- (Optional) Golang for local debugging/testing


Set up your Azure credentials
-----------------------------

To create the pipeline, we are going to use a sample application that uses the Azure Go SDK to interact with Azure. To authenticate with the Azure Go SDK you'll need an Azure service principal with a client secret. For details on how to create one, refer to Azure's documentation for `creating an Azure service principal`_.

If you don't want to manually create and setup the managed identity needed by AIB, ensure that you assign the owner role to the service principal.
 
To authenticate with Azure in later steps, you'll need your:

- Azure subscription ID
- Azure tenant ID
- Service principal client ID and
- Service principal client secret


Set up your GitHub repository
-----------------------------

To make use of GitHub Actions you will need to create a new repository. After creating the repository you'll need its URL of the form ``git@github.com:<username>/<repository-name>.git`` for SSH based authentication or ``https://github.com/<username>/<repo-name>.git`` for HTTPS authentication.

Clone the sample application from the `azure-image-builder-pipeline-demo`_ repository and set the remote URL to your newly created repository:

.. code::

  git clone https://github.com/canonical/azure-image-builder-pipeline-demo.git
  git remote set-url origin <your Git repository URL>
  git push -u origin main


Main executables
~~~~~~~~~~~~~~~~

The sample application uses the Azure Go SDK to allow programmatic access to Azure resources. It defines two executables: ``create_all_resources`` and ``run_image_builder``. 

``create_all_resources``
++++++++++++++++++++++++

``create_all_resources`` is a program that creates all the resources needed for AIB. If a resource already exists it does not create a new one, nor does it update the existing one. It attempts to:

- Create a resource group
- Create a managed identity
- Create a role for the managed identity
- Assign the role to the managed identity
- Create an image gallery
- Create an image definition
- Create an image template (this is what AIB actually uses)

The program does not expose all the configuration options for these resources, so you may prefer to perform these steps manually. The steps have to be executed only once to generate the final image template.  The image template is then used to automate the building of your golden images.

``run_image_builder``
+++++++++++++++++++++

``run_image_builder`` is a program that calls AIB with a given image template. Once you have an image template you can keep calling this program to get updated versions of your golden image.


Local setup
~~~~~~~~~~~

If you have Golang installed, you can compile the application locally to debug and test it. To install the necessary modules and compile the two executables, run: 

.. code::

  go mod tidy
  go build ./cmd/create_all_resources
  go build ./cmd/run_image_builder

Before running the executables, you need to set the following environment variables:

- AZURE_SUBSCRIPTION_ID
- AZURE_TENANT_ID
- AZURE_CLIENT_ID
- AZURE_CLIENT_SECRET

To see all the options that can be passed, run:

.. code::

  ./create_all_resources --help
  ./run_image_builder --help


Configure your golden image
---------------------------

Once you have your clone of the sample repository, you can configure it to build your golden image. If you want to use an image template that you've already created, then you can skip ahead to :ref:`configure-github-action`.

``create_all_resources`` provides the following flags to configure its behavior:

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

Some of them have a default value and can be skipped. Two important ones to note are ``--imageProperties`` and ``--customizations``.

Image properties
~~~~~~~~~~~~~~~~

By default, ``--imageProperties`` points to ``./config/imageDefinitionProperties.json``, a file that defines the base image for your golden image. In the sample repository, Ubuntu Pro 22.04 LTS is used as the base image:

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

Customization
~~~~~~~~~~~~~

``--customizations`` points to ``.config/customizations.json`` by default. This is where you define the commands to modify your base image into your golden image:

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

Once you have made the necessary changes to these files, commit and push them to your GitHub repository:

.. code::

   git add ./config/
   git commit -m "Updated golden image configuration"
   git push -u origin main


.. _configure-github-action:

Configure your GitHub Action
----------------------------

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


It is a workflow, and if you're new to GitHub Actions, `Understanding GitHub Actions`_ might help. 

You might want to modify several things in this workflow. The first is the ``on`` field that defines the trigger for your workflow. In the sample it is set to run weekly based on a cron expression. It also sets ``workflow_dispatch`` to allow the workflow to be triggered manually from the UI.

By default the action is configured to ``runs-on: ubuntu-latest``, but if you are self-hosting your runners (see `Adding self-hosted runner`_) you should change this to ``runs-on: self-hosted``.

The next thing you might want to change is to completely remove the two steps related to ``create_all_resources``. They build and run ``create_all_resources`` and as mentioned before, if you've already created your image template manually, then you don't need to run it.

The final thing you'll want to modify are the options passed to ``create_all_resources`` and ``run_image_builder``. Here you can set all the options that are not defined separately in the /config directory.

Make sure to commit and push any changes you make to the workflow file:

.. code::

  git add .github/
  git commit -m "Updated GitHub Action"
  git push -u origin main


Accept the image terms
----------------------

To use AIB you must accept the terms of the base image you choose. Unfortunately this is not a step that can be done with the SDK and you'll need to use the Azure CLI to run:

.. code::

  az vm image terms accept --plan <sku> --offer <offer> --publisher <publisher> --subscription <subID>

Just ensure that the values for ``sku``, ``offer`` and ``publisher`` match the ones that you set in ``config/imageDefinitionProperties.json``. Using the default values from the sample repository, the command becomes:

.. code::

  az vm image terms accept --plan pro-22_04-lts-gen2 --offer 0001-com-ubuntu-pro-jammy --publisher canonical --subscription <subID>


Run the GitHub Action
---------------------

Before you can run the GitHub Action, you need to set the four secrets that you see used in the workflow.

.. code::

    env:
        AZURE_SUBSCRIPTION_ID: ${{ secrets.AZURE_SUBSCRIPTION_ID }}
        AZURE_TENANT_ID: ${{ secrets.AZURE_TENANT_ID }}
        AZURE_CLIENT_ID: ${{ secrets.AZURE_CLIENT_ID }}
        AZURE_CLIENT_SECRET: ${{ secrets.AZURE_CLIENT_SECRET }}

Follow the instructions in `Using secrets in GitHub Actions`_, to add the secrets to your repository.

Go to the Actions page on your repository and select your workflow. If you have kept the ``workflow_dispatch`` field, you'll see a button which can be used to run the workflow manually. Use the button to run it manually, or it'll run as per the specified ``schedule``.


.. _`Azure Command-Line Interface`: https://learn.microsoft.com/en-us/cli/azure/?view=azure-cli-latest
.. _`creating an Azure service principal`: https://learn.microsoft.com/en-us/entra/identity-platform/howto-create-service-principal-portal
.. _`azure-image-builder-pipeline-demo`: https://github.com/canonical/azure-image-builder-pipeline-demo
.. _`Understanding GitHub Actions`: https://docs.github.com/en/actions/get-started/understanding-github-actions
.. _`Adding self-hosted runner`: https://docs.github.com/en/actions/how-tos/hosting-your-own-runners/managing-self-hosted-runners/adding-self-hosted-runners
.. _`Using secrets in GitHub Actions`: https://docs.github.com/en/actions/how-tos/security-for-github-actions/security-guides/using-secrets-in-github-actions
