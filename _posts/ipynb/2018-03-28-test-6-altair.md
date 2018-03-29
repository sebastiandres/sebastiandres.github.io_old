---
layout: post
title: "Test-6-Altair"
excerpt: 
categories: [tutorial, jekyll] 
tags: jekyll, ipynb, notebook
---
<div class="header">
Link al archivo ipython notebook original:
<a href="https://raw.githubusercontent.com/sebastiandres/sebastiandres.github.io/master/ipynb/Test-6-Altair.ipynb">Test-6-Altair.ipynb</a>.
</div>
<br>
Ejemplo de grafico Altair

<div class="in-prompt prompt-common">In [5]:</div>

<div class="input">
{% highlight python %}
from altair import Chart
import pandas as pd

data = pd.DataFrame({
    'a': ['A', 'B', 'C'],
    'b': [28, 55, 43]
})

chart = Chart(data).mark_bar().encode(
    x='b',
    y='a',
)
chart.interactive()
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [5]:</div>

<div class='execute_results'>
  <!-- Container for the visualization -->
  <div id="viz_5"></div>
  <script>
  var vlSpec_5 = 
{'$schema': 'https://vega.github.io/schema/vega-lite/v2.json', 'config': {'view': {'height': 300, 'width': 400}}, 'data': {'values': [{'a': 'A', 'b': 28}, {'a': 'B', 'b': 55}, {'a': 'C', 'b': 43}]}, 'encoding': {'x': {'field': 'b', 'type': 'quantitative'}, 'y': {'field': 'a', 'type': 'nominal'}}, 'mark': 'bar', 'selection': {'selector003': {'bind': 'scales', 'encodings': ['x', 'y'], 'mark': {'fill': '#333', 'fillOpacity': 0.125, 'stroke': 'white'}, 'on': '[mousedown, window:mouseup] > window:mousemove!', 'resolve': 'global', 'translate': '[mousedown, window:mouseup] > window:mousemove!', 'type': 'interval', 'zoom': 'wheel!'}}};

vegaEmbed("#viz_5", vlSpec_5);
</script>
</div>
