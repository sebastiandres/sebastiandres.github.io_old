---
layout: tutorial
title: Habilitar comentarios en Jekyll
categories: [tutorial, jekyll] 
tags: jekyll, disqus, comments
---

Habilitar los comentarios en el sitio ha sido increiblemente sencillo.

(1) Abrir cuenta en [https://disqus.com/]()

(2) Solicitar cuenta para sitio en [https://disqus.com/websites/]()

(3) Seleccionar la opción de Código General Embebido (Universal Emmbed code) y bucar el identificador (unique identifier).
En mi caso, era simplemente "sebastiandres"

(4) En el archivo **_config.yml**, en la línea correspondiente a disqus, agregar el identificador de disqus:
{% highlight html %}
{% raw %}
disqus: sebastiandres
{% endraw %}
{% endhighlight %}

(5) Esperar que lleguen los comentarios :)
