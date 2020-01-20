#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# import scrapy, crawler and json
import scrapy
from scrapy.crawler import CrawlerProcess
import json


# In[ ]:


# Set up pipeline for JSON file
class Pipeline(object):
    def open_spider(self, response):
        self.file = open('season.jl', '2019')
        
    def close_spider(self, response):
        self.file.close()


# In[ ]:


# Set spider
class MlsSpider(scrapy.Spider):
    name = 'Team Data'
    start_urls = ['https://www.mlssoccer.com/stats/team?year=2019&season_type=REG&op=Search&form_build_id=form-fT6I1AO5rTjQ658l5USqDMozv7zc3WNR7WeBuszsI8I&form_id=mp7_stats_hub_build_filter_form'
                 ]
    def parse(self, response):
        for season in response.xpath("//table[2]"):
            yield {
                'Season Stats': season.xpath("//table[2]").extract_first()
            }


# In[ ]:


# Start scraper
scrape = CrawlerProcess()
scrape.crawl(MlsSpider)
scrape.start()


# In[ ]:


data = 'Team Data.json'
data.head()
data.to_csv('2019 Stats(Team).csv')


#  Extra Season links - Add callback function to automate leads
#   'https://www.mlssoccer.com/stats/team?year=2018&season_type=REG&op=Search&form_build_id=form-fT6I1AO5rTjQ658l5USqDMozv7zc3WNR7WeBuszsI8I&form_id=mp7_stats_hub_build_filter_form',
#    'https://www.mlssoccer.com/stats/team?year=2017&season_type=REG&op=Search&form_build_id=form-fT6I1AO5rTjQ658l5USqDMozv7zc3WNR7WeBuszsI8I&form_id=mp7_stats_hub_build_filter_form',
#    'https://www.mlssoccer.com/stats/team?year=2016&season_type=REG&op=Search&form_build_id=form-fT6I1AO5rTjQ658l5USqDMozv7zc3WNR7WeBuszsI8I&form_id=mp7_stats_hub_build_filter_form'
#    'https://www.mlssoccer.com/stats/team?year=2015&season_type=REG&op=Search&form_build_id=form-fT6I1AO5rTjQ658l5USqDMozv7zc3WNR7WeBuszsI8I&form_id=mp7_stats_hub_build_filter_form
#    'https://www.mlssoccer.com/stats/team?year=2014&season_type=REG&op=Search&form_build_id=form-fT6I1AO5rTjQ658l5USqDMozv7zc3WNR7WeBuszsI8I&form_id=mp7_stats_hub_build_filter_form'
# 
# Defining pipeline for use in jupyter notebook
# 
# next_page = response.xpath('') 
#     class Pipeline(object):
#     def open_spider(self, response):
#         self.file = open('season.jl', '2019')
#     def close_spider(self, response):
#         self.file.close()
#     def process_item(self, item, response):
#         line = json.dumps(dict(item))
#         self.file.write(line)
#         return item
#     
#     custom_settings = {
#         'ITEM_PIPELINES': {'item.Pipeline'}, 
#         'FEED_FORMAT':'json',                                 
#         'FEED_URI': 'season.json'                        
#     }
