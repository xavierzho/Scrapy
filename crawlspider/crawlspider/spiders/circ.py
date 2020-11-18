import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CircSpider(CrawlSpider):
    name = 'circ'
    allowed_domains = ['example.com']
    start_urls = ['http://www.example.com']

    rules = (
        Rule(LinkExtractor(allow=r'href="(https:\/\/www\.iana\.org\/domains\/example)"')),
        # Rule(LinkExtractor(allow=('item\.php',)), callback='parse_item'),
    )

    def parse_item(self, response):
        pass

