import dash
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd
import random
from flask import Flask, render_template
import plotly.graph_objs as go

app = dash.Dash()
#getting data
df1 = pd.read_csv('maincoor.csv')
df3 = df1[['Bus number','ML Diff','Timings']]
mldiff = df3['ML Diff']
finaldiff = []
for i in mldiff:
    finaldiff.append(i)
timings = df3['Timings']
bustime = []
for i in timings:
    bustime.append(i)
print(finaldiff)
print(bustime)


app.layout = html.Div(
        dcc.Graph(
            id='scatter_chart',
            figure={
                'data':[
                    {'x':bustime,
                    'y':finaldiff,
                    'type':'bar'
                    }
                ],
        		'layout': go.Layout(
                title='Dash Machine Learning Accuracy for various Bus Stops'
        		)
        		}
        	)
    )
#fig = px.scatter(df3, y='ML Diff', x='Timings', hover_name='Bus number')
#write scatter plot to html
#fig.write_html('mlaccuracy.html', auto_open=True)
#fig.show()

if __name__ == '__main__':
    #refreshes server constantly
    app.run_server()
