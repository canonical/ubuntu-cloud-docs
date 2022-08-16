# Ubuntu Cloud Images

Canonical produces new Ubuntu produces new images regularly for various clouds. The Public Cloud team produces, registers, and publishes these images to the Amazon AWS EC2, Amazon AWS EKS, Google GCE, and Microsoft Azure. Other clouds and products, CPC works directly with partners to create a regular release process. These partners include: IBM VPC, IBM Classic, Oracle Cloud Infrastructure (OCI), Google GKE products, and others. CPC also owns the publication of "Premium" images to cloud marketplaces. This includes products such as Ubuntu Pro, Ubuntu Pro Fips, Anbox Cloud, and more. This document will help users understand the different places you can find official Canonical supported Ubuntu images, some of the basic terminology used throughout our docs, and the high level release plan.

## Terminology

* Image: A machine image. These can come in many formats: vmdk, qcow, and more. These may be booted as VMs or Baremetal (when supported by our partners)
* Serial: A unique ID for an image in YYYYMMDD.INCREMENT format. Y=Year, M=Month, D=Day. example: 202010720. This corresponds to the date of the archive for the image build, not necessarily the date an image was registered or published. Example: An image is publised to Microsoft Azure as 20220815. However, the ingestion pipeline takes 24 hours, and it is made available on 20220816. Thus, image creation date, as stated in the cloud, may be different than the version serial.
* Registration: The act of taking an image, and making it available for use in the cloud. For example, the act of taking a vmdk, uploading, and importing it into ec2 as an ami
* Publication: the act of taking a machine image and making it publicly available. This may involve a marketplace, or it may involve a flag in the permissions of the image itself.
* Daily: a build that can occur on a daily basis. Basic testing only provided
* Release: a build that occurs when a specific set of packages, the "release package set", has changed. This is a slower cadence, normally at longest the kernel SRU timeframe.
* Release Package Set: a set of packages, either debians or snaps, that encompass the most fundamental portions of an Ubuntu product. There is a primary set of packages which encompass first boot critical functionality.
* Appliance: An image or container that contains more than the basic Ubuntu packages. Example: Anbox Cloud

## What Do We Build

