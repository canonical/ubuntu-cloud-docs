Launch an Ubuntu Virtual Server Instance (VSI) on IBM Cloud
===========================================================

This how-to guide will give instructions for launching a Virtual Server Instance (VSI), 
IBM's equivalent of a virtual machine, on IBM Cloud using Ubuntu.
For more information on VSI's, see the official IBM Cloud documentation: `About virtual server instances for VPC <https://cloud.ibm.com/docs/vpc?topic=vpc-about-advanced-virtual-servers>`_.

Ensure you have an active IBM Cloud account before starting. If you do not have an account, you can sign up for one at
https://cloud.ibm.com/registration


Via Web Console
----------------

#. First, on the IBM Cloud Web Console, navigate to the Virtual Server creation form. To do this, navigate to     
   :guilabel:`VPC Infrastructure` > :guilabel:`Compute`> :guilabel:`Virtual server instances`>, 
   and then click on the blue :guilabel:`Create +`.  
#. Enter a unique name for your VSI in the `Name` field.
#. Under the image section, press on :guilabel:`Change image` and under the :guilabel:`Stock Images` tab, search for
   "Ubuntu" in the search bar and select the Ubuntu OS you'd like to use. For the most recent OS, select :code:`ibm-ubuntu-24-04-minimal-amd64-1`
#. Choose the desired profile for your VSI under the `Profile` section.
#. Select an existing ssh key or create a new one by pressing on :guilabel:`Add SSH key` and following the instructions.
#. Customize any other settings as needed.
#. Press on the blue :guilabel:`Create virtual server` button to launch your VSI.

Via IBM Cloud CLI
-----------------

Install IBM Cloud CLI
~~~~~~~~~~~~~~~~~~~~~
follow the official installation instructions from IBM: https://cloud.ibm.com/docs/cli?topic=cli-getting-started

once installed, you'll need to authenticate with your IBM Cloud account before running any commands. To do this, run:

.. code-block:: bash

   ibmcloud login

Then to use VPC Infrastructure, you will need to install the VPC Infrastructure plugin:

.. code-block:: bash

   ibmcloud plugin install vpc-infrastructure

Then set VPC CLI to use generation 2:

.. code-block:: bash

   ibmcloud is target --gen 2


Create ssh key
~~~~~~~~~~~~~~

SSH key pairs are needed to log in to a VSI from your local machine. To create an SSH key pair,
follow the IBM  instructions for creating key pairs:
https://cloud.ibm.com/docs/vpc?topic=vpc-managing-ssh-keys&interface=cli


Find an Ubuntu image
~~~~~~~~~~~~~~~~~~~~

To launch an instance that uses Ubuntu, you'll need to choose an appropriate Ubuntu image and get the image ID for it.
Follow the instructions from the :doc:`Find images <find-ubuntu-images>`


Choose a zone and region
~~~~~~~~~~~~~~~~~~~~~~~~

When creating a VSI, you'll need to specify a region and zone for the VSI to be created in.

For the purposes of this how-to, we'll use the `us-south` region and the `us-south-1` zone. You can choose a different
region and zone if you prefer.  
Refer to the official IBM Cloud documentation for a list of available regions and zones: https://cloud.ibm.com/docs/vpc?topic=vpc-creating-a-vpc-in-a-different-region&interface=cli


Set the region:

.. code-block:: bash

   ibmcloud is target --region us-south


Create all other resources needed for the VSI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Refer to IBM Cloud's 'Creating VPC resources with CLI and API' documentation for instructions on creating a VPC, subnet,
and security group, if you do not already have these resources set up:
https://cloud.ibm.com/docs/vpc?topic=vpc-creating-vpc-resources-with-cli-and-api&interface=cli#creating-a-vpc-using-cli

Be sure to note the ID of the VPC you wish to launch the VSI in. 

For this how-to, we'll just use an existing VPC. To list existing VPCs, run:

.. code-block:: bash

   ibmcloud is vpcs


Launch the Virtual Server Instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

With all necessary information in hand, create your VSI:

.. code-block:: bash

   ibmcloud is instance-create MyInstance <vpc-id> <zone> <instance-type> <image-id> --keys <ssh-key-id>


- Replace `<ssh-key-id>` with the ID of the SSH key you wish to login to the VSI with.
- Replace `<vpc-id>` with the ID of the VPC you wish to launch the VSI in.
- Replace `<zone>` with the zone you wish to launch the VSI in. We suggest using `us-south-1` for this how-to.

See https://cloud.ibm.com/docs/vpc?topic=vpc-profiles&interface=ui for information on selecting a profile.

A filled out example command would look like this:

.. code-block:: bash

   ibmcloud is instance-create TODO: fill in the rest of the command

This command initiates the creation of your Virtual Server Instance. The process may take a few minutes.


Access Your VSI
~~~~~~~~~~~~~~~

After the instance is provisioned, access it via SSH:

.. code-block:: bash

   ssh -i ~/.ssh/id_rsa ubuntu@<Instance-Public-IP>

Replace `<Instance-Public-IP>` with the public IP address of your new VSI.


Terminate Your VSI
~~~~~~~~~~~~~~~~~~

When you are finished with your VSI, you can terminate it to avoid incurring further charges:

.. code-block:: bash

   ibmcloud is instance-delete <instance-id>
