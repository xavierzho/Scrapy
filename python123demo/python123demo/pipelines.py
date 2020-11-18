# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
# from spiders.settings import MONGO_HOST
from pymongo import MongoClient


class Python123DemoPipeline(object):
    def process_item(self, item, spider):
        # spider.settings.get("MONGO_HOST")
        self.collection.insert(dict(item))
        return item

    def open_spider(self, spider):
        client = MongoClient()
        self.collection = client['库名']['表名']



