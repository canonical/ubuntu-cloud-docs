Find Ubuntu images on IBM Cloud
===============================


Using the IBM Cloud web console
-------------------------------


.. tabs::

    .. group-tab:: IBM VPC Infrastructure


        On your IBM Cloud Console, you can find the latest Ubuntu images by navigating to 
        :guilabel:`VPC Infrastructure` >
        :guilabel:`Compute` >
        :guilabel:`Images` >
        :guilabel:`Stock Images` >
        and then searching ``Ubuntu`` in the :guilabel:`Search Images` search bar. 

    .. group-tab:: IBM Classic Infrastructure (Legacy)
        
        On your IBM Cloud Console, you can find the latest Ubuntu images by selecting ``Ubuntu`` as the Operating System
        Vendor under 
        :guilabel:`Classic Infrastructure` > 
        :guilabel:`Devices` > 
        :guilabel:`Device List` > 
        :guilabel:`Order +` >
        :guilabel:`Virtual Server for Classic` > 
        :guilabel:`Operating System` > 
        :guilabel:`Ubuntu`


Using the IBM CLoud CLI
-----------------------


.. tabs::

    .. group-tab:: IBM VPC Infrastructure

        For a programmatic way to find the latest Ubuntu images, you can use the IBM Cloud CLI along with grep
        to filter the output.

        .. code-block:: bash

            ibmcloud is images --visibility "public" --status available | grep "ubuntu"

        For further information about this command, see the official IBM Cloud CLI documentation on `ibmcloud is images <https://cloud.ibm.com/docs/vpc?topic=vpc-vpc-reference#images-list>`_.

    .. group-tab:: IBM Classic Infrastructure (Legacy)

        For a programmatic way to find the latest Ubuntu images, you can use the IBM Cloud CLI along with grep
        to filter the output.

        .. code-block:: bash

            ibmcloud sl image list --public --name "Ubuntu"

        For further information about this command, see the official IBM Cloud CLI documentation on `ibmcloud sl image list <https://cloud.ibm.com/docs/cli?topic=cli-sl-manage-compute-images#sl_image_list>`_.
