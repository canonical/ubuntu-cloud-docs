Install Azure CLI on Ubuntu
============================

This documentation is based on the `official Azure documentation <https://docs.microsoft.com/en-us/cli/azure/install-azure-cli-linux?pivots=apt#option-2-step-by-step-installation-instructions>`_.

Install a few pre-requisites::

   sudo apt-get update
   sudo apt-get install ca-certificates curl apt-transport-https lsb-release gnupg


Download the key for the Microsoft archive::

   mkdir -p /etc/apt/keyrings
   curl -sL https://packages.microsoft.com/keys/microsoft.asc |
      gpg --dearmor |
         sudo tee /etc/apt/keyrings/microsoft.gpg > /dev/null

Add the repository to the sources list::

   SUITE=$(lsb_release -cs)
   echo "deb [arch=amd64 signed-by=/etc/apt/keyrings/microsoft.gpg] https://packages.microsoft.com/repos/azure-cli/ $SUITE main" |
       sudo tee /etc/apt/sources.list.d/microsoft.list


Pin a few rules to only allow the Azure CLI to be fetch from Microsoft's archive::

   cat << EOF | sudo tee /etc/apt/preferences.d/99-microsoft

Never prefer packages from the Microsoft repository::

   Package: *
   Pin: origin https://packages.microsoft.com/repos/azure-cli
   Pin-Priority: 1

\...except if it is the Azure CLI::

   Package: azure-cli
   Pin: origin https://packages.microsoft.com/repos/azure-cli
   Pin-Priority: 500
   EOF


Finally, install the CLI::

   sudo apt-get update && \
       sudo apt-get install -y azure-cli
