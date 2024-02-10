import sys

sys.path.append(r'..\..\..\..\..\..\PynAndPi')

import pinandpi

# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# flake8: noqa

# -- Project information -----------------------------------------------------

project = 'PynAndPi'
copyright = '2023, Fan Pu'
author = '樊圃'
version = pinandpi.version
release = version

# -- General configuration ---------------------------------------------------

root_doc = 'desc'

default_role = 'code'

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.ifconfig',
    'sphinx.ext.mathjax',
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

source_suffix = {
    '.md': 'markdown',
}

# -- Options for Extensions --------------------------------------------------

myst_enable_extensions = [
    'dollarmath',
    'tasklist',
]

# -- Options for HTML output -------------------------------------------------

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_logo = '_static/icon.png'

html_sidebars = {
    '**': ['searchbox', 'localtoc']
}

html_theme_options = {
    'body_min_width': '40vw',
}

# -- setup() for ext.ifconfig ------------------------------------------------

def setup(app):
    app.add_config_value('indoc', False, 'env')
