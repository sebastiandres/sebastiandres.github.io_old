---
layout: post
title: "OutputComplete"
categories: [tutorial, jekyll] 
tags: jekyll, ipynb, notebook
---

Archivo original [OutputComplete.ipynb | path]. <br>
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

<div style="color:#1212FF">In [11]:</div>

{% highlight python %}
# Sin output
a = 2
b = 3
{% endhighlight %}

<div style="color:#1212FF">In [12]:</div>

{% highlight python %}
# Con output correcto
print(a)
print(b)
{% endhighlight %}

<div style="color:#FF1212">Out [12]:</div>

{% highlight python %}
2
3

{% endhighlight %}

## 6 - Audio importado
Trabajar con sonidos es sencillo. Simplemente se importa la clase Audio.

<div style="color:#1212FF">In [13]:</div>

{% highlight python %}
from IPython.display import Audio
Audio(url="http://www.nch.com.au/acm/8k16bitpcm.wav")
{% endhighlight %}

<div style="color:#FF1212">Out [13]:</div>


<div align='center'>
                <audio controls="controls" >
                    <source src="http://www.nch.com.au/acm/8k16bitpcm.wav" type="audio/x-wav" />
                    Your browser does not support the audio element.
                </audio>
              </div>



## 7 - Video importado
Para mostrar videos de youtube, es posible utilizar la clase respectiva.

<div style="color:#1212FF">In [14]:</div>

{% highlight python %}
from IPython.display import YouTubeVideo
# a talk about IPython at Sage Days at U. Washington, Seattle.
# Video credit: William Stein.
YouTubeVideo('1j_HxD4iLn8')
{% endhighlight %}

<div style="color:#FF1212">Out [14]:</div>


<div align='center'>
        <iframe
            width="400"
            height="300"
            src="https://www.youtube.com/embed/1j_HxD4iLn8"
            frameborder="0"
            allowfullscreen
        ></iframe>
        </div>



## 9 - HTML desde código

Es posible utilizar la clase `HTML` para mostrar cualquier tipo de HTML.

<div style="color:#1212FF">In [21]:</div>

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

<div style="color:#FF1212">Out [21]:</div>


<div align='center'><table>
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
</table></div>



## 10 - Pandas

También podemos utilizar pandas sin demasiado problema.

<div style="color:#1212FF">In [16]:</div>

{% highlight python %}
import pandas
df = pandas.DataFrame({'impar' : [1., 3., 5.], 'par' : [2., 5., 7.]}, index=['a', 'b', 'c'])
print(df)
{% endhighlight %}

<div style="color:#FF1212">Out [16]:</div>

{% highlight python %}
   impar  par
a      1    2
b      3    5
c      5    7

{% endhighlight %}

Y podemos utilizar la versión HTML

<div style="color:#1212FF">In [17]:</div>

{% highlight python %}
df
{% endhighlight %}

<div style="color:#FF1212">Out [17]:</div>


<div align='center'><div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>impar</th>
      <th>par</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>a</th>
      <td>1</td>
      <td>2</td>
    </tr>
    <tr>
      <th>b</th>
      <td>3</td>
      <td>5</td>
    </tr>
    <tr>
      <th>c</th>
      <td>5</td>
      <td>7</td>
    </tr>
  </tbody>
</table>
</div></div>



## 11- Sitios externos
Podemos incluir sitios externos.

<div style="color:#1212FF">In [18]:</div>

{% highlight python %}
from IPython.display import IFrame
IFrame('http://en.mobile.wikipedia.org/?useformat=mobile', width='100%', height=300)
{% endhighlight %}

<div style="color:#FF1212">Out [18]:</div>


<div align='center'>
        <iframe
            width="100%"
            height="300"
            src="http://en.mobile.wikipedia.org/?useformat=mobile"
            frameborder="0"
            allowfullscreen
        ></iframe>
        </div>



## 12 - Error
Los errores se indican también en ipython.

<div style="color:#1212FF">In [19]:</div>

{% highlight python %}
# Con output de error
print(unknown_variable)
{% endhighlight %}

<div style="color:#FF1212">Out [19]:</div>

    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-19-22fdec8b207f> in <module>()
          1 # Con output de error
    ----> 2 print(unknown_variable)
    

    NameError: name 'unknown_variable' is not defined
