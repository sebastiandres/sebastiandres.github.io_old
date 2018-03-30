---
layout: post
title: "Test-8-One-complex-Altair"
excerpt: 
categories: [tutorial, jekyll] 
tags: jekyll, ipynb, notebook
---
<div class="header">
Link al archivo ipython notebook original:
<a href="https://raw.githubusercontent.com/sebastiandres/sebastiandres.github.io/master/ipynb/Test-8-One-complex-Altair.ipynb">Test-8-One-complex-Altair.ipynb</a>.
</div>
<br>
Este notebook de jupyter lab contiene diversos graficos en Altair que se convierten automaticamente 

## 3 - Grafico con display de valores

<div class="in-prompt prompt-common">In [4]:</div>

<div class="input">
{% highlight python %}
import altair as alt
import pandas as pd
import numpy as np

np.random.seed(42)
N_sample = 10
data = pd.DataFrame(np.cumsum(np.random.randn(N_sample, 3), 0).round(2),
                    columns=['A', 'B', 'C'], index=pd.RangeIndex(N_sample, name='x'))
data = data.reset_index().melt('x', var_name='category', value_name='y')

# Create a selection that chooses the nearest point & selects based on x-value
nearest = alt.selection(type='single', nearest=True, on='mouseover',
                        fields=['x'], empty='none')

# The basic line
line = alt.Chart().mark_line(interpolate='basis').encode(
    x='x:Q',
    y='y:Q',
    color='category:N'
)

# Transparent selectors across the chart. This is what tells us
# the x-value of the cursor
selectors = alt.Chart().mark_point().encode(
    x='x:Q',
    opacity=alt.value(0),
).properties(
    selection=nearest
)

# Draw points on the line, and highlight based on selection
points = line.mark_point().encode(
    opacity=alt.condition(nearest, alt.value(1), alt.value(0))
)

# Draw text labels near the points, and highlight based on selection
text = line.mark_text(align='left', dx=5, dy=-5).encode(
    text=alt.condition(nearest, 'y:Q', alt.value(' '))
)

# Draw a rule at the location of the selection
rules = alt.Chart().mark_rule(color='gray').encode(
    x='x:Q',
).transform_filter(
    nearest.ref()
)

# Put the five layers into a chart and bind the data
chart = alt.layer(line, selectors, points, rules, text,
                  data=data, width=600, height=300)
chart#.interactive()
{% endhighlight %}
</div>

<div class="output-prompt prompt-common">Out [4]:</div>

<div class='execute_results'>
  <!-- Container for the visualization -->
  <div id="viz_4"></div>
  <script>
  var vlSpec_4 = 
{'$schema': 'https://vega.github.io/schema/vega-lite/v2.json', 'config': {'view': {'height': 300, 'width': 400}}, 'data': {'values': [{'category': 'A', 'x': 0, 'y': 0.5}, {'category': 'A', 'x': 1, 'y': 2.02}, {'category': 'A', 'x': 2, 'y': 3.6}, {'category': 'A', 'x': 3, 'y': 4.14}, {'category': 'A', 'x': 4, 'y': 4.38}, {'category': 'A', 'x': 5, 'y': 3.82}, {'category': 'A', 'x': 6, 'y': 2.91}, {'category': 'A', 'x': 7, 'y': 2.69}, {'category': 'A', 'x': 8, 'y': 2.14}, {'category': 'A', 'x': 9, 'y': 2.52}, {'category': 'B', 'x': 0, 'y': -0.14}, {'category': 'B', 'x': 1, 'y': -0.37}, {'category': 'B', 'x': 2, 'y': 0.4}, {'category': 'B', 'x': 3, 'y': -0.07}, {'category': 'B', 'x': 4, 'y': -1.98}, {'category': 'B', 'x': 5, 'y': -2.99}, {'category': 'B', 'x': 6, 'y': -4.41}, {'category': 'B', 'x': 7, 'y': -4.34}, {'category': 'B', 'x': 8, 'y': -4.23}, {'category': 'B', 'x': 9, 'y': -4.83}, {'category': 'C', 'x': 0, 'y': 0.65}, {'category': 'C', 'x': 1, 'y': 0.41}, {'category': 'C', 'x': 2, 'y': -0.06}, {'category': 'C', 'x': 3, 'y': -0.52}, {'category': 'C', 'x': 4, 'y': -2.25}, {'category': 'C', 'x': 5, 'y': -1.93}, {'category': 'C', 'x': 6, 'y': -0.47}, {'category': 'C', 'x': 7, 'y': -1.89}, {'category': 'C', 'x': 8, 'y': -3.04}, {'category': 'C', 'x': 9, 'y': -3.33}]}, 'height': 300, 'layer': [{'encoding': {'color': {'field': 'category', 'type': 'nominal'}, 'x': {'field': 'x', 'type': 'quantitative'}, 'y': {'field': 'y', 'type': 'quantitative'}}, 'mark': {'interpolate': 'basis', 'type': 'line'}}, {'encoding': {'opacity': {'value': 0}, 'x': {'field': 'x', 'type': 'quantitative'}}, 'mark': 'point', 'selection': {'selector005': {'empty': 'none', 'fields': ['x'], 'nearest': True, 'on': 'mouseover', 'resolve': 'global', 'type': 'single'}}}, {'encoding': {'color': {'field': 'category', 'type': 'nominal'}, 'opacity': {'condition': {'selection': 'selector005', 'value': 1}, 'value': 0}, 'x': {'field': 'x', 'type': 'quantitative'}, 'y': {'field': 'y', 'type': 'quantitative'}}, 'mark': 'point'}, {'encoding': {'x': {'field': 'x', 'type': 'quantitative'}}, 'mark': {'color': 'gray', 'type': 'rule'}, 'transform': [{'filter': {'selection': 'selector005'}}]}, {'encoding': {'color': {'field': 'category', 'type': 'nominal'}, 'text': {'condition': {'field': 'y', 'selection': 'selector005', 'type': 'quantitative'}, 'value': ' '}, 'x': {'field': 'x', 'type': 'quantitative'}, 'y': {'field': 'y', 'type': 'quantitative'}}, 'mark': {'align': 'left', 'dx': 5, 'dy': -5, 'type': 'text'}}], 'width': 600};

vegaEmbed("#viz_4", vlSpec_4);
</script>
</div>
