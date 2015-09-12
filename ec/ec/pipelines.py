# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import json
from pymongo import MongoClient

class Pipeline(object):
    def process_item(self, item, spider):
        client = MongoClient()
        ec = client['ec']
        movie = dict(item)
        movie['type'] = 'movie'
        movie['in_out'] = 'in'
        result = ec.events.insert(movie)
        #line = json.dumps(dict(item)) + "\n"
        #self.file.write(line)
        return item

        
    def __init__(self):
        self.file = open('filme.jl', 'wb')