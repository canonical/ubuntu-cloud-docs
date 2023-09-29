Build Ubuntu Pro golden image
=============================

A golden image is a base image that is used as a template for your virtual machines. You can create it from your Google Cloud console's `Cloud Shell` (as explained below) or using other tools like Packer. 

We'll be using Ubuntu Pro 22.04 as the base image, although the steps should work fine for all Pro images available in your console.


Create a golden image
---------------------

In your Google Cloud console, search for the 'Cloud Shell' product and open it by selecting :guilabel:`Go to console`. Once in, look for the available Ubuntu Pro images:

.. code::
    
    gcloud compute images list --project=ubuntu-os-pro-cloud | grep ubuntu-pro

.. code::

    NAME: ubuntu-pro-1604-xenial-v20230710
    FAMILY: ubuntu-pro-1604-lts
    NAME: ubuntu-pro-1804-bionic-arm64-v20230921
    FAMILY: ubuntu-pro-1804-lts-arm64
    NAME: ubuntu-pro-1804-bionic-v20230921
    FAMILY: ubuntu-pro-1804-lts
    NAME: ubuntu-pro-2004-focal-arm64-v20230920
    FAMILY: ubuntu-pro-2004-lts-arm64
    NAME: ubuntu-pro-2004-focal-v20230920
    FAMILY: ubuntu-pro-2004-lts
    NAME: ubuntu-pro-2204-jammy-arm64-v20230921
    FAMILY: ubuntu-pro-2204-lts-arm64
    NAME: ubuntu-pro-2204-jammy-v20230921
    FAMILY: ubuntu-pro-2204-lts
    NAME: ubuntu-pro-fips-1804-bionic-v20230530
    FAMILY: ubuntu-pro-fips-1804-lts
    NAME: ubuntu-pro-fips-2004-focal-v20230920
    FAMILY: ubuntu-pro-fips-2004-lts

From the options seen, choose Ubuntu Pro 22.04 and use its family name in the golden image creation command below:

.. code::

    gcloud compute images create golden-image3 --source-image-family=ubuntu-pro-2204-lts --source-image-project=ubuntu-os-pro-cloud

In a bit you'll see output similar to the following and the created golden image will be available in your `image gallery`_. 

.. code::

    Created [https://www.googleapis.com/compute/v1/projects/[YOUR_PROJECT]/global/images/golden-image3].
    NAME: golden-image3
    PROJECT: [YOUR_PROJECT]
    FAMILY: 
    DEPRECATED: 
    STATUS: READY

Verify that the image contains the Ubuntu Pro license:

.. code::

    gcloud compute images describe golden-image3

.. code::

    architecture: X86_64
    archiveSizeBytes: '1094443008'
    creationTimestamp: '2023-09-29T03:56:22.275-07:00'
    diskSizeGb: '10'
    guestOsFeatures:
    - type: VIRTIO_SCSI_MULTIQUEUE
    - type: SEV_CAPABLE
    - type: SEV_SNP_CAPABLE
    - type: SEV_LIVE_MIGRATABLE
    - type: UEFI_COMPATIBLE
    - type: GVNIC
    id: '8518177910815396794'
    kind: compute#image
    labelFingerprint: 42WmSpB8rSM=
    licenseCodes:
    - '2592866803419978320'
    licenses:
    - https://www.googleapis.com/compute/v1/projects/ubuntu-os-pro-cloud/global/licenses/ubuntu-pro-2204-lts
    name: golden-image3
    selfLink: https://www.googleapis.com/compute/v1/projects/ubuntu-dimple/global/images/golden-image3
    shieldedInstanceInitialState:
    [...]

The line starting with "licenses:" shows the expected Pro license.


Create an instance using the golden image
-----------------------------------------

To create an instance based on this golden image, run:

.. code::

    gcloud compute instances create instance-from-golden-image --image=golden-image3

.. code::

    Created [https://www.googleapis.com/compute/v1/projects/ubuntu-dimple/zones/asia-southeast1-a/instances/instance-from-golden-image].
    NAME: instance-from-golden-image
    ZONE: asia-southeast1-a
    MACHINE_TYPE: n1-standard-1
    PREEMPTIBLE: 
    INTERNAL_IP: 10.148.0.2
    EXTERNAL_IP: 34.143.153.215
    STATUS: RUNNING

Now SSH into this new instance:

.. code::

    gcloud compute ssh instance-from-golden-image
 
The SSH command might need you to create an SSH key for gcloud if you don't have one already. Once you complete the steps and reach the prompt of the new instance, check its license by running:

.. code::

    ua status

The output should be similar to the following and indicates that Pro features such as ESM and livepatch are enabled.

.. code::

    SERVICE          ENTITLED  STATUS    DESCRIPTION
    anbox-cloud      yes       disabled  Scalable Android in the cloud
    esm-apps         yes       enabled   Expanded Security Maintenance for Applications
    esm-infra        yes       enabled   Expanded Security Maintenance for Infrastructure
    livepatch        yes       enabled   Canonical Livepatch service
    usg              yes       disabled  Security compliance and audit tools

    For a list of all Ubuntu Pro services, run 'pro status --all'
    Enable services with: pro enable <service>

                    Account: ubuntu-dimple
            Subscription: ubuntu-dimple
                Valid until: Fri Dec 31 00:00:00 9999 UTC
    Technical support level: essential


Share the golden image
----------------------

To share this golden image with other users, you'll need to add them as principals and assign the `Compute Image User` role to them. This will give them permission to list, read, and use the image but not to modify it.

Go to your `image gallery`_, select the image that you just created. In the INFO PANEL on the right, select :guilabel:`PERMISSIONS` > :guilabel:`ADD PRINCIPAL`:

* In the `Add principals` field insert the email addresses of all the users that you want to share your image with. 
* In the `Assign roles` field, select :guilabel:`Compute Engine` > :guilabel:`Compute Image User`

On saving these settings, the specified users will have access to the image. 

You can also grant users the `Viewer IAM` role for the project that you used to create the image in. This will ensure that the shared image appears in their image selection list.


.. _`image gallery`: https://console.cloud.google.com/compute/images