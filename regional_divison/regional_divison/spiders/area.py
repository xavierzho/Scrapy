import scrapy
from regional_divison.items import RegionalDivisonItem


class AreaSpider(scrapy.Spider):
    name = 'area'
    allowed_domains = ['51240.com']
    start_urls = ['https://xingzhengquhua.51240.com/']

    def parse(self, response):
        tr_list = response.xpath('//tr')
        for tr in tr_list:
            item = RegionalDivisonItem()
            item['area'] = tr.xpath('./td[1]/a/text()').extract_first()
            item['area_code'] = tr.xpath('./td[2]/a/text()').extract_first()
            item['area_url'] = tr.xpath('./td[1]/a/@href').extract()
            item['area_url'] = ["https://xingzhengquhua.51240.com"+i for i in item['area_url']]
            if item['area_code'] is None:
                item.clear()
            if len(item) > 0:
                yield scrapy.Request(item['area_url'][0],
                                     callback=self.parse,
                                     meta={'item': item})

                yield item

