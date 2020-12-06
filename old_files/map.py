import pandas as pd
import datetime
import folium
from folium.map import *
from folium import plugins
from folium.plugins import MeasureControl
from folium.plugins import FloatImage

prev_day = 11
prev_date_month = 5
prev_date_year = 2015
SF_COORDINATES = (37.76, -122.45)
crimedata = pd.read_csv('.//datasets//demo.csv')
state_geo = './datasets/SFPD.json'

list_of_crimes = ["WARRANTS","OTHER OFFENSES","LARCENY/THEFT","VEHICLE THEFT","VANDALISM","NON-CRIMINAL","ROBBERY","ASSAULT","WEAPON LAWS","BURGLARY","SUSPICIOUS OCC","DRUNKENNESS","FORGERY/COUNTERFEITING","DRUG/NARCOTIC","STOLEN PROPERTY","SECONDARY CODES","TRESPASS","MISSING PERSON","FRAUD","KIDNAPPING","RUNAWAY","DRIVING UNDER THE INFLUENCE","SEX OFFENSES FORCIBLE","PROSTITUTION","DISORDERLY CONDUCT","ARSON","FAMILY OFFENSES","LIQUOR LAWS","BRIBERY","EMBEZZLEMENT","SUICIDE","LOITERING","SEX OFFENSES NON FORCIBLE","EXTORTION","GAMBLING","BAD CHECKS","TREA","RECOVERED VEHICLE","PORNOGRAPHY/OBSCENE MAT"]
list_of_pdistrict = ["NORTHERN","PARK","INGLESIDE","BAYVIEW","RICHMOND","CENTRAL","TARAVAL","TENDERLOIN","MISSION","SOUTHERN"]
count_of_pdistrict = {"NORTHERN":0,"PARK":0,"INGLESIDE":0,"BAYVIEW":0,"RICHMOND":0,"CENTRAL":0,"TARAVAL":0,"TENDERLOIN":0,"MISSION":0,"SOUTHERN":0}
Step 3: Initialize map and cluster segment
# initialize empty map zoomed in on San Francisco
m = folium.Map(location=SF_COORDINATES, zoom_start=13,tiles='CartoDBPositron')
cluster = folium.plugins.MarkerCluster(name="Previous Crimes").add_to(m)


# add a marker for every record in the filtered data, use a clustered view
for each in crimedata[0:878050].iterrows():
    if ((int(each[1]['Day'])==day) and (int(each[1]['Month'])==month) and (int(each[1]['Year'])==year)):
        crime_name = list_of_crimes[int(each[1]['Category'])-1]
        occ_date = "%s-%s-%s"%(str(day),str(month),str(year))
        pdistrict = list_of_pdistrict[int(each[1]['PdDistrict'])-1]
        count_of_pdistrict[pdistrict]=(count_of_pdistrict[pdistrict])+1
        location = "%s,%s"%(each[1]['Y'],each[1]['X'])
        folium.Marker(location = [each[1]['Y'],each[1]['X']], popup='<b>Occured date: </b>%s<br></br><b>Crime Type: </b>%s<br></br><b>Police District: </b>%s<br></br><b>Location: </b>%s'%(occ_date,crime_name,pdistrict,location),).add_to(cluster)


crime_count = open('.//datasets//crime_countdata.csv','w')
crime_count.write('PD,Crime_Count\n')
for key in count_of_pdistrict:
    crime_count.write("%s,%s\n"%(key,str(count_of_pdistrict[key])))
crime_count.close()


state_data = pd.read_csv('./datasets/crime_countdata.csv')
m.choropleth(
    geo_data=state_geo,
    name='choropleth',
    data=state_data,
    columns=['PD', 'Crime_Count'],
    key_on='feature.id',
    fill_color='Reds',
    fill_opacity=0.7,
    line_opacity=0.9,
    legend_name='Crime Rate'
)

non_violent_loc =[[ 37.783003799999996,-122.4124143],[37.77436883,-122.5058834],[37.74491907,-122.47577350000002],[37.71083265,-122.43244650000001]]
violent_loc=[[37.72156474,-122.47318200000001],[37.73511269,-122.4845457],[ 37.73449811,-122.4448541],[37.76978409,-122.449123]]
for loc in non_violent_loc:
    folium.CircleMarker(location=loc, radius=30,
            popup='<b>Prediction Type: </b>Non-Violent Crime<br></br><b>Location: </b>%s'%(loc), line_color='#3186cc',
            fill_color='#FFFFFF',fill_opacity=0.7, fill=True).add_to(m)
for loc in violent_loc:
    folium.CircleMarker(location=loc, radius=30,
            popup='<b>Prediction Type: </b>Violent Crime<br></br><b>Location: </b>%s'%(loc), line_color='#3186cc',
            fill_color='#000000',fill_opacity=0.7, fill=True).add_to(m)


folium.TileLayer(tiles='Stamen Toner',name="Stamen Toner").add_to(m)
folium.TileLayer(tiles='Stamen Terrain',name="Stamen Terrain").add_to(m)
folium.LayerControl().add_to(m)
m.add_child(MeasureControl())
FloatImage(url, bottom=5, left=85).add_to(m)


m.add_child(MeasureControl())
m.save('index.html')
print "Saving the webpage for map...."
