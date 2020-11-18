import scrapy
from scrapy_splash import SplashRequest


class Demo2Spider(scrapy.Spider):
    name = 'demo2'

    def start_requests(self):
        # lua = {'lua_source': """
        # function main(splash, args)
        #     splash:set_custom_headers({['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36
        #     (KHTML, like Gecko) Chrome/84.0.4147.135 Safari/537.36'})
        #     assert(splash:go(args.url))
        #     assert(splash:wait(1))
        #     return splash:html()
        # end
        # """}
        start_urls = 'https://list.suning.com/1-502675-0.html?safp=d488778a.10038.0.f563573a26&safc=cate.0.0&safpn' \
                     '=10006.502320'
        yield SplashRequest(start_urls,
                            callback=self.parse,
                            # endpoint='execute',
                            args={'wait': 1})

    def parse(self, response):
        print(response.text)
        # info_list = response.xpath('//div[@class="res-info"]')
        # for info in info_list:
        #     item = {
        #         'title': info.xpath('./p[@class="sell-point"]/a/text()').extract_first().strip(),
        #         'price': info.xpath('./p[@class="prive-tag"]/em//text()').extract()
        #     }
        #     item['price'] = ''.join(item['price'])
        #     print(item)

