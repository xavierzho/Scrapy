import scrapy
import json
from tencent.items import TencentItem


class HrSpider(scrapy.Spider):
    name = 'hr'
    allowed_domains = ['tencent.com']
    start_urls = ['https://careers.tencent.com/tencentcareer/api/post/Query?pageIndex=1&pageSize=10']

    def parse(self, response):
        item = TencentItem()
        data = json.loads(response.text)
        data_list = data['Data']['Posts']
        for data in data_list:
            item['CategoryName'] = data['CategoryName']
            item['CountryName'] = data['CountryName']
            item['LastUpdateTime'] = data['LastUpdateTime']
            item['PostId'] = data['PostId']
            item['PostURL'] = data['PostURL']
            item['ProductName'] = data['ProductName']
            item['RecruitPostName'] = data['RecruitPostName']
            item['Responsibility'] = data['Responsibility']
            item['BGName'] = data['BGName']
            yield item

        # total_page = data['Data']['Count'] / 10
        # print(type(total_page))
        urls = ['https://careers.tencent.com/tencentcareer/api/post/Query?pageIndex={}&pageSize=10'.format(i) for i in range(2, 615 + 2)]

        for url in urls:
            yield scrapy.Request(url, callback=self.parse)
