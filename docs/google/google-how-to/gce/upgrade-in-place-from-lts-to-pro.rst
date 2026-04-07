.. meta::
   :description: Learn how to switch between Ubuntu LTS and Ubuntu Pro in-place on GCE. Includes steps to update the license and verify the changes.


Change license between LTS and Pro
====================================

You can change the license on an existing VM's disk to switch between Ubuntu LTS and Ubuntu Pro without migrating your applications to new VMs. The VM must be stopped before a license change can be applied to its disk.

.. tabs::

   .. group-tab:: Upgrade from LTS to Pro

      If your production environment is based on Ubuntu LTS and you need the premium security, support or compliance features of Ubuntu Pro, you can perform an in-place upgrade of your existing machines:

      1. Stop your machine:

         .. code::

             gcloud compute instances stop $INSTANCE_NAME

      2. Update the license on the disk to Ubuntu Pro:

         .. code::

             gcloud compute disks update $INSTANCE_NAME --zone=$ZONE \
                 --replace-license=$PREVIOUS_LICENSE_URI,$NEW_LICENSE_URI

         where

         * ``$INSTANCE_NAME`` is the name of the instance to replace the license on;
         * ``$ZONE`` is the zone containing the instance;
         * ``$PREVIOUS_LICENSE_URI`` is the license URI for the non-Pro version on your VM; and
         * ``$NEW_LICENSE_URI`` is the license URI for the Pro version that you are upgrading to.

         You can only update to Pro for the same Ubuntu series. If your VM runs Ubuntu 22.04 LTS, you need to upgrade to Ubuntu Pro 22.04 LTS.

         For ``$PREVIOUS_LICENSE_URI`` choose the appropriate URI from:

         .. list-table::
            :header-rows: 1
            :widths: 20 50

            * - **Version**
              - **License URI**
            * - Ubuntu 16.04 LTS
              - ``https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/licenses/ubuntu-1604-lts``
            * - Ubuntu 18.04 LTS
              - ``https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/licenses/ubuntu-1804-lts``
            * - Ubuntu 20.04 LTS
              - ``https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/licenses/ubuntu-2004-lts``
            * - Ubuntu 22.04 LTS
              - ``https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/licenses/ubuntu-2204-lts``
            * - Ubuntu 24.04 LTS
              - ``https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/licenses/ubuntu-2404-lts``

         For ``$NEW_LICENSE_URI`` choose the appropriate URI from:

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
            * - Ubuntu Pro 24.04 LTS
              - ``https://www.googleapis.com/compute/v1/projects/ubuntu-os-pro-cloud/global/licenses/ubuntu-pro-2404-lts``

         **Example** -- upgrading an Ubuntu 22.04 LTS VM to Ubuntu Pro 22.04 LTS:

         .. code::

             gcloud compute disks update $INSTANCE_NAME --zone=$ZONE \
                 --replace-license=projects/ubuntu-os-cloud/global/licenses/ubuntu-2204-lts,projects/ubuntu-os-pro-cloud/global/licenses/ubuntu-pro-2204-lts

      3. Start the machine:

         .. code::

             gcloud compute instances start $INSTANCE_NAME

      4. SSH into your machine and verify the upgrade by running:

         .. code::

             pro status

         The output should show the different services available and their current status. Something like:

         .. code::

             SERVICE          ENTITLED  STATUS    DESCRIPTION
             anbox-cloud      yes       disabled  Scalable Andriod in the cloud
             esm-apps         yes       enabled   Expanded Security Maintenance for Applications
             esm-infra        yes       enabled   Expanded Security Maintenance for Infrastructure
             fips-preview     yes       disabled  Preview of FIPS crypto packages undergoing certification with NIST
             fips-updates     yes       disabled  FIPS compliant crypto packages with stable security updates
             livepatch        yes       enabled   Canonical Livepatch service
             usg              yes       disabled  Security compliance and audit tools


      For comprehensive instructions, please refer to the official Google Cloud documentation for `upgrading to Pro`_.

   .. group-tab:: Downgrade from Pro to LTS

      If you no longer need the premium features of Ubuntu Pro, you can downgrade your existing VM back to standard Ubuntu LTS by replacing the Pro license with the non-Pro license on the disk.

      .. important::

         **Restrictions on downgrading:**

         * Downgrading is only permitted after a minimum of **90 days** (approximately 3 months) of Pro usage. The license change will fail if the Pro license was attached (or the instance was created) less than 90 days ago, as there is a retention period on all Pro and Pro-FIPS licenses.
         * Downgrading is **not allowed** for Ubuntu versions that have reached End of Standard Support (EOS). For example, downgrading from Ubuntu Pro 20.04 LTS (Focal) to Ubuntu 20.04 LTS is not permitted. The target version must still be within its standard support window.

      1. Stop your machine:

         .. code::

             gcloud compute instances stop $INSTANCE_NAME

      2. Update the license on the disk from Ubuntu Pro to Ubuntu LTS:

         .. code::

             gcloud compute disks update $INSTANCE_NAME --zone=$ZONE \
                 --replace-license=$PREVIOUS_LICENSE_URI,$NEW_LICENSE_URI

         where

         * ``$INSTANCE_NAME`` is the name of the instance to replace the license on;
         * ``$ZONE`` is the zone containing the instance;
         * ``$PREVIOUS_LICENSE_URI`` is the license URI for the Pro version currently on your VM; and
         * ``$NEW_LICENSE_URI`` is the license URI for the non-Pro version that you are downgrading to.

         You can only downgrade to the standard LTS version for the same Ubuntu series. If your VM runs Ubuntu Pro 22.04 LTS, you need to downgrade to Ubuntu 22.04 LTS.

         For ``$PREVIOUS_LICENSE_URI`` (Pro license to remove) choose the appropriate URI from:

         .. list-table::
            :header-rows: 1
            :widths: 20 50

            * - **Version**
              - **License URI**
            * - Ubuntu Pro 22.04 LTS
              - ``https://www.googleapis.com/compute/v1/projects/ubuntu-os-pro-cloud/global/licenses/ubuntu-pro-2204-lts``
            * - Ubuntu Pro 24.04 LTS
              - ``https://www.googleapis.com/compute/v1/projects/ubuntu-os-pro-cloud/global/licenses/ubuntu-pro-2404-lts``

         For ``$NEW_LICENSE_URI`` (standard LTS license to apply) choose the appropriate URI from:

         .. list-table::
            :header-rows: 1
            :widths: 20 50

            * - **Version**
              - **License URI**
            * - Ubuntu 22.04 LTS
              - ``https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/licenses/ubuntu-2204-lts``
            * - Ubuntu 24.04 LTS
              - ``https://www.googleapis.com/compute/v1/projects/ubuntu-os-cloud/global/licenses/ubuntu-2404-lts``

         .. note::

            Only Ubuntu versions that are still within their standard support period are listed. Versions that have reached End of Standard Support (such as 16.04, 18.04, and 20.04) cannot be downgraded.

         **Example** -- downgrading an Ubuntu Pro 22.04 LTS VM to Ubuntu 22.04 LTS:

         .. code::

             gcloud compute disks update $INSTANCE_NAME --zone=$ZONE \
                 --replace-license=projects/ubuntu-os-pro-cloud/global/licenses/ubuntu-pro-2204-lts,projects/ubuntu-os-cloud/global/licenses/ubuntu-2204-lts

      3. Start the machine:

         .. code::

             gcloud compute instances start $INSTANCE_NAME

      4. SSH into your machine and verify the downgrade by running:

         .. code::

             pro status

         The output should confirm that Ubuntu Pro services are no longer entitled.


.. _`upgrading to Pro`: https://docs.cloud.google.com/compute/docs/images/premium/ubuntu-pro/upgrade-from-ubuntu







