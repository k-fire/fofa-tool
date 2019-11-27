# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class FofaItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    domain = scrapy.Field()
    ip = scrapy.Field()
    title = scrapy.Field()
    pass
