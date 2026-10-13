.. meta::
   :description: Learn how to generate an SPDX Software Bill of Materials (SBOM) from an Ubuntu AMI on AWS using Syft on a running instance, Syft on the AMI snapshot, or Amazon Inspector.


.. _generate-spdx-sbom:

Generate an SPDX SBOM from an Ubuntu AMI
========================================

A Software Bill of Materials (SBOM) is an inventory of the software components
that make up an image. This guide shows three ways to produce an `SPDX`_ SBOM
for an Ubuntu Amazon Machine Image (AMI):

.. list-table::
   :header-rows: 1
   :widths: 25 35 15 25

   * - Method
     - What it scans
     - Boots the AMI?
     - Output
   * - `Method 1`_: Syft on a running instance
     - Live filesystem of an instance launched from the AMI
     - Yes
     - SPDX 2.3 JSON or tag-value
   * - `Method 2`_: Syft on a volume restored from the AMI snapshot
     - The root disk of the AMI, exactly as shipped
     - No
     - SPDX 2.3 JSON or tag-value
   * - `Method 3`_: Amazon Inspector SBOM export
     - OS packages (and some Python packages) on an instance launched from the
       AMI
     - Yes
     - SPDX 2.3 JSON (exported to S3)

As a rule of thumb, use Method 1 for a quick one-off and Method 2 when you need
an accurate, repeatable SBOM of the image as published (for example, in an AMI
build pipeline). Use Method 3 if Amazon Inspector is already enabled in your
account and you mainly need OS packages plus CVE references. It needs no tooling
on the instance, but its coverage is narrower than that of Syft.

Prerequisites
-------------

* AWS CLI v2 configured with permissions for EC2 (``RunInstances``,
  ``CreateVolume``, ``AttachVolume`` and so on). Refer to
  :ref:`ec2-credentials` for an introduction to AWS
  credentials.
* An SSH key pair and a security group that allows SSH from your IP address, or
  SSM Session Manager access.
* `Syft`_ installed on the machine that runs the scan:

  .. code-block:: bash

     curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b <install-dir>

* ``jq``, for inspecting the result (optional).

The examples below use Ubuntu 24.04 LTS. To find the AMI ID of the latest
image for any Ubuntu release, refer to
:ref:`Find Ubuntu images on AWS <find-ubuntu-images>`.


.. _Method 1:

Method 1: run Syft on an instance launched from the AMI
-------------------------------------------------------

Launch an instance and log in
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get the latest AMI ID for Ubuntu 24.04 LTS from the SSM Parameter Store:

.. code-block:: bash

   aws ssm get-parameters --names /aws/service/canonical/ubuntu/server/noble/stable/current/amd64/hvm/ebs-gp3/ami-id

Launch the instance. This example uses the AWS CLI, but you can also use the
EC2 console or any other tool. Use a security group that allows you to connect
through SSH, or an instance role that lets you connect through an SSM terminal
session. For a more detailed walk-through, refer to
:ref:`Launch an Ubuntu EC2 instance using the AWS CLI <launch-ubuntu-ec2-instance>`.

.. code-block:: bash

   AMI=<ami-id>
   aws ec2 run-instances --image-id $AMI --instance-type t3.small \
     --key-name <key> --security-group-ids <sg> --associate-public-ip-address \
     --tag-specifications 'ResourceType=instance,Tags=[{Key=Purpose,Value=sbom}]' \
     --query 'Instances[0].InstanceId' --output text

Connect to the instance through SSH once it is running.

Install Syft outside the tree to be scanned
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you install Syft into ``/usr/local/bin``, it shows up in the SBOM: in
testing, it added 275 Go modules that are not part of the AMI. Install it under
``/tmp`` instead, which can be excluded from the scan:

.. code-block:: bash

   curl -sSfL https://raw.githubusercontent.com/anchore/syft/main/install.sh | sh -s -- -b /tmp/syft-bin

