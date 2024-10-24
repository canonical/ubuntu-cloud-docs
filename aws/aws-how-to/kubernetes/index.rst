Using EKS
=========


**How-to guides for using Ubuntu on EKS** - If you want Ubuntu on your EKS worker nodes, choose one of options below depending on your requirements:

* Use Ubuntu AMI - Ubuntu EKS AMI is available through :doc:`AWS CLI<../../aws-how-to/instances/find-ubuntu-images>` or from the `AWS marketplace`_. Use that and follow the instructions from:
   * :doc:`Deploy an Ubuntu EKS cluster <deploy-ubuntu-cluster-with-eks-ami>`
   * :doc:`Deploy a Pro cluster using AMI <deploy-ubuntu-pro-cluster-with-eks-pro-ami>`
   * :doc:`Deploy a Pro FIPS cluster using AMI <deploy-ubuntu-pro-fips-cluster>`

* Use Pro token - For Ubuntu Pro 20.04 LTS, use your Pro token obtained from Canonical, and follow the instructions given in:
   * :doc:`Deploy a Pro cluster (with / without FIPS) using tokens  <deploy-ubuntu-pro-cluster>`

**Other EKS related how-to guides**

* :doc:`Enable GPUs on EKS worker nodes <enable-gpus-on-eks>`

.. _`AWS marketplace`: https://aws.amazon.com/marketplace/search/results?searchTerms=Ubuntu+Pro+eks&CREATOR=565feec9-3d43-413e-9760-c651546613f2&filters=CREATOR

.. toctree::
   :hidden:
   :maxdepth: 1
   
   Deploy an Ubuntu EKS cluster <deploy-ubuntu-cluster-with-eks-ami>
   Deploy Pro cluster using AMI <deploy-ubuntu-pro-cluster-with-eks-pro-ami>
   Deploy Pro FIPS cluster using AMI <deploy-ubuntu-pro-fips-cluster>
   Deploy Pro cluster using tokens <deploy-ubuntu-pro-cluster>
   Enable GPUs on EKS <enable-gpus-on-eks>
