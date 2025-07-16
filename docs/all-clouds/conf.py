# Some settings in the html_context dictionary have to be repeated 
# in the sub projects for correct functioning (don't remove them)
html_context = {

    # Change to the link to the website of your product (without "https://")
    # For example: "ubuntu.com/lxd" or "microcloud.is"
    # If there is no product website, edit the header template to remove the
    # link (see the readme for instructions).
    'product_page': 'ubuntu.com/cloud/public-cloud',

    # Add your product tag (the orange part of your logo, will be used in the
    # header) to ".sphinx/_static" and change the path here (start with "_static")
    # (default is the circle of friends)
    'product_tag': '_static/tag.png',

    # Change to the discourse instance you want to be able to link to
    # using the :discourse: metadata at the top of a file
    # (use an empty value if you don't want to link)
    'discourse': 'https://discourse.ubuntu.com/c/project/public-cloud/',

    # Change to the Mattermost channel you want to link to
    # (use an empty value if you don't want to link)
    'mattermost': 'https://chat.canonical.com/canonical/channels/public-cloud',

    # Change to the Matrix channel you want to link to
    # (use an empty value if you don't want to link)
    'matrix': 'https://matrix.to/#/#ubuntu-cloud:ubuntu.com',

    # Change to the GitHub URL for your project
    'github_url': 'https://github.com/canonical/ubuntu-cloud-docs',

    # Change to the branch for this version of the documentation
    'repo_default_branch': 'main',

    # Change to the folder that contains the documentation
    # (usually "/" or "/docs/")
    'repo_folder': '/all-clouds/',

    # Change to an empty value if your GitHub repo doesn't have issues enabled.
    # This will disable the feedback button and the issue link in the footer.
    'github_issues': 'enabled',

    # Change to the folder that contains the documentation 
    # (usually "/" or "/docs/")
    "conf_py_path": '/all-clouds/',

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
    "oci/oci-how-to/create-chiselled-ubuntu-image.html":
        "https://documentation.ubuntu.com/chisel/en/latest/tutorial/getting-started/",
    "oci/oci-how-to/deploy-pro-container-on-pro-kubernetes-cluster.html":
        "https://documentation.ubuntu.com/oci-registries/oci-how-to/deploy-pro-container-on-pro-kubernetes-cluster/"
}


############################################################
### Sitemap configuration
############################################################

html_baseurl = 'https://documentation.ubuntu.com/public-cloud/'
