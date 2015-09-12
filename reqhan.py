from pymongo import MongoClient
import math
from datetime import datetime
from datetime import time ,date,timedelta

def distance(lat1,lng1,lat2,lng2): # calculate distance in meters
    R = 6371000
    lngR1 = math.radians(lng1)
    lngR2 = math.radians(lng2)
    latR1 = math.radians(lat1)
    latR2 = math.radians(lat2)
    x = (lngR2-lngR1) * math.cos((latR1+latR2)/2);
    y = (latR2-latR1);
    distance = math.sqrt(x*x + y*y) * R;
    return distance



#myLat = 52.534986
#myLng = 13.384173
#maxDist = 2000

def getNearbyLocations(myLat,myLng,maxDist): #getNearby eventlocations

    return returnList

    
def getEventsBy(myLat,myLng,maxHoursToWait,maxDist): #get fitting events regarding to time and place
    #First of all: get locations nearby.
    client = MongoClient()
    ec = client.ec;
    locationsNearby = []
    for location in ec.locations.find():
        if distance(myLat,myLng,location['geotag']['lat'],location['geotag']['lng']) < maxDist:
            locationsNearby.append(location['name'])


    deltaZero = timedelta(hours=0)
    now = datetime.combine( date.today(),datetime.now().time() )
    for weathertime in ec.weather.find():
        timeTillWeather = datetime.strptime(weathertime['time'],'%Y-%m-%d %H:%M:%S') - now)
        if ( timeTillWeather < timedelta(hours=maxHoursToWait) and timeTillWeather > deltaZero):#is this weathertime relevant?
            print weathertime;
    returnList = []
    for event in ec.events.find():
        if event['locationName'] in locationsNearby: #is the event at a nearby location?
            eventTime = datetime.combine( date.today(), datetime.strptime(event['time'], "%H:%M").time() )
            
            
            timeDif = eventTime - now
            delta = timedelta(hours=maxHoursToWait)
            
            
            if (timeDif < delta) and (timeDif >= deltaZero): #is this event in the desired timeframe?
                returnList.append(event)
    return returnList
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
