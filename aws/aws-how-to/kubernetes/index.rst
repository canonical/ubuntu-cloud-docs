Using EKS
=========


**How-to guides for using Ubuntu Pro on EKS** - If you want Ubuntu Pro on your EKS worker nodes, you have two options:

* Use Pro AMI - The Ubuntu Pro 22.04 LTS AMI is available through :doc:`AWS CLI<../../aws-how-to/instances/find-ubuntu-images>` or from the `AWS marketplace`_. Use that and follow the instructions from:
   * :doc:`Deploy a Pro cluster using AMI <deploy-ubuntu-pro-cluster-with-eks-pro-ami>` or
   * :doc:`Deploy a Pro FIPS cluster using AMI <deploy-ubuntu-pro-fips-cluster>`

* Use Pro token - For Ubuntu Pro 20.04 LTS, use your Pro token obtained from Canonical, and follow the instructions given in:
   * :doc:`Deploy a Pro cluster (with / without FIPS) using tokens  <deploy-ubuntu-pro-cluster>`

**Other EKS related how-to guides**

* :doc:`Enable GPUs on EKS worker nodes <enable-gpus-on-eks>`

.. _`AWS marketplace`: https://aws.amazon.com/marketplace/search/results?searchTerms=Ubuntu+Pro+eks&CREATOR=565feec9-3d43-413e-9760-c651546613f2&filters=CREATOR

.. toctree::
   :hidden:
   :maxdepth: 1
   
   Deploy Pro cluster using AMI <deploy-ubuntu-pro-cluster-with-eks-pro-ami>
   Deploy Pro FIPS cluster using AMI <deploy-ubuntu-pro-fips-cluster>
   Deploy Pro cluster using tokens <deploy-ubuntu-pro-cluster>
   Enable GPUs on EKS <enable-gpus-on-eks>
