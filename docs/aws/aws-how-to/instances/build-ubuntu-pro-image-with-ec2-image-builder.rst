.. meta::
   :description: Learn how to build custom Ubuntu Pro images using EC2 Image Builder with the Ubuntu Pro component from the AWS Marketplace. Bake Pro services and security features directly into your AMIs at build time.

Build a custom Ubuntu Pro image with EC2 Image Builder
=======================================================

EC2 Image Builder lets you automate the creation, testing, and distribution of custom AMIs. By adding the `Ubuntu Pro component`_ (available on the AWS Marketplace), you can bake Ubuntu Pro services — including the 10-year security guarantee and expanded package coverage — directly into your images at build time. This removes the need to attach Pro tokens or run activation scripts after an instance starts.

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


Create an image recipe
-----------------------

An image recipe defines the base image and the components to apply during a build.

.. tab-set::

   .. tab-item:: AWS CLI

      1. Retrieve the Ubuntu Pro component ARN for your target architecture.

         For AMD:

         .. code::

            aws imagebuilder list-components \
                --owner AWSMarketplace \
                --query "componentVersionList[?productCodes[?productCodeId=='9bztusbna2lfuk6zw7upzdvsv']]"

         For ARM:

         .. code::

            aws imagebuilder list-components \
                --owner AWSMarketplace \
                --query "componentVersionList[?productCodes[?productCodeId=='291iwywwdb7ujmih1x7z4l3my']]"

         Example output:

         .. code::

            [
                {
                    "arn": "arn:aws:imagebuilder:us-east-1:aws-marketplace:component/ubuntu-pro-component-prod-w2osc53uiegx4/1.0.0",
                    "name": "Ubuntu Pro Component-prod-w2osc53uiegx4",
                    "version": "1.0.0",
                    "description": "Ubuntu Pro component",
                    "platform": "Linux",
                    "supportedOsVersions": [
                        "Ubuntu 18",
                        "Ubuntu 20",
                        "Ubuntu 22",
                        "Ubuntu 24"
                    ],
                    "type": "BUILD",
                    "owner": "AWSMarketplace",
                    "status": "ACTIVE",
                    "productCodes": [
                        {
                            "productCodeId": "9bztusbna2lfuk6zw7upzdvsv",
                            "productCodeType": "marketplace"
                        }
                    ]
                }
            ]

         Note the ``arn`` value from the output.

      2. Create the image recipe, substituting the component ARN from the previous step and the base image AMI ID for your target architecture:

         .. code::

            aws imagebuilder create-image-recipe \
                --name "ubuntu-pro-recipe" \
                --semantic-version "1.0.0" \
                --components '[{"componentArn": "<component-arn-from-above>"}]' \
                --parent-image "<your-ami-id>"

   .. tab-item:: Console

      1. Open the `EC2 Image Builder console`_.
      2. In the left navigation pane, choose :guilabel:`Image recipes`, then choose :guilabel:`Create image recipe`.
      3. Enter a name and version for the recipe.
      4. Under :guilabel:`Base image`, choose :guilabel:`Select managed images` and search for ``ubuntu``. Select the Ubuntu LTS AMI that matches your target architecture (e.g. Ubuntu 24.04 LTS for AMD or ARM).
      5. Under :guilabel:`Components`, choose :guilabel:`Add components`.
      6. Switch to the :guilabel:`AWS Marketplace` tab and search for ``Ubuntu Pro``.
      7. Select :guilabel:`Ubuntu Pro Component for EC2 Image Builder` (or the ARM variant) and choose :guilabel:`Add component`.
      8. Optionally, add any additional build or test components for your workload.
      9. Choose :guilabel:`Create recipe`.


Create an infrastructure configuration
----------------------------------------

An infrastructure configuration specifies the instance type and IAM role that Image Builder uses to run the build.

.. tab-set::

   .. tab-item:: AWS CLI

      .. code::

         aws imagebuilder create-infrastructure-configuration \
             --name "<your-infra-config-name>" \
             --instance-profile-name "EC2InstanceProfileForImageBuilder" \
             --instance-types "t3.medium"

   .. tab-item:: Console

      1. In the left navigation pane, choose :guilabel:`Infrastructure configurations`, then choose :guilabel:`Create infrastructure configuration`.
      2. Enter a name.
      3. Under :guilabel:`IAM role`, choose or create a role that includes the ``EC2InstanceProfileForImageBuilder`` managed policy.
      4. Choose an appropriate :guilabel:`Instance type` for the architecture you are targeting (e.g. ``t3.medium`` for AMD, ``t4g.medium`` for ARM).
      5. Choose :guilabel:`Create infrastructure configuration`.


Create a distribution configuration
-------------------------------------

A distribution configuration defines the Regions and output settings for the built AMI.

.. tab-set::

   .. tab-item:: AWS CLI

      .. code::

         aws imagebuilder create-distribution-configuration \
             --name "<your-distribution-config-name" \
             --distributions '[{"region": "<your-region>", "amiDistributionConfiguration": {}}]'

   .. tab-item:: Console

      1. In the left navigation pane, choose :guilabel:`Distribution settings`, then choose :guilabel:`Create distribution settings`.
      2. Enter a name.
      3. Under :guilabel:`Region`, confirm or add the target Regions where the AMI should be available.
      4. Optionally, configure AMI tags, launch permissions, or copying to additional Regions.
      5. Choose :guilabel:`Create distribution settings`.


Create and run an image pipeline
----------------------------------

An image pipeline ties together the recipe, infrastructure configuration, and distribution configuration.

.. tab-set::

   .. tab-item:: AWS CLI

      1. Create the pipeline, substituting the all ARN sections from the resources created in the previous steps:

         .. code::

            aws imagebuilder create-image-pipeline \
                --name "<your-pipeline-name>" \
                --image-recipe-arn "<recipe-arn>" \
                --infrastructure-configuration-arn "<infra-config-arn>" \
                --distribution-configuration-arn "<distro-config-arn>"

      2. To start a build immediately:

         .. code::

            aws imagebuilder start-image-pipeline-execution \
                --image-pipeline-arn "<pipeline-arn>"

   .. tab-item:: Console

      1. In the left navigation pane, choose :guilabel:`Image pipelines`, then choose :guilabel:`Create image pipeline`.
      2. Enter a pipeline name.
      3. Under :guilabel:`Build schedule`, choose :guilabel:`Manual` to trigger builds on demand, or configure a schedule.
      4. Select the recipe, infrastructure configuration, and distribution configuration created in the previous steps.
      5. Choose :guilabel:`Create pipeline`.
      6. To start a build immediately, select the pipeline and choose :guilabel:`Actions` > :guilabel:`Run pipeline`.

Image Builder will launch a temporary build instance, apply the Ubuntu Pro component (which enables Pro services), run any test components, terminate the build instance, and register the resulting AMI in the configured Regions.


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
.. _Ubuntu Pro component: https://aws.amazon.com/marketplace/pp?sku=9bztusbna2lfuk6zw7upzdvsv
.. _Ubuntu Pro Component for EC2 Image Builder (AMD): https://aws.amazon.com/marketplace/pp?sku=9bztusbna2lfuk6zw7upzdvsv
.. _Ubuntu Pro Component for EC2 Image Builder (ARM): https://aws.amazon.com/marketplace/pp?sku=291iwywwdb7ujmih1x7z4l3my
.. _EC2 Image Builder console: https://console.aws.amazon.com/imagebuilder/
