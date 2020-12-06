import pyowm
#account key
owm = pyowm.OWM('29039888ecce7edd94fe4a51361c0faa')
observation = owm.weather_at_place("Singapore")
w = observation.get_weather()
wind = w.get_wind()
temperature = w.get_temperature('celsius')

#main
print(w)
print(wind)
print(temperature)

'''
from wwo_hist import retrieve_hist_data
import os
oschdir("")
'''
from ics import Calendar, Event
c = Calendar()
e = Event()
e.name = "My cool event"
e.begin = '20140101 00:00:00'
c.events.add(e)
c.events
# [<Event 'My cool event' begin:2014-01-01 00:00:00 end:2014-01-01 00:00:01>]
with open('my.ics', 'w') as my_file:
    my_file.writelines(c)
# and it's done !
