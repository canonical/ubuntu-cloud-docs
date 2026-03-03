Provision an Ubuntu virtual machine running SQL Server in Azure
===============================================================

This guide will provide instructions for creating an Ubuntu-based VM on Azure with SQL Server installed.

Prerequisites
-------------

- A Microsoft Azure account
- A Resource Group

Pick an SQL Server version
--------------------------
SQL Server support varies per Ubuntu version. Consult the `SQL Server on Ubuntu quickstart`_ to determine which versions of Ubuntu are supported for the SQL Server version you need.

Pick an Ubuntu image
--------------------
Once you know what Ubuntu version you need you can consult :doc:`How to Find Ubuntu Images on Azure <find-ubuntu-images>` to find all Ubuntu offerings on Azure. If you are unsure about which Ubuntu product to use (Pro vs non-Pro, FIPS etc.) see :doc:`Canonical's offerings on Azure <../../azure-explanation/canonical-offerings>` for an explanation.

Launching an Ubuntu VM
----------------------
Once you have chosen your image you have two options for creating your VM.

With Azure Portal
~~~~~~~~~~~~~~~~~
Click the the "Quick start" link for your image in :doc:`How to Find Ubuntu Images on Azure <find-ubuntu-images>`. This will take you to the `Azure Portal <https://portal.azure.com/>`_ where you will be guided through the VM creation process.

With Azure CLI
~~~~~~~~~~~~~~
Take the URN for your image in :doc:`How to Find Ubuntu Images on Azure <find-ubuntu-images>` and then follow :doc:`How to Launch Ubuntu images on Azure <launch-ubuntu-images>` to create the VM with the Azure CLI.

Install and configure SQL Server
--------------------------------
Follow the `SQL Server on Ubuntu quickstart`_ to install SQL Server for your version of Ubuntu.

Open the firewall
~~~~~~~~~~~~~~~~~

If you want to connect remotely to VMs, you also have to open up port 1433 on the Linux firewall.

- Connect to your VM.
- In a terminal, run the following command:

.. code:: bash

    sudo ufw allow 1433/tcp

Connect
~~~~~~~

You can now connect to your server from your favorite client.

.. _`SQL Server on Ubuntu quickstart`: https://learn.microsoft.com/en-us/sql/linux/quickstart-install-connect-ubuntu
