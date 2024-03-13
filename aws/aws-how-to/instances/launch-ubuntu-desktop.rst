Launch and connect to an Ubuntu Mantis desktop instance on EC2
==============================================================


Open AWS Marketplace and search for Ubuntu Mantis, subscribe and agree to the Terms and Conditions.



Install TightVNC on Ubuntu Mantis instance
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

To allow an external connection to the VNC server, you'll need to ensure that the relevant port of your VM is open. On your EC2 console, modify the inbound rules for your instance by adding an entry for TCP port 5901: ``Custom TCP Rule | TCP | 5901 | Custom | 0.0.0.0/0 | VNC Connect`` 


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
