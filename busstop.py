import json
import requests


#Extracting of Bus Stops into an array


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
print(len(bstopcoor))
