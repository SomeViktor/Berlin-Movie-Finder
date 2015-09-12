# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


    
class Event(scrapy.Item):
    time = scrapy.Field()
    locationName = scrapy.Field()
    street = scrapy.Field()
    zip = scrapy.Field()
    city = scrapy.Field()
    
class Movie(Event):
    theatreName = scrapy.Field()
    movieName = scrapy.Field()
    movieGenre = scrapy.Field()
    
    
