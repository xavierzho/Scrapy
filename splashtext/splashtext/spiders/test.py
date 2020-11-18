import scrapy
from scrapy_splash import SplashRequest


class TestSpider(scrapy.Spider):
    name = 'test'

    def start_requests(self):
        lua = {"lua_source": """
        function main(splash, args)
            splash:go(args.url)
            splash:wait(1)
            splash:runjs("document.getElementsByClassName('page clearfix')[0].scrollIntoView(true)")
            splash:wait(1)
            return splash:html()
        end
        """
               }
        url = 'https://list.jd.com/list.html?cat=1713%2C3258%2C3297&page=1&s=1&click=0'
        yield SplashRequest(url, args=lua, endpoint='execute', callback=self.parse)

    def parse(self, response):
        div_list = response.xpath('//div[@class="gl-i-wrap"]')
        for div in div_list:
            name = div.xpath('./div[@class="p-name"]/a/em/text()').extract_first().strip()
            price = ''.join(div.xpath('./div[@class="p-price"]/strong//text()').extract()).strip()
            print(name, price)
