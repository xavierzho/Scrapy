# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
# import logging
#
# logger = logging.getLogger(__name__)


class ItcastPipeline:
    def process_item(self, item, spider):
        # print(item)
        if item['come_from'] == 'itcast':
            # logger.warning('-'*20)
            return item


# class ItcastPipeline2:
#     def process_item(self, item, spider):
#         print(item)
#         return item
