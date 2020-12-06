from flask import Flask, request
import folium
import random
import requests
app = Flask(__name__)

@app.route('/')
def index():
    #setting the default locations for the buses
    mapit = folium.Map(location=[1.3461471, 103.832875], zoom_start=11.7)
    bus1latlon = [(1.297353, 103.858873)]
    for coord in bus1latlon:
        folium.Marker(location=coord, fill_color='#D2691E',radius=8).add_to(mapit)

    '''bus stops markers'''
    bstops = 'http://datamall2.mytransport.sg/ltaodataservice/BusStops'

    headers = {
       'AccountKey': '2/WzCwKgTqC1lGzOtcidNg==',
       'accept': 'application/json'
    }

    data = requests.get(bstops, headers=headers).text
    maindata = json.loads(data)
    values = maindata['value']
    longitude = []
    latitude = []
    for indiv in values:
        longitude.append(indiv['Longitude'])
    for indiv2 in values:
        latitude.append(indiv2['Latitude'])
    bstopcoor = list([(i,k) for i, k in zip(latitude,longitude)])

    for coor in bstopcoor:
        folium.Circle(popup=str(random.randint(6,14))+" people predicted boarding",radius=10,location=coor,fill=True, color='orange').add_to(busmap2)

    mapit.save('templates/testmap.html')
	#bus1latlon.clear()
    return render_template("testmap.html")

    '''end of bus stop markers'''
if __name__ == '__main__':
    app.run(debug=True)
