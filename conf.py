import os
import sys
from datetime import date

project = "Théorie des Horloges Cosmologiques"
author = "Lionel Orcil"
copyright = f"{date.today().year}, {author}"

sys.path.insert(0, os.path.abspath(".."))

extensions = [
    "sphinx.ext.mathjax",
    "sphinx.ext.autosectionlabel",
    "sphinx.ext.todo",
    "sphinx.ext.intersphinx",
    "sphinx.ext.napoleon",
    "sphinxcontrib.bibtex",
]

bibtex_bibfiles = ["references.bib"]
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
}

mathjax3_config = {
    "tex": {
        "macros": {
            r"\dd":  r"{\,\mathrm{d}}",
            r"\vect": [r"{\boldsymbol{#1}}", 1],
            r"\avg":  [r"{\langle #1 \rangle}", 1],
        }
    }
}

html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
templates_path = ["_templates"]
html_show_sphinx = False
html_show_copyright = False


source_suffix = ".rst"
master_doc = "index"
language = "fr"
autosummary_generate = True
nitpicky = False

rst_prolog = r"""
.. |proj| replace:: Théorie des Horloges Cosmologiques
.. |LCDM| replace:: :math:`\Lambda\mathrm{CDM}`
"""

todo_include_todos = True
