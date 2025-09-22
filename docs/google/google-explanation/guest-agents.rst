Google agents installed on Ubuntu
=================================

There are four different "guest agents" installed on Ubuntu images in GCP, each developed by Google and packaged for Ubuntu by Canonical:

* ``google-guest-agent`` [`package <https://launchpad.net/ubuntu/+source/google-guest-agent>`__, `source code <https://github.com/GoogleCloudPlatform/guest-agent>`__]
* ``gce-compute-image-packages`` [`package <https://launchpad.net/ubuntu/+source/gce-compute-image-packages>`__, `source code <https://github.com/GoogleCloudPlatform/guest-configs>`__]
* ``google-compute-engine-oslogin`` [`package <https://launchpad.net/ubuntu/+source/google-compute-engine-oslogin>`__, `source code <https://github.com/GoogleCloudPlatform/guest-oslogin>`__]
* ``google-osconfig-agent`` [`package <https://launchpad.net/ubuntu/+source/google-osconfig-agent>`__, `source code <https://github.com/GoogleCloudPlatform/osconfig>`__]

``google-guest-agent``
----------------------
This package is installed on Ubuntu images to facilitate the different platform features available in GCP.
It's written in ``Go`` and can be described as having two main components:

#. The ``google-metadata-script-runner`` binary, which enables users to run bespoke scripts on VM startup and VM shutdown
#. The ``daemon``, which handles the following on the VM:

* SSH and account management
* OS Login (if used)
* Clock skew
* Networking and NICs
* Instance optimizations
* Telemetry
* Mutual TLS Metadata Service (mTLS MDS)

``gce-compute-image-packages``
------------------------------
This package (written in ``BASH``) is a collection of different configuration scripts that are dropped into the ``.d`` directories of the following:

* ``apt``
* ``dhcp``
* ``modprobe``
* ``NetworkManager/dispatcher``
* ``rsyslog``
* ``sysctl``
* ``systemd``

``google-compute-engine-oslogin``
---------------------------------
Written in a mixture of ``C`` and ``C++``, this package is responsible for providing GCP's `OS Login <https://cloud.google.com/compute/docs/oslogin>`_ to Ubuntu VMs.
At a high level it can be described as providing the following:

* **Authorized Keys Command**: provides SSH keys (from an OS Login profile) to ``sshd`` for authentication
* **NSS Modules**: support for making OS Login user/group information available to the VM using NSS (Name Service Switch)
* **PAM Modules**: provides authorization (and authentication if ``2FA`` is enabled) to allow the VM to grant ``ssh`` access/``sudo`` privileges based on the user's allotted `IAM permissions <https://cloud.google.com/iam/docs>`_

``google-osconfig-agent``
-------------------------
This package is written in ``Go`` and is installed to facilitate GCP's `OS Config <https://cloud.google.com/compute/docs/osconfig/rest>`_ (also known as "`VM manager <https://cloud.google.com/compute/vm-manager/docs>`_").
At a high level, OS Config supports the following:

* `OS inventory management <https://cloud.google.com/compute/vm-manager/docs/os-inventory/os-inventory-management>`_
* `Patch <https://cloud.google.com/compute/vm-manager/docs/patch>`_
* `OS policies <https://cloud.google.com/compute/vm-manager/docs/os-policies>`_
