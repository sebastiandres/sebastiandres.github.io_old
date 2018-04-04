---
layout: post
title: "Test-9-Todos-los-test"
excerpt:
categories: [tutorial, jekyll]
tags: jekyll, ipynb, notebook
---
<div class="header">
Link al archivo ipython notebook original:
<a href="https://github.com/sebastiandres/sebastiandres.github.io/blob/master/ipynb/Test-9-Todos-los-test.ipynb" download>Test-9-Todos-los-test.ipynb</a>.
|
<a href="https://raw.githubusercontent.com/sebastiandres/sebastiandres.github.io/master/ipynb/Test-9-Todos-los-test.ipynb" download>Descargar</a>.
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

<div class="in-prompt prompt-common">In [1]:</div>

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

<div class="in-prompt prompt-common">In [2]:</div>

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

<div class="output-prompt prompt-common">Out [2]:</div>

<div class="stream">
{% highlight text %}
2
3.14
string
True
[1, 2, 3]
{'vaca': 'cow', 'perro': 'dog'}

{% endhighlight %}
</div>

## 4 - Audio importado
Trabajar con sonidos es sencillo. Simplemente se importa la clase Audio.

<div class="in-prompt prompt-common">In [3]:</div>

<div class="input">
{% highlight python %}
from IPython.display import Audio
Audio(url="http://www.nch.com.au/acm/8k16bitpcm.wav")
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [3]:</div>

<div class='execute_results'>

                <audio controls="controls" >
                    <source src="http://www.nch.com.au/acm/8k16bitpcm.wav" type="audio/x-wav" />
                    Your browser does not support the audio element.
                </audio>
</div>

## 5 - Video importado
Para mostrar videos de youtube, es posible utilizar la clase respectiva.

<div class="in-prompt prompt-common">In [4]:</div>

<div class="input">
{% highlight python %}
from IPython.display import YouTubeVideo
# a talk about IPython at Sage Days at U. Washington, Seattle.
# Video credit: William Stein.
YouTubeVideo('1j_HxD4iLn8')
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [4]:</div>

<div class='execute_results'>

        <iframe
            width="400"
            height="300"
            src="https://www.youtube.com/embed/1j_HxD4iLn8"
            frameborder="0"
            allowfullscreen
        ></iframe>
</div>

## 6 - HTML desde código

Es posible utilizar la clase `HTML` para mostrar cualquier tipo de HTML.

<div class="in-prompt prompt-common">In [5]:</div>

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

<div class="output-prompt prompt-common">Out [5]:</div>

<div class='execute_results'>
<table>
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
</table>
</div>

## 7 - Pandas

También podemos utilizar pandas sin demasiado problema.

<div class="in-prompt prompt-common">In [6]:</div>

<div class="input">
{% highlight python %}
import pandas
df = pandas.DataFrame({'impar' : [1., 3., 5.], 'par' : [2., 5., 7.]}, index=['a', 'b', 'c'])
print(df)
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [6]:</div>

<div class="stream">
{% highlight text %}
   impar  par
a    1.0  2.0
b    3.0  5.0
c    5.0  7.0

{% endhighlight %}
</div>

Y podemos utilizar la versión HTML

<div class="in-prompt prompt-common">In [7]:</div>

<div class="input">
{% highlight python %}
df
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [7]:</div>

<div class='execute_results'>
<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
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
      <td>1.0</td>
      <td>2.0</td>
    </tr>
    <tr>
      <th>b</th>
      <td>3.0</td>
      <td>5.0</td>
    </tr>
    <tr>
      <th>c</th>
      <td>5.0</td>
      <td>7.0</td>
    </tr>
  </tbody>
</table>
</div>
</div>

## 8- Sitios externos
Podemos incluir sitios externos.

<div class="in-prompt prompt-common">In [8]:</div>

<div class="input">
{% highlight python %}
from IPython.display import IFrame
IFrame('http://www.wikipedia.org/', width='100%', height=300)
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [8]:</div>

<div class='execute_results'>

        <iframe
            width="100%"
            height="300"
            src="http://www.wikipedia.org/"
            frameborder="0"
            allowfullscreen
        ></iframe>
