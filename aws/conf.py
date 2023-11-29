# Configuration file for the Sphinx documentation builder.
project = 'Ubuntu on AWS'

# Set up redirects (https://documatt.gitlab.io/sphinx-reredirects/usage.html)
# For example: "explanation/old-name.html": "../how-to/prettify.html",
redirects = {
    
    "aws-how-to/automatically-update-ubuntu-instances":
        "../instances/automatically-update-ubuntu-instances/",
    "aws-how-to/build-cloudformation-templates":
        "../instances/build-cloudformation-templates/",
    "aws-how-to/build-pro-ami-using-packer":
        "../instances/build-pro-ami-using-packer/",
    "aws-how-to/find-ubuntu-images":
        "../instances/find-ubuntu-images/",
    "aws-how-to/launch-ubuntu-desktop":
        "../instances/launch-ubuntu-desktop/",
    "aws-how-to/upgrade-from-focal-to-jammy":
        "../instances/upgrade-from-focal-to-jammy/",

    "aws-how-to/deploy-charmed-kubernetes-on-ubuntu-pro":
        "../kubernetes/deploy-charmed-kubernetes-on-ubuntu-pro/",
    "aws-how-to/deploy-ubuntu-pro-cluster":
        "../kubernetes/deploy-ubuntu-pro-cluster/",
    "aws-how-to/enable-gpus-on-eks":
        "../kubernetes/enable-gpus-on-eks/",

    "aws-how-to/use-secureboot-and-vtpm":
        "../security/use-secureboot-and-vtpm/"
}