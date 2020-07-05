# -*- coding: utf-8 -*-
import scrapy


class HttpbinSpider(scrapy.Spider):
    name = 'httpbin'
    allowed_domains = ['httpbin.org']
    start_urls = ['http://httpbin.org/ip','http://httpbin.org/headers']

    def parse(self, response):
        print(response.text)
