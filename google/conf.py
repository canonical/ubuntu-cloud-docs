# Configuration file for the Sphinx documentation builder.
project = 'Ubuntu on GCP'

# The title you want to display for the documentation in the sidebar.
# You might want to include a version number here.
# To not display any title, set this option to an empty string.
html_title = project + ' documentation'

# Some settings in the html_context dictionary have to be repeated 
# in the sub projects for correct functioning (don't remove them)
html_context = {

    # Change to the link to the website of your product (without "https://")
    # For example: "ubuntu.com/lxd" or "microcloud.is"
    # If there is no product website, edit the header template to remove the
    # link (see the readme for instructions).
    'product_page': 'ubuntu.com/gcp',

    # Add your product tag (the orange part of your logo, will be used in the
    # header) to ".sphinx/_static" and change the path here (start with "_static")
    # (default is the circle of friends)
    'product_tag': '_static/tag.png',

    # Change to the discourse instance you want to be able to link to
    # using the :discourse: metadata at the top of a file
    # (use an empty value if you don't want to link)
    'discourse': 'https://discourse.ubuntu.com/c/public-cloud/gcp/',

    # Change to the Mattermost channel you want to link to
    # (use an empty value if you don't want to link)
    'mattermost': 'https://chat.canonical.com/canonical/channels/public-cloud',

    # Change to the Matrix channel you want to link to
    # (use an empty value if you don't want to link)
    'matrix': 'https://matrix.to/#/#ubuntu-cloud:ubuntu.com',

    # Change to the GitHub URL for your project
    'github_url': 'https://github.com/canonical/ubuntu-cloud-docs',

    # Change to the branch for this version of the documentation
    'github_version': 'main',

    # Change to the folder that contains the documentation
    # (usually "/" or "/docs/")
    'github_folder': '/google/',

    # Change to an empty value if your GitHub repo doesn't have issues enabled.
    # This will disable the feedback button and the issue link in the footer.
    'github_issues': 'enabled',

    # Change to the folder that contains the documentation 
    # (usually "/" or "/docs/")
    "conf_py_path": '/google/',

    # Controls the existence of Previous / Next buttons at the bottom of pages
    # Valid options: none, prev, next, both
    # You can override the default setting on a page-by-page basis by specifying
    # it as file-wide metadata at the top of the file, see
    # https://www.sphinx-doc.org/en/master/usage/restructuredtext/field-lists.html
    'sequential_nav': "both"
}

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
    "google-how-to/create-customized-docker-container":
        "../gce/create-customized-docker-container/",
    "google-how-to/upgrade-from-focal-to-jammy":
        "../gce/upgrade-from-focal-to-jammy/",

    "google-how-to/deploy-kubernetes-with-ubuntu-pro":
        "../gke/deploy-kubernetes-with-ubuntu-pro/"
}
