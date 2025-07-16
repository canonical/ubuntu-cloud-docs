Find Ubuntu images on Oracle Cloud 
==================================

Different versions of Ubuntu images are available on Oracle Cloud: 

* All LTS releases that haven't reached end of life 
* Full and minimal versions
* Versions for x86_64 and AArch64 (ARM64) platforms

For each of these versions, Oracle publishes a new image build every month. The latest three builds (for each version) are always listed on their cloud console, while the older ones are archived. 

Find the latest Ubuntu images
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

You can find the latest three image builds using either the web console or the CLI.

.. tabs::

    .. group-tab:: Web console

      While creating an instance using :guilabel:`Compute` > :guilabel:`Instances` > :guilabel:`Create instance`, under *Image and shape* select :guilabel:`Change image` > :guilabel:`Ubuntu`. From the displayed list, select your desired LTS release and variant (full or minimal). Then use the drop-down to select one of the three builds available for it.

      .. image:: find-ubuntu-images-images/1_latest_ubuntu_image.png
    
      The latest build is always recommended as it'll have the most recent package updates and security vulnerability fixes. However, if you need a specific build, you can either choose one of the remaining two builds or refer to the :ref:`Find older Ubuntu images<old_images>` section ahead.


    .. group-tab:: CLI

      To find images using the CLI, run: 
      
      .. code::

        oci compute image list --all --compartment-id <ocid> --operating-system "Canonical Ubuntu"
      
      where ``<ocid>`` is replaced with the appropriate compartment ID.
      
      It will return a JSON output with details for all available image builds. You can use ``jq`` to filter the fields that you need. You can also optionally include --region <region_name> to search in a region different from the one configured in your ~/.oci/config file. Note that the id of the images will be different for different regions. 

      Other options can also be added to the command. For instance, to list all Ubuntu 22.04 LTS base images (non-minimal versions), use:

      .. code::

        oci compute image list --all --compartment-id <compartment_id> --operating-system "Canonical Ubuntu"
          --operating-system-version 22.04
      
      which (after some filtering) will give an output similar to:

      .. code::

        {
          "data": [
            {
              [...]
              "display-name": "Canonical-Ubuntu-22.04-aarch64-2023.09.27-0",
              [...]
              "id": "ocid1.image.oc1.iad.aaaaaaaah3ahpwe2l4bpxl3q3hiz6ovnw2fmakh3ma4dnauhniktmiwxl72q",
              [...]
              "operating-system": "Canonical Ubuntu",
              "operating-system-version": "22.04",
              [...]
            },
            {
              [...]
              "display-name": "Canonical-Ubuntu-22.04-aarch64-2023.08.23-0",
              [...]
              "id": "ocid1.image.oc1.iad.aaaaaaaa6owneddgivjqxbot4nmftxao2t4lodkifzr54tqcrts26v2ppqra",
              [...]
              "operating-system": "Canonical Ubuntu",
              "operating-system-version": "22.04",
              [...]
            },
            {
              [...]
              "display-name": "Canonical-Ubuntu-22.04-aarch64-2023.07.20-0",
              [...]
              "id": "ocid1.image.oc1.iad.aaaaaaaagbgiy3w3psyvqarm5lcyjyort7ufmcx7qisizxsae3rdm6k75odq",
              [...]
              "operating-system": "Canonical Ubuntu",
              "operating-system-version": "22.04",
              [...]
            },
            {
              [...]
              "display-name": "Canonical-Ubuntu-22.04-2023.09.27-0",
              [...]
              "id": "ocid1.image.oc1.iad.aaaaaaaaxdnjyq2drtrl5njggtas25gspssotsdzpa55cdpxwafda7essgna",
              [...]
              "operating-system": "Canonical Ubuntu",
              "operating-system-version": "22.04",
              [...]
            },
            {
              [...]
              "display-name": "Canonical-Ubuntu-22.04-2023.08.28-0",
              [...]
              "id": "ocid1.image.oc1.iad.aaaaaaaaevjttsicdlm4h3zomclg6pztgxgg7ba54e27c4oopvkbaftvjqna",
              [...]
              "operating-system": "Canonical Ubuntu",
              "operating-system-version": "22.04",
              [...]
            },
            {
              [...]
              "display-name": "Canonical-Ubuntu-22.04-2023.07.20-0",
              [...]
              "id": "ocid1.image.oc1.iad.aaaaaaaaq7lzb7lkmbnp6zlcbgbcxnypaugvm2cymqtmpfsyd45jxub5ktha",
              [...]
              "operating-system": "Canonical Ubuntu",
              "operating-system-version": "22.04",
              [...]
            }
          ]
        }
      
      This sample output shows three images for AArch64 (ARM64) and three for AMD64.

      Once you know the id of the image you want, you can create an instance with:
      
      .. code:: 

        oci compute instance launch 
          --compartment-id <compartment>
          --availability-domain <availability-domain>
          --subnet-id <public-subnet>
          --image-id <image-id>
          --display-name ubuntu-vm
          --shape VM.Standard.E4.Flex
          --shape-config '{"ocpus": 1, "memoryInGBs": 12}' 
          --assign-public-ip true 
          --ssh-authorized-keys-file ~/.ssh/id_rsa.pub

      These are the minimal parameters that you'll need to provide with the ``instance launch`` command. For further details about this command and all of its options, refer to the `Oracle CLI documentation`_ for launching a Linux instance.