Scan the root filesystem
~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   sudo /tmp/syft-bin/syft scan dir:/ \
     --exclude './proc/**' --exclude './sys/**' --exclude './dev/**' \
     --exclude './run/**' --exclude './tmp/**' \
     --select-catalogers '-linux-kernel-cataloger' \
     --source-name "$AMI" --source-version ubuntu-24.04 \
     -o spdx-json=ami-sbom.spdx.json

Notes on the flags:

* **Exclusion patterns must be relative** (``./proc/**``). Absolute patterns
  such as ``/proc/**`` make Syft fail with
  ``invalid exclusion pattern(s) ... (must start with one of: './', '*/', or '**/')``.
  With ``-q``, the failure is silent: no output file and no error message is
  generated.
* ``--select-catalogers '-linux-kernel-cataloger'`` stops Syft from listing
  every kernel module (``.ko``) as a separate ``pkg:generic`` package. Without
  it, the SBOM contained 6,047 kernel-module entries out of 8,053 packages. The
  kernel itself is still reported through its ``linux-image-*`` deb.
* ``--source-name`` and ``--source-version`` set the document name of the SBOM.
  Without them, Syft gives a warning and derives a name from the path ``/``.
* Use ``-o spdx-tag-value=ami-sbom.spdx`` for tag-value output. Several ``-o``
  flags can be combined.

Copy the SBOM and terminate the instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   scp ubuntu@<ip>:ami-sbom.spdx.json .
   aws ec2 terminate-instances --instance-ids <instance-id>

Results
~~~~~~~

Measured on Ubuntu 24.04 LTS:

.. list-table::
   :header-rows: 1
   :widths: 30 70

   * - Metric
     - Value
   * - Scan time (t3.small)
     - About 2 min 20 s
   * - SBOM size
     - 48 MB (SPDX JSON includes per-file entries)
   * - Packages
     - 1,730: 931 deb, 679 Go, 111 PyPI, 5 generic, 3 Maven

.. note::

   **Scanning a running instance is not the same as scanning the AMI.**
   Software can change after boot, and that change ends up in the SBOM. In
   testing, the live instance contained software that is not in the AMI:

   * ``snapd`` auto-refreshed ``amazon-ssm-agent`` from revision 13349 to
     13736, so both revisions were reported.
   * Amazon Inspector (enabled in the account) pushed ``inspectorssmplugin``
     to ``/opt/aws/inspector`` through SSM.
   * cloud-init, user data and unattended-upgrades can also install or upgrade
     packages.

   If the SBOM must describe the image itself, use `Method 2`_.


.. _Method 2:

Method 2: scan the AMI snapshot without booting it
--------------------------------------------------

Each EBS-backed AMI is made of EBS snapshots. Restore the root snapshot to a
volume, attach it to a helper instance, mount it read-only and scan the mount
point. Nothing in the image runs, and the result is reproducible.

Find the root snapshot of the AMI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get the latest AMI ID for Ubuntu 24.04 LTS from the SSM Parameter Store:

.. code-block:: bash

   aws ssm get-parameters --names /aws/service/canonical/ubuntu/server/noble/stable/current/amd64/hvm/ebs-gp3/ami-id

Use it to find the root snapshot:

.. code-block:: bash

   AMI=<ami-id>
   ROOT_DEV=$(aws ec2 describe-images --image-ids $AMI --query 'Images[0].RootDeviceName' --output text)
   SNAP=$(aws ec2 describe-images --image-ids $AMI \
     --query "Images[0].BlockDeviceMappings[?DeviceName=='$ROOT_DEV'].Ebs.SnapshotId" --output text)
   echo $SNAP

Create a volume in the Availability Zone of the helper and attach it
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The helper can be any Linux instance, including an existing one. It must be in
the same Availability Zone as the new volume.

.. code-block:: bash

   HELPER=<helper-instance-id>
   AZ=$(aws ec2 describe-instances --instance-ids $HELPER \
     --query 'Reservations[0].Instances[0].Placement.AvailabilityZone' --output text)

   VOL=$(aws ec2 create-volume --snapshot-id $SNAP --availability-zone $AZ --volume-type gp3 \
     --tag-specifications 'ResourceType=volume,Tags=[{Key=Purpose,Value=sbom}]' \
     --query VolumeId --output text)
   aws ec2 wait volume-available --volume-ids $VOL
   aws ec2 attach-volume --volume-id $VOL --instance-id $HELPER --device /dev/sdf
   aws ec2 wait volume-in-use --volume-ids $VOL

Identify the device and mount it read-only
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On Nitro instances, ``/dev/sdf`` appears as an NVMe device. Match it by serial
number, which is the volume ID without the dash:

.. code-block:: bash

   lsblk -o NAME,SIZE,FSTYPE,LABEL,SERIAL,MOUNTPOINT | grep -v loop

.. code-block:: text

   nvme1n1          8G                          vol0cffc917af5a486af
   |-nvme1n1p1      7G ext4     cloudimg-rootfs
   |-nvme1n1p15   106M vfat     UEFI
   `-nvme1n1p16   913M ext4     BOOT

Mount the root partition. The mount options make sure that nothing is written
to the disk, not even a journal replay:

.. code-block:: bash

   sudo mkdir -p /mnt/ami

   # ext4 (Ubuntu, Debian, ...)
   sudo mount -o ro,noload /dev/nvme1n1p1 /mnt/ami

   # XFS (Amazon Linux 2023, RHEL, ...)
   sudo mount -t xfs -o ro,norecovery,nouuid /dev/nvme1n1p1 /mnt/ami

* **Always mount by device path, never by label or UUID.** If the helper runs
  the same distribution, both disks have the same label (both were
  ``cloudimg-rootfs`` in testing).
* ``nouuid`` is needed for XFS when the root filesystem of the helper has the
  same UUID, which happens when the helper was launched from the same AMI. It
  does no harm otherwise.
* ``noload`` and ``norecovery`` skip the journal replay, so a read-only mount
  really is read-only.

Mount the snaps that the image ships (Ubuntu only)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

On a running Ubuntu system, snaps are SquashFS images mounted under
``/snap/<name>/<revision>``. On an offline disk they are just files in
``/var/lib/snapd/snaps/``, so Syft cannot see what is inside them. In testing,
skipping this step missed 277 deb packages (264 from ``core22`` and 13 from
``snapd``) and the Go modules in the snaps.

The mount points already exist in the image, so mount each snap at its native
path:

.. code-block:: bash

   for s in /mnt/ami/var/lib/snapd/snaps/*.snap; do
     b=$(basename "$s" .snap); name=${b%_*}; rev=${b##*_}
     sudo mount -t squashfs -o ro,loop "$s" "/mnt/ami/snap/$name/$rev"
   done
   findmnt -R /mnt/ami

Scan the mounted volume
~~~~~~~~~~~~~~~~~~~~~~~

No ``--exclude`` flags are needed, because ``/proc``, ``/sys`` and similar
directories are empty on an offline disk.

.. code-block:: bash

   sudo syft scan dir:/mnt/ami \
     --select-catalogers '-linux-kernel-cataloger' \
     --source-name "$AMI" --source-version ubuntu-24.04 \
     -o spdx-json=ami-sbom.spdx.json

Clean up
~~~~~~~~

.. code-block:: bash

   sudo umount -R /mnt/ami
   aws ec2 detach-volume --volume-id $VOL
   aws ec2 wait volume-available --volume-ids $VOL
   aws ec2 delete-volume --volume-id $VOL

Results
~~~~~~~

Measured on Ubuntu 24.04 LTS:

.. list-table::
   :header-rows: 1
   :widths: 24 38 38

   * - Metric
     - With snaps mounted
     - Without snaps mounted
   * - Scan time (t3.small)
     - About 2 min 10 s
     - About 2 min 15 s
   * - SBOM size
     - 48 MB
     - 46 MB
   * - Packages
     - 1,493: 928 deb, 445 Go, 111 PyPI, 5 generic, 3 Maven
     - 967: 651 deb, 235 Go, 77 PyPI, 3 Maven

Compared with Method 1 on the same AMI, the snapshot scan reported 3 fewer debs
and 234 fewer Go modules. All of the differences came from software added at
runtime: the refreshed SSM agent snap and the Inspector SSM plugin (see the
note at the end of Method 1).

.. note::

   Volumes restored from snapshots load blocks lazily from S3, so the first
   full read is slower than on a warm disk. For large AMIs or frequent pipeline
   runs, consider `EBS fast snapshot restore`_. It is billed per hour and per
   Availability Zone.


.. _Method 3:

Method 3: export an SBOM from Amazon Inspector for a running instance
---------------------------------------------------------------------

Amazon Inspector can export SBOMs in SPDX 2.3 (or CycloneDX 1.4) format for the
resources it scans. It does not scan AMIs directly: you launch an instance from
the AMI, Inspector scans it, and you export the result. Everything happens
through the AWS API, so you do not need SSH, open ports or a scanner on the
instance.

Requirements
~~~~~~~~~~~~

* **Inspector EC2 scanning is enabled**
  (``aws inspector2 enable --resource-types EC2``). Check with:

  .. code-block:: bash

     aws inspector2 batch-get-account-status --query 'accounts[0].resourceState.ec2.status'
     aws inspector2 get-configuration --query 'ec2Configuration.scanModeState'

* **The instance is SSM-managed** (for the default ``EC2_SSM_AGENT_BASED`` scan
  mode). This requires either an instance profile with
  ``AmazonSSMManagedInstanceCore``, or `Default Host Management Configuration`_
  enabled in the account and region. The instance also needs outbound access
  to the SSM endpoints. Ubuntu AMIs ship the SSM agent as a snap.

Launch and tag an instance from the AMI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Get the latest AMI ID for Ubuntu 24.04 LTS from the SSM Parameter Store:

.. code-block:: bash

   aws ssm get-parameters --names /aws/service/canonical/ubuntu/server/noble/stable/current/amd64/hvm/ebs-gp3/ami-id

Use it to launch and tag an instance. No key pair or inbound rules are needed:

.. code-block:: bash

   AMI=<ami-id>
   IID=$(aws ec2 run-instances --image-id $AMI --instance-type t3.small --associate-public-ip-address \
     --metadata-options HttpTokens=required \
     --tag-specifications 'ResourceType=instance,Tags=[{Key=Purpose,Value=sbom}]' \
     --query 'Instances[0].InstanceId' --output text)

Wait until Inspector has scanned the instance
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   aws inspector2 list-coverage \
     --filter-criteria "{\"resourceId\":[{\"comparison\":\"EQUALS\",\"value\":\"$IID\"}]}" \
     --query 'coveredResources[0].[scanStatus.statusCode,scanStatus.reason,lastScannedAt]' --output text

In testing, the status changed as follows, and the whole scan took about two
minutes after launch:

.. list-table::
   :header-rows: 1
   :widths: 18 32 50

   * - Time after launch
     - Status
     - Meaning
   * - About 30 s
     - ``INACTIVE  NO_INVENTORY``
     - SSM has not delivered the software inventory yet. This is normal, not a
       failure.
   * - About 1 min
     - ``ACTIVE  DEEP_INSPECTION_NO_INVENTORY``
     - OS packages scanned; language packages (deep inspection) still pending.
   * - About 2 min
     - ``ACTIVE  SUCCESSFUL``
     - Scan complete; ready to export.

Wait for ``SUCCESSFUL``. If you export at ``DEEP_INSPECTION_NO_INVENTORY``,
the SBOM will be missing language packages.

Create an S3 bucket and a KMS key for the export
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

This is a one-time setup. The export must go to S3, encrypted with a
customer-managed KMS key. Both the key policy and the bucket policy must allow
the ``inspector2.amazonaws.com`` service principal. Scope them to the Inspector
reports of your account:

.. code-block:: bash

   ACCT=$(aws sts get-caller-identity --query Account --output text); REGION=us-east-1
   BUCKET=sbom-exports-$ACCT
   COND="{\"StringEquals\":{\"aws:SourceAccount\":\"$ACCT\"},\"ArnLike\":{\"aws:SourceArn\":\"arn:aws:inspector2:$REGION:$ACCT:report/*\"}}"

   cat > kms-policy.json <<EOF
   {"Version":"2012-10-17","Statement":[
    {"Sid":"root","Effect":"Allow","Principal":{"AWS":"arn:aws:iam::$ACCT:root"},"Action":"kms:*","Resource":"*"},
    {"Sid":"inspector","Effect":"Allow","Principal":{"Service":"inspector2.amazonaws.com"},
     "Action":["kms:Decrypt","kms:GenerateDataKey*"],"Resource":"*","Condition":$COND}]}
   EOF
   cat > bucket-policy.json <<EOF
   {"Version":"2012-10-17","Statement":[
    {"Sid":"inspector","Effect":"Allow","Principal":{"Service":"inspector2.amazonaws.com"},
     "Action":["s3:PutObject","s3:PutObjectAcl","s3:AbortMultipartUpload"],
     "Resource":"arn:aws:s3:::$BUCKET/*","Condition":$COND}]}
   EOF

   KEY=$(aws kms create-key --description "Inspector SBOM exports" --policy file://kms-policy.json \
     --query KeyMetadata.Arn --output text)
   aws s3api create-bucket --bucket $BUCKET
   aws s3api put-bucket-policy --bucket $BUCKET --policy file://bucket-policy.json

Outside ``us-east-1``, add
``--create-bucket-configuration LocationConstraint=$REGION`` to the
``create-bucket`` command. Reuse the bucket and the key for every later export.

Request the export and wait for it
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code-block:: bash

   REPORT=$(aws inspector2 create-sbom-export --report-format SPDX_2_3 \
     --resource-filter-criteria '{"ec2InstanceTags":[{"comparison":"EQUALS","key":"Purpose","value":"sbom"}]}' \
     --s3-destination bucketName=$BUCKET,keyPrefix=sbom/,kmsKeyArn=$KEY \
     --query reportId --output text)

   aws inspector2 get-sbom-export --report-id $REPORT --query status --output text

The status changes from ``IN_PROGRESS`` to ``SUCCEEDED``. The export took about
two minutes in testing.

.. warning::

   Make the filter specific. Without one, the export covers every resource that
   Inspector scans in the account. You can also filter on ``resourceId``
   instead of tags.

Download the SBOM
~~~~~~~~~~~~~~~~~

Inspector writes one SPDX file per resource:

.. code-block:: bash

   aws s3 cp --recursive s3://$BUCKET/sbom/ ./inspector-sbom/

The files are stored under
``sbom/SPDX_2_3_outputs_<report-id>/account=<account>/resource=AWS_EC2_INSTANCE/<instance-id>_SPDX_2_3.json``.
The SPDX document is named ``<account>/EC2/<instance-id>/<ami-id>``, so the AMI
ID is recorded.

Clean up
~~~~~~~~

Terminate the instance:

.. code-block:: bash

   aws ec2 terminate-instances --instance-ids $IID

Only if you will not reuse the bucket and the key, remove them as well:

.. code-block:: bash

   aws s3 rm --recursive s3://$BUCKET/ && aws s3api delete-bucket --bucket $BUCKET
   aws kms schedule-key-deletion --key-id $KEY --pending-window-in-days 7

Seven days is the minimum waiting period for KMS key deletion.

Results
~~~~~~~

Measured on Ubuntu 24.04 LTS, compared with Syft (Method 1) on the same AMI:

.. list-table::
   :header-rows: 1
   :widths: 24 34 42

   * - Metric
     - Inspector
     - Syft, Method 1 (live instance)
   * - Time
     - About 2 min scan + about 2 min export
     - About 2 min 20 s scan
   * - SBOM size
     - 572 KB
     - 48 MB
   * - Packages
     - 664: 652 dpkg, 11 PyPI
     - 1,730: 931 deb, 679 Go, 111 PyPI, 5 generic, 3 Maven
   * - Host OS (dpkg) packages
     - 652
     - 652 (same package names; versions matched after normalising)
   * - Packages inside snaps
     - Not reported
     - Reported (for example, 264 debs from ``core22``)
   * - Go modules
     - None
     - 679
   * - Python packages
     - 11 (system packages only)
     - 84 unique
   * - Licenses (``licenseDeclared``)
     - None
     - From dpkg copyright files
   * - Per-file entries
     - No
     - Yes
   * - CVE references
     - 1,780 ``SECURITY/vulnerability`` references
     - None (pair with `Grype`_ for this)

Notes on the Inspector export:

* **It describes the running instance, not the AMI.** Like Method 1, the
  result includes changes made after boot. The export included
  ``inspectorssmplugin``, which Inspector itself installs through SSM.
* **Non-standard purl type.** Packages use ``pkg:dpkg/...`` instead of the
  standard `purl`_ type ``pkg:deb/...``. Tools that match on purl
  (vulnerability scanners, Dependency-Track and others) may not recognise them.
* **Version strings differ from dpkg.** Epochs are dropped
  (``1:2.0.34-1ubuntu2`` becomes ``2.0.34-1ubuntu2``), and packages with no
  Debian revision get a literal ``-null`` suffix (``apt@2.8.3-null``; 73
  packages in testing). Normalise versions before comparing with other SBOMs.
* **Coverage is narrow.** There are no snap contents, Go binaries or licenses,
  and only system Python packages. This suits vulnerability management but
  makes for a thin SBOM for licence or supply-chain compliance.
* **The KMS key cannot be deleted immediately.** Deletion has a seven-day
  minimum waiting period.
* **The** ``inspector-sbomgen`` **CLI is not an SPDX option.** It can scan
  directories and volumes without a running instance, but it outputs CycloneDX
  only.


Verify an SBOM
--------------

Quick checks with ``jq``:

.. code-block:: bash

   # SPDX version, document name, and package count
   jq -r '.spdxVersion, .name, (.packages|length)' ami-sbom.spdx.json

   # Package count per ecosystem (purl type)
   jq -r '[.packages[].externalRefs[]? | select(.referenceType=="purl")
           | .referenceLocator | split("/")[0]] | group_by(.) | map("\(.[0]) \(length)") | .[]' ami-sbom.spdx.json

   # Look up specific packages
   jq -r '.packages[] | select(.name=="openssl") | "\(.name) \(.versionInfo) \(.licenseDeclared)"' ami-sbom.spdx.json

For a schema-level check, use the `SPDX tools-python`_ project:

.. code-block:: bash

   pyspdxtools -i ami-sbom.spdx.json


.. LINKS
.. _SPDX: https://spdx.dev/
.. _Syft: https://github.com/anchore/syft
.. _Grype: https://github.com/anchore/grype
.. _purl: https://github.com/package-url/purl-spec
.. _SPDX tools-python: https://github.com/spdx/tools-python
.. _EBS fast snapshot restore: https://docs.aws.amazon.com/ebs/latest/userguide/ebs-fast-snapshot-restore.html
.. _Default Host Management Configuration: https://docs.aws.amazon.com/systems-manager/latest/userguide/fleet-manager-default-host-management-configuration.html
