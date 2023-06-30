# Configuration file for the Sphinx documentation builder.
project = 'Ubuntu on OCI Registries'

html_context = {
    # Change to the discourse instance you want to be able to link to
    # (use an empty value if you don't want to link)
    "discourse": "https://discourse.ubuntu.com",
    # Change to the GitHub info for your project
    "github_url": "https://github.com/canonical/ubuntu-cloud-docs",
    # Change to the branch for this version of the documentation
    "github_version": "main",
    # Change to the folder that contains the documentation (usually "/" or "/docs/")
    "github_folder": "/oci/",
    # Change to an empty value if your GitHub repo doesn't have issues enabled
    "github_issues": "enabled"
}