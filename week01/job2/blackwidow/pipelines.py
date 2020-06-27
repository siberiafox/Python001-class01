# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

class BlackwidowPipeline:
    def process_item(self, item, spider):
        file_name = item['file_name']
        file_type = item['file_type']
        file_rel_date = item['file_rel_date']

        output = f'{file_name},{file_type},{file_rel_date}'

        with open ('./PAC3/week01/job2_result.csv','a+',encoding='utf8') as fo:
            fo.write(output)
        
        return item


