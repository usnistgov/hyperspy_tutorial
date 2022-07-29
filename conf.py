# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))

# -- Project information -----------------------------------------------------

project = '2022 M&M Short Course X-16'
# copyright = '2021, Joshua Taillon'
author = 'HyperSpy Developers'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinx.ext.githubpages']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'furo'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_logo = "_static/hyperspy_mandm22_logo.png"
html_favicon = "_static/tutorial_favicon.ico"
html_title = project
html_show_copyright = False
html_show_sphinx = False
# html_add_permalinks = ''
html_show_sourcelink = False

html_sidebars = {'**': [
    "sidebar/scroll-start.html",
    "sidebar/brand.html",
    "sidebar/navigation.html",
    "sidebar/scroll-end.html",
] }
html_css_files = [
    'css/custom-styles.css',
]

# Theme options are theme-specific and customize the look and feel of a
# theme further.
html_theme_options = {
    "announcement": 'We look forward to seeing you on Sunday, July 31 in Room B114 for the short course!',
    "light_css_variables": {
        "color-brand-primary": "#008cba",
        "color-brand-content": "#008cba",
        "font-stack": '"Open Sans","Helvetica Neue",Helvetica,Arial,sans-serif',
        "font-stack--monospace": "Courier, monospace",
    },
}

# def setup(app):
#     app.add_css_file('css/custom-styles.css')  # may also be an URL
