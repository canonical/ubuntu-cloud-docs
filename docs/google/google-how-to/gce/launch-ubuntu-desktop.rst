Launch an Ubuntu desktop on a VM
================================

If you want an Ubuntu desktop environment on your VM, you can set it up and use the `Chrome Remote Desktop`_ service to access it from your local Chrome web browser.

.. Note::

    1. These instructions work for a VM running Ubuntu 22.04 LTS.
    2. If you don't have an Ubuntu VM already, you can create one based on :ref:`create-lts-on-gcp`, but using ``Ubuntu 22.04 LTS`` as the OS version.


Install Chrome Remote Desktop
-----------------------------

SSH into your VM and update the package manager:

.. code::

    sudo apt update

Download and install the Chrome Remote Desktop installation package:

.. code::

    wget https://dl.google.com/linux/direct/chrome-remote-desktop_current_amd64.deb
    sudo apt-get install --assume-yes ./chrome-remote-desktop_current_amd64.deb


Install Ubuntu desktop
----------------------

Install a lightweight graphical display manager like SLiM (Simple Login Manager) on your VM: 

.. code::

    sudo apt install slim 


Install the Ubuntu desktop environment:

.. code::

    sudo apt install ubuntu-desktop

During the installation,

* you might be asked to choose the default display manager, with ``slim`` highlighted. Select it by hitting the enter key. 
* you might be asked to select the services that need a restart. Some of the services are selected by default, accept that selection by hitting the enter key.

Once the installation is done, reboot the machine:

.. code::

    sudo reboot


SSH back into the VM when the connection is restored, and start SLiM:

.. code::

    sudo service slim start


Configure the remote desktop service
------------------------------------

To start the remote desktop connection, you'll need an authorization key. This can be created using Chrome on your local machine. Browse to the `Chrome Remote Desktop setup`_ page, where you'll see the option to `Set up another computer` on the `Set up via SSH` tab.

* Select :guilabel:`Begin`
* Select :guilabel:`Next`, since you have already installed Chrome Remote Desktop on the remote computer
* Select :guilabel:`Authorize`
* Copy the command shown for `Debian Linux`.

Back on your VM's SSH window:

* Paste the command and run it
* Enter a 6-digit pin when prompted. This pin will be needed during remote login to the VM.


Connect to your Ubuntu desktop
------------------------------

On your local machine, go to the `Chrome Remote Desktop access`_ page, and you'll see your VM under `Remote devices` on the `Remote Access` tab. Select the VM and you will be prompted to input the 6-digit pin that you created in the previous step.

You might see a window with messages similar to "This session logs you into Ubuntu". Select :guilabel:`OK` to close the window. If you see a page that says "Authentication is required to create a color managed device", select :guilabel:`Cancel` to ignore it.

You might also see a setup screen that you can follow through by selecting :guilabel:`Start Setup` > :guilabel:`Next` > :guilabel:`Next` > :guilabel:`Start Using Ubuntu`

Your VM with an Ubuntu desktop is now fully functional and accessible within your Chrome browser. Select :guilabel:`Activities` to access search and other desktop shortcuts.



.. _`Chrome Remote Desktop`: https://support.google.com/chrome/answer/1649523
.. _`Chrome Remote Desktop setup`: https://remotedesktop.google.com/headless
.. _`Chrome Remote Desktop access`: https://remotedesktop.google.com/access