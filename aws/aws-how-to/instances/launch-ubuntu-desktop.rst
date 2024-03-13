Launch and connect to an Ubuntu Mantic desktop instance on EC2
==============================================================

This how to uses Tightvnc and Remmina to connect to an AWS EC2 instance of Ubuntu Mantis.

Select and configure Ubuntu Mantis 
----------------------------------

Open AWS Marketplace and search for Ubuntu Mantic. Subscribe and agree to the Terms and Conditions. Select Launch Instance to configure.

Select a region closest to you. eg if you're in the UK EU-West-2 would be a good option. Cick Continue to Launch Through EC2 Instance.

Name your instance Ubuntu Mantic. Mantic requires least two cores and at least 8gb RAM, which should be the default option. A minimum of 8gb volumes space is required, however in order to allow space to install more applications, more space will be needed.

Create a security group
-----------------------

Select Create Security Group. Make sure ssh tick box is ticked to allow remote access.

If you already have instances set up, you can select a key pair that you have previously set up. However, if this is your first EC2 instance you will need to create a key pair. Select Create Key Pair.

Name the Key Pair, select RSA and Pem and create key pair. A Pem file will be downloaded automatically.

Launch instance and connect either via ssh or the AWS Console.


Install TightVNC on Ubuntu Mantic instance
------------------------------------------

To install Ubuntu desktop and TightVNC server on your EC2 instance, SSH into it and run:

.. code::

    sudo apt update
    sudo apt install ubuntu-desktop
    sudo apt install tightvncserver
    sudo apt install gnome-panel gnome-settings-daemon metacity nautilus gnome-terminal

Save the password created during the installation of the VNC server.


Configure the VNC server
------------------------

On your VM, launch the VNC server to create an initial configuration file:

.. code::

    vncserver :1

Edit the configuration file ``~/.vnc/xstartup`` to include:

.. code::

    #!/bin/sh

    export XKL_XMODMAP_DISABLE=1
    unset SESSION_MANAGER
    unset DBUS_SESSION_BUS_ADDRESS

    [ -x /etc/vnc/xstartup ] && exec /etc/vnc/xstartup
    [ -r $HOME/.Xresources ] && xrdb $HOME/.Xresources
    xsetroot -solid grey

    vncconfig -iconic &
    gnome-panel &
    gnome-settings-daemon &
    metacity &
    nautilus &
    gnome-terminal &


Kill and restart the VNC server:

.. code::

    vncserver -kill :1

    vncserver :1


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
