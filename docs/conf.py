# -*- coding: utf-8 -*-
#
# Configuration file for the Sphinx documentation builder.
#
# This file does only contain a selection of the most common options. For a
# full list see the documentation:
# http://www.sphinx-doc.org/en/master/config

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.

import sphinx_rtd_theme

import deeppavlov

# -- Project information -----------------------------------------------------

project = 'DeepPavlov'
copyright = '2018, ' + deeppavlov.__author__
author = deeppavlov.__author__

# The short X.Y version
version = deeppavlov.__version__
# The full version, including alpha/beta/rc tags
release = version


# -- General configuration ---------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.doctest',
    'sphinx.ext.intersphinx',
    'sphinx.ext.todo',
    'sphinx.ext.coverage',
    'sphinx.ext.napoleon',
    'sphinx.ext.viewcode',
    'sphinx.ext.mathjax',
    'sphinx.ext.extlinks',
    'nbsphinx',
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = None

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', '**.ipynb_checkpoints']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
html_theme_options = {
    'collapse_navigation': False,
    'display_version': True,
    'logo_only': True,
}

html_logo = '_static/deeppavlov.png'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

html_context = {
    'css_files': [
        'https://media.readthedocs.org/css/sphinx_rtd_theme.css',
        'https://media.readthedocs.org/css/readthedocs-doc-embed.css',
        '_static/deeppavlov.css'
    ]
}

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}


# -- Options for HTMLHelp output ---------------------------------------------

# Output file base name for HTML help builder.

htmlhelp_basename = f'{project}-Docs'


# -- Options for LaTeX output ------------------------------------------------

latex_engine = 'xelatex'

latex_elements = {

    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',

    'extraclassoptions': 'openany,oneside',

    'fncychap': r'\usepackage[Sonny]{fncychap}'

}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, f'{project}.tex', f'{project} Documentation',
     author, 'manual'),
]


# -- Options for manual page output ------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, project.lower(), f'{project} Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, project, f'{project} Documentation',
     author, project, deeppavlov.__description__,
     str(deeppavlov.__keywords__)),
]


# -- Extension configuration -------------------------------------------------

autodoc_mock_imports = ['aiml', 'bert_dp', 'bs4', 'faiss', 'fastText', 'fasttext', 'gensim', 'hdt', 'kenlm', 'librosa',
                        'lxml', 'nemo', 'nemo_asr', 'nemo_tts', 'nltk', 'rapidfuzz', 'rasa', 'russian_tagsets',
                        'sacremoses', 'sortedcontainers', 'spacy', 'tensorflow', 'tensorflow_hub', 'torch',
                        'transformers', 'udapi', 'whapi', 'xeger']

extlinks = {
    'config': (f'https://github.com/deepmipt/DeepPavlov/blob/{release}/deeppavlov/configs/%s', None)
}

# -- Options for intersphinx extension ---------------------------------------

# Configuration for intersphinx
intersphinx_mapping = {
    'python': ('https://docs.python.org/3.6', None),
    'scipy': ('https://docs.scipy.org/doc/scipy/reference', None)
}

# -- Options for todo extension ----------------------------------------------

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False
