Ubuntu Base and Minimal Images
==============================

Broadly speaking, CPC produces two types of images - a base image and a minimal
image.

What are base and minimal images?
---------------------------------

Base images are those that are directly derived from Ubuntu Server-like images
and are meant for general consumption. On the other hand, minimal or minimized
images are those that are meant for machine-to-machine interactions, and have
some niceties meant for humans stripped out (such as manpages, translations,
editors, etc.). A great example would be our k8s images.


State of minimal images from Mantic onwards
-------------------------------------------

From Mantic Minotaur release onward (including Noble Numbat 24.04 LTS), we
worked through the minimal images to make it more efficient and truly minimal
by constructing a “cloud-minimal” seed, which is nothing but the list of basic
packages that we need in a minimal cloud installation. The package list is then
expanded by a program called “germinate”, which includes the dependencies of
the listed packages in the seed. Combined, we get the “image manifest”, aka the
list of packages you’d expect to see in the minimal cloud image.

With that effort, we could reduce the package size from package count 426 to
288 (difference: 138) and also reduce the size of the minimal image. Taking
download qcow2 images as an example, the image size reduced from 337.19MiB to
226.75MiB (difference: 110.44MiB).


What is unminimize? What does it do?
------------------------------------

Unminimize is essentially a script that’s shipped in /usr/bin by a package
called “unminimize”. The goal of this unminimize script is to unminimize the
minimal image and make it as close to that of a base image. It does this by
re-enabling installation of all documentation in DPKG, restoring system
documentation and man pages, restoring system translations, and then finally
installing some package on the top, like linux-image-virtual, et al. These
packages make the human interaction easier as it installed the basic packages
needed for so, like editors, et al.

To run ``unminimize``, you simply need to call:

``$ sudo unminimize``
