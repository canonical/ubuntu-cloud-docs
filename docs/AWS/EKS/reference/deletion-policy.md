# EKS image deletion policy

There are multiple EKS images for every EKS version (eg. 1.23, 1.24, ...). When a EKS version
is no longer [supported by AWS](https://docs.aws.amazon.com/eks/latest/userguide/kubernetes-versions.html),
all the images except the latest released one for that unsupported EKS version will be deleted on the Canonical AWS account.

## Example

Let's assume there are currently these images under the Canonical AWS account:

```
ubuntu-eks/k8s_1.24/images/hvm-ssd/ubuntu-focal-20.04-arm64-server-20221214
ubuntu-eks/k8s_1.24/images/hvm-ssd/ubuntu-focal-20.04-arm64-server-20221206.1
ubuntu-eks/k8s_1.23/images/hvm-ssd/ubuntu-focal-20.04-arm64-server-20221214
ubuntu-eks/k8s_1.23/images/hvm-ssd/ubuntu-focal-20.04-arm64-server-20221011
ubuntu-eks/k8s_1.23/images/hvm-ssd/ubuntu-focal-20.04-arm64-server-20220822.2
```

Now EKS 1.23 is no longer supported. That would result in deleting the following 2 images:

```
ubuntu-eks/k8s_1.23/images/hvm-ssd/ubuntu-focal-20.04-arm64-server-20221011
ubuntu-eks/k8s_1.23/images/hvm-ssd/ubuntu-focal-20.04-arm64-server-20220822.2
```

but the single latest image `ubuntu-eks/k8s_1.23/images/hvm-ssd/ubuntu-focal-20.04-arm64-server-20221214` would still be there.
