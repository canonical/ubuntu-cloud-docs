# Upgrading from Focal Fossa to Jammy Jellyfish on GCE

## General Advice
When deciding how to upgrade an image, a main consideration should be whether the system can be setup or deployed with automation, or whether it requires manual configuration.

Running [`do-release-upgrade`](https://manpages.ubuntu.com/manpages/focal/man8/do-release-upgrade.8.html) currently requires some manual intervention ([see Manual upgrade steps](#Manual-upgrade-steps)), which makes it a good option for systems which require manual configuration and cannot be easily created or destroyed.

For system deployments which are fully automated, it is recommended to redeploy with a new Jammy Jellyfish instances instead of upgrading from Focal Fossa.

## Manual upgrade steps
If the workflow is to upgrade from Focal Fossa to Jammy Jellyfish, the following prompts requesting manual input should be expected.

### Additional SSH daemon
When upgrading in a session over SSH there is an inherent risk of losing access if something goes wrong with the SSH daemon. To mitigate this risk, an additional SSH daemon is started on a different port as a backup.
![A warning regarding the risk of upgrading in a session over SSH. The prompt is notifying the user that an additional SSH daemon will be started to mitigate the risk. The user is prompted whether they would like to continue or cancel the upgrade.](/docs/explanations/Google/GCE/Focal_To_Jammy_Upgrade_Images/additional-ssh-daemon.png)

### Optional firewall rules for additional SSH daemon
If a firewall is present, there is a chance the port used by the backup ``sshd`` is not open. Opening this port is not done automatically as it is a security risk.
![A warning that the port used by the backup ssh daemon could be blocked if there a firewall. An optional command to open the port is provided. The user is prompted to press enter to continue](/docs/explanations/Google/GCE/Focal_To_Jammy_Upgrade_Images/additional-ssh-daemon.png)

### Start upgrade
A final prompt before starting the upgrade. Information regarding the amount of changes and estimated time are provided. Once you start the upgrade process it cannot be cancelled.
![A prompt asking if the user would like to start the upgrade process. Some information is provided regarding the amount of changes and estimated time to complete. The user is prompted to continue, cancel or see additional details.](/docs/explanations/Google/GCE/Focal_To_Jammy_Upgrade_Images/start-upgrade.png)

### Restart services automatically
Some services need to be restarted when certain libraries are upgraded. The user has the option to allow the system to automatically restart these services or to be asked after every library upgrade which services they want to be restarted.
![A prompt asking the user if they would like services to be restarted automatically during package upgrades. If no is selected there will be prompts later for which services to restart on each library upgrade.](/docs/explanations/Google/GCE/Focal_To_Jammy_Upgrade_Images/restart-services.png)

### ``sshd`` configuration modified
Canonical makes changes to `/etc/ssh/sshd_config` for GCE images. As a result when upgrading there will be a prompt asking whether to keep this version, use the default in the newer version, or take some other action.
![A prompt notifying the user that there is a newer version available of the sshd_config file. Options include keeping the local version, using the default and a couple of other actions.](/docs/explanations/Google/GCE/Focal_To_Jammy_Upgrade_Images/configure-open-ssh-server.png)

### ``chrony`` configuration modified
Due to a possible bug in ``ucf``, even if there are no changes in ``/etc/chrony/chrony.conf`` there will be a prompt asking whether to keep the current version, use the default in the newer version, or take some other action.
![A prompt notifying the user that there is a newer version available of chrony. Options include keeping the local version, using the default and a couple of other actions.](/docs/explanations/Google/GCE/Focal_To_Jammy_Upgrade_Images/chony-configuration.png)

### Remove obsolete packages
An obsolete package is a package which is no longer available in any of the sources for ``apt``. Usually it is safe and recommended to remove these packages, but the option to verify which packages are to be removed is available.
![A prompt asking the user if they wish to remove obsolete packages. There are options for yes, no and more details.](/docs/explanations/Google/GCE/Focal_To_Jammy_Upgrade_Images/delete-old-pkgs.png)

### Restart to finish upgrade
A restart will be necessary for some parts of the upgrade to be applied. If no is selected, `/var/run/reboot-required.pkgs` may be checked to see which services need rebooting to be applied.
![A prompt asking the user to restart the system because it is required to complete the upgrade.](/docs/explanations/Google/GCE/Focal_To_Jammy_Upgrade_Images/upgrade-finished.png)
