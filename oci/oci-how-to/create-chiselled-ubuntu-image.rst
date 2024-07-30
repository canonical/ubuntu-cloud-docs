Create a chiselled Ubuntu image for C/C++, Go and Rust applications
*******************************************************************

This guide will provide step-by-step instructions on how to create your own chiselled Ubuntu container image to run a compiled application.

- Chiselled Ubuntu are appliance-type container images combining both the advantages of distroless and Ubuntu to create smaller, more secure containers, without loosing the value add of a stable Linux distribution.
- The reduced size of the containers reduces the overall attack surface. Combined with the support and content quality from the Ubuntu distribution, chiselled Ubuntu is a significant security improvement.
- Chisel provides a developer-friendly CLI to install slices of packages from the upstream Ubuntu distribution onto the container filesystem.


Build the chiselled Ubuntu image
--------------------------------

This image must contain all the essential slices that are required for the execution of common compiled applications. As a base, the must-have list of slices is:

- **base-files_base** and **base-files_release-info**: will give you the overall base structure of the container image's filesystem, together with the underlying Ubuntu release information,
- **ca-certificates_data**: for cryptographic certificate verifications,
- **libgcc-s1_libs** and **libc6_libs**: for the libgcc-s1 and libc6 libraries.

Additionally, if you need SSL for your applications, make sure to also install the **openssl_config** slice.
Here are other slices that might be useful (or even needed) depending on your target application's requirements:

- **tzdata_zoneinfo**: for the timezone database,
- **libc-bin_nsswitch**: used by some applications to obtain name-service information.

For this guide, let's use Ubuntu Jammy as the reference Ubuntu release for the target chiselled image.

Start by creating a Dockerfile with the following content:

..  code-block:: dockerfile

   ARG UBUNTU_RELEASE=22.04

   # Build the chiselled filesystem based on the desired slices.
   FROM ubuntu:$UBUNTU_RELEASE AS builder
   ARG UBUNTU_RELEASE
   ARG TARGETARCH

   # Get chisel binary
   ADD https://github.com/canonical/chisel/releases/download/v0.9.1/chisel_v0.9.1_linux_$TARGETARCH.tar.gz chisel.tar.gz
   RUN tar -xvf chisel.tar.gz -C /usr/bin/
   RUN apt-get update \
      && DEBIAN_FRONTEND=noninteractive apt-get install -y ca-certificates
   WORKDIR /rootfs
   RUN chisel cut --release ubuntu-$UBUNTU_RELEASE --root /rootfs \
      base-files_base \
      base-files_release-info \
      ca-certificates_data \
      libgcc-s1_libs \
      libc6_libs  

   # Make the chiselled filesystem the only thing
   # present in the final image.
   FROM scratch
   COPY --from=builder /rootfs /

Build the chiselled Ubuntu image by running:

..  code-block:: bash
   
   docker build -t chiselled-ubuntu:latest .

You'll then find yourself with a new container image with approximately 5MB (or 2.5MB when compressed). 

Build the application image
---------------------------

Now that you have the ``chiselled-ubuntu:latest`` image, you can simply add your compiled application to the image and run it from there. For the sake of simplicity, this guide will give you three very simple “Hello World” application examples for C, Go and Rust.


.. tabs::

	.. tab:: C

         Assume the following ``app.c`` source code:

         .. code-block:: c

            #include <stdio.h>

            int main() {
               printf("Hello World!");
               return 0;
            }
            
         You'd typically compile this via ``gcc app.c -o app``.
   
	.. tab:: Go

         Assume the following ``app.go`` source code:

         .. code-block:: go
            
            package main
            import "fmt"

            func main() {
               fmt.Println("Hello World!")
            }
                        
         You'd typically compile this via ``go build -o app app.go``.
   
	.. tab:: Rust

         Assume the following ``app.rs`` source code:

         .. code-block:: rust
      
            
            fn main() {
               println!("Hello World!");
            }

               
         You'd typically compile this via ``rustc app.rs``.
   


To build the final application image, you simply need to add your compiled executable to the ``chiselled-ubuntu:latest`` container image. So your new Dockerfile should be similar to:

.. code-block:: dockerfile

   FROM chiselled-ubuntu:latest
   COPY app /
   ENTRYPOINT [ "./app" ]

Build this chiselled application image with ``docker build  -t chiselled-app:latest .`` and then run it:

.. code-block:: bash
   
   docker run chiselled-app:latest

And the output should be:

.. code-block:: 

   Hello World!


What's achieved?
----------------

The demonstrated chiselled Ubuntu image provides a sub-5MB runtime container image for your C/C++, Go and Rust applications whilst still allowing for additional slices to be easily added to cope with more complex use cases.

Chiselled Ubuntu images offer the benefits of a well-known and well-maintained Linux distribution combined with the advantages of ultra-small distroless-type container images, offering a secure and efficient foundation for building and deploying containerised applications.