The Canonical Public Cloud (CPC) team builds the images found at [cloud-images.ubuntu.com](http://cloud-images.ubuntu.com), and the officially produce images for major clouds such as Google Cloud, AWS EC2, Oracle Cloud, IBM Cloud VPC, IBM Cloud Classic, and Microsoft Azure. CPC also supports host or worker OS deployments on cloud Kubernetes offerings, such as GKE and EKS. Partnering with the Canonical ROCKS team, CPC helps to publish the Docker containers for Dockerhub (the official Ubuntu containers), EKS, and GKE. 

## What's In An Image?

Ubuntu Cloud Images are derived from Ubuntu Server. All Ubuntu images come from a "seed." These are basic sets of packages that define an Ubuntu Flavor. These include package management (`apt`), system start and setup (`systemd`), bootloader (`grub2`), and other fundamental packages such as the Python programming language, a pager (`less`), and a command line editor (`nano` and `vi`). Cloud images also contain `cloud-init`, the program used by many clouds to provide initial configuration to an image. Canonical is regularly examining the packages included as a part of a base image, and evaluate the total image size. The goal is to create a lean, but user friendly image. A full discussion of seeds and packages is out of scope for this overview.

Cloud images also come with cloud agents pre-installed. These are programs required by a cloud to have full functionality. Each cloud's requirements are unique, and are therefore catalogued per cloud.

Clouds may also require specific configuration to be in place in the image. Like the package contents, configurations may differ between clouds, and are documented per cloud. Examples are: 

* setting up default `apt` lists for in-cloud mirrors.
* configuration of `iptables` to allow `iscsi` based root discs (Oracle Cloud).
* configuring `chrony` to use an in-cloud source.


The Public Cloud team also offers an image meant for automated deployments, [Ubuntu Minimal](https://wiki.ubuntu.com/Minimal). Human related optional items such as manual pages, pagers, and text editors have been removed. This creates a small image, but one that is difficult to use outside of automated systems. An "un-minimize" script is provided to turn a Minimal image into a Cloud Server image.

## When Do We Build?

CPC will initiate a "daily" build whenever a package (debian or snap) has changed in the image. CPC does this by keeping a manifest that contains all packages within an image, then querying the Ubuntu debian archives and the Snapstore for what version is available, and doing a version comparison. If a difference is found, we initiate a new image build and mark the serial for the day as a "Daily Candidate." A build is then initiated to create our "Download" images found at [cloud-images.ubuntu.com](http://cloud-images.ubuntu.com). We produce images for x86(amd64), ARM64, powerpcel64, s390x, and RiscV. Older releases also fully support armhf (arm32) and i386 (32bit amd). 


## Testing
Images are registered into each cloud for testing purposes. This includes a Canonical hosted OpenStack deployment with access to supported architectures, as well as our cloud partners. After registration, CPC runs tests against a wide number of instance types, architectures, and cloud capabilities. While our tests are not exhaustive, we do strive to cover the most basic functionality of Ubuntu and the specific customizations provided in each cloud.

## Release Candidacy

Each product CPC produces has a unique list of packages that constitute a "release." There is a baseline set of packages:

* kernel (linux-$CLOUD)
* openssl
* openssh
* amd64-microcode
* intel-microcode
* cloud-init

After that, specific products have packages, as catalogued in their individual documentation. This means that it is possible, for instance, for one product to have a Release without another. Example:

A bug has been found in the `linux-azure==5.15` kernel, and _only_ this kernel. It was caused by a specific cherry-pick for functionality from a newer upstream kernel for enablement of a specific Azure feature. An emergency respin is done by the Canonical kernel team, and `linux-azure==5.15` is released to the `updates` pocked of the Ubuntu archives for Focal (20.04). This leads to a Release build for Focal Azure images _only_, as none of the other kernels were released.

Due to the Stable Release Updates (SRU) cycle, CPC generally produces release images every three week. As releases become more stable over time, and fewer bugs are backported, older Ubuntu releases may not get as many daily releases.

## Registration and Publication

Getting images into the clouds is a two step process. First there is a registration process in which we get the image ingested into the Compute engine for the cloud. These are registered privately for testing purposes. After testing, images are published for public consumption. If an image is marked as a Release Candidate and all testing passes, the release stream on the clouds, as well as any cloud marketplace listings are updated.

For clouds in which we do not own publication, and we retain formal relations, we still register and test images. However, we do not set the dates by which the cloud themselves publish these images to end users. These updates may occur monthly or quarterly. For clouds where publication is owned by Canonical, we produce LTS and non-LTS images. For Cloud Platform owned partners, LTS only are released.

Current rolling release clouds:

* GCE (Google Compute Engine)
* AWS EC2
* AWS EKS
* Microsoft Azure (gen1 and gen2)

Current Regularly Release Cloud Platform Owned Clouds (publication owned by the cloud):

* Oracle Compute Infrastructure (OCI)
* GKE (Google Kubernetes Engine)
* IBM NextGen VPC
* IBM Classic

## Bug Reporting

CPC can take public bug request via [Launchpad at the cloud-images project](https://launchpad.net/cloud-images). Use this to report issues found on Canonical LTD published images on the major clouds. For instance, if you go to spin up an EC2 AMI from the [AWS Marketplace Listing for Focal](https://aws.amazon.com/marketplace/pp/prodview-iftkyuwv2sjxi) and the image fails to boot, please open a bug ASAP. You can also use Launchpad to ask questions or request improvements. 

# Finale
This is not an exhaustive explanation of all of CPC's products. CPC can register upwards of 2000 images a day across all our partner clouds. Our build pipelines include all supported releases of Ubuntu, including those in standard and [extended support](https://ubuntu.com/security/esm).These pipelines range across thousands of jobs and multiple CI servers. You can reach CPC at the aforementioned [launchpad link for bugs or feature requests](https://launchpad.net/cloud-images), improve the docs via [Github](https://github.com/canonical/ubuntu-cloud-docs), and on IRC on libera.chat `#ubuntu-cloud` and other `#ubuntu` channels. 
