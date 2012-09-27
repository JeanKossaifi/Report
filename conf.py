# -*- coding: utf-8 -*-
#
# Internship report documentation build configuration file, created by
# sphinx-quickstart on Thu Sep 13 18:48:47 2012.
#
# This file is execfile()d with the current directory set to its containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

import sys, os

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#sys.path.insert(0, os.path.abspath('.'))

# -- General configuration -----------------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be extensions
# coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.doctest',  'sphinx.ext.mathjax', 'sphinx.ext.viewcode']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']
sys.path.append('/home/jean/FISTA/')

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
#source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'Internship report'
copyright = u'2012, Jean KOSSAIFI'

# The version info for the project you're documenting, acts as replacement for
# |version| and |release|, also used in various other places throughout the
# built documents.
#
# The short X.Y version.
version = '1'
# The full version, including alpha/beta/rc tags.
release = '1'

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#language = None

# There are two options for replacing |today|: either, you set today to some
# non-false value, then it is used:
#today = ''
# Else, today_fmt is used as the format for a strftime call.
#today_fmt = '%B %d, %Y'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
exclude_patterns = ['_build']

# The reST default role (used for this markup: `text`) to use for all documents.
#default_role = None

# If true, '()' will be appended to :func: etc. cross-reference text.
#add_function_parentheses = True

# If true, the current module name will be prepended to all description
# unit titles (such as .. function::).
#add_module_names = True

# If true, sectionauthor and moduleauthor directives will be shown in the
# output. They are ignored by default.
#show_authors = False

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# A list of ignored prefixes for module index sorting.
#modindex_common_prefix = []


# -- Options for HTML output ---------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#html_theme_options = {}

# Add any paths that contain custom themes here, relative to this directory.
#html_theme_path = []

# The name for this set of Sphinx documents.  If None, it defaults to
# "<project> v<release> documentation".
#html_title = None

# A shorter title for the navigation bar.  Default is the same as html_title.
#html_short_title = None

# The name of an image file (relative to this directory) to place at the top
# of the sidebar.
#html_logo = None

# The name of an image file (within the static path) to use as favicon of the
# docs.  This file should be a Windows icon file (.ico) being 16x16 or 32x32
# pixels large.
#html_favicon = None

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# If not '', a 'Last updated on:' timestamp is inserted at every page bottom,
# using the given strftime format.
#html_last_updated_fmt = '%b %d, %Y'

# If true, SmartyPants will be used to convert quotes and dashes to
# typographically correct entities.
#html_use_smartypants = True

# Custom sidebar templates, maps document names to template names.
#html_sidebars = {}

# Additional templates that should be rendered to pages, maps page names to
# template names.
#html_additional_pages = {}

# If false, no module index is generated.
#html_domain_indices = True

# If false, no index is generated.
#html_use_index = True

# If true, the index is split into individual pages for each letter.
#html_split_index = False

# If true, links to the reST sources are added to the pages.
#html_show_sourcelink = True

# If true, "Created using Sphinx" is shown in the HTML footer. Default is True.
#html_show_sphinx = True

# If true, "(C) Copyright ..." is shown in the HTML footer. Default is True.
#html_show_copyright = True

# If true, an OpenSearch description file will be output, and all pages will
# contain a <link> tag referring to it.  The value of this option must be the
# base URL from which the finished HTML is served.
#html_use_opensearch = ''

# This is the file name suffix for HTML files (e.g. ".xhtml").
#html_file_suffix = None

# Output file base name for HTML help builder.
htmlhelp_basename = 'Internshipreportdoc'


# -- Options for LaTeX output --------------------------------------------------

