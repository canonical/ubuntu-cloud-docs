# Configuration file for the Sphinx documentation builder.
project = 'Ubuntu on GCP'

# Set up redirects (https://documatt.gitlab.io/sphinx-reredirects/usage.html)
# For example: "explanation/old-name.html": "../how-to/prettify.html",
redirects = {
    
    "google-how-to/find-ubuntu-images":
        "../gce/find-ubuntu-images/",
    "google-how-to/create-different-instance-types":
        "../gce/create-different-instance-types/",
    "google-how-to/launch-ubuntu-desktop":
        "../gce/launch-ubuntu-desktop/",
    "google-how-to/upgrade-in-place-from-lts-to-pro":
        "../gce/upgrade-in-place-from-lts-to-pro/",
    "google-how-to/enable-pro-features":
        "../gce/enable-pro-features/",
    "google-how-to/build-ubuntu-pro-golden-image":
        "../gce/build-ubuntu-pro-golden-image/",
    "google-how-to/create-customised-docker-container":
        "../gce/create-customised-docker-container/",
    "google-how-to/upgrade-from-focal-to-jammy":
        "../gce/upgrade-from-focal-to-jammy/",

    "google-how-to/deploy-kubernetes-with-ubuntu-pro":
        "../gke/deploy-kubernetes-with-ubuntu-pro/"
}
