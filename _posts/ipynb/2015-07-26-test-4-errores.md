---
layout: post
title: "Test-4-Errores"
excerpt: 
categories: [tutorial, jekyll] 
tags: jekyll, ipynb, notebook
---
<div class="header">
Link al archivo ipython notebook original:
<a href="https://raw.githubusercontent.com/sebastiandres/sebastiandres.github.io/master/ipynb/Test-4-Errores.ipynb">Test-4-Errores.ipynb</a>.
</div>
<br>
En este ipython notebook examinaremos tipos de errores en ipython notebook.
# Tipos de errores

<div class="in-prompt prompt-common">In [1]:</div>

<div class="input">
{% highlight python %}
print 1.0
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [1]:</div>

      File "<ipython-input-1-321881e2aa75>", line 1
        print 1.0
                ^
    SyntaxError: invalid syntax


<div class="in-prompt prompt-common">In [2]:</div>

<div class="input">
{% highlight python %}
print(1/0)
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [2]:</div>

    ---------------------------------------------------------------------------

    ZeroDivisionError                         Traceback (most recent call last)

    <ipython-input-2-0f9f90da76dc> in <module>()
    ----> 1 print(1/0)
    

    ZeroDivisionError: division by zero

<div class="in-prompt prompt-common">In [3]:</div>

<div class="input">
{% highlight python %}
print(x)
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [3]:</div>

    ---------------------------------------------------------------------------

    NameError                                 Traceback (most recent call last)

    <ipython-input-3-81745ac23551> in <module>()
    ----> 1 print(x)
    

    NameError: name 'x' is not defined

<div class="in-prompt prompt-common">In [4]:</div>

<div class="input">
{% highlight python %}
print?x
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [4]:</div>

      File "<ipython-input-4-f8bb9fc10637>", line 1
        print?x
             ^
    SyntaxError: invalid syntax

