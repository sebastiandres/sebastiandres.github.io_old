{% extends 'display_priority.tpl' %}

###############################################################################
# HEADER
###############################################################################
{%- block header -%}
---
layout: post
title: "{{resources['metadata']['name']}}"
excerpt: 
categories: [tutorial, jekyll] 
tags: jekyll, ipynb, notebook
---
<div class="header">
Link al archivo ipython notebook original:
<a href="https://raw.githubusercontent.com/sebastiandres/sebastiandres.github.io/master/ipynb/{{resources['metadata']['name']}}.ipynb">{{resources['metadata']['name']}}.ipynb</a>.
</div>
<br>
{%- endblock header -%}

###############################################################################
# Markdown cell
###############################################################################
{% block markdowncell scoped %}
{{ cell.source | sanitize_markdown }}
{% endblock markdowncell %}
 
###############################################################################
# CODE CELL INPUTS
###############################################################################
{% block in_prompt %}
<div class="in-prompt prompt-common">In [{{ cell.execution_count }}]:</div>
{% endblock in_prompt %}
  
{% block input %}
<div class="input">
{{ '{% highlight python %}' }}
{{ cell.source }}
{{ '{% endhighlight %}' }}
</div>
{% endblock input %}

###############################################################################
# CODE CELL OUTPUT
###############################################################################
{% block output_prompt %}
<div class="output-prompt prompt-common">Out [{{ cell.execution_count }}]:</div>
{% endblock output_prompt %}

# The regular output (string)
{% block stream %}
<div class="stream">
{{ '{% highlight text %}' }}
{{ output.text }}
{{ '{% endhighlight %}' }}
</div>
{% endblock stream %}

# Audio, video, any html
{% block execute_result %}
<div class='execute_results'>
{{ output | process_execute_result }}
</div>
{% endblock execute_result %}

###############################################################################
# ERRORS
###############################################################################
{% block traceback_line %}
{{ line | indent | strip_ansi }}
{% endblock traceback_line %}

###############################################################################
# UNUSED BLOCKS
###############################################################################
{% block data_png %}
{{ output | process_execute_result }}
<br>
{% endblock data_png %}

{% block data_jpg %}
{{ output | process_execute_result }})
<br>
{% endblock data_jpg %}
 
###############################################################################
# UNUSED BLOCKS (BLOCKS THAT I DON'T UNDERSTAND AND I'M NOT USING SO FAR)
###############################################################################
{% block pyout %}
block pyout\n
{{ '{% highlight python %}' }}
{{ super() }}
{{ '{% endhighlight %}' }}
{% endblock pyout %}

{% block pyerr %}
block pyerr
{{ super() }}
{% endblock pyerr %}
 
{% block data_svg %}
block data_svg
![svg]({{ output.svg_filename | path2support }})
{% endblock data_svg %}


{% block data_latex %}
block data_latex
{{ output.latex }}
{% endblock data_latex %}

{% block data_html scoped %}
block data_html scoped
{{ output.html }}
{% endblock data_html %}
 
{% block data_text scoped %}
block data_text scoped
{{ output.text | indent }}
{% endblock data_text %}
 
{% block headingcell scoped %}
block headingcell scoped
{{ '#' * cell.level }} {{ cell.source | replace('\n', ' ') }}
{% endblock headingcell %}
 
{% block unknowncell scoped %}
block unknowncell scoped
unknown type  {{ cell.type }}
{% endblock unknowncell %}
