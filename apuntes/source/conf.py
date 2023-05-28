# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Apuntes AED'
copyright = '2023, Daniel Tossutti (chipaco)'
html_show_copyright = False
html_title = "♛ Apuntes AED 2023 by chipaco"
html_theme_options = {
    "announcement": "⚠ Prueba de concepto, sitio no terminado ⚠",
}
html_favicon = '_static/favicon.ico'
author = 'Daniel Tossutti (chipaco)'
release = '0.2'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx_inline_tabs', 'sphinx_copybutton', 'sphinx.ext.githubpages']

templates_path = ['_templates']
exclude_patterns = []

language = 'es'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_static_path = ['_static']
