# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from blackwidow.items import BlackwidowItem as BW

class CateyeSpider(scrapy.Spider):
    name = 'cateye'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/']


    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url, callback=self.parse2, meta={'cookiejar':1}, dont_filter=True)

    def parse(self, response):
        pass

    def parse2(self,response):
        parser = Selector(response)
        films = parser.xpath('//*[@id="app"]/div/div[2]/div[2]/dl/dd')
        for film in films:
            bw_item = BW()
            film_name = film.xpath('./div[1]/div[2]/a/div/div[2]/@title').extract_first().strip()
            film_type = film.xpath('./div[1]/div[2]/a/div/div[2]/text()').extract_first().strip()
            film_rel_date = film.xpath('./div[1]/div[2]/a/div/div[4]/text()').extract_first().strip()
            bw_item['film_name'] = film_name
            bw_item['film_type'] = film_type
            bw_item['film_rel_date'] = film_rel_date
            yield bw_item
        
