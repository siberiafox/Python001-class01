# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
import pretty_errors
from mysql_config import db_info

class BlackwidowPipeline:
    def process_item(self, item, spider):
        if spider.name == 'cateyes':
            film_name = item['film_name']
            film_type = item['film_type']
            film_rel_date = item['film_rel_date']

            # personal process item by week01
            output = f'{film_name},{film_type},{film_rel_date}\n'
            with open ('./job1_result.csv', 'a+', encoding='utf-8') as fo:
                fo.write(output)
            print('job1_result.csv has dump!')
            return item
        
        elif spider.name == 'freeproxy':
            if item == None:
                return item
            col_names = {
                'ip': 'varchar',
                'port': 'varchar',
                'protocol': 'varchar',
                'validate': 'varchar',
                'speed': 'varchar'
            }
            _saved_mysql(item, col_names, spider.name)
            return item


    # protected method, using default database 'test'
    @staticmethod
    def _saved_mysql(item, col_names, spider_name, db = 'test'):
        # connect mysql
        conn = pymysql.connect(
            host = db_info['host'],
            port = db_info['port'],
            user = db_info['user'],
            password = db_info['pwd'],
            db = db,
            charset = 'utf8mb4'
        )
        # get cursor of this conn
        cur = conn.cursor()
        # saved or rollback
        try:
            # saved in mysql
            cur.execute(f'show tables')
            existed_table = cur.fetchone()
            # print(existed_table)
            if spider_name not in existed_table:
                create_info = ','.join([i + ' ' + j for i,j in col_names.items()])
                cur.execute(f'create table if not exists {spider_name} ({create_info})')
            insert_info = ""
            for i in item.items():
                insert_info+="'"
                insert_info+=str(i[1])
                insert_info+="'"
                insert_info+=","
            insert_info = insert_info[:-1]
            cur.execute(f'insert into {spider_name} values ({insert_info})')
            # print('insertion over!')
            cur.close()
            conn.commit()
        except:
            print('something wrong,db will rollback!')
            conn.rollback()
        finally:
            conn.close()

        



