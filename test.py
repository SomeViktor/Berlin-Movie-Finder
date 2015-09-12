sys.path.append('/ec/')

from geocoder import *
from reqhan import *

#from time to time:


#update_locations_db()
#geotag()




#ordinary request:
events = getEventsBy(52.534986,13.384173,1,6000)
print "+++++++++++++++++++++++++++++++++++++++++++++"
print "Filme in deiner Naehe:"
for event in events:
    print event['movieName'] + "  " + event['time'] +"  " +event['locationName']
    pass
