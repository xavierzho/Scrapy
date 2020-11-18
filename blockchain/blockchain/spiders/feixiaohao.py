import scrapy


class FeixiaohaoSpider(scrapy.Spider):
    name = 'feixiaohao'  # 爬虫名
    allowed_domains = ['https://www.feixiaohao.com/']  # 允许爬虫范围
    start_urls = ['https://www.feixiaohao.com/']  # 最开始请求地址

    def parse(self, response):
        # 处理start_url对应的响应
        response.xpath("")
        pass
