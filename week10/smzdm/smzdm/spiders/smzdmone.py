# -*- coding: utf-8 -*-

import scrapy

from smzdm.items import SmzdmItem
from scrapy.selector import Selector
from .smzdm_one import datasmzdm

class SmzdmoneSpider(scrapy.Spider):
    name = 'smzdmone'
    allowed_domains = ['smzdm.com']
    start_urls = ['https://www.smzdm.com/fenlei/qipaoshui/']

    # def parse(self, response):
    #     pass

# 开始爬虫的内容
def parse(self,response):
    urLList = response.xpath('//ul[@id="feed-main-list"]/li[position()<=10]//h5/a/@href').extract()
    for urL in urLList:
        yield scrapy.Request(url = urL, callback=self.check_page, meta={'url': urL})


    def check_page(self, response):
        pageList = response.xpath('//*[@id="comment"]/div[1]/ul[@class="pagination"]/li[position()<last()-2]/a/@href').extract()
        for page in pageList:
            yield scrapy.Request(url = page, callback=self.get_inforpage)
        


    def get_inforpage(self, response):
        Name = response.xpath('//article//h1/text()').extract()[0].replace(' ','').replace('\n','')
        comments = response.xpath('//div[@id="commentTabBlockNew"]//li/div[2]')
        item = SmzdmItem()
        for pinglong in comments:
            user_name = pinglong.xpath('.//a[@class="a_underline user_name"]/span/text()').extract()[0]
            comment_time = pinglong.xpath('.//div[@class="time"]/meta/@content').extract()[0]
            comment_content = pinglong.xpath('./div[@class="comment_conWrap"]/div[1]/p/span/text()').extract()
            content = ''.join(comment_content).replace(' ','')
            item['Name'] = Name
            item['username'] = user_name
            item['comment_content'] = content
            item['sentiments'] = datasmzdm(content)
            item['comment_time'] = comment_time
            yield item