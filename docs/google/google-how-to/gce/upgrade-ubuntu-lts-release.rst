.. meta::
   :description: Learn how to upgrade Ubuntu LTS releases on GCE. Includes manual intervention steps and best practices to ensure a smooth upgrade process.


.. _upgrade-ubuntu-lts-release:

Upgrade Ubuntu LTS release on GCE
==================================

General advice
---------------

Once you have decided to upgrade your system, the next question is how? There are two options depending on whether your system is setup/deployed with automation or whether it requires manual configuration.

For fully automated system deployments it is recommended to redeploy with new instances instead of upgrading from an older release.

For systems that cannot be easily created or destroyed and require manual configuration, running `do-release-upgrade <https://manpages.ubuntu.com/manpages/noble/en/man8/do-release-upgrade.8.html>`_ is a good option. However this option requires some :ref:`manual intervention <manual intervention gce lts>` as explained below.

Getting started
----------------

Ensure all the packages on your machine are current:

.. code-block::

   sudo apt update -y
   sudo apt upgrade -y
   sudo reboot

Run the following command to start the release upgrade process:

.. code-block::

   sudo do-release-upgrade


.. _manual intervention gce lts:

Manual intervention steps
-------------------------

While upgrading releases, manual decision making will be needed for the following options that are presented.

New release announcement
~~~~~~~~~~~~~~~~~~~~~~~~~

After downloading and verifying the upgrade tool, you'll see a welcome message for the new release with links to its release notes:

.. code-block:: text

   Checking for a new Ubuntu release

   = Welcome to Ubuntu 24.04 LTS 'Noble Numbat' =

   ...

   Continue [yN]

Type ``y`` and press :kbd:`Enter` to continue.

Additional SSH daemon
~~~~~~~~~~~~~~~~~~~~~

When upgrading in a session over SSH there is an inherent risk of losing access if something goes wrong with the SSH daemon. To mitigate this risk an additional SSH daemon is started on a different port as a backup.

You'll see a prompt similar to the following, and you can either continue or cancel the upgrade:

.. code-block:: text

   Continue running under SSH?

   This session appears to be running under ssh. It is not recommended
   to perform a upgrade over ssh currently because in case of failure it
   is harder to recover.

   If you continue, an additional ssh daemon will be started at port
   '1022'.
   Do you want to continue?

   Continue [yN]

Type ``y`` and press :kbd:`Enter` to continue. A follow-up informational message confirms the additional daemon is starting on port 1022:

.. code-block:: text

   Starting additional sshd

   To make recovery in case of failure easier, an additional sshd will
   be started on port '1022'. If anything goes wrong with the running
   ssh you can still connect to the additional one.

   To continue please press [ENTER]

Press :kbd:`Enter` to continue (no ``y``/``N`` needed here).


Optional firewall rules for additional SSH daemon
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This step only appears if a firewall is active on the instance and blocking port 1022. If you are using a firewall there is a chance that the port used by the backup SSHD is not open. Opening this port is not done automatically since it could be a security risk. You'll see a prompt similar to:

.. code-block:: text

   If you run a firewall, you may need to temporarily open this port. As
   this is potentially dangerous it's not done automatically. You can
   open the port with e.g.:
     iptables -I INPUT -p tcp --dport 1022 -j ACCEPT

   To continue please press [ENTER]

If needed, open the port from another terminal before continuing:

.. code-block::

   sudo iptables -I INPUT -p tcp --dport 1022 -j ACCEPT

Then press :kbd:`Enter` in the upgrade session to continue.


Third party sources disabled
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Any third-party entries in your ``sources.list`` are temporarily disabled for the duration of the upgrade:

.. code-block:: text

   Third party sources disabled

   Some third party entries in your sources.list were disabled. You can
   re-enable them after the upgrade with the 'software-properties' tool
   or your package manager.

   To continue please press [ENTER]

Press :kbd:`Enter` to continue. You can re-enable these sources after the upgrade completes.


Start upgrade
~~~~~~~~~~~~~

A final prompt is provided before starting the upgrade. It gives information about the number of changes and the estimated time to complete because once started, the upgrade process cannot be canceled:

.. code-block:: text

   Do you want to start the upgrade?

   1 installed package updates are no longer downloadable.
   123 packages are going to be removed. 456 new packages are going to be
   installed. 789 packages are going to be upgraded.

   To continue please press [ENTER]

   Continue [yN]  Details [d]

Type ``y`` and press :kbd:`Enter` to start the upgrade, or ``d`` to see additional details first.


Restart services automatically
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

During the upgrade of certain libraries, dependent services may need to be restarted. In most cases this is handled automatically and silently as each package is unpacked, shown as informational output rather than a prompt:

.. code-block:: text

   Checking for services that may need to be restarted...
   Checking init scripts...
   Nothing to restart.

If services are detected that need restarting and the system cannot decide automatically, you may instead see an interactive prompt (as seen separately during a regular ``apt upgrade``) asking which services to restart, for example:

.. code-block:: text

   Which services should be restarted?

    1. service-a.service   2. service-b.service   3. none of the above

   (Enter the items or ranges you want to select, separated by spaces.)

Enter the full range (for example ``1-2``) to restart all listed services, excluding "none of the above".


Modified configuration files
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Depending on several factors, including the Ubuntu release, you may see a prompt during the upgrade notifying you about the availability of a newer version of a configuration file. In such cases, you'll be asked whether you want to keep the existing modified version, use the default one from the new version of the associated package, or take some other action. The following is an example of the prompt you might see for the file ``/etc/chrony/chrony.conf``:

.. code-block:: text

   Modified configuration file
   ---------------------------

   A new version (/usr/share/chrony/chrony.conf) of configuration file /etc/chrony/chrony.conf is available, but the version installed
   currently has been locally modified.

     1. install the package maintainer's version             5. show a 3-way difference between available versions
     2. keep the local version currently installed            6. do a 3-way merge between available versions
     3. show the differences between the versions             7. start a new shell to examine the situation
     4. show a side-by-side difference between the versions
   What do you want to do about modified configuration file chrony.conf?

If you don't know why the file was modified or aren't sure which version to keep, option ``2`` (keep the local version currently installed) is the safer default, since it preserves whatever is already working on your instance. Only choose option ``1`` if you specifically want to discard local changes and reset to the package default.


Remove obsolete packages
~~~~~~~~~~~~~~~~~~~~~~~~

An obsolete package is a package which is no longer available in any of the sources for apt. Usually it is safe and recommended to remove obsolete packages:

.. code-block:: text

   Remove obsolete packages?

   28 packages are going to be removed.

   Continue [yN]  Details [d]

Type ``y`` and press :kbd:`Enter` to remove them, or ``d`` to see the full list first.


Restart to finish upgrade
~~~~~~~~~~~~~~~~~~~~~~~~~

Finally, a restart will be necessary for some parts of the upgrade to be applied:

.. code-block:: text

   System upgrade is complete.

   Restart required

   To finish the upgrade, a restart is required.
   If you select 'y' the system will be restarted.

   Continue [yN]

Type ``y`` and press :kbd:`Enter` to restart. If you select ``N``, you can check later for the packages that need a reboot:

.. code-block::

   cat /var/run/reboot-required.pkgs
