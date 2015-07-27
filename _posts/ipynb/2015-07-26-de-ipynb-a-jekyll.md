---
layout: tutorial
title: De ipynb a jekyll
search_omit: false
categories: tutorial, python, notebook
tags: ipython, notebook, jupyter
---

Desde que comencé con el blog en jekyll quería integrar el posteo con ipython notebooks.
Inspirándome en otros blogs, creé 2 archivos: [`ipynb_v4_to_jekyll.py`](https://github.com/sebastiandres/sebastiandres.github.io/blob/master/ipynb_v4_to_jekyll.py) y [`ipynb_v4_to_jekyll.tpl`](https://github.com/sebastiandres/sebastiandres.github.io/blob/master/ipynb_v4_to_jekyll.tpl).

Para convertir un ipython notebook, simplemente debe hacerse:
{% highlight text %} 
ipython nbconvert ipython nbconvert --config ipynb_v4_to_jekyll.py path/to/Mi_Notebook.ipynb 
{% endhighlight %}

Se creará automáticamente un archivo en `path/to/` en markdown con nombre `yyyy-mm-dd-mi-notebook.md`. 
Solo será necesario moverlo a la carpeta `_post` y hacer ediciones menores (el excerpt, por ejemplo). 

Actualmente está funcionando para todos los ejemplos que he tratado:

 * [Imagenes creadas](../test-1-imagenes-creadas)
 * [Imagenes linkeadas](../test-2-imagenes-linkeadas)
 * [Fórmulas matemáticas](../test-3-formulas)
 * [Errores](../test-4-errores)
 * [Tipos de celdas](../test-5-tipos-de-celdas)

Al realizarlo he tomado las siguientes consideraciones:
 * Las imágenes que no son linkeadas se incluyen como código en el contenido. A pesar que ipython notebook genera imágenes, prefiero incluirlas directamente para mover únicamente el archivo markdown generado y no preocuparme de nada más.
 * Conversión de fórmulas desde el formato en ipython notebook (latex puro) a mathjax.


[Blog de mobeets sobre jekyll-ipython-markdown](https://github.com/mobeets/jekyll-ipython-markdown)

[Documentación de nbconvert](http://nbconvert.readthedocs.org/en/latest/customizing.html)
