import requests
import json
from pymongo import MongoClient
import time;




def update_locations_db():
    client = MongoClient()
    ec = client.ec;
    ec.drop_collection('locations')
    for event in client.ec.events.find():
        #print client.ec.location.find({'locationName': event['locationName']}).limit(1)
        
        
        #print client.ec.location.find_one({'name': "Blauer Stern"})
        
        if  client.ec.locations.find({'name': event['locationName']}).count() == 0:
            
            name = event['locationName']
            street = event['street']
            zip = event['zip']
            city = event['city']
            geotag = {'lat':-1,'lng':-1}
            locationDoc = {'name' : name,'street':street,'zip':zip,'city':city,'geotag':geotag}
            
            
            client.ec.locations.insert(locationDoc)
            print "current number of found locations: "+ str(client.ec.locations.count())
            
            
            
            
    print "number of locations:"        
    print ec.locations.count()

#first: sort theatres in a seperate collection
#second: check if every theatre has a geotag, if not, request it.
def geotag():
    client = MongoClient()
    ec = client.ec;
    for location in client.ec.locations.find():
        if location['geotag']['lat'] == -1:
            while 1 == 1:
                apiKey = "AIzaSyDl0YjH-dGaRv1AO7T5pLVtgcIQxq9LlGc"


                r = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=' + location['street'] + ' ' +location['zip'] + location['city'] + '&key='+apiKey);

                x = r.json()
                if not x['results']:
                    print "we have to wait for google -_-";
                    print ""
                    time.sleep(10);
                else:    
                    
                    lat = x['results'] [0] ['geometry'] ['location'] ['lat'];
                    lng = x['results'] [0] ['geometry'] ['location'] ['lng'];
                    print location['name'];
                    print lat
                    print lng
                    location['geotag'] ['lat'] = lat;
                    ec.locations.update({'_id':location['_id']},{'$set':{'geotag.lat' : lat, 'geotag.lng' : lng}})
                    location['geotag'] ['lng'] = lng;
                    break;

