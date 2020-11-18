# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TencentItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    CategoryName = scrapy.Field()
    CountryName = scrapy.Field()
    LastUpdateTime = scrapy.Field()
    PostId = scrapy.Field()
    PostURL = scrapy.Field()
    ProductName = scrapy.Field()
    RecruitPostName = scrapy.Field()
    Responsibility = scrapy.Field()
    BGName = scrapy.Field()



