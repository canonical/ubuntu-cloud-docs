.. meta::
   :description: Understand how Canonical tests Ubuntu AWS images before release, using its own internal test suite covering EC2, hibernation and EKS worker images.

.. _aws-image-testing:

Image testing
=============

Every Ubuntu image that Canonical publishes to Amazon Web Services (AWS) is built daily and tested automatically before it can be offered to users. Testing is **gated**: a freshly built image is only promoted to a release image once it has passed the full set of automated tests. This page explains what that testing covers and how it fits into the image life-cycle.

We run **Canonical's own internal test suite** on each daily EC2 image. This suite verifies that the image behaves the way an Ubuntu image is expected to behave on AWS.


Testing in the image life-cycle
-------------------------------

Ubuntu images on AWS move through a life-cycle of *daily* builds that may be promoted to *release* images. (For background on these image types, see :ref:`image release types <all-clouds:release-types>` and the :ref:`EC2 image retention policy <ec2-image-retention-policy>`.)

New images are built daily from the latest packages. Each daily build is uploaded and then exercised by the tests described below.


Canonical's internal test suite
--------------------------------

Canonical's internal test suite launches real instances on EC2 and runs a battery of checks that confirm the image is correctly built and well-behaved. At a high level, this covers:

* **Boot and basic health**: the image boots reliably and reaches a healthy running state.
* **First-boot configuration**: `cloud-init` runs correctly, including the expected behavior around SSH and password authentication.
* **AWS guest integration**: ec2-instance-connect allows connection to a running instance and Amazon SSM agent is present, enabled and running.
* **Hibernation and resume**: on instances that support it, an image can hibernate and later resume correctly, with in-memory workloads and on-disk state preserved across the cycle, and system uptime reflecting the time already spent running before hibernation.
* **Ubuntu Pro and FIPS**: on Pro and Pro FIPS images, the Pro entitlements and FIPS-certified components are present and enabled as expected.
* **Package and configuration correctness**: checks such as copyright compliance and APT pin priorities, which guard against subtle packaging or configuration regressions.
* **secureboot**: ensure that an image registered with secureboot enabled launches and validates attestations. Note that we do not ship images with secureboot enabled by default.
* **EKS worker image readiness**: for images intended as EKS worker nodes, a full EKS cluster is created with node groups built from the image under test, and a Kubernetes conformance test suite is run against the cluster to confirm the image works correctly as a worker node.

The exact set of tests run against any given image depends on its family and the features it is expected to support.

How an internal test runs
~~~~~~~~~~~~~~~~~~~~~~~~~~

Each image is validated on a live instance rather than by static inspection. For every test, the suite:

#. **Selects an instance type** (one cell of the test matrix described below) suited to the architecture and to the feature being tested.
#. **Launches a fresh instance** from the exact daily image under test.
#. **Connects over SSH**, retrying until the instance is reachable and can run commands.
#. **Waits for the instance to settle** before testing anything. It first waits for first-boot configuration (`cloud-init`) to finish, and then waits for `systemd` to settle, that is, until the system reports it has finished booting and no units are still in the process of starting. This avoids races where a test would otherwise run against a system that is still coming up.
#. **Runs the test suite** against the running instance and records the outcome of each test case in a standard, machine-readable JUnit XML report.
#. **Collects diagnostics and cleans up.** Regardless of the outcome, the harness gathers logs and boot-timing data from the instance (boot timings feed our boot-speed tracking) before tearing the instance down.

Testing across a matrix of hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A given image is not tested just once. The internal test stage is organized as a **matrix**, whose main axes are:

* the **test suite** (the baseline Ubuntu suite, `cloud-init`, hibernation, and so on);
* the **architecture** (``amd64`` and ``arm64``); and
* the **instance type**, and with it the underlying CPU platform

Running every suite on every instance type would be prohibitively slow and costly, so only a deliberate, representative subset of the full set of combinations is selected for testing. This subset is chosen to span a spread of instance families and storage options, so that regressions which only appear on a particular processor generation or storage type are still caught before an image is released. Suites that exercise a specific hardware capability are run on the instance types that provide it: the hibernation suite on instance types that support hibernation, and so on.


Image families and architectures
--------------------------------

The image families published for AWS (including standard, minimal, Ubuntu Pro and EKS worker images) are each tested with the checks relevant to them. Tests run across the supported architectures (`amd64` and `arm64`), so both architectures of an image are validated before release.

Coverage is tailored per family: for example, EKS worker images additionally run a full Kubernetes conformance suite against a live cluster. For more on the available families, see :ref:`Canonical's offerings on AWS <canonical-offerings>`.


Test outcomes
-------------

Test outcomes determine whether a daily image can be promoted: if all tests pass, the build becomes eligible for promotion to a release image; if any test fails, the build is not promoted.

The result of this process is that the Ubuntu images you launch from AWS have each passed Canonical's own internal test suite for their family and architecture. For more on the security features validated along the way, see the :ref:`security overview <ubuntu-security-on-aws>`.
