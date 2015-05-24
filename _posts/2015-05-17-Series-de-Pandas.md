---
layout: post
title: Tutorial de Pandas - Series
---

Una **Serie** es un objeto "bipolar". 
Puede comportarse como un array 1D y como un diccionario.
Para hacerlo una **Serie** de pandas tiene 3 componentes: offset, key y values.

## Introducción

Si una **Serie** tiene N elementos:

* **offset/offset**: Comienza en 0 y termina en N-1, con la notación como en un array.

* **key/llaves**: Lista de N elementos. Conviene que los elementos no se repitan.

* **values/valores**: Lista de N valores, sí pueden repetirse.

Consideremos lo siguiente:

* Cuando necesitas offsets y valores, en realidad debes usar arrays.

* Cuando necesitas llaves y valores, necesitas utilizar un diccionario.

* Cuando necesitas utilizar simulatáneamente offsets, llaves y valores... ¡Necesitas utilizar una Series de pandas!


## Archivos

Descargar los archivos: python, ipython

## Imprimir una Serie

Para imprimir una serie, basta utilizar print(s).
Cuando se imprime una serie, sólo se muestra la llave y el valor.
El orden con el cual se imprimen los elementos de la Serie corresponde al orden otorgado
por el offset.

{% highlight python %}
print(s)
{% endhighlight %}

## Crear una Serie

Es posible crear una **Serie** a partir de una tupla, una lista, un array 1D o un diccionario.

{% highlight python %}
# From a list.
# The key (index) is assumed to be equal to the offset.
s = pd.Series(["Uno","Dos","Tres","Cuatro"])
print(s)

# From a list.  Explicitely give the index.
s = pd.Series(["Uno","Dos","Tres","Cuatro"], index=["Eins","Zwei","Drei","Vier"])
print(s)

# From an array.  The key (index) is assumed to be equal to the offset.
a = np.linspace(10.0, 20.0, 10)
s = pd.Series(a)
print(s)

# From an array.  The key (index) is assumed to be equal to the offset.
s = pd.Series(a, index=range(1,11))
print(s)

# From a dic. The key (index) are the keys of the dic. 
# The offset is the same internal order of the dic. 
# Notice they are different to the order statically tipped
d = {"Jan":4, "Feb":0, "Mar":8, "Apr":10}
s = pd.Series(d)
{% endhighlight %}


## Editar nombres de una Serie

Es posible editar los detalles de una serie: el nombre de la Serie y del index. 

{% highlight python %}
s.name = "Price"
s.index.name = "Month"
print(s)
{% endhighlight %}

## Editar datos de una Serie

Es posible ingresar nuevos datos o editar datos previamente ingresados.

{% highlight python %}
s["Nuevo"] = "Bleble"
print(s)
{% endhighlight %}

## Resumir una Serie

{% highlight python %}
print(s)
{% endhighlight %}

## Operaciones en una Serie

{% highlight python %}
print(s)
{% endhighlight %}

