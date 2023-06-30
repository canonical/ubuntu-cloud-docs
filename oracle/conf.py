# Configuration file for the Sphinx documentation builder.
project = 'Ubuntu on Oracle'

html_context = {
    # Change to the GitHub info for your project
    "github_url": "https://github.com/canonical/ubuntu-cloud-docs/",
    # Change to the branch for this version of the documentation
    "github_version": "main",
    # Change to the folder that contains the documentation (usually "/" or "/docs/")
    "github_folder": "/oracle/"
}


# Used for related links - no need to change
if 'discourse' in html_context:
    html_context['discourse_prefix'] = html_context['discourse'] + "/t/"

html_js_files = []
if "github_issues" in html_context and html_context["github_issues"]:
    html_js_files.append('github_issue_links.js')
