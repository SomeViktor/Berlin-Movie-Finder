from pymongo import MongoClient

client = MongoClient()
ec = client['ec']
client.ec.drop_collection('events')
print "Eventcrawler was started."