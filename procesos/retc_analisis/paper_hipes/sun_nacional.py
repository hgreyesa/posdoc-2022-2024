import plotly.express as px
import numpy as np
import pandas as pd


f = "out_puts/highlight_nacional_iarc_sun_es.csv"
f_out = "out_plots/highlight_nacional_iarc_sun_es.hmtl"
print("\tIniciando la lectura del archivo: " + f)

emisiones = pd.read_csv(f, low_memory=False, encoding='utf-8')
#data = emisiones.loc[(emisiones["aire"]>0) ]
fig = px.sunburst(emisiones, path=["iarc"], values='percentage')
                  #color='percentage')
                  #hover_data=['percentage'], color_continuous_scale=[[0, 'yellow'], [66, 'orange'], [100, 'red']])
                  #color_continuous_midpoint=np.average(emisiones['percentage'], weights=emisiones['percentage']))
#fg.update_layout(uniformtext = dict(minsize = 12, mode = 'hide'))   
#fig.update_traces(texttemplate='%{text}', textposition='inside')

fig.update_layout({
"plot_bgcolor": "rgba(0, 0, 0, 0)",
"paper_bgcolor": "rgba(0, 0, 0, 0)",
})

fig.update_layout(margin = dict(t=0, l=0, r=0, b=0))

#fig.show() 

fig.write_html(f_out)
fig.write_image(file="out_plots/sun_nacional_es.png", scale=3)




