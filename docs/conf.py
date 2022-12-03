"""Sphinx configuration."""
project = "Cookie Test"
author = "Soshi Mizutani"
copyright = "2022, Soshi Mizutani"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
