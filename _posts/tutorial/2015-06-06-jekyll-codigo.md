---
layout: tutorial
title: Código en Jekyll
categories: [tutorial, jekyll] 
tags: jekyll, inline, code
---

Hay distintas formas de mostrar código en Jekyll. Mostraré las que conozco

## Código en la misma línea

Si queremos hablar de variables como `_nombre_muy_extrano_` o 
de comandos del terminal como `ssh-keygen` o `grep`
queremos que el texto tenga el formato correcto. 
Para ello hay que utilizar "`". Por ejemplo, el texto anterior se crea con
{% highlight bash %} 
{% raw %} 
Si queremos hablar de variables como `_nombre_muy_extrano_` o 
de comandos del terminal como `ssh-keygen` o `grep`
queremos que el texto tenga el formato correcto.
{% endraw %} 
{% endhighlight %}

## Código que debe colorearse
Si queremos mostrar código y que se muestre correctamente, como en el siguiente ejemplo
{% highlight python %} 
def foo(Bar,N=3):
    print(Bar*N)
    return
foo(1)
foo("a")
{% endhighlight %}
debemos utilizar el comando highlight de jekyll, de la siguiente manera

{% highlight text %} 
{% raw %} 
{% highlight python %} 
def foo(Bar,N=3):
    print(Bar*N)
    return
foo(1)
foo("a")
{% endhighlight %}
{% endraw %} 
{% endhighlight %}

Además de python, podemos utilizar un sinnúmero de lenguajes.

## Código que NO debe colorearse
Si queremos mostrar texto plano, como en el siguiente ejemplo
{% highlight text %} 
def foo(Bar,N=3):
    print(Bar*N)
    return
foo(1)
foo("a")
{% endhighlight %}
debemos utilizar el comando highlight de jekyll, de la siguiente manera

{% highlight text %} 
{% raw %} 
{% highlight text %} 
def foo(Bar,N=3):
    print(Bar*N)
    return
foo(1)
foo("a")
{% endhighlight %}
{% endraw %} 
{% endhighlight %}

## Código que debe interpretarse
.

## Código que NO debe interpretarse
.
