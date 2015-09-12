# -*- coding: utf-8 -*-

# Scrapy settings for ec project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'ec'

SPIDER_MODULES = ['ec.spiders']
NEWSPIDER_MODULE = 'ec.spiders'

ITEM_PIPELINES = {
    'ec.pipelines.Pipeline': 300
}

LOG_LEVEL='INFO'    #alt: DEBUG
DUPEFILTER_CLASS ='scrapy.dupefilter.BaseDupeFilter'
DUPEFILTER_DEBUG =True

# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'ec (+http://www.yourdomain.com)'
