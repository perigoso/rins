# Configuration file for the Sphinx documentation builder.

# -- Project information -----------------------------------------------------

project = "RINS"
copyright = "2023, RINS Contributors"
author = "RINS Contributors"

# -- General configuration ---------------------------------------------------

extensions = [
    "sphinx.ext.githubpages",
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.todo",
    "sphinx_autodoc_typehints",
]

intersphinx_mapping = {
    "python": ("https://docs.python.org/3/", None),
}

templates_path = ["_templates"]

exclude_patterns = [".github/*", "build/*", "LICENSE", "README.rst"]

# -- Options for HTML output -------------------------------------------------

html_theme = "furo"
html_title = "RINS"
html_static_path = ["_static"]

todo_include_todos = True

autoclass_content = "both"
