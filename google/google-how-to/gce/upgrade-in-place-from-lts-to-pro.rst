Upgrade in-place from LTS to Pro
================================

If your production environment is based on Ubuntu LTS and you need the premium security, support or compliance features of Ubuntu Pro, then you don't have to migrate your applications to new Ubuntu Pro VMs. You can just perform an in-place upgrade of your existing machines in three simple steps:

1. Stop your machine:

.. code::

    gcloud compute instances stop $INSTANCE_NAME

2. Append an Ubuntu Pro license to the disk:

.. code::

    gcloud beta compute disks update $INSTANCE_NAME --zone=$ZONE --update-user-licenses=”LICENSE_URI”

where,

* INSTANCE_NAME: is the name of the instance (boot disk) to append the license to
* ZONE: is the zone containing the instance 
* LICENSE_URI: is the license URI for the Pro version that you are upgrading to. If your VM runs Ubuntu 16.04 LTS, you need to upgrade to Ubuntu Pro 16.04 LTS. Choose the appropriate URI from: 

.. list-table::
   :header-rows: 1
   :widths: 20 50

   * - **Version**
     - **License URI**
   * - Ubuntu Pro 16.04 LTS
     - ``https://www.googleapis.com/compute/v1/projects/ubuntu-os-pro-cloud/global/licenses/ubuntu-pro-1604-lts``
   * - Ubuntu Pro 18.04 LTS
     - ``https://www.googleapis.com/compute/v1/projects/ubuntu-os-pro-cloud/global/licenses/ubuntu-pro-1804-lts``
   * - Ubuntu Pro 20.04 LTS
     - ``https://www.googleapis.com/compute/v1/projects/ubuntu-os-pro-cloud/global/licenses/ubuntu-pro-2004-lts``
   * - Ubuntu Pro 22.04 LTS
     - ``https://www.googleapis.com/compute/v1/projects/ubuntu-os-pro-cloud/global/licenses/ubuntu-pro-2204-lts``


3. Start the machine

.. code::

    gcloud compute instances start $INSTANCE_NAME

SSH into your machine and verify the upgrade by running:

.. code::

    pro status

The output should show the different services available and their current status. Something like:

.. code::

    SERVICE          ENTITLED  STATUS    DESCRIPTION
    esm-apps         yes       enabled   Expanded Security Maintenance for Applications
    esm-infra        yes       enabled   Expanded Security Maintenance for Infrastructure
    fips             yes       disabled  NIST-certified core packages
    fips-updates     yes       disabled  NIST-certified core packages with priority security updates
    livepatch        yes       enabled   Canonical Livepatch service
    usg              yes       disabled  Security compliance and audit tools


For comprehensive instructions, please refer to the official Google Cloud documentation for `upgrading to Pro`_.

.. _`upgrading to Pro`: https://cloud.google.com/compute/docs/images/premium/ubuntu-pro/upgrade-from-ubuntu







