# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from blackwidow.items import BlackwidowItem


class CateyesSpider(scrapy.Spider):
    name = 'cateyes'
    allowed_domains = ['maoyan.com']
    start_urls = ['http://maoyan.com/']

    def start_requests(self):
        url = 'https://maoyan.com/films?showType=3'
        yield scrapy.Request(url, callback = self.parse)

    def parse(self, response):
        parser = Selector(response)
        films = parser.xpath('//dd')

        for film in films[:10]:
            bw_item = BlackwidowItem()
            film_name = film.xpath('./div[1]/div[2]/a/div/div[2]/@title').extract_first().strip()
            film_type = film.xpath('./div[1]/div[2]/a/div/div[2]/text()').extract()
            film_rel_date = film.xpath('./div[1]/div[2]/a/div/div[4]/text()').extract()
            bw_item['film_name'] = film_name
            bw_item['film_type'] = film_type[1].split()[0]
            bw_item['film_rel_date'] = film_rel_date[1].split()[0]
            yield bw_item
