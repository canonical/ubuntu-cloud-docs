# Upgrading from Focal to Jammy on Oracle

## General Advice
When deciding how to upgrade the main consideration is whether your system can be setup/deployed with automation or requires manual configuration.

Running [`do-release-upgrade`](https://manpages.ubuntu.com/manpages/focal/man8/do-release-upgrade.8.html) requires some manual intervention ([see Manual upgrade steps](#manual-upgrade-steps)), which makes it a good option for systems which require manual configuration and cannot be easily created or destroyed.

For system deployments which are fully automated it is recommended to redeploy with new Jammy instances instead of upgrading from Focal.

## Manual upgrade steps
If you are upgrading from Focal to Jammy you can expect to run into the following prompts requesting manual input.

### Additional SSH daemon
When upgrading in a session over SSH there is an inherent risk of losing access if something goes wrong with the SSH daemon. To mitigate this risk an additional SSH daemon is started on a different port as a backup.
![A warning regarding the risk of upgrading in a session over SSH. The prompt is notifying the user that an additional SSH daemon will be started to mitigate the risk. The user is prompted whether they would like to continue or cancel the upgrade.](Focal_To_Jammy_Upgrade_Images/0_additional_ssh_daemon.png)

### Optional firewall rules for additional SSH daemon
If you are using a firewall there is a chance the port used by the backup SSHD is not open. Opening this port is not done automatically since it could be security risk.
![An informational warning that the port used by the backup SSH daemon could be blocked if you are using a firewall. Opening the port is not done automatically due to security risks. An optional command to open the port is provided. The user is prompted to press enter to continue](Focal_To_Jammy_Upgrade_Images/1_firewall_for_additional_ssh.png)

### Start upgrade
A final prompt before starting the upgrade. Information regarding the amount of changes and estimated time are provided because once you start the upgrade process it cannot be cancelled.
![A prompt asking if the user would like to start the upgrade process. Some information is provided regarding the amount of changes and estimated time to complete. The user is prompted to continue, cancel or see additional details.](Focal_To_Jammy_Upgrade_Images/2_start_upgrade.png)

### Restart services automatically
Some services need to be restarted when certain libraries are upgraded. The user has the option to allow the system to automatically restart these services or to be asked after every library upgrade which services they want to be restarted.
![A prompt asking the user if they would like services to be restarted automatically during package upgrades. If no is selected there will be prompts later for which services to restart on each library upgrade.](Focal_To_Jammy_Upgrade_Images/3_restart_services.png)

### Iptables configuration modified
Canonical makes changes to `/etc/iptables/rules.v4` and `/etc/iptables/rules.v6` for Oracle images. As a result when upgrading there will be a prompt asking whether to save current IPv4 and IPv6 rules even if no user changes were made. If additional changes to iptables rules were made, selecting `Yes` is recommended if preserving those added rules is desired.  Selecting `No` will use the prexisting persistent `rules.v4` and `rules.v6` which contain the Canonical changes, unless previously modified.
![A prompt asking the user if they wish to save current IPv4 rules. Options are Yes or No.](Focal_To_Jammy_Upgrade_Images/4_ipv4_save_rules)
![A prompt asking the user if they wish to save current IPv6 rules. Options are Yes or No.](Focal_To_Jammy_Upgrade_Images/5_ipv6_save_rules)

### SSHD configuration modified
Canonical makes changes to `/etc/ssh/sshd_config` for Oracle images. As a result when upgrading there will be a prompt asking whether to keep this version, use the default in the newer version or take some other action.
![A prompt notifying the user that there is a newer version available of the sshd_config file. Options include keeping the local version, using the default and a couple other actions.](Focal_To_Jammy_Upgrade_Images/6_sshd_modified_config.png)

### Remove obsolete packages
An obsolete package is a package which is no longer available in any of the sources for Apt. Usually it is safe and recommended to remove obsolete packages but you can verify which packages would be removed before doing so.
![A prompt asking the user if they wish to remove obsolete packages. There are options for yes, no and more details.](Focal_To_Jammy_Upgrade_Images/7_remove_obsolete.png)

### Restart to finish upgrade
A restart will be necessary for some parts of the upgrade to be applied. If you select no to the restart you can check `/var/run/reboot-required.pkgs` to see which things need a reboot to be applied.
![A prompt asking the user to restart the system because it is required to complete the upgrade.](Focal_To_Jammy_Upgrade_Images/8_finish_upgrade.png)
