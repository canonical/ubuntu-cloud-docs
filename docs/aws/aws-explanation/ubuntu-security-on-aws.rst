Security features with Ubuntu on AWS
====================================

Ubuntu images on AWS include the security features provided by both Ubuntu and AWS. Some of these features might need to be specifically enabled. This explanation provides pointers to these features and to the specific how-to guides that help you enable them.


Ubuntu security features
------------------------

Ubuntu on AWS provides all the security features available on Ubuntu Server. A detailed description of these features can be found on the `Ubuntu security page`_ and in our explanation about :doc:`Security in the Ubuntu cloud images <all-clouds:all-clouds-explanation/security-overview>`. For further guidance on usage refer to  Ubuntu server's `Introductory page on security`_. 


AWS security features
---------------------

AWS offers comprehensive security and data protection in the cloud. `Security in Amazon EC2`_ explains how users can benefit from AWS security features.

Secure Boot and TPM
~~~~~~~~~~~~~~~~~~~

AWS Secure Boot is a feature of Amazon EC2 instances, that allows only trusted software to be used during the booting process. To create and configure a secure boot image using an Ubuntu AMI, refer to :doc:`../aws-how-to/security/use-secureboot-and-vtpm`.

CIS hardened image
~~~~~~~~~~~~~~~~~~

CIS hardened images are available for use on Amazon EC2. These images include the security related configurations specified by the Center for Internet Security (CIS).

To create a hardened image using Ubuntu Pro, refer to `Build a CIS hardened Ubuntu Pro server image on the AWS Console`_.

AMD SEV-SNP
~~~~~~~~~~~

AMD Secure Encrypted Virtualization-Secure Nested Paging (AMD SEV-SNP) provides strong memory integrity protection to instances that use AMD EPYC processors. Details about launching AMD SEV-SNP instances are given in :doc:`../aws-how-to/instances/launch-and-attest-amd-sev-snp-instances`.

Enhanced security using Ubuntu Pro
----------------------------------

Apart from the Ubuntu Server images, AWS also has images for `Ubuntu Pro`_, which come with enhanced security features:

* Expanded Security Maintenance (ESM): Provides 10 years of security patching for packages in the Ubuntu (main and universe) repositories.
* Live kernel updates: These reduce downtime and unplanned reboots in case of kernel vulnerabilities.
* FIPS compliance: Includes FIPS-certified modules to enable the use of Ubuntu in highly regulated environments.

To find Ubuntu Pro images on AWS (for both EC2 and EKS), refer to :doc:`../aws-how-to/instances/find-ubuntu-images`. The product parameter allows you to specify Pro.


.. _`Ubuntu security page`: https://ubuntu.com/security
.. _`Introductory page on security`: https://documentation.ubuntu.com/server/explanation/intro-to/security/
.. _`Security in Amazon EC2`: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-security.html
.. _`Build a CIS hardened Ubuntu Pro server image on the AWS Console`: https://www.youtube.com/watch?v=t5js7q-Cvko
.. _`Ubuntu Pro`: https://ubuntu.com/aws/pro

