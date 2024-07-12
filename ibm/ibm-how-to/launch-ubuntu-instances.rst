Launch an Ubuntu VSI on IBM Cloud
=================================

To launch a Virtual Server Instance (VSI) with Ubuntu on IBM Cloud, you can use either the IBM Cloud web console or the CLI. 

.. note::
   
   A Virtual Server Instance (VSI) is IBM's equivalent of a virtual machine. For more information, refer to `IBM's documentation about VSI`_.

Before starting, ensure that you have an active IBM Cloud account. If you don't, you can `sign up for one`_.


Using the web console
---------------------
On the IBM Cloud web console:

* Go to :guilabel:`VPC Infrastructure` > :guilabel:`Compute`> :guilabel:`Virtual server instances`>, and select :guilabel:`Create +` to open the virtual server creation form.  
* Enter a unique name for your VSI in the `Name` field.
* Under the image section, go to :guilabel:`Change image` > :guilabel:`Stock Images` and search for "Ubuntu" in the search bar to select the Ubuntu OS of your preference.
* Choose the desired profile for your VSI under the `Profile` section.
* Select an existing ssh key or create a new one using :guilabel:`Add SSH key`.
* Customise any other settings as needed and select :guilabel:`Create virtual server` to launch your VSI.

Using the CLI
-------------

Install and configure the CLI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
To install the CLI, follow the `IBM instructions for installing CLI`_. Once installed, authenticate with your IBM Cloud account, by running:

.. code-block:: bash

   ibmcloud login
 
Install the VPC infrastructure plugin:

.. code-block:: bash

   ibmcloud plugin install vpc-infrastructure

Set VPC CLI to use generation 2:

.. code-block:: bash

   ibmcloud is target --gen 2


Create an SSH key pair
~~~~~~~~~~~~~~~~~~~~~~

SSH key pairs are needed to log in to a VSI from your local machine. To create one, follow the `IBM  instructions for creating key pairs`_.

Find an Ubuntu image
~~~~~~~~~~~~~~~~~~~~

Use :doc:`Find Ubuntu images <find-ubuntu-images>` to find an appropriate Ubuntu image and its ID.


Choose a zone and region
~~~~~~~~~~~~~~~~~~~~~~~~

When creating a VSI, you'll need to specify a region and zone for the VSI to be created in. For a list of available regions and zones, refer to `IBM's documentation about regions`_.


Set the region (e.g. us-south):

.. code-block:: bash

   ibmcloud is target --region us-south


Create other needed resources
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you don't have an existing VPC, subnet and security group, set them up by following `IBM's instructions for creating VPC resources`_. Note the created VPC ID for later use.

For existing VPCs, you can list them using:

.. code-block:: bash

   ibmcloud is vpcs


Launch the VSI
~~~~~~~~~~~~~~

Create the VSI using:

.. code-block:: bash

   ibmcloud is instance-create MyInstance \
            <vpc-id> <zone> <instance-type> <image-id> \
            --keys <ssh-key-id>


Replace ``<vpc-id>``, ``<zone>``, ``<image-id>`` and ``<ssh-key-id>`` with the information gathered above. If you need help deciding on the instance-type refer to `IBM's documentation on instance profiles`_.

An example command with the image ID for Ubuntu 24.04 LTS (and other IDs hidden) would look something like this:

.. code-block:: bash

   ibmcloud is instance-create MyUbuntuInstance \ 
            xxxx-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx us-south-1 bx2-2x8 \
            r006-3a44e4ee-9c9f-4693-98ae-fced7a46ffce \
            --keys xxxx-xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx

The command initiates the creation of your VSI and may take a few minutes to complete.


Access Your VSI
~~~~~~~~~~~~~~~

After the instance is provisioned, access it via SSH:

.. code-block:: bash

   ssh -i ~/.ssh/id_rsa ubuntu@<Instance-Public-IP>

where `<Instance-Public-IP>` is the public IP address of your new VSI.


Terminate Your VSI
~~~~~~~~~~~~~~~~~~

When you are finished with your VSI, you can terminate it using:

.. code-block:: bash

   ibmcloud is instance-delete <instance-id>


.. _`IBM's documentation about VSI`: https://cloud.ibm.com/docs/vpc?topic=vpc-about-advanced-virtual-servers
.. _`sign up for one`: https://cloud.ibm.com/registration
.. _`IBM instructions for installing CLI`: https://cloud.ibm.com/docs/cli?topic=cli-getting-started
.. _`IBM  instructions for creating key pairs`: https://cloud.ibm.com/docs/vpc?topic=vpc-managing-ssh-keys&interface=cli
.. _`IBM's documentation about regions`: https://cloud.ibm.com/docs/vpc?topic=vpc-creating-a-vpc-in-a-different-region&interface=cli
.. _`IBM's instructions for creating VPC resources`: https://cloud.ibm.com/docs/vpc?topic=vpc-creating-vpc-resources-with-cli-and-api&interface=cli#creating-a-vpc-using-cli
.. _`IBM's documentation on instance profiles`: https://cloud.ibm.com/docs/vpc?topic=vpc-profiles&interface=ui