.. _old_images:

Find older Ubuntu images
~~~~~~~~~~~~~~~~~~~~~~~~

If you want to use an image that is older than the latest three builds, you need to know its Oracle Cloud Identifier (OCID) and use that while creating the instance. 

To find the OCID of archived images, visit `Oracle's image documentation`_ website and select the required Ubuntu release. A list of all available variants for that release will be displayed. Browse to the desired variant to see its OCID for each region.

With the region / image specific OCID, you can create an instance either through the web console or through the CLI.

.. tabs::

    .. group-tab:: Web console

      While creating an instance using :guilabel:`Compute` > :guilabel:`Instances` > :guilabel:`Create instance`, under *Image and shape* select :guilabel:`Change image` > :guilabel:`My images`. Then choose :guilabel:`Image OCID` as the image source and enter the OCID (obtained above) before launching the instance.

      .. image:: find-ubuntu-images-images/2_older_ubuntu_image.png

    .. group-tab:: CLI

      Use the --image-id flag while creating the instance:

      .. code::

        oci compute instance launch 
          --compartment-id <compartment>
          --availability-domain <availability-domain>
          --subnet-id <public-subnet>
          --image-id <image-id>
          --display-name ubuntu-vm
          --shape VM.Standard.E4.Flex
          --shape-config '{"ocpus": 1, "memoryInGBs": 12}' 
          --assign-public-ip true 
          --ssh-authorized-keys-file ~/.ssh/id_rsa.pub


Find Ubuntu images for use on OKE nodes 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ubuntu images are available for worker nodes on Oracle Kubernetes Engine (OKE) in Oracle Cloud. You need to find a suitable image and register it before you can use it to create OKE nodes. 

.. include:: ../../reuse/OKE-nodes.txt
   :start-after: Start: Find and register an image
   :end-before: End: Find and register an image
  

.. _`Oracle CLI documentation`: https://docs.public.oneportal.content.oci.oraclecloud.com/en-us/iaas/Content/GSG/Tasks/gettingstartedwiththeCLI.htm#launchLinux
.. _`Oracle's image documentation`: https://docs.oracle.com/en-us/iaas/images/
.. _`managing custom images`: https://docs.oracle.com/en-us/iaas/Content/Compute/Tasks/managingcustomimages.htm
.. _`import from-object-uri`: https://docs.oracle.com/en-us/iaas/tools/oci-cli/3.59.0/oci_cli_docs/cmdref/compute/image/import/from-object-uri.html


