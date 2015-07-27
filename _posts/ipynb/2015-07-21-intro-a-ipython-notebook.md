---
layout: tutorial
title: Intro a ipython notebook
excerpt: Hace ya bastante tiempo que llevo usando ipython notebooks, pero no me había dado el tiempo de explorarlos con detalle.
search_omit: false
categories: tutorial, python, notebook
tags: ipython, notebook, jupyter
---

Hace ya bastante tiempo que llevo usando ipython notebooks, 
pero no me había dado el tiempo de explorarlos con detalle.

## ¿Que és un ipython notebook?

Vamos por partes:

 * Python es el lenguaje de programación.

 * IPython es un interprete interactivo para Python. Es como un "matlab para python".

 * IPython Notebook  (ahora proyecto jupyter) es un intérprete interactivo y enriquecido para Python.
 Tiene las ventajas de Python e IPython, además de permitir escribir texto en markdown y latex.
 Es como un "mathematica para python".

El formato de ipython notebook ha variado con el tiempo, pero actualmente se utiliza el formato v4. 
Una buena galería de ejemplos puede encontrarse en el siguiente link:
[galería de notebooks](https://github.com/ipython/ipython/wiki/A-gallery-of-interesting-IPython-Notebooks).

Github está soportando de manera nativa los ipython notebook. Si un archivo tiene extension ipynb, 
se mostrará "ejecutado", como en el siguiente link: [ejemplo de ipython notebook](https://github.com/sebastiandres/sebastiandres.github.io/blob/master/ipynb/OutputComplete.ipynb).

## ¿De que está compuesto un ipython notebook?
Un archivo ipython notebook tiene extensión ipynb, y es simplemente un archivo json.
Es posible abrir el archivo como un archivo de texto, como en el siguiente link: [contenido de un ipython notebook](https://raw.githubusercontent.com/sebastiandres/sebastiandres.github.io/master/ipynb/OutputComplete.ipynb).
De hecho, ¡podemos explorarlo directamente en python o mejor aún, en IPython!

{% highlight python %}
ipynb_file = "path/to/my_notebook.ipynb"
ipynb = json.load(open(ipynb_file, "r"))
print("File {0} loaded:".format(ipynb_file))
print("\nMetadata")
print(ipynb[u'metadata'])
print("\nnbformat")
print(ipynb[u'nbformat'])
print("\nnbformat_minor")
print(ipynb[u'nbformat_minor'])
cells = ipynb["cells"]
print("\nHas {0} cells\n".format(len(cells)))
for i, cell in enumerate(cells):
    print("Cell {0} has type {1}".format(i, cell["cell_type"]))
    print("\t keys: " + ", ".join(sorted(cell.keys())))
{% endhighlight %}

El código anterior es integrado en el siguiente [archivo ejecutable](https://github.com/sebastiandres/sebastiandres.github.io/blob/master/ipynb/debug_ipynb.py).

La estructura de un archivo ipynb es el siguiente

[![Foo](https://raw.githubusercontent.com/sebastiandres/sebastiandres.github.io/master/images/ipython/ipython_notebooktype_dict.png)](https://embed.coggle.it/diagram/55a538a177c48bb86bf0dea0/3ebb78e30f3581250d5d2036c4404ba85fd44bf6f79032e71b81619e0d72d13c)


Un archivo ipython (versión 4) es un diccionario con las siguientes llaves:

 * "nbformat" : Entero con la versión del archivo. En nuestro ejemplo, `4`.
 * "nbformat_minor" : Entero con la versión del archivo. En nuestro archivo de ejemplo `0`.
 * "metadata" : Diccionario con información sobre el lenguaje utilizando en notebook. En nuestro archivo de ejemplo 
`{
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.4.0"
  }
 }`
 * "cells" : Lista de las distintas celdas del notebook. Cada celda es en sí un nuevo diccionario (con muchísima información y que exploraremos en otro post).

En los siguientes posts exploraremos con mayor profundidad la estructura del notebook:

 * [Tipos de celdas](../cells-de-ipython-notebook)

 * [Convertir desde ipython notebook a markdown para jekyll](../de-ipynb-a-jekyll)

