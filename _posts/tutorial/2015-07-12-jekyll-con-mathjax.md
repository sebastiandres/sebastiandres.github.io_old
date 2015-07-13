---
layout: tutorial
title: Mathjax y Jekyll 
categories: [tutorial, jekyll] 
tags: mathjax, latex, jekyll
---

Para habilitar [MathJax](https://www.mathjax.org/) en Jekyll, solamente es necesario incluir 

{% highlight html %} 
{% raw %} 
<script type="text/javascript"
    src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML">
</script>
{% endraw %} 
{% endhighlight %}

en el archivo `_includes/meta.html`. Ahora es posible escribir fórmulas como \\( X \times \mathsf{X} \times \mathbf{X} / \alpha! \\)

Hay 5 distinciones al latex tradicional:

 * Fórmula completa: En latex se usa `\[\sin(\alpha)^2 + \cos(\alpha)^2 = 1\]` pero en mathjax hay que usar `\\[\sin(\alpha)^2 + \cos(\alpha)^2 = 1\\]`, para obtener \\[\sin(\alpha)^2 + \cos(\alpha)^2 = 1\\]

 * Fórmula inline: En latex es `$\sin(\alpha)^2 + \cos(\alpha)^2 = 1$` mientras que en mathjax es `\\( \sin(\alpha)^2 + \cos(\alpha)^2 = 1\\)`, para obtener \\( \sin(\alpha)^2 + \cos(\alpha)^2 = 1\\)

 * Texto sin compilar: En latex se puede utilizar `\textrm{}` pero en mathjax se usa `\mathsf{}`, para mostrar \\( \mathsf{Velocidad} \times \mathsf{Tiempo}\\) en vez de \\( Velocidad \times Tiempo \\).

 * Texto en negritas (tipo matriz): En latex se puede utilizar `\textbf{}` pero en mathjax se usa `\mathbf{}`, para obtener \\( \mathbf{X} \\) en lugar de \\( X \\).

 * Subíndices: En latex se utiliza `x_n`, pero en mathjax se usa `x\_n`, para obtener \\( x\_n \\).

La ayuda vino del siguiente link: [MathJax with Jekyll](http://gastonsanchez.com/blog/opinion/2014/02/16/Mathjax-with-jekyll.html)


