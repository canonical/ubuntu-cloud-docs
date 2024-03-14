Launch and connect to an Ubuntu Mantic desktop EC2 instance
===========================================================

This how to uses xrdp server and Remmina to connect to an AWS EC2 instance of Ubuntu Mantis.

Select and configure Ubuntu Mantic 
----------------------------------

Open AWS Marketplace and search for Ubuntu Mantic. Subscribe and agree to the Terms and Conditions. Select Launch Instance to configure.

Select a region closest to you. For exapmple, if you're in the ``UK EU-West-2`` would be a good option. Click :guilabel:`Continue to Launch Through EC2 Instance`.

Give your instance a name. Mantic requires least two cores and at least 8gb RAM, which should be the default option. The default volume space of 8gb is the minimum required, however, more space will be required to install applications.

Create a security group
-----------------------

Select :guilabel:`Create Security Group`. Make sure the ssh tick box is selected to allow remote access.

You can select an existing key pair if you already have one set up or create a new key pair. To create a key pair give it a name and Select ``RSA`` and ``PEM``. A Pem file will be automatically downloaded.

Launch the instance and connect to it either via ssh or the AWS Console.

Install Ubuntu Desktop Packages
-------------------------------

.. code::

    sudo apt-get update && apt-get upgrade -y
    sudo apt-get install -y ubuntu-desktop
    sudo snap install snap-store --edge

Install and Configure RDP
-------------------------

Install the xrdp server.

.. code::

    sudo apt-get install -y xrdp

Configure xrdp to use SSL to get an encrypted connection.

.. code::

    sudo usermod -a -G ssl-cert xrdp

Set up a password for the Ubuntu user.

.. code::

    passwd

Finally, restart the xrdp service.

.. code::

    systemctl restart xrdp

Configure the Ubuntu Session
----------------------------

Connect to your instance using RDP to check the previous steps were succseful. Create a configuration script called ``ubuntu-session`` in ``/usr/local/bin/`` to run on RDP connections.

.. code::

    sudo nano /usr/local/bin/ubuntu-session

Add the following to the ubuntnu-session script.

.. code::

    #!/bin/sh

    export GNOME_SHELL_SESSION_MODE=ubuntu
    export DESKTOP_SESSION=ubuntu-xorg
    export XDG_SESSION_DESKTOP=ubuntu-xorg
    export XDG_CURRENT_DESKTOP=ubuntu:GNOME
    
    exec /usr/bin/gnome-session --session=ubuntu

Make the script executable.

.. code::

    sudo chmod +x /usr/local/bin/ubuntu-session

Update the session manager to use the new session configuration.

.. code::

    update-alternatives --install /usr/bin/x-session-manager x-session-manager /usr/local/bin/ubuntu-session 60



Allow traffic on the VNC port
-----------------------------

Ensure that the relevant port of your Mantic EC2 Instance is open. On the EC2 console, modify the inbound rules for your instance by adding an entry for TCP port 5901: ``Custom TCP Rule | TCP | 5901 | Custom | 0.0.0.0/0 | VNC Connect`` 


Install Remmina on your local machine
--------------------------------------

To access the Ubuntu desktop installed on your VM, use a remote desktop client like Remmina on your local machine. Install Remmina using:

.. code::

    sudo apt install remmina


Connect to your remote Ubuntu desktop
-------------------------------------

Launch Remmina, and choose the connection type as 'VNC'. For the connection string, enter your EC2 instance URL along with 1 as the port number, something similar to:

.. code::

    ec2-54-172-197-171.compute-1.amazonaws.com:1

Select :guilabel:`Connect!` and enter the VNC server password saved earlier. This should give you access to the remote Ubuntu desktop.
