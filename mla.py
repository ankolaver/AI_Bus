#testing platform for the machine learning, not used in production

from flask import Flask, render_template, redirect, url_for, request
import folium
import random
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import os

#opening file from python
#DATA_DIR = './buses/'
#glob
import glob
g = glob.glob('**/*.csv')
#data

df1 = pd.read_csv(g[0])
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
busno = []
for j in df3['Bus number']:
    j = 'Bus Number'+str(j)
    busno.append(j)
print(busno)

#Initialise Dash for the machine learning accuracy visualisation
app = dash.Dash(
    __name__,
    routes_pathname_prefix='/mla/',
    
)


colors = {
    'background': '#000000',
    'text': '#7FDBFF'
}

app.layout = html.Div(
        style={'backgroundColor': colors['background']}, children=[
        html.H1(
        children='Machine Learning Accuracy for various Bus Stops',
        style={
            'textAlign': 'center',
            'color': colors['text']

            }
        ),

        dcc.Graph(
            id='basic-interactions',
            figure={
                'data':[
                go.Scatter(
                x = bustime,
                y = finaldiff,
                hovertext=busno
                )
                ],
                'layout': {
                'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']},
                'xaxis':{
                'title':'Time of the Day'
                },
                'yaxis':{
                'title':'Machine Learning Demand'
                }

                }
                }
            )])