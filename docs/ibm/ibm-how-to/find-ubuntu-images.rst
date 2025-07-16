Find Ubuntu images on IBM Cloud
===============================


Using the web console
---------------------


.. tabs::

    .. group-tab:: IBM VPC infrastructure


        On your IBM Cloud console, you can find the latest Ubuntu images by navigating to
        :guilabel:`VPC Infrastructure` >
        :guilabel:`Compute` >
        :guilabel:`Images` >
        :guilabel:`Stock Images` >
        and then searching for ``Ubuntu`` in the :guilabel:`Search Images` search bar.

    .. group-tab:: IBM Classic infrastructure (legacy)
        
        On your IBM Cloud console, you can find the latest Ubuntu images by selecting ``Ubuntu`` as the operating system vendor under
        :guilabel:`Classic Infrastructure` > 
        :guilabel:`Devices` > 
        :guilabel:`Device List` > 
        :guilabel:`Order +` >
        :guilabel:`Virtual Server for Classic` > 
        :guilabel:`Operating System` > 
        :guilabel:`Ubuntu`


Using the CLI
-------------


.. tabs::

    .. group-tab:: IBM VPC infrastructure

        For a programmatic way to find the latest Ubuntu images, you can use the IBM Cloud CLI along with grep
        to filter the output.

        .. code-block:: bash

            ibmcloud is images --visibility "public" --status available | grep "ubuntu"

        For further information about this command, refer to `IBM's CLI documentation on is_images`_.

    .. group-tab:: IBM Classic infrastructure (legacy)

        For a programmatic way to find the latest Ubuntu images, you can use the IBM Cloud CLI along with grep
        to filter the output.

        .. code-block:: bash

            ibmcloud sl image list --public --name "Ubuntu"

        For further information about this command, refer to `IBM's CLI documentation`_.

.. _`IBM's CLI documentation on is_images`: https://cloud.ibm.com/docs/vpc?topic=vpc-vpc-reference#images-list
.. _`IBM's CLI documentation`: https://cloud.ibm.com/docs/cli?topic=cli-sl-manage-compute-images#sl_image_list