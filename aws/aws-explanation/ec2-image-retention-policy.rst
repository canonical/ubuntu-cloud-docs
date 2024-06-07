AWS image retention policies
=============================

Ubuntu images on AWS have three stage of life cycle : *release* > *deprecation* > *deletion*. 

Whenever a new image is built and released to AWS, all the previous serials for that image are deprecated except for the last 3. A deprecated image is not visible on the AWS console, but it can still be launched from the `AWS CLI`_ using its AMI ID. You can also find and view details of deprecated images using the AWS CLI `describe-images`_ command by including the ``--include-deprecated`` flag.
This policy determines when an image will be deleted. Deleted images are no longer accessible for use, but instances already launched with those images will not be affected.


Image retention policy
----------------------

.. include:: ../../reuse/common-intro.txt
   :start-after: Start: Daily vs release images
   :end-before: End: Daily vs release images

For more details about these image types, check out our documentation of :doc:`image release types <all-clouds:all-clouds-explanation/release-types>`, and to get a list of these images on AWS, refer to: :doc:`../aws-how-to/instances/find-ubuntu-images`.

The retention policy can be summarised as follows:

.. list-table:: 
   :header-rows: 1

   * - **Ubuntu suite**
     - 
     - **Daily Images**
     - **Release Images**
   * - Interim Release
     - Active 
     - Delete all *but* the last 3 serials
     - Deprecate all except last 3 serials
   * - 
     - EOL*
     - Delete all images
     - Deprecate all except latest serial
   * - LTS Release
     - Active
     - Delete all *but* the last 3 serials
     - Deprecate all except last 3 serials 
   * - 
     - EOSS**
     - Delete all images
     - Deprecate all except latest serial
   * - EKS Release
     - Active
     - N/A
     - Deprecate all except last 3 serials
   * - 
     - EOL*
     - N/A
     - Delete all except last 3 serials

where:
  - **EOL** refers to when an interim Ubuntu release (for example, Lunar Lobster 23.04) has reached end-of-life `and will no longer enjoy support <https://ubuntu.com/about/release-cycle/>`_, or when EKS is `no longer supported by AWS`_.
  - **EOSS** refers to when an LTS Ubuntu release (for example, Bionic Beaver 18.04 LTS) has reached "End of Standard Support" but will remain supported under Ubuntu Pro

.. _`AWS CLI`: https://docs.aws.amazon.com/cli/
.. _`describe-images`: https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-images.html
.. _`and will no longer enjoy support`: https://ubuntu.com/about/release-cycle/
.. _`no longer supported by AWS`: https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html
