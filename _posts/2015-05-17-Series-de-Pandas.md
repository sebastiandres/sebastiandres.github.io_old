---
layout: post
title: Tutorial de Pandas - Series
---

Una *Serie* es un objeto "bipolar". 
Puede comportarse como un array 1D y como un diccionario.
Para hacerlo una Serie de pandas tiene 3 componentes: offset, key y values.

## Introducción

If a *Series* has N elements:

* **offset**: It ranges from 0 to N-1

* **key**: List of N elements, cannot be repeated.

* **values**: List of N values, can be repeated.

The main differences are:

* When you need to use offsets and values, you need to use an array.

* When you need to use keys and values, you end up using a dict.

* When you need to use offset, keys and value, you will use a Series.

## Printing a Series

When you print a Series, print(s), it only shows the key and the value.
The order displayed in the printing of the Series is provided by the offset.

## Printing a Series
{% highlight python linenos %}
## From a list.  The key (index) is assumed to be equal to the offset.
s = pd.Series(["Uno","Dos","Tres","Cuatro"])
print(s)

## From a list.  Explicitely give the index.
s = pd.Series(["Uno","Dos","Tres","Cuatro"], index=["Eins","Zwei","Drei","Vier"])
print(s)

## From an array.  The key (index) is assumed to be equal to the offset.
a = np.linspace(10.0, 20.0, 10)
s = pd.Series(a)
print(s)

## From an array.  The key (index) is assumed to be equal to the offset.
s = pd.Series(a, index=range(1,11))
print(s)

## From a dic. The key (index) are the keys of the dic. 
## The offset is the same internal order of the dic. 
## Notice they are different to the order statically tipped
d = {"Jan":4, "Feb":0, "Mar":8, "Apr":10}
s = pd.Series(d)
## We can add information
s.name = "Price"
s.index.name = "Month"
print(s)
{% endhighlight %}


