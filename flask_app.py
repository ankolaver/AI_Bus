from flask import Flask, render_template, redirect, url_for
from flask import request
import folium
import random
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from dash.dependencies import Input, Output
import glob
import time
import requests
import json
from busstop import bstopcoor
#main

'''Extracting of Bus Stops into an array'''
#refer to busstop.py for the extraction from the LTA dataset
'''End of extraction'''

server = Flask(__name__)

import pyowm
#account key
owm = pyowm.OWM('29039888ecce7edd94fe4a51361c0faa')
#observation = owm.weather_at_place("Singapore")

#fc = owm.three_hours_forecast('Singapore')
#fc.will_have_rain()
@server.route("/")
def index():
	#initialising the main map
	busmap2 = folium.Map(location=[1.3461471, 103.823874],
						tiles='Stamen Toner',
	 					zoom_start=12,
						width='100%',
						height='80%')
	bus1latlon = []
	for k in range(0,random.randint(1,35)):
		a = random.uniform(1.30,1.35)
		b = random.uniform(103.71,103.90)
		bus1latlon.append((a,b))


	'''start of markers for individual buses'''
	for coor in bus1latlon:
		folium.Marker(popup=str(random.randint(0,60))+"/90 people full", location=coor,icon=folium.Icon(color='blue', icon='bus', prefix='fa')).add_to(busmap2)

	#marker for example case
	folium.Marker(location=[1.29684825487647,103.85253591654006],popup='76/85 people full',icon=folium.Icon(color='red', icon='bus', prefix='fa')).add_to(busmap2)

	#marker for the maps
	'''Start of markers for busstop'''
	for coor in bstopcoor:
		'''weather, not used due to API restrictions'''
		'''
		lat = float(coor[0])
		long = float(coor[1])
		observation = owm.weather_at_coords(lat,long)
		w = observation.get_weather()
		rainfall = w.get_rain()
		temperature = w.get_temperature('celsius')
		temperature = temperature['temp']
		#main
		if len(rainfall)==0:
			rainfall = "No rain"
		else:
			rainfall = "Raining"
		'''
		#folium.Circle(popup=str(random.randint(6,14))+" people predicted boarding \n"+rainfall+"\n  Current Temperature:\n"+str(temperature),radius=10,location=coor,fill=True, color='orange').add_to(busmap2)
		folium.Circle(popup=str(random.randint(6,14))+" people predicted boarding \n",radius=10,location=coor,fill=True, color='orange').add_to(busmap2)
		print(coor)
	'''End of markers for bus stops'''

	busmap2.save('templates/map1.html')
	bus1latlon.clear()
	return render_template("index2.html")


'''Plotly, Dash to make a graph'''
#opening file from python
DATA_DIR = './buses/'

#glob to locate the main csv file in sub folder
g = glob.glob('**/*.csv')


#extracting of data
df1 = pd.read_csv(g[0])
df3 = df1[['Timings','Bus 1','Bus 2']]

#mldiff = df3['ML Diff']
finaldiff = []
'''
for i in mldiff:
    finaldiff.append(i)
'''
timings = df3['Timings']
bustime = []
for i in timings:
    bustime.append(i)
#print(bustime)

#Initialise Dash for the machine learning accuracy visualisation
app = dash.Dash(
	__name__,
	server=server,
	routes_pathname_prefix='/dash/'
)

colors = {
    'background': '#000000',
    'text': '#7FDBFF'
}

app.layout = html.Div(
		style={'backgroundColor': colors['background']},
		children=[
    	html.H1(
        children='Machine Learning Accuracy for Various Bus Services at a Bus Stop',
        style={
            'textAlign': 'center',
            'color': colors['text']

        	}
		),

        dcc.Graph(
            id='basic-interactions'
        	),

		dcc.Input(id='my-id', value='Bus 1', type='text'),
			])

#callback component to view different bus demand differences

#output  'my-div'is a property of component id 'children'
#input 'value' is a property of component id 'myid'
@app.callback(
	Output('basic-interactions', 'figure'),
	[Input('my-id', 'value')])

def diffbusmap(input_value):
	input_value = str(input_value)
	print(input_value)
	currbus = df3[input_value]
	finalbus = []
	for j in currbus:
		finalbus.append(j)
	traces = []
	traces.append(go.Scatter(
				x = bustime,
				y = finalbus
				))
	return {
        'data': traces,
        'layout': {
				'plot_bgcolor': colors['background'],
                'paper_bgcolor': colors['background'],
                'font': {
                    'color': colors['text']},
				'xaxis':{
                'title':'Time of the Day'
            	},
            	'yaxis':{
                 'title':'Difference in Predicted Machine Learning Demand for the Bus'
            	}
        		}

    }
'''values were added back to the main function'''

#machine learning accuracy to connect to secondary check machine learning accuracy app
@server.route("/machine_learning_accuracy", methods=["GET","POST"])
def machinelaccuracy():
	return app.index()

'''
	if request.method == 'POST':
		if request.form.get('inputbutton') == 'Bus Number 2':
			print("bus number 2")
			#mla.machineaccuracy()
		elif request.form.get('inputbutton') == 'Bus Number 1':
			print("hi")
			#mla.machineaccuracy(0,server)
	elif request.method =='GET':
		return render_template("mla.html")
'''


#telegram messaging function
@server.route("/available_buses")
def avail_bus():
	return render_template("avail_buses.html")


if __name__ == '__main__':
    server.run(debug=True)

#trash

'''
print(df2)

plt.bar(xx,yy,width=0.8,bottom=None,align='center')
plt.show()
fig = px.bar(df2, y='Difference', x='Bus Timings')
fig.show()

@app.callback(
	dash.dependencies.Output('button_return', 'children'),
	[dash.dependencies.Input('button', 'n_clicks')])
def return_page(n_clicks):
	#if n_clicks is not None:
	#return redirect(url_for('index'))
	return "this is the {} of clicks".format(n_clicks)


html.Button('Back to main page', id='button'),
html.Div([
	dcc.Markdown("""
		**Hover Data**
		Mouse over values in the graph.
	"""),
	html.Pre(id='hover-data')
], className='three columns'),




figure={
                'data':[
				go.Scatter(
				#x = bustime,
				#y = finaldiff,
				#hovertext=busno
				x = df3[df3[busnumber]==input],
				y = bustime
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
                 'title':'Machine Learning Demand for the bus'.format()
            	}
        		}
        		}
'''
