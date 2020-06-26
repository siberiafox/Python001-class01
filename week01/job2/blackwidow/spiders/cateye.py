# -*- coding: utf-8 -*-
import scrapy


class CateyeSpider(scrapy.Spider):
    name = 'cateye'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    def parse(self, response):
        pass
