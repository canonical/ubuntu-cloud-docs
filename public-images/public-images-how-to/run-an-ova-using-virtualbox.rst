.. _run-an-ova-using-virtualbox:

Run an OVA using VirtualBox
===========================

An :ref:`ova` is a single file package that allows for easy distribution and
setup of virtual machines (VMs). `VirtualBox <https://www.virtualbox.org/>`__ is an open source
virtualisation platform that allows you to use OVA files to create and
manage VMs. This guide will cover how to acquire an OVA file,
install VirtualBox, and configure and launch an Ubuntu VM that you can connect
to via the virtual console or over SSH.

Getting an OVA
--------------

The easiest way to get an OVA is to download one from
`cloud-images.ubuntu.com <https://cloud-images.ubuntu.com>`__. You can
get the latest daily OVA for a given
``$SERIES`` by downloading ``https://cloud-images.ubuntu.com/$SERIES/current/$SERIES-server-cloudimg-amd64.ova``.

We will create a new directory and get the latest daily for Ubuntu 24.04
LTS (Noble Numbat).

.. code:: bash

  mkdir virtualbox-ova
  cd virtualbox-ova/
  wget https://cloud-images.ubuntu.com/noble/current/noble-server-cloudimg-amd64.ova


Getting VirtualBox
------------------

There are two ways of getting VirtualBox depending on whether or not you
are on an Ubuntu system.

From the Ubuntu archive
~~~~~~~~~~~~~~~~~~~~~~~

If you are on Ubuntu, the simplest way to get VirtualBox is through the
Ubuntu archive, the official repository provided by Ubuntu.

.. code:: bash

  sudo apt update
  sudo apt install virtualbox

From the upstream source
~~~~~~~~~~~~~~~~~~~~~~~~

Alternatively, you can download VirtualBox from the `upstream
source <https://www.virtualbox.org/wiki/Downloads>`__. The page
provides instructions for installing VirtualBox on your OS, so they will
not be covered here.

Importing the OVA in VirtualBox
-------------------------------

Once the installation is complete you can start VirtualBox.

.. image:: run-an-ova-using-virtualbox-images/0-launch-virtualbox.png
   :align: center

Click **Import** or select **File > Import Appliance...** from the menu bar to add our OVA as a virtual appliance.

.. image:: run-an-ova-using-virtualbox-images/1-import-appliance.png
   :align: center

Click **Next** to proceed once you have selected your file.

.. image:: run-an-ova-using-virtualbox-images/2-appliance-settings.png
   :align: center

From here, we can modify the settings of the appliance. Double-click
on the items to change properties, or enable/disable applicable
properties using the check boxes. We will leave everything as per the
suggested settings. Click **Import** to continue.

.. image:: run-an-ova-using-virtualbox-images/3-imported-vm.png
   :align: center

Now from the VirtualBox home screen, we can select the imported
appliance from the left sidebar. Before we attempt to run the appliance however,
we will need to generate and attach an ISO image containing
configuration data for cloud-init to initialise the instance during
initial boot. This step is required since we are using a cloud image instead of a standard desktop image.
You can learn more about the local cloud-init datasource :ref:`here <use-local-cloud-init-ds>`.

Adding the local datasource
---------------------------

To create the ISO image we will use the ``cloud-localds`` function from
the ``cloud-utils`` package. On Ubuntu and Debian systems we can install
this via apt.

.. code:: bash

  sudo apt install cloud-utils

For other operating systems, follow the instructions in the `upstream
repository <https://github.com/canonical/cloud-utils>`__.

Additionally, you will need to have a set of SSH keys in order to set up
remote access for your machine. You can learn more about SSH keys and
how to generate them
`here <https://help.ubuntu.com/community/SSH/OpenSSH/Keys>`__.

Once those prerequisites are complete, we can generate and attach the
ISO seed image.

1. Make a YAML file with password authorisation enabled and your public
   SSH key. Replace ``<YOUR_PUB_KEY>`` with your public key.

