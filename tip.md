---
layout: page
title: Tips
permalink: /tip/
---

<div class="tips">
  {% for entry in site.categories.tip %}
    <article class="tip">
      <h3> {{ entry.title }} </h3>
      <a href="{{ site.baseurl }}{{ entry.url }}" class="read-more">
        <div class="entry">
          {{ entry.excerpt }}
        </div>
      </a>
    </article>
  {% endfor %}
</div>