latex_elements = {
# The paper size ('letterpaper' or 'a4paper').
#'papersize': 'letterpaper',

# The font size ('10pt', '11pt' or '12pt').
#'pointsize': '10pt',

'listing': '\\usepackage{listings}',
'algorithm': ' \\usepackage{algorithm}',
'algotithmic': '\\usepackage{algorithmic}',
'math': '\\usepackage{amssymb}',

# Additional stuff for the LaTeX preamble.
'preamble': r"""
\usepackage{listings}
\usepackage{algorithm}
\usepackage{algorithmic}
\newcommand{\deblist}{\begin{lstlisting}[language=Python]}
\newcommand{\finlist}{\end{lstlisting}}



\usepackage{dsfont}
\usepackage{braket}
\usepackage{slashed}
\usepackage{yfonts}
\usepackage{mathrsfs}
\def\degrees{^\circ}
\def\d{{\rm d}}

\def\sign{\mathop{\mathrm{sign}}}
\def\L{{\mathcal L}}
\def\H{{\mathcal H}}
\def\M{{\mathcal M}}
\def\matrix{}
\def\F{{\bf F}}
\def\R{{\bf R}}
\def\J{{\bf J}}
\def\x{{\bf x}}
\def\y{{\bf y}}
\def\h{{\rm h}}
\def\a{{\rm a}}

%% MARIE 
%% Just to ease notation

%% Packages
\usepackage{amsmath,amsfonts,amsthm}
\usepackage{empheq}
\usepackage{enumerate}
\usepackage{url}
\usepackage{stmaryrd}
\usepackage{times}

%% Theorems, etc
\newtheorem{theorem}{Theorem}
\newtheorem{proposition}{Proposition}
\newtheorem{property}{Property}
\newtheorem{corollary}{Corollary}
\newtheorem{lemma}{Lemma}

\theoremstyle{definition}
\newtheorem{definition}{Definition}
\newtheorem{algo}{Algorithm}
\floatname{algorithm}{\small Algorithm}

\theoremstyle{remark}
\newtheorem{remark}{Remark}



%% Operators
\DeclareMathOperator*{\argmin}{argmin}
\DeclareMathOperator*{\argmax}{argmax}
\DeclareMathOperator*{\prox}{prox}
\DeclareMathOperator*{\diag}{diag}
%\newcommand{\prox}{\mathrm{prox}}


%% Bold (Greek) letters
\newcommand{\bfalpha}{\boldsymbol{\alpha}}
\newcommand{\bflambda}{\boldsymbol{\lambda}}
\newcommand{\bfsigma}{\boldsymbol{\sigma}}
\newcommand{\bfmu}{\boldsymbol{\mu}}
\newcommand{\bfw}{{\bf w}}
\newcommand{\bfx}{{\bf x}}
\newcommand{\bfz}{{\bf z}}
\newcommand{\bfu}{{\bf u}}
\newcommand{\bfv}{{\bf v}}
\newcommand{\bfk}{{\bf k}}
\newcommand{\bfone}{{\bf 1}}
\newcommand{\by}{{\bf y}}
\newcommand{\bx}{{\bf x}}
\newcommand{\bz}{{\bf z}}
\newcommand{\bu}{{\bf u}}
\newcommand{\bv}{{\bf v}}
\newcommand{\bd}{{\bf d}}
 


%% Misc commands
\newcommand{\labelset}{\mathcal{Y}}
\newcommand{\inputspace}{\mathcal{X}}
\newcommand{\inputset}{S}
\newcommand{\productspace}{\mathcal{Z}}
\newcommand{\realset}{\mathbb{R}}
\newcommand{\naturalset}{\mathbb{N}}
\newcommand{\RR}{\mathbb{R}}
\newcommand{\family}{\mathcal{F}}
\newcommand{\kernels}{\mathcal{K}}
\newcommand{\distribution}{D}
\renewcommand{\atop}[2]{\genfrac{}{}{0pt}{}{#1}{#2}}
\newcommand{\indicator}[1]{\mathbb{I}{(#1)}}
\newcommand{\proba}{\mathbb{P}}
\newcommand{\expectation}{\mathbb{E}}
\newcommand{\variance}{\mathbb{V}}
\newcommand{\alphaset}{\mathcal{A}}
\newcommand{\bubble}{{\bullet}}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% SMALL EQUATIONS

\usepackage{exscale}
\makeatletter
\newenvironment{equationsize}[1]{% 
  \skip@=\baselineskip 
  #1% 
  \baselineskip=\skip@ 
  \equation
}{\endequation \ignorespacesafterend} 
\makeatother

\makeatletter
\newenvironment{equationsize*}[1]{% 
  \skip@=\baselineskip 
  #1% 
  \baselineskip=\skip@ 
  \equation
}{\nonumber\endequation \ignorespacesafterend} 
\makeatother


\makeatletter
\newenvironment{alignsize}[1]{% 
  \skip@=\baselineskip 
  #1% 
  \baselineskip=\skip@ 
  \align
}{\endalign \ignorespacesafterend} 
\makeatother

\makeatletter
\newenvironment{alignsize*}[1]{% 
  \skip@=\baselineskip 
  #1% 
  \baselineskip=\skip@ 
  \start@align\@ne\st@rredtrue\m@ne
}{\endalign\ignorespacesafterend} 
\makeatother

%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

%% Comments
\newcommand{\mybracket}[1]{\textcolor{red}{[#1]}}%  \textcolor{red}{]}}
\newcommand{\lr}[1]{{\bf (LR} #1 {\bf RL)}}
\newcommand{\ms}[1]{{\bf (MS} #1 {\bf SM)}}
\newcommand{\mk}[1]{{\bf (MK} #1 {\bf KM)}}
"""
#\newcommand{\bfx}{\mbox{\boldmath $x$}}
#\newcommand{\bfy}{\mbox{\boldmath $y$}}
#\newcommand{\bfz}{\mbox{\boldmath $z$}}
#\newcommand{\bfv}{\mbox{\boldmath $v$}}
#\newcommand{\bfu}{\mbox{\boldmath $u$}}
#\newcommand{\bfF}{\mbox{\boldmath $F$}}
#\newcommand{\bfJ}{\mbox{\boldmath $J$}}
#\newcommand{\bfU}{\mbox{\boldmath $U$}}
#\newcommand{\bfY}{\mbox{\boldmath $Y$}}
#\newcommand{\bfR}{\mbox{\boldmath $R$}}
#\newcommand{\bfg}{\mbox{\boldmath $g$}}
#\newcommand{\bfc}{\mbox{\boldmath $c$}}
#\newcommand{\bfxi}{\mbox{\boldmath $\xi$}}
#
#
#%\def\back{\!\!\!\!\!\!\!\!\!\!}
#\def\back{}
#\def\col#1#2{\left(\matrix{#1#2}\right)}
#\def\row#1#2{\left(\matrix{#1#2}\right)}
#\def\mat#1{\begin{pmatrix}#1\end{pmatrix}}
#\def\matd#1#2{\left(\matrix{#1\back0\cr0\back#2}\right)}
#\def\p#1#2{{\partial#1\over\partial#2}}
#\def\cg#1#2#3#4#5#6{({#1},\,{#2},\,{#3},\,{#4}\,|\,{#5},\,{#6})}
#\def\half{{\textstyle{1\over2}}}
#\def\jsym#1#2#3#4#5#6{\left\{\matrix{
#{#1}{#2}{#3}
#{#4}{#5}{#6}
#}\right\}}
#\def\diag{\hbox{diag}}
#
#\font\dsrom=dsrom10
#\def\one{\hbox{\dsrom 1}}
#
#\def\res{\mathop{\mathrm{Res}}}
#
#\def\mathnot#1{\text{"$#1$"}}
#
#
#%See Character Table for cmmib10:
#%http://www.math.union.edu/~dpvc/jsmath/download/extra-fonts/cmmib10/cmmib10.html
#\font\mib=cmmib10
#\def\balpha{\hbox{\mib\char"0B}}
#\def\bbeta{\hbox{\mib\char"0C}}
#\def\bgamma{\hbox{\mib\char"0D}}
#\def\bdelta{\hbox{\mib\char"0E}}
#\def\bepsilon{\hbox{\mib\char"0F}}
#\def\bzeta{\hbox{\mib\char"10}}
#\def\boldeta{\hbox{\mib\char"11}}
#\def\btheta{\hbox{\mib\char"12}}
#\def\biota{\hbox{\mib\char"13}}
#\def\bkappa{\hbox{\mib\char"14}}
#\def\blambda{\hbox{\mib\char"15}}
#\def\bmu{\hbox{\mib\char"16}}
#\def\bnu{\hbox{\mib\char"17}}
#\def\bxi{\hbox{\mib\char"18}}
#\def\bpi{\hbox{\mib\char"19}}
#\def\brho{\hbox{\mib\char"1A}}
#\def\bsigma{\hbox{\mib\char"1B}}
#\def\btau{\hbox{\mib\char"1C}}
#\def\bupsilon{\hbox{\mib\char"1D}}
#\def\bphi{\hbox{\mib\char"1E}}
#\def\bchi{\hbox{\mib\char"1F}}
#\def\bpsi{\hbox{\mib\char"20}}
#\def\bomega{\hbox{\mib\char"21}}
#
#\def\bvarepsilon{\hbox{\mib\char"22}}
#\def\bvartheta{\hbox{\mib\char"23}}
#\def\bvarpi{\hbox{\mib\char"24}}
#\def\bvarrho{\hbox{\mib\char"25}}
#\def\bvarphi{\hbox{\mib\char"27}}
#
#%how to use:
#%$$\alpha\balpha$$
#%$$\beta\bbeta$$
#%$$\gamma\bgamma$$
#%$$\delta\bdelta$$
#%$$\epsilon\bepsilon$$
#%$$\zeta\bzeta$$
#%$$\eta\boldeta$$
#%$$\theta\btheta$$
#%$$\iota\biota$$
#%$$\kappa\bkappa$$
#%$$\lambda\blambda$$
#%$$\mu\bmu$$
#%$$\nu\bnu$$
#%$$\xi\bxi$$
#%$$\pi\bpi$$
#%$$\rho\brho$$
#%$$\sigma\bsigma$$
#%$$\tau\btau$$
#%$$\upsilon\bupsilon$$
#%$$\phi\bphi$$
#%$$\chi\bchi$$
#%$$\psi\bpsi$$
#%$$\omega\bomega$$
#%
#%$$\varepsilon\bvarepsilon$$
#%$$\vartheta\bvartheta$$
#%$$\varpi\bvarpi$$
#%$$\varrho\bvarrho$$
#%$$\varphi\bvarphi$$
#
#%small font
#\font\mibsmall=cmmib7
#\def\bsigmasmall{\hbox{\mibsmall\char"1B}}
#
#\def\Tr{\hbox{Tr}\,}
#\def\Arg{\hbox{Arg}}
#\def\atan{\hbox{atan}}
#"""
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass [howto/manual]).
latex_documents = [
  ('index', 'Internship_report.tex', u'Internship report',
   u'Jean KOSSAIFI', 'manual'),
]

# The name of an image file (relative to this directory) to place at the top of
# the title page.
latex_logo = 'logo_ENSIIE.png'

# For "manual" documents, if this is true, then toplevel headings are parts,
# not chapters.
#latex_use_parts = False

# If true, show page references after internal links.
#latex_show_pagerefs = False

# If true, show URL addresses after external links.
#latex_show_urls = False

# Documents to append as an appendix to all manuals.
#latex_appendices = []

# If false, no module index is generated.
#latex_domain_indices = True


# -- Options for manual page output --------------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    ('index', 'internshipreport', u'Internship report Documentation',
     [u'Jean KOSSAIFI'], 1)
]

# If true, show URL addresses after external links.
#man_show_urls = False


# -- Options for Texinfo output ------------------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
  ('index', 'Internshipreport', u'Internship report Documentation',
   u'Jean KOSSAIFI', 'Internshipreport', 'One line description of project.',
   'Miscellaneous'),
]

# Documents to append as an appendix to all manuals.
#texinfo_appendices = []

# If false, no module index is generated.
#texinfo_domain_indices = True

# How to display URL addresses: 'footnote', 'no', or 'inline'.
#texinfo_show_urls = 'footnote'
