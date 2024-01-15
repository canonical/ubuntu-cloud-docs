Get Ubuntu Pro on Azure
=======================

What is Ubuntu Pro?
-------------------

Ubuntu Pro is an additional stream of security updates and packages that meet compliance requirements such as FIPS or HIPAA, on top of an Ubuntu LTS. To learn more about Ubuntu Pro you can read this `FAQ <https://discourse.ubuntu.com/t/ubuntu-pro-faq/34042>`_.

How to get Ubuntu Pro on Azure?
-------------------------------

New instances
~~~~~~~~~~~~~

For new instances or instances that are easy to redeploy (e.g. launched programmatically in a CI/CD pipeline), the best option is to redeploy onto a new Azure Ubuntu Pro instance. These Ubuntu Pro instances on Azure attach to their entitlements automatically and will receive all the Pro features by default without further steps. Pro offers on Azure are listed at: :ref:`find-ubuntu-pro-on-azure`.

Running instances
~~~~~~~~~~~~~~~~~

You can perform an in-place upgrade from Ubuntu Server to Ubuntu Pro to achieve the upgrade without any downtime. Here are the steps:

Run the following command with the Azure CLI to enable Ubuntu Pro on an Ubuntu Server VM:
``az vm update -g myResourceGroup -n myVmName --license-type UBUNTU_PRO``

Run these commands in the instance that you have converted:
``sudo apt install ubuntu-advantage-tools
sudo pro auto-attach``

Verify that Ubuntu Pro is enabled on your instance by running
``pro status --all --wait`` 
