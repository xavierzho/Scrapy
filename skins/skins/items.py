# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class SkinsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    hero_name = scrapy.Field()
    image_urls = scrapy.Field()
    image_name = scrapy.Field()
