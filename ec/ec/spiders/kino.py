# -*- coding: utf-8 -*-
import scrapy

from scrapy.http import HtmlResponse
from scrapy.selector import Selector
from ec.items import *
import copy

class KinoSpider(scrapy.Spider):
    name = "kino"
    start_urls = (
        'http://www.kino.de/kinoprogramm/berlin/',
    )

    def parse(self, response):
        bigField = response.selector.xpath('//ul[@class="cinema-city-list"]')
        kinos = bigField[0].xpath('li')
                
        
        reqlist = []
        
        print "es wurden so viele kinos gefunden: " + str(len(kinos))
        for kino in kinos:
            movie = Movie()
            
            #Kinoname
            movie['locationName'] = kino.xpath('div/div/a/span/strong/text()').extract()[0];
            #print "KINO: jetzt wird " + movie['locationName'] + " geparst."
            
            #Adresse
            adressenteile = kino.xpath('div/div/span/span/text()').extract()
            movie['street']  = adressenteile[2]
            movie['zip'] = adressenteile[0]
            movie['city'] = adressenteile[1]
            
            #Filme
            
            
            films = kino.xpath('ul/li')
            
               
            for film in films:
                name = film.xpath('div/a/text()').extract()
                times = film.xpath('div[2]/span/p[1]/text()')
                
                if name:
                    movie['movieName'] = name[0];
                else:
                    name =  film.xpath('div/text()').extract()[0].strip(' \n \r')
                    if name:
                        movie['movieName'] = name.strip(' ')

                
                for time in times:
                    movie['time'] = time.extract().strip(' \n \r');
                    detailLink = film.xpath('div/a/@href').extract()
                    
                    if detailLink:
                        #print detailLink
                        #print movie['time']
                        genreUrl = ("http://www.kino.de" + detailLink[0])
                        genreRequest = scrapy.Request(genreUrl, callback=self.parse_genre,dont_filter=True)
                        movie['movieGenre'] = ""
                        genreRequest.meta['movie'] = copy.deepcopy(movie);
                        #print "requesting genre for: " + movie['movieName']
                        #reqlist.append(genreRequest)
                        yield genreRequest                        
                    else:
                        #print "parsed a movie without genre with name: " + movie['movieName']
                        pass
                        #yield movie
        
                   
        nextPageUrl = response.selector.xpath('/html/body/div[2]/div[2]/div[9]/div[2]/div[1]/div[3]/div/div[3]/div[3]/div[3]/a[2]/@href').extract()
        
        if ("http://www.kino.de"+ nextPageUrl[0]) != response.request.url:
            print nextPageUrl;
            nextRequest = scrapy.Request("http://www.kino.de"+ nextPageUrl[0],dont_filter = False)
            yield nextRequest;
        else:
            print "now finished."
            yield None
        
        print "-------------------------------------------------"   
            
            
            
            
            
    def parse_genre(self, response):
        #print "I got a request."
        genres = response.selector.xpath('/html/body/div[2]/div[2]/div[9]/div[2]/div[1]/div/div[2]/div[1]/div[3]/ul/li[1]/span[2]/a/text()').extract();
        movie = response.meta['movie'];
        print movie['movieName'] + " " + movie['locationName'] + " " +movie['time']
        if movie['movieGenre'] != "":
            #print "unclean movie coming in"
            pass
        else:
            for genre in genres:
                movie['movieGenre'] += genre + " ";
                pass
            
            return movie  
        