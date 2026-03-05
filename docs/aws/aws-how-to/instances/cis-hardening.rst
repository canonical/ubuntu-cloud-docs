.. _cis_post_deploy_hardening:

Post-deployment CIS Hardening for Ubuntu 22.04 EC2
==================================================

.. note::

   Amazon Inspector currently implements the CIS benchmark 2.0.0 version for Ubuntu 22.04, and 1.0.0 for Ubuntu 24.04, which may be updated in the future.
   This may cause the exact version number of a control to differ from the one listed here, but the underlying issue will remain the same.

This guide explains how to apply **CIS Level 1** controls that are **not**
pre-configured in Canonical's Ubuntu 22.04 *CIS-hardened* AMIs.  
Because these controls require environment-specific details,
they cannot be included in our base AMI.


CIS 6.2.1.2.2 - Configure ``systemd-journal-remote`` authentication
-------------------------------------------------------------------

``systemd-journal-upload`` supports the ability to send log events it gathers to a remote log host.

1. Edit the ``/etc/systemd/journal-upload.conf`` file or a file in ``/etc/systemd/journal-upload.conf.d``.
   Ensure the following lines are set in the [Upload] section as per your environment::

      [Upload]
      URL=192.168.50.42
      ServerKeyFile=/etc/ssl/private/journal-upload.pem
      ServerCertificateFile=/etc/ssl/certs/journal-upload.pem
      TrustedCertificateFile=/etc/ssl/ca/trusted.pem

2. Restart the service

.. code-block:: console

   systemctl restart systemd-journal-upload

CIS 5.1.4 - Restrict *sshd* Access
----------------------------------

Limit SSH log-ins to known users or groups.

1. Edit */etc/ssh/sshd_config* **above** any ``Include`` or ``Match`` lines::

      sudo nano /etc/ssh/sshd_config

2. Add one (or a mix) of the following:

   .. code-block:: none

      AllowUsers  ubuntu  $ALLOWED_USER_1 $ALLOWED_USER_2
      AllowGroups $ALLOWED_GROUP_1 $ALLOWED_GROUP_2
      # DenyUsers  baduser
      # DenyGroups oldstaff

   The *first* occurrence of each directive takes precedence over any other occurrence of the same directive.

3. Reload SSH

.. code-block:: console

   sudo systemctl restart sshd

.. warning::

   Consider opening a **second** SSH session to test your new ``config`` before closing the first, to confirm you are not locked out.

CIS 4.2.8 - Set a default-deny policy
-------------------------------------

The base CIS hardened image already contains the base chains (ordered lists of ``nftables`` rules for how a connection should be handled), so all you need to do is:

1. Add permit rules for ``loopback``, established traffic, and SSH:

   .. code-block:: console

      # add the ssh input rules to allow ssh connections to be made
      sudo sed -i '/^[[:space:]]*chain input {/a\
      \        ct state established,related accept\n\
      \        tcp dport 22 ct state new accept'  /etc/inet-filter.rules

   .. code-block:: console
   
      # add http/s output rules to allow cloudinit to function
      sudo sed -i '/^[[:space:]]*chain output {/a\
      \        tcp dport 80 ct state new accept\n\
      \        tcp dport 443 ct state new accept\n\
      \        ct state established,related accept'  /etc/inet-filter.rules


2. Set default policies on the chains

   A **DROP** policy denies all traffic by default unless explicitly allowed by earlier rules.
   An **ACCEPT** policy allows all traffic by default. CIS requires a DROP policy on the input chain.
   The output chain can remain ACCEPT (allowing all outbound traffic) if you prefer, since inbound
   traffic is already restricted and the rules above permit necessary outbound connections.

   .. code-block:: console

      # set the default to drop
      sudo sed -Ei 's/\<policy[[:space:]]+accept;/policy drop;/' /etc/inet-filter.rules

3. Reload from disk (make the above ``config`` changes active) ::

      sudo nft -c -f /etc/nftables.conf
      sudo nft -f /etc/nftables.conf

.. warning::

   If the input chain policy is changed to drop without a carve-out for SSH, your current 
   connection will be dropped. Always add SSH rules (step 1) before setting the drop policy (step 2).


CIS 1.1.2.1.x - Isolate and Harden ``/tmp``
-------------------------------------------

The world-writable ``/tmp`` directory should reside on its own filesystem with
``nodev,nosuid,noexec``. We recommend using a ``tmpfs``, though any free partition is usable.

