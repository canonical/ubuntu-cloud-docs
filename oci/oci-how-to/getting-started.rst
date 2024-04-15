Getting started
***************

This is where to find the Ubuntu container images:

.. tabs::

	.. tab:: Docker Hub

         .. code-block:: bash

            docker pull ubuntu:latest
            

	.. tab:: Amazon ECR

         .. code-block:: bash
            
            docker pull public.ecr.aws/ubuntu/ubuntu:latest

	.. tab:: Microsoft ACR

         .. code-block:: bash
            
            docker pull ubuntu.azurecr.io/ubuntu:latest

	.. tab:: IronBank

         .. note::
            Please note that these Ubuntu container images may have special terms of use and fall under Ubuntu Pro. Please `reach out <rocks@canonical.com>`_ if you would like to use the Ubuntu container images from IronBank.
            



Refresh rate
------------

The Ubuntu base container images can be automatically updated multiple times a
day, depending on whether there have been upstream changes in the Ubuntu archives
affecting the packages that constitute the container image.

**Exception**: the only exception is the official Ubuntu image in Docker Hub which,
due to Docker's policies, cannot be submitted too regularly, and so are
only updated every two weeks.