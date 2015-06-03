---
layout: page
title: New Tags
permalink: /new_tag/
---

<h2><a href="{{ site.baseurl }}{{ Hey }}">{{ Titulo }}</a></h2>

<div class="new_tag">
  {% for entry in site.new_tag %}
    <article class="new_tag">
      <h2><a href="{{ site.baseurl }}{{ entry.url }}">{{ entry.title }}</a></h2>
    </article>
  {% endfor %}
</div>
