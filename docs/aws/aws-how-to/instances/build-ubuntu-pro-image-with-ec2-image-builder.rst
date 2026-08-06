.. meta::
   :description: Learn how to build custom Ubuntu Pro images using EC2 Image Builder with the Ubuntu Pro component from the AWS Marketplace. Bake Pro services and security features directly into your AMIs at build time.

Build a custom Ubuntu Pro image with EC2 Image Builder
=======================================================

EC2 Image Builder lets you automate the creation, testing, and distribution of custom AMIs. By adding the `Ubuntu Pro component`_ (available on the AWS Marketplace for AMD64 and Graviton), you can attach an Ubuntu Pro subscription directly to your images during the build process. This enables any custom image—including those running non-Ubuntu operating systems—to attach a Pro license at build time for metered billing.

 .. note::

    Attaching an Ubuntu Pro subscription to a non-Ubuntu operating system only enables those machines to join EKS/ECS clusters running Ubuntu Pro containers. It does not provide access to other Ubuntu Pro services, such as 10 years of maintenance, FIPS, or Kernel Livepatch.

This guide walks through the steps to subscribe to the Ubuntu Pro component and use it in an EC2 Image Builder pipeline.


Prerequisites
-------------

* An AWS account with sufficient IAM permissions to use EC2 Image Builder (``imagebuilder:*``), create and manage EC2 instances, and access the AWS Marketplace.
* Familiarity with the EC2 Image Builder console or AWS CLI. If you are new to Image Builder, the `EC2 Image Builder tutorials`_ are a good starting point.


Subscribe to the Ubuntu Pro component
--------------------------------------

Before using the component in a pipeline, you must subscribe to it on the AWS Marketplace. For general guidance on working with Marketplace components in Image Builder, refer to the `AWS documentation on using Marketplace components`_.

1. Open the AWS Marketplace listing for your target architecture:

   * `Ubuntu Pro Component for EC2 Image Builder (AMD)`_
   * `Ubuntu Pro Component for EC2 Image Builder (Arm)`_

2. Choose :guilabel:`View purchase options`.
3. Review the terms and choose :guilabel:`Accept Terms`.
4. Wait for the subscription to become active.

.. note::

   A separate subscription is required for each architecture (AMD and ARM) if you intend to build images for both.


Create an image recipe and pipeline
------------------------------------

An image recipe defines the base image and the components to apply during a build. For detailed instructions on creating recipes, infrastructures, and pipelines, refer to the `AWS documentation on managing components`_.

To add the Ubuntu Pro component to your image:

1. Open the `EC2 Image Builder console`_.
2. In the left navigation pane, choose :guilabel:`Image recipes`, then choose :guilabel:`Create image recipe`.
3. Enter a name and version for the recipe.
4. Under :guilabel:`Base image`, choose :guilabel:`Select managed images` and search for ``ubuntu``. Select the Ubuntu LTS AMI that matches your target architecture (e.g. Ubuntu 24.04 LTS for AMD or ARM).
5. Under :guilabel:`Components`, choose :guilabel:`Add components`.
6. Switch to the :guilabel:`AWS Marketplace` tab and search for ``Ubuntu Pro``.
7. Select :guilabel:`Ubuntu Pro Component for EC2 Image Builder` (or the ARM variant) and choose :guilabel:`Add component`.
8. Optionally, add any additional build or test components for your workload.
9. Follow the AWS documentation to complete the infrastructure and distribution configuration, then create and run your pipeline.


Verify the resulting AMI
-------------------------

Once the pipeline run completes:

1. In the pipeline details page, choose the completed image version to view its ARN and AMI ID.
2. Launch an instance from the AMI.
3. Connect to the instance and confirm that Pro is active:

   .. code::

      sudo pro status

   The output should show Ubuntu Pro as ``attached`` with the relevant services enabled.


.. _EC2 Image Builder tutorials: https://docs.aws.amazon.com/imagebuilder/latest/userguide/ib-tutorials.html
.. _AWS documentation on using Marketplace components: https://docs.aws.amazon.com/imagebuilder/latest/userguide/use-marketplace-components.html
.. _AWS documentation on managing components: https://docs.aws.amazon.com/imagebuilder/latest/userguide/manage-components.html
.. _Ubuntu Pro component: https://aws.amazon.com/marketplace/pp?sku=9bztusbna2lfuk6zw7upzdvsv
.. _Ubuntu Pro Component for EC2 Image Builder (AMD): https://aws.amazon.com/marketplace/pp?sku=9bztusbna2lfuk6zw7upzdvsv
.. _Ubuntu Pro Component for EC2 Image Builder (Arm): https://aws.amazon.com/marketplace/pp?sku=291iwywwdb7ujmih1x7z4l3my
.. _EC2 Image Builder console: https://console.aws.amazon.com/imagebuilder/
