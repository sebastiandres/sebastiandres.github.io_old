---
layout: tutorial
title: Creando categorias
categories: [tutorial, jekyll] 
tags: jekyll, categoria
---

Me costó encontrar información rápida para crear nuevas secciones en el blog, 
como lo son las secciones de Tips y Tutoriales. En resumen, se llaman categorías y requieren la definición de varios archivos.
Utilizaré como ejemplo la creación de la categoría **tutorial**:

(1) Agregar el link correspondiente a la nueva sección, en el archivo **./_layout/default.html**.
El enlace a agregar debería quedar junto a los otros enlaces:

{% highlight html %}
{% raw %}
<a href="{{ site.baseurl }}/tutorial">Tutorial</a>
{% endraw %}
{% endhighlight %}

(2) Crear el layout de la nueva categoría. Para ello, basta crear un archivo **./_layout/tutorial.html**.
Se pueden inspirar en el archivo **./_layout/post.html** ya presente en el directorio. Debería quedar algo del tipo:

{% highlight html %}
{% raw %}
---
layout: default
---
<article class="tutorial">
  <h1>{{ page.title }}</h1>
  <div class="date">
    Written on {{ page.date | date: "%B %e, %Y" }}
  </div>
  <div class="entry">
    {{ content }}
  </div>
  {% include disqus.html %}
</article>
{% endraw %}
{% endhighlight %}

(3) Crear un archivo **./tutorial.md**, que controla la vista en la página cuando se pincha en el enlace tutorial.
Lo que hace este archivo es realizar una lista de los posts contenidos en la sección Tutoriales.
Pueden pueden inspirarse del index.md, por ejemplo:
{% highlight html %}
{% raw %}
---
layout: page
title: Tutoriales
permalink: /tutorial/
---
<div class="new_category">
  {% for entry in site.categories.tutorial %}
    <article class="new_tag">
      <h2><a href="{{ site.baseurl }}{{ entry.url }}">{{ entry.title }}</a></h2>
    </article>
  {% endfor %}
</div>
{% endraw %}
{% endhighlight %}

(4) Realizar posts, aplicando la categoría creada. Resulta conveniente crear subcarpetas para tener todo ordenado, por ejemplo,
el archivo que están leyendo corresponde a **./_posts/tutorial/2015-06-05-creando-nuevas-secciones.md** que tiene por encabezado:

{% highlight html %}
{% raw %}
---
layout: tutorial
title: Creando categorias
categories: [tutorial, jekyll] 
tags: jekyll, categoria
---

Me costó encontrar información rápida para crear nuevas secciones en el blog, 
...
 * [http://www.minddust.com/post/tags-and-categories-on-github-pages/](): 
Esquema de uso de tags, similar a lo hecho con categorías.
{% endraw %}
{% endhighlight %}

La parte crucial fue entender que existían las categorías, y que deben listarse en el inicio del archivo, mediante

{% highlight html %}
{% raw %}
categories: [tutorial, jekyll] 
{% endraw %}
{% endhighlight %}

Los enlaces (en inglés) que utilicé fueron los siguientes:

 * [http://jekyllrb.com/docs/home/](): Documentación extensiva de Jekyll. 
Abundante en información, pero cuesta encontrar la respuesta precisa.

 * [http://www.minddust.com/post/tags-and-categories-on-github-pages/](): 
Esquema de uso de tags, similar a lo hecho con categorías.
