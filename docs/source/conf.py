# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------

project = 'Energy Efficiency Standard for Building Specification'
copyright = '2021, Building Research Institute'
author = 'BRI'

# The full version, including alpha/beta/rc tags
release = '0.0.1'


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'ja'

# 通常のlatexだと日本語PDF化がうまくいかないため、latexエンジンをplatexに変更した。
latex_engine = 'platex'
latex_use_xindy = False

# latex は、章・節という概念があり、章はpart 節はsection
# 節は、1,2,3 の後に,Appendix があるため自動振番をキャンセルしたかったため、
# latex のプリアンブル部にセクションをカウントする深さを0（つまり番号をつけない）とした。
# 図・表に勝手に図1とか表1とかの番号がつくためキャンセルさせた。
latex_elements = {
    'preamble': '''
\\setcounter{secnumdepth}{0}
\\usepackage[labelformat=empty,labelsep=none]{caption}

'''
}

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']