</div>

## 9 - Error
Los errores se indican también en ipython.

<div class="in-prompt prompt-common">In [9]:</div>

<div class="input">
{% highlight python %}
# Con output de error
print(unknown_variable)
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [9]:</div>

    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-9-a572254bf6f2> in <module>()
          1 # Con output de error
    ----> 2 print(unknown_variable)
    

    NameError: name 'unknown_variable' is not defined

## 10- Grafico Altair
Ejemplo de visualizacion en Altair.

<div class="in-prompt prompt-common">In [11]:</div>

<div class="input">
{% highlight python %}
import altair as alt
import pandas as pd
import numpy as np

np.random.seed(42)
data = pd.DataFrame(np.cumsum(np.random.randn(100, 3), 0).round(2),
                    columns=['A', 'B', 'C'], index=pd.RangeIndex(100, name='x'))
data = data.reset_index().melt('x', var_name='category', value_name='y')

# Create a selection that chooses the nearest point & selects based on x-value
nearest = alt.selection(type='single', nearest=True, on='mouseover',
                        fields=['x'], empty='none')

# The basic line
line = alt.Chart().mark_line(interpolate='basis').encode(
    x='x:Q',
    y='y:Q',
    color='category:N'
)

# Transparent selectors across the chart. This is what tells us
# the x-value of the cursor
selectors = alt.Chart().mark_point().encode(
    x='x:Q',
    opacity=alt.value(0),
).properties(
    selection=nearest
)

# Draw points on the line, and highlight based on selection
points = line.mark_point().encode(
    opacity=alt.condition(nearest, alt.value(1), alt.value(0))
)

# Draw text labels near the points, and highlight based on selection
text = line.mark_text(align='left', dx=5, dy=-5).encode(
    text=alt.condition(nearest, 'y:Q', alt.value(' '))
)

# Draw a rule at the location of the selection
rules = alt.Chart().mark_rule(color='gray').encode(
    x='x:Q',
).transform_filter(
    nearest.ref()
)

# Put the five layers into a chart and bind the data
chart = alt.layer(line, selectors, points, rules, text,
                  data=data, width=600, height=300)
chart.interactive()
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [11]:</div>

