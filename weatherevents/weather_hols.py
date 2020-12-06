
import pyowm
#account key
owm = pyowm.OWM('29039888ecce7edd94fe4a51361c0faa')
#observation = owm.weather_at_place("Singapore")
observation = owm.weather_at_coords(1.29684825487647,103.85253591654006)
w = observation.get_weather()
wind = w.get_wind()
temperature = w.get_temperature('celsius')
rain = w.get_rain()
if len(rain)==0:
    rain = "its not raining"

#main
print(w)
print(wind)
print(temperature)
print(rain)


'''
from wwo_hist import retrieve_hist_data
import os
oschdir("")
'''
x = (135,633)
print((x[0],x[1]))