.. code:: bash

  cat <<EOF > my-cloud-config.yaml
  #cloud-config
  chpasswd:
    list: |
      ubuntu:ubuntu
  expire: False
  ssh_pwauth: True
  ssh_authorized_keys: <YOUR_PUB_KEY>
  EOF

2. Make the ISO.

.. code:: bash

  cloud-localds my-seed.iso my-cloud-config.yaml

3. Attach the ISO as an optical drive.

  a. From the VirtualBox main menu, select the image on the left, right
     click and choose **Settings.**

  b. Select **Storage** from the menu options.

  .. image:: run-an-ova-using-virtualbox-images/4-add-optical.png
     :align: center

  c. Click on the +CD icon (**Adds Optical Drive**) beside **Controller:
     IDE.**

  .. image:: run-an-ova-using-virtualbox-images/5-select-seed.png
     :align: center

  d. Click **Add** and select the ``my-seed.iso`` file we created above, then
     click **Choose**.

We are now ready to launch the VM.

Launching the VM
----------------

From the VirtualBox main menu, click **Start**. This will open a new
window and begin the launch process for your VM. This may take some
time.

.. image:: run-an-ova-using-virtualbox-images/6-vm-login-prompt.png
   :align: center

When you reach the ``ubuntu login:`` prompt, enter the username and
password from the YAML file above. If you didn’t change the template,
both the username and password will be ``ubuntu``.

.. image:: run-an-ova-using-virtualbox-images/7-vm-logged-in.png
   :align: center

Success! Now is a good time to run some commands to ensure everything is
set up correctly.

-  Verify that you can access the internet.

.. code:: bash

   ping -c 3 ubuntu.com

-  Check your IP configuration (needed for connecting via SSH).

.. code:: bash

   ip a

-  Verify that the SSH service is running.

.. code:: bash

   sudo systemctl status ssh

-  Check disk configuration.

.. code:: bash

   df -h

When you have finished with you session, you can turn off the VM by
selecting **File** > **Close** from the top bar menu of the window
running the machine. There are more options available under the
**Machine** heading.

Connecting via SSH
------------------

To connect via SSH, we will make use of the bridged network adapter
that was configured during the appliance setup. You will need to have
the IP address of the VM. Run the following from the virtual console of
the VM.

.. code:: bash

  ip a

Below is an example output of this command.

.. terminal::

   $ ip a
   1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN
       group default qlen 1000
       link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
       inet 127.0.0.1/8 scope host lo
       valid_lft forever preferred_lft forever
   2: enp0s3: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel
       state UP group default qlen 1000
       link/ether xx:xx:xx:xx:xx:xx brd ff:ff:ff:ff:ff:ff
       inet 192.168.1.123/24 brd 192.168.1.255 scope global dynamic enp0s3
       valid_lft 86389sec preferred_lft 86389sec

We ignore the ``loopback`` interface and focus on the Ethernet interface
(``enp0s3``). The IP address we want is on the line starting with ``inet``.
In our case the IP address is ``192.168.1.123``.

After ensuring that the VM is running, we can now log in via SSH from out
host terminal with the command ``ssh $USERNAME@$IP_ADDRESS``.

.. code:: bash

  ssh ubuntu@192.168.1.123

If this is the first time connecting to this VM, you will have to
confirm that you want to connect.

.. terminal::

  $ ssh ubuntu@192.168.1.123
  The authenticity of host ‘192.168.1.123 (192.168.1.123)’ can’t be
  established.
  ED25519 key fingerprint is
  SHA256:7vJHf4BcNaZ9dQKSPG8tFw3uRlXnV1kTbmYgEjL0h5o.
  This key is not known by any other names
  Are you sure you want to continue connecting (yes/no/[fingerprint])?
  yes
  Warning: Permanently added ‘192.168.1.123’ (ED25519) to the list of
  known hosts.

When you are done with your SSH session, remember that disconnecting
will not power down the VM unless you explicitly called ``poweroff`` or
another similar command as part of that process.
