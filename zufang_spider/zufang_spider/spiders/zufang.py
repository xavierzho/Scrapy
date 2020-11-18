import scrapy
from zufang_spider.zufang_spider.items import ZufangSpiderItem


class zufangSpider(scrapy.Spider):
    name = 'zufang'
    start_url = ['https://gz.zu.anjuke.com/fangyuan/fanyu/p1/']

    def parse(self, response):
        for zufang_item in response.xpath("//div[@class='zu-itemmod']"):
            yield {
                "title": zufang_item.xpath("//div[@class='zu-info']/h3/a/b/text()").extract(),
                'price': zufang_item.xpath("//div[@class='zu-side']/p/strong/b/text()").extract()+'元/每月',
                'areas': zufang_item.xpath("//div[@class='zu-side']/p/strong/b/text()").extract(),
                'district': zufang_item.xpath("//div[@class='zu-side']/p/strong/b/text()").extract()
            }
        next_page_url = response.xpath("//div[@class='page-content']/div[@class='multi-page']/a[1]/@href").extract()
        if next_page_url is not None:
            yield scrapy.Request(response.url(next_page_url))
