---
layout: page
title:
permalink: /blog/
---
<h1>Entradas del blog:</h1>
<div class="tutorials">
  <ul>
  {% for entry in site.categories.blog %}
    <article class="blog">
      <li><a href="{{ site.baseurl }}{{ entry.url }}">{{ entry.title }}</a></li>
    </article>
  {% endfor %}
  </ul>
</div>

