.. _cis_post_deploy_hardening:

Post-deployment CIS Hardening for Ubuntu 22.04 EC2
==================================================

This guide explains how to apply **CIS Level 1** controls that are **not**
pre-configured in Canonical’s Ubuntu 22.04 *CIS-hardened* AMIs.  
Because these controls require environment-specific details,
they cannot be included in our base AMI.

CIS 5.1.4 - Restrict *sshd* Access
----------------------------------

Limit SSH log-ins to known users or groups.

1. Edit */etc/ssh/sshd_config* **above** any ``Include`` or ``Match`` lines::

      sudo nano /etc/ssh/sshd_config

2. Add one (or a mix) of the following:

   .. code-block:: none

      AllowUsers  ubuntu  your allowed users
      AllowGroups your allowed groups
      # DenyUsers  baduser
      # DenyGroups oldstaff

   The *first* occurrence of each directive wins, even with ``Include`` files.

3. Reload SSH::

      sudo systemctl restart sshd

.. warning::

   Consider opening a **second** SSH session to test your new config before closing the first, to confirm you are not locked out.

CIS 4.2.8 - Set a default-deny policy
-------------------------------------

The base CIS hardened image already contains the base chains so all you need to do is

1. Add permit rules for ``loopback``, established traffic, and SSH:

   .. code-block:: console

      # add the ssh INPUT rules right in the input chain
      sudo sed -i '/^[[:space:]]*chain input {/a\
      \        ct state established,related accept\n\
      \        tcp dport 22 ct state new accept'  /etc/inet-filter.rules

   .. code-block:: console
   
      # add http/s output rules for cloudinit to function
      sudo sed -i '/^[[:space:]]*chain output {/a\
      \        tcp dport 80 ct state new accept\n\
      \        tcp dport 443 ct state new accept\n\
      \        ct state established,related accept'  /etc/inet-filter.rules


2. Activate a **DROP** policy on the existing chains

   .. code-block:: console

      # set the default to drop
      sudo sed -Ei 's/\<policy[[:space:]]+accept;/policy drop;/' /etc/inet-filter.rules

   (The output chain can be left ``accept`` if you prefer; CIS allows either as long as needed rules are present.)

3. Reload from disk (make the above config changes active) ::

      sudo nft -c -f /etc/nftables.conf
      sudo nft -f /etc/nftables.conf

.. warning::

   If the default is changed to drop without a carve-out for ssh connections your current connection will be dropped with no way to make new connections. Consider testing on a temporary instance beforehand.


CIS 1.1.2.1.x - Isolate and Harden ``/tmp``
-------------------------------------------

The world-writable ``/tmp`` directory should reside on its own filesystem with
``nodev,nosuid,noexec``. We recommend using a ``tmpfs`` though any free partition is usable.  

1. (Optional) back up current contents:

   .. code-block:: console

      sudo mkdir -p /mnt/tmpbackup
      sudo cp -a /tmp/. /mnt/tmpbackup/

2. In ``/etc/fstab`` add:

   .. code-block:: none

      tmpfs  /tmp  tmpfs  rw,nodev,nosuid,noexec,relatime,size=2G  0  0

   Replacing 2G with your preferred size

3. Remount::

      Either reboot or run 'sudo mount -a' to apply the changes immediately.

CIS 1.4.1 - Set a GRUB 2 boot-loader password
---------------------------------------------

Ubuntu’s default GRUB installation lets anyone with EC2 serial console access to an instance modify kernel parameters on boot. While this is a rather specific attack surface, CIS requires protecting those actions with a boot-loader password.


1. **Generate the hash**

   .. code-block:: console

      sudo grub-mkpasswd-pbkdf2 --iteration-count=600000 --salt=64
      Enter password:
      Reenter password:
      PBKDF2 hash of your password is grub.pbkdf2.sha512.600000.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

2. **Add the hash to a custom /etc/grub.d config file:**

   .. code-block:: console

      sudo tee /etc/grub.d/01_password >/dev/null <<'EOF'
      #!/bin/sh
      exec tail -n +3 $0
      set superusers="grubadmin"
      password_pbkdf2 grubadmin grub.pbkdf2.sha512.600000.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
      EOF

   .. code-block:: console
      
      sudo chmod 600 /etc/grub.d/01_password

   Replace ``grubadmin`` with any username you like, and paste the full
   ``PBKDF2`` string from step 1 in place of the long ``grub.pbkdf2…`` value.

3. **Allow unattended boots**

   To allow the instance to boot without entering the password through the serial console (while still requiring it for *edit / command-line* access), edit */etc/grub.d/10_linux* and add ``--unrestricted`` to the line ``CLASS=``

   .. code-block:: console

      sudo sed -i 's/^CLASS="\(.*\)"/CLASS="\1 --unrestricted"/' \
          /etc/grub.d/10_linux

4. **Update GRUB**

   .. code-block:: console

      sudo update-grub



Additional Password-Policy Controls
-----------------------------------

By default EC2 instances are configured to use public keys and no passwords for ssh. If you for whatever reason **enable** local passwords, to comply with CIS, you must also configure:

* ``PASS_MAX_DAYS``, ``PASS_MIN_DAYS``, ``PASS_WARN_AGE`` in
  ``/etc/login.defs``
* Inactivity lock:: ``sudo chage -I 45 <user>``
* Complexity in ``/etc/security/pwquality.conf``
* Password history::

      password requisite pam_pwhistory.so remember=10 use_authtok

* Add ``enforce_for_root`` to relevant PAM lines if root gains a password.
