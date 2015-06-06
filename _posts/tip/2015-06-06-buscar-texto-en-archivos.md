---
layout: tip
title: Buscar texto en archivos con grep
categories: tip
tags: grep, terminal, texto
---

Probablemente, `grep -Hrn "mi texto" .` es el comando que más utilizo a diario.

Este comando permite buscar una secuencia de caracteres ("mi texto" en el ejemplo)
en nombres de archivos y dentro del contenido de los a archivos. Yo lo uso para:

 * Saber en jekyll donde aparece una determinada palabra. Por ejemplo, si quiero modificar
algo que no conozco, busco un texto relacionado, hago el `grep` correspondiente y 
veo en todas las partes que el texto aparece.

 * Saber en python donde se utiliza una cierta función. Por ejemplo, en un gran proyecto
creo que la función `convert_to_old_format` dejó de usarse, basta con ver si `grep -Hrn "convert_to_old_format" .`
aparece en un archivo. 
Esto también permite ver si el paso de argumentos en la función es consistente en todas las llamadas,
y mucho más.

El comando se entiende de la siguiente forma:

 * -H: Muestra el nombre del archivo
 * -r: Busca recursivamente en las carpetas
 * -n: Muestra el número de línea
 
Así, por ejemplo, si quiero saber donde he escrito la palabra `función` en el blog escribo en el terminal
{% highlight html %}
{% raw %}
grep -Hrn "función" .
{% endraw %}
{% endhighlight %}

lo cual me arroja como resultado

{% highlight html %}
{% raw %}
_posts/tip/2015-06-06-buscar-palabra-en-archivos.md:17: 
 * Saber en python donde se utiliza una cierta función. Por ejemplo, en un gran proyecto

_posts/tip/2015-06-06-buscar-palabra-en-archivos.md:18:
creo que la función `convert_to_old_format` dejó de usarse, basta con ver si `grep -Hrn "convert_to_old_format" .`

_posts/tip/2015-06-06-buscar-palabra-en-archivos.md:20:
Esto también permite ver si el paso de argumentos en la función es consistente en todas las llamadas,

_posts/tip/2015-06-06-buscar-palabra-en-archivos.md:18:
creo que la función `convert_to_old_format` dejó de usarse, basta con ver si `grep -Hrn "convert_to_old_format" .`

_posts/tip/2015-06-06-buscar-palabra-en-archivos.md:20:
Esto también permite ver si el paso de argumentos en la función es consistente en todas las llamadas,
{% endraw %}
{% endhighlight %}

Si queremos buscar en un tipo particular de archivos, por ejemplo sólo en archivos de markdown (*.md), podemos agregar la opción correspondiente ``, y escribir en el terminal:
{% highlight html %}
{% raw %}
grep -Hrn "función" --include=*.md
{% endraw %}
{% endhighlight %}
