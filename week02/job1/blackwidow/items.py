# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BlackwidowItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()

    # items for cateyes spider, WARNING:this items not fit 'piplines.BlackwidowPipeline.saved_mysql' method
    film_name = scrapy.Field()
    film_type = scrapy.Field()
    film_rel_date = scrapy.Field()

    # items for freeproxy spider
    proxy_ip = scrapy.Field()
    proxy_port = scrapy.Field()
    proxy_protocol = scrapy.Field()
    proxy_validate = scrapy.Field()
    proxy_speed = scrapy.Field()