<div class='execute_results'>
  <!-- Container for the visualization -->
  <div id="viz_11"></div>
  <script>
  var vlSpec_11 = 
{
    "$schema": "https://vega.github.io/schema/vega-lite/v2.json",
    "config": {
        "view": {
            "height": 300,
            "width": 400
        }
    },
    "data": {
        "values": [
            {
                "category": "A",
                "x": 0,
                "y": 0.5
            },
            {
                "category": "A",
                "x": 1,
                "y": 2.02
            },
            {
                "category": "A",
                "x": 2,
                "y": 3.6
            },
            {
                "category": "A",
                "x": 3,
                "y": 4.14
            },
            {
                "category": "A",
                "x": 4,
                "y": 4.38
            },
            {
                "category": "A",
                "x": 5,
                "y": 3.82
            },
            {
                "category": "A",
                "x": 6,
                "y": 2.91
            },
            {
                "category": "A",
                "x": 7,
                "y": 2.69
            },
            {
                "category": "A",
                "x": 8,
                "y": 2.14
            },
            {
                "category": "A",
                "x": 9,
                "y": 2.52
            },
            {
                "category": "A",
                "x": 10,
                "y": 1.92
            },
            {
                "category": "A",
                "x": 11,
                "y": 0.86
            },
            {
                "category": "A",
                "x": 12,
                "y": 1.07
            },
            {
                "category": "A",
                "x": 13,
                "y": 1.27
            },
            {
                "category": "A",
                "x": 14,
                "y": 1.15
            },
            {
                "category": "A",
                "x": 15,
                "y": 0.43
            },
            {
                "category": "A",
                "x": 16,
                "y": 0.77
            },
            {
                "category": "A",
                "x": 17,
                "y": 0.39
            },
            {
                "category": "A",
                "x": 18,
                "y": 1.42
            },
            {
                "category": "A",
                "x": 19,
                "y": 1.11
            },
            {
                "category": "A",
                "x": 20,
                "y": 0.63
            },
            {
                "category": "A",
                "x": 21,
                "y": -0.57
            },
            {
                "category": "A",
                "x": 22,
                "y": -0.64
            },
            {
                "category": "A",
                "x": 23,
                "y": -1.28
            },
            {
                "category": "A",
                "x": 24,
                "y": -1.32
            },
            {
                "category": "A",
                "x": 25,
                "y": -0.5
            },
            {
                "category": "A",
                "x": 26,
                "y": -0.4
            },
            {
                "category": "A",
                "x": 27,
                "y": -0.05
            },
            {
                "category": "A",
                "x": 28,
                "y": -0.86
            },
            {
                "category": "A",
                "x": 29,
                "y": -0.53
            },
            {
                "category": "A",
                "x": 30,
                "y": -0.43
            },
            {
                "category": "A",
                "x": 31,
                "y": -0.76
            },
            {
                "category": "A",
                "x": 32,
                "y": -0.46
            },
            {
                "category": "A",
                "x": 33,
                "y": -0.7
            },
            {
                "category": "A",
                "x": 34,
                "y": -1.04
            },
            {
                "category": "A",
                "x": 35,
                "y": -0.64
            },
            {
                "category": "A",
                "x": 36,
                "y": -0.38
            },
            {
                "category": "A",
                "x": 37,
                "y": -0.4
            },
            {
                "category": "A",
                "x": 38,
                "y": -0.6
            },
            {
                "category": "A",
                "x": 39,
                "y": -1.77
            },
            {
                "category": "A",
                "x": 40,
                "y": -0.97
            },
            {
                "category": "A",
                "x": 41,
                "y": -2.38
            },
            {
                "category": "A",
                "x": 42,
                "y": -3.37
            },
            {
                "category": "A",
                "x": 43,
                "y": -3.87
            },
            {
                "category": "A",
                "x": 44,
                "y": -4.93
            },
            {
                "category": "A",
                "x": 45,
                "y": -3.38
            },
            {
                "category": "A",
                "x": 46,
                "y": -2.57
            },
            {
                "category": "A",
                "x": 47,
                "y": -1.26
            },
            {
                "category": "A",
                "x": 48,
                "y": -1
            },
            {
                "category": "A",
                "x": 49,
                "y": -2.32
            },
            {
                "category": "A",
                "x": 50,
                "y": -2.07
            },
            {
                "category": "A",
                "x": 51,
                "y": -1.84
            },
            {
                "category": "A",
                "x": 52,
                "y": 0.03
            },
            {
                "category": "A",
                "x": 53,
                "y": 0.68
            },
            {
                "category": "A",
                "x": 54,
                "y": 1.84
            },
            {
                "category": "A",
                "x": 55,
                "y": 2.25
            },
            {
                "category": "A",
                "x": 56,
                "y": 2.01
            },
            {
                "category": "A",
                "x": 57,
                "y": 1.19
            },
            {
                "category": "A",
                "x": 58,
                "y": 1.47
            },
            {
                "category": "A",
                "x": 59,
                "y": 2.92
            },
            {
                "category": "A",
                "x": 60,
                "y": 3.55
            },
            {
                "category": "A",
                "x": 61,
                "y": 4.03
            },
            {
                "category": "A",
                "x": 62,
                "y": 4.5
            },
            {
                "category": "A",
                "x": 63,
                "y": 2.99
            },
            {
                "category": "A",
                "x": 64,
                "y": 3.2
            },
            {
                "category": "A",
                "x": 65,
                "y": 3.59
            },
            {
                "category": "A",
                "x": 66,
                "y": 3.65
            },
            {
                "category": "A",
                "x": 67,
                "y": 4.21
            },
            {
                "category": "A",
                "x": 68,
                "y": 2.83
            },
            {
                "category": "A",
                "x": 69,
                "y": 3.34
            },
            {
                "category": "A",
                "x": 70,
                "y": 3.92
            },
            {
                "category": "A",
                "x": 71,
                "y": 4.57
            },
            {
                "category": "A",
                "x": 72,
                "y": 3.79
            },
            {
                "category": "A",
                "x": 73,
                "y": 3.88
            },
            {
                "category": "A",
                "x": 74,
                "y": 4.56
            },
            {
                "category": "A",
                "x": 75,
                "y": 5.65
            },
            {
                "category": "A",
                "x": 76,
                "y": 4.94
            },
            {
                "category": "A",
                "x": 77,
                "y": 5.15
            },
            {
                "category": "A",
                "x": 78,
                "y": 7.3
            },
            {
                "category": "A",
                "x": 79,
                "y": 7.48
            },
            {
                "category": "A",
                "x": 80,
                "y": 6.69
            },
            {
                "category": "A",
                "x": 81,
                "y": 7.56
            },
            {
                "category": "A",
                "x": 82,
                "y": 7.08
            },
            {
                "category": "A",
                "x": 83,
                "y": 7.49
            },
            {
                "category": "A",
                "x": 84,
                "y": 9.61
            },
            {
                "category": "A",
                "x": 85,
                "y": 9.12
            },
            {
                "category": "A",
                "x": 86,
                "y": 9.57
            },
            {
                "category": "A",
                "x": 87,
                "y": 9.51
            },
            {
                "category": "A",
                "x": 88,
                "y": 9.26
            },
            {
                "category": "A",
                "x": 89,
                "y": 7.83
            },
            {
                "category": "A",
                "x": 90,
                "y": 9.27
            },
            {
                "category": "A",
                "x": 91,
                "y": 9.28
            },
            {
                "category": "A",
                "x": 92,
                "y": 9.48
            },
            {
                "category": "A",
                "x": 93,
                "y": 9.09
            },
            {
                "category": "A",
                "x": 94,
                "y": 10.68
            },
            {
                "category": "A",
                "x": 95,
                "y": 8.72
            },
            {
                "category": "A",
                "x": 96,
                "y": 9.01
            },
            {
                "category": "A",
                "x": 97,
                "y": 8.51
            },
            {
                "category": "A",
                "x": 98,
                "y": 8.87
            },
            {
                "category": "A",
                "x": 99,
                "y": 9.18
            },
            {
                "category": "B",
                "x": 0,
                "y": -0.14
            },
            {
                "category": "B",
                "x": 1,
                "y": -0.37
            },
            {
                "category": "B",
                "x": 2,
                "y": 0.4
            },
            {
                "category": "B",
                "x": 3,
                "y": -0.07
            },
            {
                "category": "B",
                "x": 4,
                "y": -1.98
            },
            {
                "category": "B",
                "x": 5,
                "y": -2.99
            },
            {
                "category": "B",
                "x": 6,
                "y": -4.41
            },
            {
                "category": "B",
                "x": 7,
                "y": -4.34
            },
            {
                "category": "B",
                "x": 8,
                "y": -4.23
            },
            {
                "category": "B",
                "x": 9,
                "y": -4.83
            },
            {
                "category": "B",
                "x": 10,
                "y": -2.98
            },
            {
                "category": "B",
                "x": 11,
                "y": -2.15
            },
            {
                "category": "B",
                "x": 12,
                "y": -4.11
            },
            {
                "category": "B",
                "x": 13,
                "y": -3.38
            },
            {
                "category": "B",
                "x": 14,
                "y": -3.68
            },
            {
                "category": "B",
                "x": 15,
                "y": -4.14
            },
            {
                "category": "B",
                "x": 16,
                "y": -5.9
            },
            {
                "category": "B",
                "x": 17,
                "y": -6.58
            },
            {
                "category": "B",
                "x": 18,
                "y": -5.65
            },
            {
                "category": "B",
                "x": 19,
                "y": -5.31
            },
            {
                "category": "B",
                "x": 20,
                "y": -5.5
            },
            {
                "category": "B",
                "x": 21,
                "y": -4.69
            },
            {
                "category": "B",
                "x": 22,
                "y": -3.68
            },
            {
                "category": "B",
                "x": 23,
                "y": -3.32
            },
            {
                "category": "B",
                "x": 24,
                "y": -1.76
            },
            {
                "category": "B",
                "x": 25,
                "y": -1.67
            },
            {
                "category": "B",
                "x": 26,
                "y": -3.66
            },
            {
                "category": "B",
                "x": 27,
                "y": -2.18
            },
            {
                "category": "B",
                "x": 28,
                "y": -2.68
            },
            {
                "category": "B",
                "x": 29,
                "y": -3.21
            },
            {
                "category": "B",
                "x": 30,
                "y": -2.24
            },
            {
                "category": "B",
                "x": 31,
                "y": -2.64
            },
            {
                "category": "B",
                "x": 32,
                "y": -2.37
            },
            {
                "category": "B",
                "x": 33,
                "y": -3.79
            },
            {
                "category": "B",
                "x": 34,
                "y": -4.59
            },
            {
                "category": "B",
                "x": 35,
                "y": -2.71
            },
            {
                "category": "B",
                "x": 36,
                "y": -2.78
            },
            {
                "category": "B",
                "x": 37,
                "y": -2.72
            },
            {
                "category": "B",
                "x": 38,
                "y": -2.42
            },
            {
                "category": "B",
                "x": 39,
                "y": -1.28
            },
            {
                "category": "B",
                "x": 40,
                "y": -2.19
            },
            {
                "category": "B",
                "x": 41,
                "y": -1.6
            },
            {
                "category": "B",
                "x": 42,
                "y": -2.16
            },
            {
                "category": "B",
                "x": 43,
                "y": -3.72
            },
            {
                "category": "B",
                "x": 44,
                "y": -3.24
            },
            {
                "category": "B",
                "x": 45,
                "y": -4.03
            },
            {
                "category": "B",
                "x": 46,
                "y": -5.26
            },
            {
                "category": "B",
                "x": 47,
                "y": -6.86
            },
            {
                "category": "B",
                "x": 48,
                "y": -6.08
            },
            {
                "category": "B",
                "x": 49,
                "y": -5.56
            },
            {
                "category": "B",
                "x": 50,
                "y": -5.21
            },
            {
                "category": "B",
                "x": 51,
                "y": -4.92
            },
            {
                "category": "B",
                "x": 52,
                "y": -4.45
            },
            {
                "category": "B",
                "x": 53,
                "y": -5.42
            },
            {
                "category": "B",
                "x": 54,
                "y": -6.24
            },
            {
                "category": "B",
                "x": 55,
                "y": -5.42
            },
            {
                "category": "B",
                "x": 56,
                "y": -6.17
            },
            {
                "category": "B",
                "x": 57,
                "y": -6.25
            },
            {
                "category": "B",
                "x": 58,
                "y": -5.42
            },
            {
                "category": "B",
                "x": 59,
                "y": -5.69
            },
            {
                "category": "B",
                "x": 60,
                "y": -6.55
            },
            {
                "category": "B",
                "x": 61,
                "y": -6.77
            },
            {
                "category": "B",
                "x": 62,
                "y": -6.84
            },
            {
                "category": "B",
                "x": 63,
                "y": -7.29
            },
            {
                "category": "B",
                "x": 64,
                "y": -8.53
            },
            {
                "category": "B",
                "x": 65,
                "y": -9.42
            },
            {
                "category": "B",
                "x": 66,
                "y": -10.56
            },
            {
                "category": "B",
                "x": 67,
                "y": -9.48
            },
            {
                "category": "B",
                "x": 68,
                "y": -10.42
            },
            {
                "category": "B",
                "x": 69,
                "y": -9.9
            },
            {
                "category": "B",
                "x": 70,
                "y": -8.76
            },
            {
                "category": "B",
                "x": 71,
                "y": -9.08
            },
            {
                "category": "B",
                "x": 72,
                "y": -9.32
            },
            {
                "category": "B",
                "x": 73,
                "y": -7
            },
            {
                "category": "B",
                "x": 74,
                "y": -8.61
            },
            {
                "category": "B",
                "x": 75,
                "y": -8.55
            },
            {
                "category": "B",
                "x": 76,
                "y": -7.87
            },
            {
                "category": "B",
                "x": 77,
                "y": -7.83
            },
            {
                "category": "B",
                "x": 78,
                "y": -7.19
            },
            {
                "category": "B",
                "x": 79,
                "y": -7.85
            },
            {
                "category": "B",
                "x": 80,
                "y": -7.97
            },
            {
                "category": "B",
                "x": 81,
                "y": -9.17
            },
            {
                "category": "B",
                "x": 82,
                "y": -9.82
            },
            {
                "category": "B",
                "x": 83,
                "y": -11.08
            },
            {
                "category": "B",
                "x": 84,
                "y": -10.05
            },
            {
                "category": "B",
                "x": 85,
                "y": -8.78
            },
            {
                "category": "B",
                "x": 86,
                "y": -8.01
            },
            {
                "category": "B",
                "x": 87,
                "y": -11.25
            },
            {
                "category": "B",
                "x": 88,
                "y": -12.5
            },
            {
                "category": "B",
                "x": 89,
                "y": -12.94
            },
            {
                "category": "B",
                "x": 90,
                "y": -14.37
            },
            {
                "category": "B",
                "x": 91,
                "y": -15.35
            },
            {
                "category": "B",
                "x": 92,
                "y": -15.96
            },
            {
                "category": "B",
                "x": 93,
                "y": -15.84
            },
            {
                "category": "B",
                "x": 94,
                "y": -17.08
            },
            {
                "category": "B",
                "x": 95,
                "y": -17.23
            },
            {
                "category": "B",
                "x": 96,
                "y": -17.85
            },
            {
                "category": "B",
                "x": 97,
                "y": -18.44
            },
            {
                "category": "B",
                "x": 98,
                "y": -19.14
            },
            {
                "category": "B",
                "x": 99,
                "y": -18.32
            },
            {
                "category": "C",
                "x": 0,
                "y": 0.65
            },
            {
                "category": "C",
                "x": 1,
                "y": 0.41
            },
            {
                "category": "C",
                "x": 2,
                "y": -0.06
            },
            {
                "category": "C",
                "x": 3,
                "y": -0.52
            },
            {
                "category": "C",
                "x": 4,
                "y": -2.25
            },
            {
                "category": "C",
                "x": 5,
                "y": -1.93
            },
            {
                "category": "C",
                "x": 6,
                "y": -0.47
            },
            {
                "category": "C",
                "x": 7,
                "y": -1.89
            },
            {
                "category": "C",
                "x": 8,
                "y": -3.04
            },
            {
                "category": "C",
                "x": 9,
                "y": -3.33
            },
            {
                "category": "C",
                "x": 10,
                "y": -3.35
            },
            {
                "category": "C",
                "x": 11,
                "y": -4.57
            },
            {
                "category": "C",
                "x": 12,
                "y": -5.9
            },
            {
                "category": "C",
                "x": 13,
                "y": -5.73
            },
            {
                "category": "C",
                "x": 14,
                "y": -7.2
            },
            {
                "category": "C",
                "x": 15,
                "y": -6.15
            },
            {
                "category": "C",
                "x": 16,
                "y": -5.82
            },
            {
                "category": "C",
                "x": 17,
                "y": -5.21
            },
            {
                "category": "C",
                "x": 18,
                "y": -6.05
            },
            {
                "category": "C",
                "x": 19,
                "y": -5.07
            },
            {
                "category": "C",
                "x": 20,
                "y": -6.18
            },
            {
                "category": "C",
                "x": 21,
                "y": -4.82
            },
            {
                "category": "C",
                "x": 22,
                "y": -4.46
            },
            {
                "category": "C",
                "x": 23,
                "y": -2.93
            },
            {
                "category": "C",
                "x": 24,
                "y": -5.54
            },
            {
                "category": "C",
                "x": 25,
                "y": -5.84
            },
            {
                "category": "C",
                "x": 26,
                "y": -6.06
            },
            {
                "category": "C",
                "x": 27,
                "y": -6.58
            },
            {
                "category": "C",
                "x": 28,
                "y": -5.67
            },
            {
                "category": "C",
                "x": 29,
                "y": -5.15
            },
            {
                "category": "C",
                "x": 30,
                "y": -5.86
            },
            {
                "category": "C",
                "x": 31,
                "y": -7.32
            },
            {
                "category": "C",
                "x": 32,
                "y": -7.31
            },
            {
                "category": "C",
                "x": 33,
                "y": -7.73
            },
            {
                "category": "C",
                "x": 34,
                "y": -7.9
            },
            {
                "category": "C",
                "x": 35,
                "y": -7.72
            },
            {
                "category": "C",
                "x": 36,
                "y": -9.64
            },
            {
                "category": "C",
                "x": 37,
                "y": -7.18
            },
            {
                "category": "C",
                "x": 38,
                "y": -7.21
            },
            {
                "category": "C",
                "x": 39,
                "y": -6.46
            },
            {
                "category": "C",
                "x": 40,
                "y": -5.06
            },
            {
                "category": "C",
                "x": 41,
                "y": -2.87
            },
            {
                "category": "C",
                "x": 42,
                "y": -2.77
            },
            {
                "category": "C",
                "x": 43,
                "y": -2.7
            },
            {
                "category": "C",
                "x": 44,
                "y": -3.62
            },
            {
                "category": "C",
                "x": 45,
                "y": -3.94
            },
            {
                "category": "C",
                "x": 46,
                "y": -3.71
            },
            {
                "category": "C",
                "x": 47,
                "y": -3.53
            },
            {
                "category": "C",
                "x": 48,
                "y": -4.76
            },
            {
                "category": "C",
                "x": 49,
                "y": -4.47
            },
            {
                "category": "C",
                "x": 50,
                "y": -5.15
            },
            {
                "category": "C",
                "x": 51,
                "y": -5.86
            },
            {
                "category": "C",
                "x": 52,
                "y": -7.05
            },
            {
                "category": "C",
                "x": 53,
                "y": -6.27
            },
            {
                "category": "C",
                "x": 54,
                "y": -5.3
            },
            {
                "category": "C",
                "x": 55,
                "y": -3.41
            },
            {
                "category": "C",
                "x": 56,
                "y": -4.29
            },
            {
                "category": "C",
                "x": 57,
                "y": -3.95
            },
            {
                "category": "C",
                "x": 58,
                "y": -3.94
            },
            {
                "category": "C",
                "x": 59,
                "y": -1.22
            },
            {
                "category": "C",
                "x": 60,
                "y": -2.29
            },
            {
                "category": "C",
                "x": 61,
                "y": -1.58
            },
            {
                "category": "C",
                "x": 62,
                "y": -2.42
            },
            {
                "category": "C",
                "x": 63,
                "y": -1.57
            },
            {
                "category": "C",
                "x": 64,
                "y": -1.39
            },
            {
                "category": "C",
                "x": 65,
                "y": -1.24
            },
            {
                "category": "C",
                "x": 66,
                "y": -0.88
            },
            {
                "category": "C",
                "x": 67,
                "y": 0.17
            },
            {
                "category": "C",
                "x": 68,
                "y": 0.69
            },
            {
                "category": "C",
                "x": 69,
                "y": 4.54
            },
            {
                "category": "C",
                "x": 70,
                "y": 5.49
            },
            {
                "category": "C",
                "x": 71,
                "y": 6.25
            },
            {
                "category": "C",
                "x": 72,
                "y": 5.77
            },
            {
                "category": "C",
                "x": 73,
                "y": 3.9
            },
            {
                "category": "C",
                "x": 74,
                "y": 3.43
            },
            {
                "category": "C",
                "x": 75,
                "y": 2.35
            },
            {
                "category": "C",
                "x": 76,
                "y": 1.62
            },
            {
                "category": "C",
                "x": 77,
                "y": 0.97
            },
            {
                "category": "C",
                "x": 78,
                "y": -1.06
            },
            {
                "category": "C",
                "x": 79,
                "y": -0.21
            },
            {
                "category": "C",
                "x": 80,
                "y": 0.3
            },
            {
                "category": "C",
                "x": 81,
                "y": -0.04
            },
            {
                "category": "C",
                "x": 82,
                "y": 1.73
            },
            {
                "category": "C",
                "x": 83,
                "y": 2.65
            },
            {
                "category": "C",
                "x": 84,
                "y": 1.13
            },
            {
                "category": "C",
                "x": 85,
                "y": 0.42
            },
            {
                "category": "C",
                "x": 86,
                "y": -0.51
            },
            {
                "category": "C",
                "x": 87,
                "y": -1.53
            },
            {
                "category": "C",
                "x": 88,
                "y": 0.1
            },
            {
                "category": "C",
                "x": 89,
                "y": 0.23
            },
            {
                "category": "C",
                "x": 90,
                "y": 1.4
            },
            {
                "category": "C",
                "x": 91,
                "y": 1.86
            },
            {
                "category": "C",
                "x": 92,
                "y": 1.93
            },
            {
                "category": "C",
                "x": 93,
                "y": 2.59
            },
            {
                "category": "C",
                "x": 94,
                "y": 4.72
            },
            {
                "category": "C",
                "x": 95,
                "y": 5.31
            },
            {
                "category": "C",
                "x": 96,
                "y": 5.1
            },
            {
                "category": "C",
                "x": 97,
                "y": 5.95
            },
            {
                "category": "C",
                "x": 98,
                "y": 6.85
            },
            {
                "category": "C",
                "x": 99,
                "y": 7.48
            }
        ]
    },
    "height": 300,
    "layer": [
        {
            "encoding": {
                "color": {
                    "field": "category",
                    "type": "nominal"
                },
                "x": {
                    "field": "x",
                    "type": "quantitative"
                },
                "y": {
                    "field": "y",
                    "type": "quantitative"
                }
            },
            "mark": {
                "interpolate": "basis",
                "type": "line"
            },
            "selection": {
                "selector002": {
                    "bind": "scales",
                    "encodings": [
                        "x",
                        "y"
                    ],
                    "mark": {
                        "fill": "#333",
                        "fillOpacity": 0.125,
                        "stroke": "white"
                    },
                    "on": "[mousedown, window:mouseup] > window:mousemove!",
                    "resolve": "global",
                    "translate": "[mousedown, window:mouseup] > window:mousemove!",
                    "type": "interval",
                    "zoom": "wheel!"
                }
            }
        },
        {
            "encoding": {
                "opacity": {
                    "value": 0
                },
                "x": {
                    "field": "x",
                    "type": "quantitative"
                }
            },
            "mark": "point",
            "selection": {
                "selector001": {
                    "empty": "none",
                    "fields": [
                        "x"
                    ],
                    "nearest": true,
                    "on": "mouseover",
                    "resolve": "global",
                    "type": "single"
                }
            }
        },
        {
            "encoding": {
                "color": {
                    "field": "category",
                    "type": "nominal"
                },
                "opacity": {
                    "condition": {
                        "selection": "selector001",
                        "value": 1
                    },
                    "value": 0
                },
                "x": {
                    "field": "x",
                    "type": "quantitative"
                },
                "y": {
                    "field": "y",
                    "type": "quantitative"
                }
            },
            "mark": "point"
        },
        {
            "encoding": {
                "x": {
                    "field": "x",
                    "type": "quantitative"
                }
            },
            "mark": {
                "color": "gray",
                "type": "rule"
            },
            "transform": [
                {
                    "filter": {
                        "selection": "selector001"
                    }
                }
            ]
        },
        {
            "encoding": {
                "color": {
                    "field": "category",
                    "type": "nominal"
                },
                "text": {
                    "condition": {
                        "field": "y",
                        "selection": "selector001",
                        "type": "quantitative"
                    },
                    "value": " "
                },
                "x": {
                    "field": "x",
                    "type": "quantitative"
                },
                "y": {
                    "field": "y",
                    "type": "quantitative"
                }
            },
            "mark": {
                "align": "left",
                "dx": 5,
                "dy": -5,
                "type": "text"
            }
        }
    ],
    "width": 600
};

vegaEmbed("#viz_11", vlSpec_11);
</script>
</div>
