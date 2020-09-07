# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html

from itemadapter import ItemAdapter
import pymysql, json
class SmzdmPipeline:
    # def process_item(self, item, spider):
    #     return item

    def process_item(self,item,spider):
        with open('/root/smzdm/mysql.json','r') as file:
            mysql_conf = json.load(file)
        self.conn = pymysql.connect(
            host = mysql_conf['host'],
            port = mysql_conf['port'],
            user = mysql_conf['user'],
            password = mysql_conf['passwd'],
            database = mysql_conf['dbqipaoshui']
        )
        self.cur = self.conn.cursor()
        values = [item['Name'], item['user_name'], item['comment_content'], item['comment_time'], item['sentiments']]
        try:
            sql = 'insert into product(Name, user_name, comment_content, comment_time, sentiments) \
                 select %s,%s,%s,%s,%s from qipaoshui ;'
            self.cur.execute(sql,values)
            self.cur.close()
            self.conn.commit()
        except Exception as error:
            print(error)
            self.conn.rollback()
        self.conn.close()