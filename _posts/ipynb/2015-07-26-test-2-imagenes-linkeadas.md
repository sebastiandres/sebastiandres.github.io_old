---
layout: post
title: "Test-2-Imagenes-Linkeadas"
excerpt: 
categories: [tutorial, jekyll] 
tags: jekyll, ipynb, notebook
---
<div class="header">
Link al archivo ipython notebook original:
<a href="https://raw.githubusercontent.com/sebastiandres/sebastiandres.github.io/master/ipynb/Test-2-Imagenes-Linkeadas.ipynb">Test-2-Imagenes-Linkeadas.ipynb</a>.
</div>
<br>
En este post/notebook exploraremos cómo insertar imágenes ya existentes.

## 1 - Resumen

 * Es posible usar `<img alt='JPG' src='my\_url'>` para insertar imágenes en markdown. Deben tener extensión jpg, png o gif (incluso gifs animados). Redimensionan automáticamente menos que se use height/width.

 * Es posible usar `IPython.diplay.HTML(<img alt='JPG' src='my\_url'>)` para insertar imágenes desde el código. Deben tener extensión jpg o png. Los gif ahí si me funcionaron nuevamente.

## 2 - Imágenes desde markdown

### JPG
<img alt='JPG' src='https://raw.githubusercontent.com/sebastiandres/sebastiandres.github.io/master/images/test/colores.jpg'  height="200" width="200">

### PNG
<img alt='PNG' src='https://raw.githubusercontent.com/sebastiandres/sebastiandres.github.io/master/images/test/colores.png' height="200" width="200">

### GIF 
<img alt='GIF' src='https://raw.githubusercontent.com/sebastiandres/sebastiandres.github.io/master/images/test/colores.gif' height="200" width="200">

### GIF (animated)
<img alt='Animated GIF' src='https://raw.githubusercontent.com/sebastiandres/sebastiandres.github.io/master/images/test/pbjt.gif'>


## 3 - Imágenes con código, utilizando IPython.display.HTML()
Es posible rehacer los mismo que directamente con html.

<div class="in-prompt prompt-common">In [1]:</div>

<div class="input">
{% highlight python %}
from IPython.display import HTML
template = "<img src='{0}' height='200' width='200'>"
url = 'https://raw.githubusercontent.com/sebastiandres/sebastiandres.github.io/master/images/test/colores.jpg'
HTML(template.format(url))
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [1]:</div>

<div class='execute_results'>
<img src='https://raw.githubusercontent.com/sebastiandres/sebastiandres.github.io/master/images/test/colores.jpg' height='200' width='200'>
</div>

<div class="in-prompt prompt-common">In [2]:</div>

<div class="input">
{% highlight python %}
url = 'https://raw.githubusercontent.com/sebastiandres/sebastiandres.github.io/master/images/test/colores.png'
HTML(template.format(url))
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [2]:</div>

<div class='execute_results'>
<img src='https://raw.githubusercontent.com/sebastiandres/sebastiandres.github.io/master/images/test/colores.png' height='200' width='200'>
</div>

<div class="in-prompt prompt-common">In [3]:</div>

<div class="input">
{% highlight python %}
url = 'https://raw.githubusercontent.com/sebastiandres/sebastiandres.github.io/master/images/test/colores.gif'
HTML(template.format(url))
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [3]:</div>

<div class='execute_results'>
<img src='https://raw.githubusercontent.com/sebastiandres/sebastiandres.github.io/master/images/test/colores.gif' height='200' width='200'>
</div>

<div class="in-prompt prompt-common">In [5]:</div>

<div class="input">
{% highlight python %}
url = 'https://raw.githubusercontent.com/sebastiandres/sebastiandres.github.io/master/images/test/pbjt.gif'
HTML(template.format(url))
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [5]:</div>

<div class='execute_results'>
<img src='https://raw.githubusercontent.com/sebastiandres/sebastiandres.github.io/master/images/test/pbjt.gif' height='200' width='200'>
</div>
