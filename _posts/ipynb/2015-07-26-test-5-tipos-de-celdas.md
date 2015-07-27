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

<div class="in-prompt prompt-common">In [1]:</div>

<div class="input">
{% highlight python %}
# Sin output
a = 2
b = 3
{% endhighlight %}
</div>

<div class="in-prompt prompt-common">In [2]:</div>

<div class="input">
{% highlight python %}
# Con output correcto
print(a)
print(b)
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [2]:</div>

<div class="stream">
{% highlight text %}
2
3

{% endhighlight %}
</div>

## 6 - Audio importado
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

## 7 - Video importado
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

## 9 - HTML desde código

Python objects can declare HTML representations that will be displayed in the Notebook. If you have some HTML you want to display, simply use the `HTML` class.

<div class="in-prompt prompt-common">In [5]:</div>

<div class="input">
{% highlight python %}
from IPython.display import HTML
{% endhighlight %}
</div>

<div class="in-prompt prompt-common">In [6]:</div>

<div class="input">
{% highlight python %}
s = """<table>
<tr>
<th>Header 1</th>
<th>Header 2</th>
</tr>
<tr>
<td>row 1, cell 1</td>
<td>row 1, cell 2</td>
</tr>
<tr>
<td>row 2, cell 1</td>
<td>row 2, cell 2</td>
</tr>
</table>"""
{% endhighlight %}
</div>

<div class="in-prompt prompt-common">In [7]:</div>

<div class="input">
{% highlight python %}
h = HTML(s); h
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [7]:</div>

<div class='execute_results'>
<table>
<tr>
<th>Header 1</th>
<th>Header 2</th>
</tr>
<tr>
<td>row 1, cell 1</td>
<td>row 1, cell 2</td>
</tr>
<tr>
<td>row 2, cell 1</td>
<td>row 2, cell 2</td>
</tr>
</table>
</div>

## 10 - Pandas

Pandas makes use of this capability to allow `DataFrames` to be represented as HTML tables.


<div class="in-prompt prompt-common">In [8]:</div>

<div class="input">
{% highlight python %}
import pandas
{% endhighlight %}
</div>

Here is a small amount of stock data for APPL:

<div class="in-prompt prompt-common">In [9]:</div>

<div class="input">
{% highlight python %}
%%file data.csv
Date,Open,High,Low,Close,Volume,Adj Close
2012-06-01,569.16,590.00,548.50,584.00,14077000,581.50
2012-05-01,584.90,596.76,522.18,577.73,18827900,575.26
2012-04-02,601.83,644.00,555.00,583.98,28759100,581.48
2012-03-01,548.17,621.45,516.22,599.55,26486000,596.99
2012-02-01,458.41,547.61,453.98,542.44,22001000,540.12
2012-01-03,409.40,458.24,409.00,456.48,12949100,454.53
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [9]:</div>

<div class="stream">
{% highlight text %}
Writing data.csv

{% endhighlight %}
</div>

Read this as into a `DataFrame`:

<div class="in-prompt prompt-common">In [10]:</div>

<div class="input">
{% highlight python %}
df = pandas.read_csv('data.csv')
print(df)
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [10]:</div>

<div class="stream">
{% highlight text %}
         Date    Open    High     Low   Close    Volume  Adj Close
0  2012-06-01  569.16  590.00  548.50  584.00  14077000     581.50
1  2012-05-01  584.90  596.76  522.18  577.73  18827900     575.26
2  2012-04-02  601.83  644.00  555.00  583.98  28759100     581.48
3  2012-03-01  548.17  621.45  516.22  599.55  26486000     596.99
4  2012-02-01  458.41  547.61  453.98  542.44  22001000     540.12
5  2012-01-03  409.40  458.24  409.00  456.48  12949100     454.53

{% endhighlight %}
</div>

And view the HTML representation:

<div class="in-prompt prompt-common">In [11]:</div>

<div class="input">
{% highlight python %}
df
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [11]:</div>

<div class='execute_results'>
<div style="max-height:1000px;max-width:1500px;overflow:auto;">
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Volume</th>
      <th>Adj Close</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2012-06-01</td>
      <td>569.16</td>
      <td>590.00</td>
      <td>548.50</td>
      <td>584.00</td>
      <td>14077000</td>
      <td>581.50</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2012-05-01</td>
      <td>584.90</td>
      <td>596.76</td>
      <td>522.18</td>
      <td>577.73</td>
      <td>18827900</td>
      <td>575.26</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2012-04-02</td>
      <td>601.83</td>
      <td>644.00</td>
      <td>555.00</td>
      <td>583.98</td>
      <td>28759100</td>
      <td>581.48</td>
    </tr>
    <tr>
      <th>3</th>
      <td>2012-03-01</td>
      <td>548.17</td>
      <td>621.45</td>
      <td>516.22</td>
      <td>599.55</td>
      <td>26486000</td>
      <td>596.99</td>
    </tr>
    <tr>
      <th>4</th>
      <td>2012-02-01</td>
      <td>458.41</td>
      <td>547.61</td>
      <td>453.98</td>
      <td>542.44</td>
      <td>22001000</td>
      <td>540.12</td>
    </tr>
    <tr>
      <th>5</th>
      <td>2012-01-03</td>
      <td>409.40</td>
      <td>458.24</td>
      <td>409.00</td>
      <td>456.48</td>
      <td>12949100</td>
      <td>454.53</td>
    </tr>
  </tbody>
</table>
</div>
</div>

## 11- Sitios externos

You can even embed an entire page from another site in an iframe; for example this is today's Wikipedia
page for mobile users:

<div class="in-prompt prompt-common">In [12]:</div>

<div class="input">
{% highlight python %}
from IPython.display import IFrame
IFrame('http://en.mobile.wikipedia.org/?useformat=mobile', width='100%', height=300)
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [12]:</div>

<div class='execute_results'>

        <iframe
            width="100%"
            height="300"
            src="http://en.mobile.wikipedia.org/?useformat=mobile"
            frameborder="0"
            allowfullscreen
        ></iframe>
</div>

## 12 - Error

<div class="in-prompt prompt-common">In [13]:</div>

<div class="input">
{% highlight python %}
# Con output de error
print(unknown_variable)
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [13]:</div>

    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-13-22fdec8b207f> in <module>()
          1 # Con output de error
    ----> 2 print(unknown_variable)
    

    NameError: name 'unknown_variable' is not defined
