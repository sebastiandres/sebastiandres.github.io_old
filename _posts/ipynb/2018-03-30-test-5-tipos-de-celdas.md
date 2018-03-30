---
layout: post
title: "Test-5-Tipos-de-celdas"
excerpt: 
categories: [tutorial, jekyll] 
tags: jekyll, ipynb, notebook
---
<div class="header">
Link al archivo ipython notebook original:
<a href="https://raw.githubusercontent.com/sebastiandres/sebastiandres.github.io/master/ipynb/Test-5-Tipos-de-celdas.ipynb">Test-5-Tipos-de-celdas.ipynb</a>.
</div>
<br>
Este notebook de ipython contiene diversos tipos de elementos (código, imágenes, videos, html, etc.) 
para poder indicar el modo de uso y ver cómo se transforman utilizando el "plugin" para jekyll.

## 1 - Código Markdown con diversidad de tags
Con *italicas* y **negritas**, y listas

 * Uno

 * Dos

 * Tres

## 2 - Código Markdown con mathjax
Variables en latex \\( \alpha \\) y \\( \beta \\). 

También se pueden insertar fórmulas

\\[ 
F(b)-F(a) = \int\_{a}^{b} f(x)\, dx \approx \sum\_{k=1}^{N} \Delta x f(x\_{k})
 \\]


## 3 - Código de python

<div class="in-prompt prompt-common">In [3]:</div>

<div class="input">
{% highlight python %}
# Sin output
a = 2
b = 3.14
c = "string"
d = True
e = [1,2,3]
f = {"vaca":"cow", "perro":"dog"}
{% endhighlight %}
</div>

<div class="in-prompt prompt-common">In [4]:</div>

<div class="input">
{% highlight python %}
# Con output correcto
print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [4]:</div>

<div class="stream">
{% highlight text %}
2
3.14
string
True
[1, 2, 3]
{'perro': 'dog', 'vaca': 'cow'}

{% endhighlight %}
</div>

## 4 - Audio importado
Trabajar con sonidos es sencillo. Simplemente se importa la clase Audio.

<div class="in-prompt prompt-common">In [5]:</div>

<div class="input">
{% highlight python %}
from IPython.display import Audio
Audio(url="http://www.nch.com.au/acm/8k16bitpcm.wav")
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [5]:</div>

<div class='execute_results'>
&lt;IPython.lib.display.Audio object&gt;
</div>

## 5 - Video importado
Para mostrar videos de youtube, es posible utilizar la clase respectiva.

<div class="in-prompt prompt-common">In [6]:</div>

<div class="input">
{% highlight python %}
from IPython.display import YouTubeVideo
# a talk about IPython at Sage Days at U. Washington, Seattle.
# Video credit: William Stein.
YouTubeVideo('1j_HxD4iLn8')
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [6]:</div>

<div class='execute_results'>
&lt;IPython.lib.display.YouTubeVideo at 0x7fa7a9a00358&gt;
</div>

## 6 - HTML desde código

Es posible utilizar la clase `HTML` para mostrar cualquier tipo de HTML.

<div class="in-prompt prompt-common">In [7]:</div>

<div class="input">
{% highlight python %}
from IPython.display import HTML
s = """<table>
<tr>
<th>Fecha</th>
<th>Temperatura [°C]</th>
<th>Humedad [%]</th>
</tr>
<tr>
<td>Ayer</td>
<td>12</td>
<td>32</td>
</tr>
<tr>
<td>Hoy</td>
<td>20</td>
<td>20</td>
</tr>
<tr>
<td>Mañana</td>
<td>26</td>
<td>11</td>
</tr>
</table>"""
HTML(s)
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [7]:</div>

<div class='execute_results'>
&lt;IPython.core.display.HTML object&gt;
</div>

## 7 - Pandas

También podemos utilizar pandas sin demasiado problema.

<div class="in-prompt prompt-common">In [8]:</div>

<div class="input">
{% highlight python %}
import pandas
df = pandas.DataFrame({'impar' : [1., 3., 5.], 'par' : [2., 5., 7.]}, index=['a', 'b', 'c'])
print(df)
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [8]:</div>

<div class="stream">
{% highlight text %}
   impar  par
a      1    2
b      3    5
c      5    7

{% endhighlight %}
</div>

Y podemos utilizar la versión HTML

<div class="in-prompt prompt-common">In [9]:</div>

<div class="input">
{% highlight python %}
df
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [9]:</div>

<div class='execute_results'>
   impar  par
a      1    2
b      3    5
c      5    7
</div>

## 8- Sitios externos
Podemos incluir sitios externos.

<div class="in-prompt prompt-common">In [10]:</div>

<div class="input">
{% highlight python %}
from IPython.display import IFrame
IFrame('http://en.mobile.wikipedia.org/?useformat=mobile', width='100%', height=300)
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [10]:</div>

<div class='execute_results'>
&lt;IPython.lib.display.IFrame at 0x7fa7a9a2dda0&gt;
</div>

## 9 - Error
Los errores se indican también en ipython.

<div class="in-prompt prompt-common">In [11]:</div>

<div class="input">
{% highlight python %}
# Con output de error
print(unknown_variable)
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [11]:</div>

    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-11-22fdec8b207f> in <module>()
          1 # Con output de error
    ----> 2 print(unknown_variable)
    

    NameError: name 'unknown_variable' is not defined
