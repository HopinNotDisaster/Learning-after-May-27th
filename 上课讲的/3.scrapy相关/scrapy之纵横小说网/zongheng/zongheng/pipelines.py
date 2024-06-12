# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import redis
import hashlib
import json


class DataFilter:
    # 默认的set_name为data_filter
    def __init__(self, set_name="data_filter"):
        self.redis_client = redis.Redis(host="localhost", port=6379, db=3, password="123456")
        self.set_name = set_name

    def is_duplicate(self, data: dict):
        hash_value = hashlib.md5(json.dumps(data).encode('utf-8')).hexdigest()

        if not self.redis_client.sismember(self.set_name, hash_value):
            self.redis_client.sadd(self.set_name, hash_value)
            # print("新数据！", data)
            return False
        else:
            # print("重复数据！", data)
            return True

    def close(self):
        self.redis_client.close()


import pymongo


# 管道模块模式是不激活的，需要在settings中进行激活！
class ZonghengPipeline:
    def __init__(self):
        self.book_filter = DataFilter("book_set")
        self.chapter_filter = DataFilter("chapter_set")
        self.mongo_con = pymongo.MongoClient()

    # 爬虫模块中的每一个item对象，都会被scrapy engine传到这里来！
    def process_item(self, item, spider):
        # 在这里这个item有两种可能！
        item = dict(item)
        if "book_name" in item:
            # 这是一个小说数据！
            if not self.book_filter.is_duplicate(item):
                # zongheng为数据库名字     collection的集合里面有一张book_info表！里面有很多的字典类型的数据！
                self.mongo_con["zongheng"]["book_info"].insert_one(item)
            # print("管道模块接受的数据！", item)
        else:
            # 这是一个章节的数据！
            if not self.chapter_filter.is_duplicate(item):
                self.mongo_con["zongheng"]["chapter_info"].insert_one(item)
                # 把item对象返回给下一个管道
        return item

    # 爬虫模块中的爬虫执行完毕后，会执行close_spider方法
    def close_spider(self, spider):
        self.mongo_con.close()
    #     self.filter.close()
