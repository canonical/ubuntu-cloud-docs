# Configuration file for the Sphinx documentation builder.
project = 'Ubuntu on GCP'

html_context = {    
    # Change to the GitHub info for your project
    "github_url": "https://github.com/canonical/ubuntu-cloud-docs"    
}

html_static_path = ['.sphinx/_static']
html_css_files = [
    'custom.css',
    'github_issue_links.css',
]

html_js_files = []
if "github_issues" in html_context and html_context["github_issues"]:
    html_js_files.append('github_issue_links.js')
