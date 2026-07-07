import os
import textwrap

# Configuration file for the Sphinx documentation builder.
project = 'Ubuntu on Oracle'

# The title you want to display for the documentation in the sidebar.
# You might want to include a version number here.
# To not display any title, set this option to an empty string.
html_title = project + ' documentation'


# Some settings in the html_context dictionary have to be repeated 
# in the sub projects for correct functioning (don't remove them)
html_context = {

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
    'repo_folder': '/docs/oracle/',

    # Change to an empty value if your GitHub repo doesn't have issues enabled.
    # This will disable the feedback button and the issue link in the footer.
    'github_issues': 'enabled',

    # Change to the folder that contains the documentation 
    # (usually "/" or "/docs/")
    "conf_py_path": '/oracle/',

    # Controls the existence of Previous / Next buttons at the bottom of pages
    # Valid options: none, prev, next, both
    # You can override the default setting on a page-by-page basis by specifying
    # it as file-wide metadata at the top of the file, see
    # https://www.sphinx-doc.org/en/master/usage/restructuredtext/field-lists.html
    'sequential_nav': "both"
}

# If your documentation is hosted on https://docs.ubuntu.com/,
#       uncomment and update as needed.

slug = 'docs/oracle'

html_baseurl = f"https://ubuntu.com/docs/oracle/"
ogp_site_url = f"https://ubuntu.com/docs/oracle/"

# Adds custom JavaScript files, located remotely or in 'html_static_path'.
html_js_files = ['js/bundle.js', 'js/overwrite_links_oracle.js']


############################
# sphinx-llm configuration #
############################

# This description is included in llms.txt to provide some initial context for your
# product docs.
# TODO: Add a description in the form "This is the documentation for <product name>,
# <first sentence of home page>".
llms_txt_description = textwrap.dedent(
    """\
    This is the documentation for Ubuntu images available on Oracle cloud.
    """
)

# The base URL for references built by sphinx-markdown-builder.
if os.environ.get("READTHEDOCS"):
    markdown_http_base = html_baseurl