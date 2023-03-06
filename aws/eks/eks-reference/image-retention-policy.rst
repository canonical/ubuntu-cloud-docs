EKS image retention policy
===========================

There are multiple EKS images available for every EKS Kubernetes version (1.23, 1.24, ...). When an EKS Kubernetes version
is no longer `supported by AWS <https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html>`_,
all the images for that unsupported version are deleted from the Canonical AWS account, except for the latest released one.

Example
-------

Let's assume that the currently available images under the Canonical AWS account are::


    ubuntu-eks/k8s_1.24/images/hvm-ssd/ubuntu-focal-20.04-arm64-server-20221214
    ubuntu-eks/k8s_1.24/images/hvm-ssd/ubuntu-focal-20.04-arm64-server-20221206.1
    ubuntu-eks/k8s_1.23/images/hvm-ssd/ubuntu-focal-20.04-arm64-server-20221214
    ubuntu-eks/k8s_1.23/images/hvm-ssd/ubuntu-focal-20.04-arm64-server-20221011
    ubuntu-eks/k8s_1.23/images/hvm-ssd/ubuntu-focal-20.04-arm64-server-20220822.2


If EKS 1.23 is no longer supported, it would result in the deletion of the following two images::

    ubuntu-eks/k8s_1.23/images/hvm-ssd/ubuntu-focal-20.04-arm64-server-20221011
    ubuntu-eks/k8s_1.23/images/hvm-ssd/ubuntu-focal-20.04-arm64-server-20220822.2

but the latest image ``ubuntu-eks/k8s_1.23/images/hvm-ssd/ubuntu-focal-20.04-arm64-server-20221214`` would still exist.