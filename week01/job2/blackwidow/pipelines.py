# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

class BlackwidowPipeline:
    def process_item(self, item, spider):
        film_name = item['film_name']
        film_type = item['film_type']
        film_rel_date = item['film_rel_date']

        output = f'{film_name},{film_type},{film_rel_date}\n'

        with open ('./job2_result.txt','a+',encoding='utf-8') as fo:
            fo.write(output)
        print('job2_result.txt has dump!')
        
        return item


