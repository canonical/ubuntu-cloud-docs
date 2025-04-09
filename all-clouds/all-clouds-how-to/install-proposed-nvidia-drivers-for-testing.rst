Install NVIDIA drivers from proposed pocket for testing
=======================================================
This guide will help you test your workload on NVIDIA drivers available in proposed pocket before they are released.

NVIDIA drivers are not immediately released for Ubuntu after they are available from NVIDIA. 
They are first available in the proposed pocket, where they undergo extensive testing before release. This process can take up to 11 weeks.
NVIDIA drivers in the proposed pocket are unsigned.


.. caution::

    Important considerations:
        1. Packages in the proposed pocket are intended for testing only. Please do not install NVIDIA drivers from proposed on production systems.
        2. If you have customized ``apt`` configurations, these instructions may introduce conflicts.
        3. Once the proposed pocket is enabled, new drivers will be installed as available in from the proposed pocket.  To ensure new unsigned drivers are not installed, changes must be rolled back.

For more details on installing proposed packages and Stable Release Update (SRU) testing see `Enable Proposed`_.

Enable the proposed pocket
------------------------------

First, enable the proposed pocket in ``apt`` configuration.

.. tabs::

    .. group-tab:: 22.04 and earlier

        .. code::

            export $(cat /etc/os-release | grep UBUNTU_CODENAME)

            # Add the proposed pocket
            sudo tee /etc/apt/sources.list.d/proposed.sources > /dev/null << EOF
            Types: deb
            URIs: https://archive.ubuntu.com/ubuntu/
            Suites: $UBUNTU_CODENAME-proposed
            Components: main restricted universe multiverse
            Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg
            EOF

            # Configure apt to allow selective installs of packages from proposed
            sudo tee /etc/apt/preferences.d/proposed-updates > /dev/null << EOF
            Package: *
            Pin: release a=$UBUNTU_CODENAME-proposed
            Pin-Priority: 400
            EOF

            # Update apt cache 
            sudo apt update


    .. group-tab:: 24.04 and later

        .. code::

            export $(cat /etc/os-release | grep UBUNTU_CODENAME)

            # Add the proposed pocket
            sudo tee /etc/apt/sources.list.d/proposed.sources > /dev/null << EOF
            Types: deb
            URIs: https://archive.ubuntu.com/ubuntu/
            Suites: $UBUNTU_CODENAME-proposed
            Components: main restricted universe multiverse
            Signed-By: /usr/share/keyrings/ubuntu-archive-keyring.gpg
            EOF

            # Update apt cache 
            sudo apt update



Install NVIDIA drivers from proposed
------------------------------------

Set ``NVIDIA_DRIVER_VERSION`` to the required driver version.

.. tabs::

   .. group-tab:: 22.04 and earlier

        .. code::

            export NVIDIA_DRIVER_VERSION=570 # Export the NVIDIA driver version you wish to install
            export $(cat /etc/os-release | grep UBUNTU_CODENAME)

            sudo apt install nvidia-driver-$NVIDIA_DRIVER_VERSION-server-open/$UBUNTU_CODENAME-proposed


   .. group-tab:: 24.04 and later

        .. code::

            export NVIDIA_DRIVER_VERSION=570 # Export the NVIDIA driver version you wish to install
            export $(cat /etc/os-release | grep UBUNTU_CODENAME)

            sudo apt install nvidia-driver-$NVIDIA_DRIVER_VERSION-server-open -t $UBUNTU_CODENAME-proposed


Make sure the expected NVIDIA driver is installed.

.. code::

    nvidia-smi


In order to ensure you update to the signed version of the driver as soon as it is available, it is recommended that you subscribe to the Launchpad bug associated with the SRU of the driver, e.g. https://bugs.launchpad.net/ubuntu/+source/nvidia-graphics-drivers-570-server/+bug/2095341.


Rolling back
------------

This section will guide you to replace drivers from proposed to the released version and remove proposed archive configuration from previous steps.
Note that this removes all package versions from proposed, not just the NVIDIA drivers, and installs their respective release versions.

Start by removing proposed archive configuration.

.. tabs::

   .. group-tab:: 22.04 and earlier

        .. code::

            sudo rm /etc/apt/sources.list.d/proposed.sources
            sudo rm /etc/apt/preferences.d/proposed-updates
            sudo apt update


   .. group-tab:: 24.04 and later

        .. code::

            sudo rm /etc/apt/sources.list.d/proposed.sources
            sudo apt update

Setup ``apt`` to, where necessary, downgrade to release version of packages on the system. 
Run ``apt upgrade`` to replace proposed package versions with the release versions.

.. code:: 
    
    export $(cat /etc/os-release | grep UBUNTU_CODENAME)
    
    # Configure apt to install from the release archive, even if that means downgrading packages
    sudo tee /etc/apt/preferences.d/release-pinning-for-downgrades > /dev/null << EOF
    Package: *
    Pin: release a=$UBUNTU_CODENAME*
    Pin-Priority: 1000
    EOF

    sudo tee /etc/apt/apt.conf.d/99-unproposed > /dev/null << EOF
    APT::Get::allow-downgrades "true";
    EOF

    sudo apt update

    # Replace proposed package versions with the release versions
    # This will also install available package updates
    # -y will skip any user prompts
    sudo apt upgrade -y


Finally, clean-up to prevent ``apt`` from downgrading packages going forward.

.. code::

    sudo rm /etc/apt/preferences.d/release-pinning-for-downgrades
    sudo rm /etc/apt/apt.conf.d/99-unproposed

    sudo apt update



.. LINKS
.. _Enable Proposed: https://wiki.ubuntu.com/Testing/EnableProposed
