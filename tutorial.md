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

