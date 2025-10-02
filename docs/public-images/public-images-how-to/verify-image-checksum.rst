.. _verify-image-checksum:

Verify an image checksum
========================

For every `ubuntu cloud image`_, Canonical provides a corresponding SHA256 checksum. 
These checksums help reassure that the image you have downloaded is not corrupted in any way and that it is an authentic image that hasn't been tampered with.

We will go over how you can use the provided checksums to verify the authenticity of your downloaded image.

Installing the necessary packages
---------------------------------
The packages you will require are ``sha256sum``, ``md5sum`` and ``gpg``. Follow the guide corresponding to your system.

Ubuntu
~~~~~~
These are part of the ``coreutils`` and ``gnupg`` packages, which are installed by default.

MacOS
~~~~~
Install the latest GnuPG and coreutils

.. code:: bash

    brew install gnupg coreutils

Windows
~~~~~~~
If you are using bash on Windows 10, these tools are part of the default install.

Verify the installed packages
-----------------------------
.. code:: bash

    gpg --list-keys
    md5sum --version
    sha256sum --version

Download the relevant file and keys
-----------------------------------

Make sure you have the ``SHA256SUMS`` and ``SHA256SUMS.gpg`` files corresponding to the ISO image you have downloaded available locally.
You can find these files at https://cloud-images.ubuntu.com

**Note:** The following part of this how-to assumes you have the ISO image, SHA256SUMS and SHA256SUMS.gpg files in the current working directory.

Check if you have the Public key
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    gpg --keyid-format long --verify SHA256SUMS.gpg SHA256SUMS

If the public keys aren't present in your system, you will get an error message similar to the following

.. code:: text

    gpg: Signature made Tue Sep 30 13:04:34 2025 EDT
    gpg:                using RSA key D2EB44626FDDC30B513D5BB71A5D6C4C7DB87C81
    gpg: Can't check signature: No public key

Using these ID numbers (*D2EB44626FDDC30B513D5BB71A5D6C4C7DB87C81 in the example*), we can request them from the Ubuntu key server.


Note: Since the ID numbers are hexadecimal, we prefix them with a ``0x``


.. code:: bash

    gpg --keyid-format long --keyserver hkp://keyserver.ubuntu.com --recv-keys 0xD2EB44626FDDC30B513D5BB71A5D6C4C7DB87C81



You can now inspect the key fingerprints by running:

.. code:: bash

    gpg --keyid-format long --list-keys --with-fingerprint 0xD2EB44626FDDC30B513D5BB71A5D6C4C7DB87C81


Verify the checksum and image
-----------------------------

Now that we have the tools and keys required, we can verify our image. We will perform the following steps:

#. Verify that the checksum file is authentic
#. Generate a checksum of the ISO image and match it with the authenticated checksum file

Verify the checksum file
~~~~~~~~~~~~~~~~~~~~~~~~

.. code:: bash

    gpg --keyid-format long --verify SHA256SUMS.gpg SHA256SUMS


In the output, you should see something like this:

.. code:: text

    gpg: Signature made Tue Sep 30 13:04:34 2025 EDT
    gpg:                using RSA key D2EB44626FDDC30B513D5BB71A5D6C4C7DB87C81
    gpg: Good signature from "UEC Image Automatic Signing Key <cdimage@ubuntu.com>" [unknown]
    gpg: WARNING: This key is not certified with a trusted signature!
    gpg:          There is no indication that the signature belongs to the owner.
    Primary key fingerprint: D2EB 4462 6FDD C30B 513D  5BB7 1A5D 6C4C 7DB8 7C81


Verify the ISO image
~~~~~~~~~~~~~~~~~~~~

Finally, now that we have an authentic checksum file, we can generate a SHA256 checksum of the image and compare it with the file we just authenticated.


Make sure you preserve the filename of the original downloaded ISO image file

.. code:: bash

    sha256sum -c SHA256SUMS 2>&1 | grep OK

The output should look similar to the following:

.. code:: text

    questing-server-cloudimg-amd64.img: OK


.. _`ubuntu cloud image`: https://cloud-images.ubuntu.com