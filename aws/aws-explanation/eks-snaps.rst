Snap usage in EKS worker images
===============================

The EKS worker images bundle several snaps that provide
Kubernetes components. This page will provide a brief
explanation on what snaps are bundled and why.

Snaps
-----

.. list-table::
   :header-rows: 1

   * - **Snap Name**
     - **Provides**
     - **Bundled Since**
   * - :doc:`kubelet-eks </aws-reference/eks-kubelet-snap>`
     - the `kubelet <https://kubernetes.io/docs/reference/command-line-tools-reference/kubelet/>`_ binary, which includes the primary configuration mechanism for kubelet
     - EKS 1.17
   * - kubectl-eks
     - the `kubectl <https://kubernetes.io/docs/reference/kubectl/>`_ binary, for providing CLI access to a k8s cluster's control plane
     - EKS 1.17
   * - ecr-credential-provider
     - `aws-credential-provider <https://github.com/kubernetes/cloud-provider-aws/tree/master?tab=readme-ov-file#aws-credential-provider>`_, which provides credentials for allowing a k8s cluster to pull container images from ECR
     - EKS 1.28

