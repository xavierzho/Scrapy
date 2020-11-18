# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from pymongo import MongoClient
from scrapy.exceptions import DropItem

client = MongoClient()
collection = client['tencent']['hr']


class TencentPipeline:
    def __init__(self):
        self.postId_seen = set()

    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        if adapter['PostId'] in self.postId_seen:
            raise DropItem("Duplicate item found:%r" % item)
        else:
            self.postId_seen.add(adapter['PostId'])
            collection.insert(item)
            return item
