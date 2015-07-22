---
layout: page
title:
permalink: /tutorial/
---

<div class="tutorials">
  <h1>Tutorial de Jekyll:</h1>
  <ul>
  {% for entry in site.categories.tutorial %}
    <article class="tutorial">
      <li><a href="{{ site.baseurl }}{{ entry.url }}">{{ entry.title }}</a></li>
    </article>
  {% endfor %}
  </ul>
</div>

<div class="notebook">
  <h1>Tutorial de ipython notebook:</h1>
  <ul>
  {% for entry in site.categories.notebook %}
    <article class="notebook">
      <li><a href="{{ site.baseurl }}{{ entry.url }}">{{ entry.title }}</a></li>
    </article>
  {% endfor %}
  </ul>
</div>