1. (Optional) back up current contents:

   .. code-block:: console

      sudo mkdir -p /mnt/tmpbackup
      sudo cp -a /tmp/. /mnt/tmpbackup/

2. In ``/etc/fstab`` add:

   .. code-block:: none

      tmpfs  /tmp  tmpfs  rw,nodev,nosuid,noexec,relatime,size=2G  0  0

   Replacing 2G with your preferred size

3. Remount: Either ``reboot`` or run:

   .. code-block::

      sudo mount -a

   to apply the changes immediately.

CIS 1.4.1 - Set a GRUB 2 boot-loader password
---------------------------------------------

.. note::

   Most EC2 guidance strongly discourages setting a GRUB password because it can prevent
   automated reboots and recovery operations. This control is included here for completeness.

Ubuntu's default GRUB installation allows anyone to modify kernel parameters on boot, if they have EC2 serial console access to the instance. While this is a rather specific attack surface, CIS requires protecting those actions with a boot-loader password.

1. **Generate the hash**

   .. code-block:: console

      sudo grub-mkpasswd-pbkdf2 --iteration-count=600000 --salt=64
      Enter password:
      Reenter password:
      PBKDF2 hash of your password is grub.pbkdf2.sha512.600000.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX

2. **Add the hash to a custom /etc/grub.d ``config`` file:**

   .. code-block:: console

      sudo tee /etc/grub.d/01_password >/dev/null <<'EOF'
      #!/bin/sh
      exec tail -n +3 $0
      set superusers="grubadmin"
      password_pbkdf2 grubadmin grub.pbkdf2.sha512.600000.XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
      EOF

   Replace ``grubadmin`` with any username you like, and paste the full
   ``PBKDF2`` string from step 1 in place of the long ``grub.pbkdf2…`` value.

   .. code-block:: console
      
      sudo chmod 600 /etc/grub.d/01_password

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

By default EC2 instances use SSH public-key authentication - local passwords are disabled.
If you **enable** local passwords, the following CIS Level 1 controls are also required.

.. note::

   Settings in ``/etc/login.defs`` only apply to **new** accounts. For existing accounts, use
   the ``chage`` command shown in each section.

CIS 5.4.1.1 - Password expiration / CIS 5.4.1.3 - Expiration warning days
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Edit ``/etc/login.defs`` and set:

.. code-block:: none

   PASS_MAX_DAYS   365
   PASS_MIN_DAYS   1
   PASS_WARN_AGE   7

For existing accounts::

   sudo chage --maxdays 365 --mindays 1 --warndays 7 <user>

CIS 5.4.1.5 - Inactive password lock
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Lock accounts after 30 days of inactivity. Set the system default::

   sudo useradd -D -f 30

For existing accounts::

   sudo chage -I 30 <user>

CIS 5.3.2.4 / 5.3.3.3 - Enable ``pam_pwhistory`` and configure password history
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Enable the ``pam_pwhistory`` module and configure it in ``/etc/pam.d/common-password``.
Add or update the line so that:

* ``remember=24`` retains the last 24 passwords (CIS 5.3.3.3.1)
* ``use_authtok`` ensures the module re-uses the token set by an earlier module (CIS 5.3.3.3.3)
* ``enforce_for_root`` applies history enforcement to the root account (CIS 5.3.3.3.2)

.. code-block:: none

   password required pam_pwhistory.so remember=24 use_authtok enforce_for_root

CIS 5.3.3.4.1 / 5.3.3.4.2 - Remove ``nullok`` and ``remember`` from ``pam_unix``
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ensure the ``pam_unix`` entry in ``/etc/pam.d/common-password`` and ``/etc/pam.d/common-auth``
does **not** include ``nullok`` (which allows blank passwords) or ``remember`` 
(password history is handled by ``pam_pwhistory`` above, not ``pam_unix``):

.. code-block:: console

   sudo sed -i 's/ nullok//g; s/ remember=[0-9]*//g' /etc/pam.d/common-password
   sudo sed -i 's/ nullok//g; s/ remember=[0-9]*//g' /etc/pam.d/common-auth

CIS 5.3.3.1.2 - Password unlock time
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Set the account unlock time after failed login attempts in ``/etc/security/faillock.conf``:

.. code-block:: console

   sudo sed -i 's/^#\?\s*unlock_time.*/unlock_time = 900/' /etc/security/faillock.conf

CIS 5.3.3.2 - Password complexity (``pwquality``)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Edit ``/etc/security/pwquality.conf`` to configure complexity requirements:

