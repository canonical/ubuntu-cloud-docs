Using EKS
=========


**How-to guides for using Ubuntu on EKS** - If you want to use Ubuntu on your EKS worker nodes, choose from one of the following deployment options:

* Use an Ubuntu AMI - Ubuntu EKS AMIs are available through :doc:`AWS CLI<../../aws-how-to/instances/find-ubuntu-images>` or from the `AWS marketplace`_. They can be used to:
   * :doc:`Deploy an Ubuntu EKS cluster <deploy-ubuntu-cluster-with-eks-ami>`
   * :doc:`Deploy an Ubuntu Pro cluster <deploy-ubuntu-pro-cluster-with-eks-pro-ami>`
   * :doc:`Deploy an Ubuntu Pro FIPS cluster <deploy-ubuntu-pro-fips-cluster>`

* Use a Pro token - If you want to create an EKS cluster using your Pro token obtained from Canonical, follow the instructions given in:
   * :doc:`Deploy a Pro cluster (with / without FIPS) using tokens  <deploy-ubuntu-pro-cluster>`

**Other EKS related how-to guides**

* :doc:`Enable GPUs on EKS worker nodes <enable-gpus-on-eks>`
* `Install Kubeflow on EKS (external link)`_

.. _`AWS marketplace`: https://aws.amazon.com/marketplace/search/results?searchTerms=Ubuntu+Pro+eks&CREATOR=565feec9-3d43-413e-9760-c651546613f2&filters=CREATOR
.. _`Install Kubeflow on EKS (external link)`: https://documentation.ubuntu.com/charmed-kubeflow/how-to/install/install-eks/



.. toctree::
   :hidden:
   :maxdepth: 1
   
   Deploy an Ubuntu cluster <deploy-ubuntu-cluster-with-eks-ami>
   Deploy an Ubuntu Pro cluster <deploy-ubuntu-pro-cluster-with-eks-pro-ami>
   Deploy an Ubuntu Pro FIPS cluster <deploy-ubuntu-pro-fips-cluster>
   Deploy an Ubuntu Pro cluster using tokens <deploy-ubuntu-pro-cluster>
   Deploy a self-managed Ubuntu node group <deploy-self-managed-node-group>
   Enable GPUs on EKS <enable-gpus-on-eks>
