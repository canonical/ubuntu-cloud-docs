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

It is possible to upgrade an Ubuntu Server LTS instance to receive Ubuntu Pro entitlements by buying a token and attaching this with ``sudo pro attach [YOUR_TOKEN]`` on the relevant instance. The best way to purchase tokens for Azure instances is to `contact Canonical <https://ubuntu.com/azure/pro#get-in-touch>`_.
