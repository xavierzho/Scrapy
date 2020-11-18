# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BlockchainItemBase(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    symbol = scrapy.Field()

    def __str__(self):
        return ''


class BlockchainMongoItem(BlockchainItemBase):
    collection = scrapy.Field()
    item_type = scrapy.Field()
    response_url = scrapy.Field()
    spider_ident = scrapy.Field()
    no_item_log = scrapy.Field()

    mongo_update_instruction = scrapy.Field()
