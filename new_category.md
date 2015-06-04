---
layout: page
title: New Category
permalink: /new_category/
---

<div class="new_category">
  {% for entry in site.categories.new_category %}
    <article class="new_tag">
      <h2><a href="{{ site.baseurl }}{{ entry.url }}">{{ entry.title }}</a></h2>
      <p>{{ entry.data | date: "%B %e, %Y"}} </p>
    </article>
  {% endfor %}
</div>