.. list-table::
   :header-rows: 1
   :widths: 15 20 15 50

   * - CIS control
     - Setting
     - Value
     - Description
   * - 5.3.3.2.1
     - ``difok``
     - ``2``
     - Minimum characters that must differ from the previous password
   * - 5.3.3.2.4
     - ``maxrepeat``
     - ``3``
     - Maximum allowed consecutive identical characters
   * - 5.3.3.2.5
     - ``maxsequence``
     - ``3``
     - Maximum allowed monotonic character sequence (e.g. ``abcd``, ``1234``)
   * - 5.3.3.2.8
     - ``enforce_for_root``
     - *(flag)*
     - Apply complexity rules to the root account as well

Apply all settings:

.. code-block:: console

   FILE=/etc/security/pwquality.conf

   sudo grep -qE '^[[:space:]]*#?[[:space:]]*difok\>' "$FILE" \
   && sudo sed -i -E 's|^[[:space:]]*#?[[:space:]]*difok\>.*|difok = 2|' "$FILE" \
   || echo 'difok = 2' | sudo tee -a "$FILE" >/dev/null

   sudo grep -qE '^[[:space:]]*#?[[:space:]]*maxrepeat\>' "$FILE" \
   && sudo sed -i -E 's|^[[:space:]]*#?[[:space:]]*maxrepeat\>.*|maxrepeat = 3|' "$FILE" \
   || echo 'maxrepeat = 3' | sudo tee -a "$FILE" >/dev/null

   sudo grep -qE '^[[:space:]]*#?[[:space:]]*maxsequence\>' "$FILE" \
   && sudo sed -i -E 's|^[[:space:]]*#?[[:space:]]*maxsequence\>.*|maxsequence = 3|' "$FILE" \
   || echo 'maxsequence = 3' | sudo tee -a "$FILE" >/dev/null

   sudo grep -qE '^[[:space:]]*#?[[:space:]]*enforce_for_root\>' "$FILE" \
   && sudo sed -i -E 's|^[[:space:]]*#?[[:space:]]*enforce_for_root\>.*|enforce_for_root|' "$FILE" \
   || echo 'enforce_for_root' | sudo tee -a "$FILE" >/dev/null


Known Scan Issues
-----------------

The following CIS checks are known to produce false-positive failures in Amazon Inspector.
They represent limitations in the Inspector implementation of the CIS benchmark rather
than genuine security gaps in the image.

CIS 6.2.2.1 - Ensure access to all ``logfiles`` has been configured
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Amazon Inspector flags ``/var/log/apt/history.log`` (mode ``0644``). The apt package manager
continually recreates this log file with ``0644`` permissions, and there is no configuration
option for how apt sets permissions on this file. Though this specific file should not be a
security concern - the equivalent STIG benchmark includes an explicit exclusion for it.

CIS 5.4.1.5 / 5.4.1.1 - Ensure inactive password lock is configured (and related password-age checks)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Amazon Inspector evaluates this control against every account on the system, including
service and system accounts. The CIS benchmark is intended to apply only to accounts with
passwords and interactive logins.

If passwords are enabled, follow the instructions in the
`Additional Password-Policy Controls`_ section above.

CIS 5.1.1 - Ensure permissions on /etc/ssh/sshd_config are configured
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The USG remediation sets permissions on ``/etc/ssh/sshd_config`` itself but leaves files
inside ``/etc/ssh/sshd_config.d/`` unchanged. Files added by cloud-init or other tooling
after remediation may not have ``0600`` permissions. Check and correct manually if needed::

   sudo chmod 0600 /etc/ssh/sshd_config.d/*

CIS 2.4.1.8 - Ensure ``crontab`` is restricted to authorized users
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The CIS benchmark permits cron access to be restricted via ``/etc/cron.allow``,
``/etc/cron.deny``, or directory permissions. Amazon Inspector checks only for the
existence of ``/etc/cron.allow`` and does not ``recognise`` the other permitted
access-control mechanisms.

CIS 1.5.5 - Ensure Automatic Error Reporting is not enabled
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
The ``apport`` service is masked (``symlinked`` to ``/dev/null``) in the base image. USG
considers masking sufficient to meet this control, but Amazon Inspector checks the
``/etc/default/apport`` config file directly and flags ``enabled=1`` regardless of the
actual service state. To silence the finding, explicitly set ``enabled=0``::

   sudo sed -i 's/^enabled=.*/enabled=0/' /etc/default/apport

