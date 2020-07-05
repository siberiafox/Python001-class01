# -*- coding: utf-8 -*-
import scrapy
from items import BlackwidowItem

class FreeproxySpider(scrapy.Spider):
    name = 'freeproxy'
    allowed_domains = ['ip.jiangxianli.com']
    start_urls = ['http://ip.jiangxianli.com/']

    def start_requests(self):
        url = 'https://ip.jiangxianli.com/api/proxy_ips'
        yield scrapy.Request(url)

    def parse(self, response):
        try:
            # return dataset in the json format
            result = response.json()['data']
            # get the key's information
            for proxy in result:
                bw_item = BlackwidowItem()
                bw_item['proxy_ip'] = result['ip']
                bw_item['proxy_port'] = result['port']
                bw_item['proxy_protocol'] = result['protocol']
                bw_item['proxy_validate'] = result['validated_at']
                bw_item['proxy_speed'] = result['speed']
                yield bw_item
        except Exception as e:
            print(e)
            yield None
        


        
