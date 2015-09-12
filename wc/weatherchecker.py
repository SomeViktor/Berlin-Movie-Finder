import requests
import datetime
from pymongo import MongoClient

client = MongoClient()
ec = client['ec']
client.ec.drop_collection('weather')

r = requests.get('http://api.openweathermap.org/data/2.5/forecast?q=Berlin,de&mode=json&units=metric')
x = r.json()
weathertimes = x['list']
weather = {}
for timewindow in weathertimes:
    timeOfWeather = datetime.datetime.fromtimestamp(int(timewindow['dt'])).strftime('%Y-%m-%d %H:%M:%S')
    
    if ec.weather.find({'time' : timeOfWeather}).count() == 0:
        weathertime = {}
        weathertime ['text'] = timewindow['weather'] [0] ['main']
        weathertime ['temp'] = timewindow['main'] ['temp']
        weathertime ['time'] = timeOfWeather
        ec.weather.insert_one(weathertime)


for weathertime in ec.weather.find():
    print weathertime['time']
    print ""
    
    