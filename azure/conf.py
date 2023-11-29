# Configuration file for the Sphinx documentation builder.
project = 'Ubuntu on Azure'

# Set up redirects (https://documatt.gitlab.io/sphinx-reredirects/usage.html)
# For example: "explanation/old-name.html": "../how-to/prettify.html",
redirects = {
    
    "azure-how-to/install-azure-cli":
        "../instances/install-azure-cli/",
    "azure-how-to/find-ubuntu-images":
        "../instances/find-ubuntu-images/",
    "azure-how-to/get-ubuntu-pro":
        "../instances/get-ubuntu-pro/",
    "azure-how-to/create-pro-fips-golden-image":
        "../instances/create-pro-fips-golden-image/",
    "azure-how-to/upgrade-from-focal-to-jammy":
        "../instances/upgrade-from-focal-to-jammy/",

    "azure-how-to/install-kubeflow-on-aks":
        "../kubernetes/install-kubeflow-on-aks/",
    "azure-how-to/deploy-kubeflow-pipelines-with-aks-spot-instances":
        "../kubernetes/deploy-kubeflow-pipelines-with-aks-spot-instances/"
}