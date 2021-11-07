# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
from sphinx.highlighting import PygmentsBridge
from pygments.formatters.latex import LatexFormatter

class CustomLatexFormatter(LatexFormatter):
    def __init__(self, **options):
        super(CustomLatexFormatter, self).__init__(**options)
        self.verboptions = r"formatcom=\footnotesize"

PygmentsBridge.latex_formatter = CustomLatexFormatter
# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
# import os
# import sys
# sys.path.insert(0, os.path.abspath('.'))


# -- Project information -----------------------------------------------------
master_doc = 'index'

project = 'Estudio del comportamiento de micro-ROS. Un análisis teórico y práctico'
copyright = '2021, Carlos Castillo Martínez'
author = 'Carlos Castillo Martínez'

# The full version, including alpha/beta/rc tags
release = ''


# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = ['sphinxcontrib.bibtex']

bibtex_bibfiles = ['refs.bib']

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'es'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# -- Options for LaTeX output ---------------------------------------------

latex_custom = r'''
\usepackage{pdfpages}
\usepackage{afterpage}
\newcommand\blankpage{%
    \null
    \thispagestyle{empty}%
    \addtocounter{page}{-1}%
    \newpage}
\makeatletter

   \fancypagestyle{normal}{
    \fancyhf{}
    \fancyfoot[RO]{{\py@HeaderFamily \thepage}}
    \fancyfoot[LO]{{\py@HeaderFamily Carlos Castillo Martínez}}
    \fancyhead[RO]{{\py@HeaderFamily \@title\sphinxheadercomma\py@release}}
    \if@twoside
     \fancyfoot[LE]{{\py@HeaderFamily\thepage}}
     \fancyfoot[RE]{{\py@HeaderFamily Escuela Técnica Superior de Ingenieros Industriales (UPM)}}
     \fancyhead[LE]{{\py@HeaderFamily \nouppercase{\leftmark}}}
    \fi
    \renewcommand{\headrulewidth}{0.4pt}
    \renewcommand{\footrulewidth}{0.4pt}
    % define chaptermark with \@chappos when \@chappos is available for Japanese
    \ltx@ifundefined{@chappos}{}
      {\def\chaptermark##1{\markboth{\@chapapp\space\thechapter\space\@chappos\space ##1}{}}}

    }
\makeatother
'''
latex_maketitle = r'''
\newpage
\thispagestyle{empty}
\includepdf{Portada_TFG_CCM2.pdf}

\newpage
\thispagestyle{empty}


\begin{flushright} % Se alinea el texto en el lado derecho de la página.
\vspace*{5cm} % Se añade un espacio vertical de 5cm para situar la cita en ~1/3 de la página.

\textit{“If I have seen further it is by standing on the shoulders of Giants”} 

\medskip % Salto a la línea de tamaño medio (existen \smallskip, \medskip y \bigskip)
- Sir Isaac Newton

\end{flushright}

\afterpage{\blankpage} % Se añade una página en blanco después de la cita.

\pagenumbering{roman}

% Se comienza una página nueva con formato plano (sin encabezado/pie de página pero con número de página):
\newpage

\section*{Agradecimientos} % Se añade un asterisco a \section para que el título no esté numerado.
%\addcontentsline{toc}{chapter}{Agradecimientos} % Al utilizar \section* se ha de añadir manualmente el apartado al índice (Table Of Contents, TOC).

En primer lugar quería agradecer a mi familia el haber sido un apoyo incondicional para mí en todo momento por celebrar mis éxitos como si de los suyos se tratara y por evitar que me hundiese en los momentos más difíciles.

Le doy las gracias a mi tutor, Ricardo Sanz, por haberme brindado la oportunidad de realizar este proyecto y aprender de él. También quería agradecer a la doctoranda Esther Aguado su disponibilidad y ayuda durante todo el trabajo, fundamentales para el desarrollo del mismo. 

Por último, quisiera recordar a todos mis amigos y compañeros que me han acompañado en este largo viaje los últimos años. Sin ellos hubiera sido imposible llegar hasta este punto.

Quiero dedicar este trabajo especialmente a mis padres, por ser mis principales referentes en todo aquello que quiero llegar a ser en mi vida, tanto personal como profesionalmente.

\afterpage{\blankpage}

\newpage
\section*{Resumen Ejecutivo} % Se añade un asterisco a \section para que el título no esté numerado.
\markright{Resumen Ejecutivo} % Al utilizar \section* se ha de añadir manualmente el título del apartado al encabezado.

\addcontentsline{toc}{chapter}{Resumen Ejecutivo} % Al utilizar \section* se ha de añadir manualmente el apartado al índice (Table Of Contents, TOC).

Durante los últimos años, la tecnología ha ido creciendo a una velocidad exponencial en relación a etapas anteriores. Este hecho se traduce en la irrupción de la ya actual cuarta revolución industrial, también denominada industria 4.0.

Este fenómeno viene marcado por la aparición de nuevas tecnologías que están relacionadas con el tratamiento masivo de datos o “big data” y el Internet de las cosas (IoT).

Este último concepto se refiere a una interconexión digital de objetos cotidianos con Internet, lo cual genera un ecosistema de dispositivos inteligentes habilitados para recoger, enviar y actuar sobre los datos que adquieren de sus entornos.

En este sentido, la robótica constituye un sector fundamental en esta novedosa tecnología, que aprovecha y potencia las posibilidades que los robots ofrecen. Asimismo, los sistemas embebidos juegan un papel clave en la creación de estos ecosistemas, ya que permiten implementarse de manera sencilla en una gran cantidad de objetos cotidianos a un reducido coste, manteniendo unas prestaciones más que suficientes para las tareas que van a acometer.

Esto ha producido que el mundo de la robótica acelere su desarrollo a pasos agigantados en la última década, tanto a nivel de hardware como de software.

ROS es una tecnología pionera en el control de robots en tiempo real. Su crecimiento durante estos años está permitiendo a día de hoy la monitorización de muchos robots de una manera muy efectiva. Actualmente la versión en uso es ROS2. Sin embargo, recientemente se ha creado micro-ROS, una tecnología que acerca el mundo de ROS a los microcontroladores.

En este trabajo se va a estudiar el comportamiento de esta tecnología. En una primera etapa se analizará la base del funcionamiento de las comunicaciones en tiempo real. En este apartado se incluirán las restricciones que dichos sistemas requieren y las ventajas que pueden aportar.

Seguidamente se realizará un estudio teórico del funcionamiento de ROS. Esto incluye la base de programación que soporta ROS2, las distintas partes que forman la arquitectura del software y las herramientas que se utilizan para lograr integrar las funciones de ROS2 en microcontroladores.

Finalmente se plantearán una serie de análisis que simulen aplicaciones que se puedan dar en la vida real y se medirá el comportamiento que presenta micro-ROS instalado en una placa ESP-32.

Todo esto se realizará de manera autónoma sin ninguna experiencia previa en el sector, por lo que el trabajo resultante servirá también como guía de iniciación para la introducción a la programación del sistema operativo de robots.\\

\textbf{Codigos Unesco:}

120317 Informática

120323 Lenguajes de Programación

120324 Teoría de la Programación

120326 Simulación

'''
latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
     'papersize': 'a4paper',

    # The font size ('10pt', '11pt' or '12pt').
    #
     'pointsize': '11pt',

    # Additional stuff for the LaTeX preamble.
    #
     'preamble': latex_custom,
     'releasename': '',

    # Latex figure (float) alignment
    'maketitle': latex_maketitle
    #
}

latex_logo = 'Fotos/ets_industriales.png'

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title,
#  author, documentclass [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'tfg_ccm.tex', project,
     author, 'manual'),
]

