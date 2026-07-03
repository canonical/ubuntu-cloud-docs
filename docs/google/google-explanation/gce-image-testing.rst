.. meta::
   :description: Understand how Canonical tests Ubuntu GCE images before release, using its own internal test suite and Google's upstream cloud-image-tests.

Image testing
=============

Every Ubuntu image that Canonical publishes to Google Compute Engine (GCE) is built daily and tested automatically before it can be offered to users. Testing is **gated**: a freshly built image is only promoted to a release image once it has passed the full set of automated tests. This page explains what that testing covers and how it fits into the image life-cycle.

We run two sets of automated tests on each daily GCE image:

* **Canonical's own internal test suite**, which verifies that the image behaves the way an Ubuntu image is expected to behave on GCE.
* The **Cloud Image Tests (CIT)**, Google's own upstream test suite, which validate the image against Google's expectations for a guest operating system on GCE.


Testing in the image life-cycle
-------------------------------

Ubuntu images on GCE move through a life-cycle of *daily* builds that may be promoted to *release* images. (For background on these image types, see :doc:`image release types <all-clouds:all-clouds-explanation/release-types>` and the :doc:`GCE image retention policy <gce-image-retention-policy>`.)

New images are built daily from the latest packages. Each daily build is uploaded and then exercised by the two sets of tests described below.


The two sets of tests
---------------------

Canonical's internal test suite
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Canonical's internal test suite launches real instances on GCE and runs a battery of checks that confirm the image is correctly built and well-behaved. At a high level, this covers:

* **Boot and basic health**: the image boots reliably, reaches a healthy running state, and (where applicable) boots within expected time bounds.
* **First-boot configuration**: `cloud-init` runs correctly, including the expected behavior around SSH and password authentication.
* **GCE guest integration**: the Google guest environment works as expected, including metadata-driven behavior, start-up and shutdown scripts (including those sourced from a URL), and automatic root disk resizing.
* **Confidential computing and secure boot**: features such as AMD SEV, SEV-SNP, Intel TDX and UEFI Secure Boot are validated on the images that support them, including live migration of confidential VMs where supported.
* **Ubuntu Pro and FIPS**: on Pro and Pro FIPS images, the Pro entitlements and FIPS-certified components are present and enabled as expected.
* **Package and configuration correctness**: checks such as copyright compliance and APT pin priorities, which guard against subtle packaging or configuration regressions.
* **Workload building blocks**: capabilities that customers commonly rely on, such as launching system containers with LXD and, on accelerator images, GPU readiness.

The exact set of tests run against any given image depends on its family and the features it is expected to support.

How an internal test runs
^^^^^^^^^^^^^^^^^^^^^^^^^^

Each image is validated on a live instance rather than by static inspection. For every test, the suite:

#. **Selects an instance (machine) type and disk type** (one cell of the test matrix described below) suited to the architecture and to the feature being tested. For example, a confidential-computing test runs on a machine type that supports confidential VMs.
#. **Launches a fresh instance** from the exact daily image under test.
#. **Connects over SSH**, retrying until the instance is reachable and can run commands.
#. **Waits for the instance to settle** before testing anything. It first waits for first-boot configuration (`cloud-init`) to finish, and then waits for `systemd` to settle, that is, until the system reports it has finished booting and no units are still in the process of starting. This avoids races where a test would otherwise run against a system that is still coming up.
#. **Runs the test suite** against the running instance and records the outcome of each test case in a standard, machine-readable JUnit XML report.
#. **Collects diagnostics and cleans up.** Regardless of the outcome, the harness gathers logs and boot-timing data from the instance (boot timings feed our boot-speed tracking) before tearing the instance down.

Testing across a matrix of hardware
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

A given image is not tested just once. The internal test stage is organized as a **matrix**, whose main axes are:

* the **test suite** (the baseline Ubuntu suite, `cloud-init`, the confidential-computing suites, and so on);
* the **architecture** (``amd64`` and ``arm64``);
* the **machine type**, and with it the underlying CPU platform; and
* the **boot disk type**.

Running every suite on every machine type and every disk type would be prohibitively slow and costly, so only a deliberate, representative subset of the full set of combinations is selected for testing. This subset is chosen to span a spread of CPU families from **AMD, Intel and Arm** and the range of Compute Engine storage options, so that regressions which only appear on a particular processor generation or storage type are still caught before an image is released. Suites that exercise a specific hardware capability are run on the machine types that provide it: confidential-computing suites on confidential-VM-capable machines, GPU suites on GPU-enabled machines, and so on.

Cloud Image Tests (CIT)
~~~~~~~~~~~~~~~~~~~~~~~~

We also run Google's own `cloud-image-tests`_ (CIT), the same upstream test suite Google uses to validate guest images for Compute Engine. Running CIT gives independent assurance that Ubuntu images meet Google's expectations for a Compute Engine guest. The suites cover areas including:

* the Google guest agent, plugin and metadata server (including OS Login, SSH and metadata server security);
* networking and load balancing;
* disks, including local SSD and hot-attach;
* package management, upgrades and validation;
* image boot, hostname validation, license validation and VM specification;
* confidential VMs, live migration and suspend/resume.

Rather than simply following the upstream development branch, Canonical runs CIT from a known-good upstream revision, which is updated roughly monthly, so that changes to the upstream tests are taken up deliberately.

A number of upstream suites are still maturing and are tracked but not yet used to gate releases: for example, some performance, advanced networking and accelerator-specific suites. These are evaluated as they stabilize and added to the gating set once they are reliable enough to block a release on.


Image families and architectures
--------------------------------

The image families published for GCE (including Base, Minimal, Accelerator, TPU, Ubuntu Pro, Ubuntu Pro FIPS and Ubuntu Core) are each tested with the checks relevant to them. Tests run across the supported architectures (`amd64` and `arm64`), so both architectures of an image are validated before release.

Coverage is tailored per family: for example, Pro images additionally validate Pro entitlements, accelerator images additionally validate GPU readiness, and Ubuntu Core images follow a dedicated test path suited to their image format. For more on the available families, see :doc:`Canonical's offerings on GCP <canonical-offerings>`.


Test outcomes
-------------

Test outcomes determine whether a daily image can be promoted: if all tests pass, the build becomes eligible for promotion to a release image; if any test fails, the build is not promoted.

The result of this process is that the Ubuntu images you launch from GCE have each passed both Canonical's own internal test suite and Google's upstream Cloud Image Tests for their family and architecture. For more on the security features validated along the way, see the :doc:`security overview <security-overview>`.


.. _`cloud-image-tests`: https://github.com/GoogleCloudPlatform/cloud-image-tests
