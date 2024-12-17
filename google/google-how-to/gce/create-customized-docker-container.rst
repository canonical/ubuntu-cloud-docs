Create customized docker containers on Ubuntu Pro
=================================================

Docker containers are extremely useful for running applications reliably on different computing environments. This is because they package the application along with all its dependencies into a single image that can be easily deployed.

Docker is the underlying technology used to run these containers / images. Docker also allows you to modify the container and create new customized versions easily. As an example, on your Ubuntu Pro VM, we'll run a container based on the latest Ubuntu image and then customize it by including Python.  


.. Note::

    If you don't have an Ubuntu Pro VM already, you can create one based on :ref:`create-pro-on-gcp`


Install Docker
--------------

On your Ubuntu Pro VM, the easiest way to install Docker is to use snap. Update your package manager data and then install docker using:

.. code::

    sudo apt update
    sudo snap install docker


Download a Docker image
-----------------------

Search for available Ubuntu images:

.. code::

    sudo docker search ubuntu

You'll find many ubuntu related images, some of which have an [OK] under the 'OFFICIAL' column indicating that they are images built and supported by a company.

.. code::

    NAME                             DESCRIPTION                                     STARS     OFFICIAL   AUTOMATED
    ubuntu                           Ubuntu is a Debian-based Linux operating sys…   16442     [OK]       
    websphere-liberty                WebSphere Liberty multi-architecture images …   297       [OK]       
    ubuntu-upstart                   DEPRECATED, as is Upstart (find other proces…   115       [OK]       
    neurodebian                      NeuroDebian provides neuroscience research s…   104       [OK]       
    ubuntu/nginx                     Nginx, a high-performance reverse proxy & we…   100                  
    ubuntu/squid                     Squid is a caching proxy for the Web. Long-t…   67                   
    [...]

Pull the latest official Ubuntu image:

.. code::

    sudo docker pull ubuntu

It'll give an output similar to:

.. code::

    Using default tag: latest
    latest: Pulling from library/ubuntu
    445a6a12be2b: Pull complete 
    Digest: sha256:aabed3296a3d45cede1dc866a24476c4d7e093aa806263c27ddaadbdce3c1054
    Status: Downloaded newer image for ubuntu:latest
    docker.io/library/ubuntu:latest

You can check the downloaded images using:

.. code::

    sudo docker images

The image that you just pulled will show up in the output:

.. code::

    REPOSITORY   TAG       IMAGE ID       CREATED       SIZE
    ubuntu       latest    c6b84b685f35   6 weeks ago   77.8MB


Run the container
-----------------

Run a container based on this downloaded image and it'll take you to the new container's command prompt:

.. code::

    sudo docker run -it ubuntu
    root@0587b9a5915d:/# 

In this container, you can check if it is the latest version of Ubuntu:

.. code::

    cat /etc/lsb-release

.. code::

    DISTRIB_ID=Ubuntu
    DISTRIB_RELEASE=22.04
    DISTRIB_CODENAME=jammy
    DISTRIB_DESCRIPTION="Ubuntu 22.04.3 LTS"


Customize the image
-------------------

To customize the image, you can for instance install Python within the container:

.. code::

    apt update
    apt install python3

Check the installed version:

.. code::

    /usr/bin/python3 -V

.. code::

    Python 3.10.12

Now that you have modified the original Ubuntu image, you can save the changes to create a new image. Use ``Ctrl + P`` and ``Ctrl + Q`` to exit the container interface and get back into the VM.

To save the changes you'll need the container ID (of the container where you made the changes). You can get this by checking the containers running on your VM:

.. code::

    sudo docker ps

.. code::

    CONTAINER ID   IMAGE     COMMAND       CREATED         STATUS         PORTS     NAMES
    0587b9a5915d   ubuntu    "/bin/bash"   3 minutes ago   Up 3 minutes             quirky_lamarr

Now commit the changes to create a new Docker image:

.. code::

    sudo docker commit -m "installed python3" -a "myname" 0587b9a5915d

where the parameter -m (message) is used to indicate the changes made and -a (author) is used to indicate the author of the changes.

If you look at the list of images on your VM, you'll see the newly added one:

.. code::

    sudo docker images

.. code::

    REPOSITORY   TAG       IMAGE ID       CREATED          SIZE
    <none>       <none>    4fad28bffebd   53 seconds ago   152MB
    ubuntu       latest    c6b84b685f35   6 weeks ago      77.8MB

