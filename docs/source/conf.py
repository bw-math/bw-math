# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'bishop-walsh-ap-stats'
copyright = '2023, Grant Moore'
author = 'Grant Moore'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.githubpages',
    'sphinx.ext.imgmath'
]

templates_path = [
    '_templates'
]

exclude_patterns = []

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "sphinx_book_theme"

html_static_path = [
    'imgs',
    'css'
]

html_css_files = [
    'stylesheet.css',
]


imgmath_latex_preamble = r'''
    
'''