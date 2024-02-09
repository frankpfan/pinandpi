import sys

sys.path.append(r'..\..\..\..\PynAndPi')

import pinandpi

# flake8: noqa

# Configuration file for the Sphinx documentation builder.
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------

project = 'PynAndPi'
copyright = '2023, Fan Pu'
author = '樊圃'
version = pinandpi.version
release = version

# -- General configuration ---------------------------------------------

default_role = 'code'

extensions = [
    'sphinx.ext.duration',
    'sphinx.ext.napoleon',
    'sphinx.ext.autodoc',
    'sphinx.ext.ifconfig',
#    'sphinx.ext.autosummary',
    'sphinx.ext.mathjax',
#    'sphinx.ext.intersphinx',
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

smartquote_action = 'De'  # dash and ellipsis

source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}

# -- Options for Extensions --------------------------------------------

napoleon_use_param = False
napoleon_use_rtype = False

autodoc_default_options = {
    'member-order': 'bysource',
}

myst_enable_extensions = [
    'dollarmath',
    'tasklist',
]

# -- Options for HTML output -------------------------------------------

html_theme = 'pydata_sphinx_theme'
html_static_path = ['_static']
html_logo = '_static/icon.png'

html_sidebars = {
    '**': ['search-field', 'globaltoc', 'relations'],
    'index': ['search-field'],
    'spec/about': ['relations'],
    'spec/update': ['relations'],
}

html_theme_options = {
    'show_nav_level': 2,
    'logo': {
        'image_light': 'icon.png',
        'image_dark': 'dark_icon.png',
    },
#   'body_min_width': '40vw',
}

# -- setup() for ext.ifconfig ------------------------------------------

def setup(app):
    app.add_config_value('indoc', True, 'env')
