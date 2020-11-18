import scrapy
from skins.items import SkinsItem
from scrapy_splash import SplashRequest


class LolSpider(scrapy.Spider):
    name = 'lol'
    allowed_domains = ['qq.com']
    start_urls = ['https://lol.qq.com/data/info-heros.shtml']
    lua_scripts = """
                    function main(splash)
                        splash:go(splash.args.url)
                        splash:wait(1)
                        return splash:html()
                    end
                    """

    def start_requests(self):
        header = {'referer': 'https://lol.qq.com'}
        yield SplashRequest(self.start_urls[0], args={'lua_source': self.lua_scripts}, headers=header)

    def parse(self, response):

        # print(response)
        item = SkinsItem()
        # item['hero_name'] = response.xpath('//ul[@id="jSearchHeroDiv"]/li/a/p/text()').extract_first()
        # print(item['hero_name'])
        # li_list = response.xpath('//ul[@id="jSearchHeroDiv"]/li')
        # for li in li_list:
        #
        hrefs = response.xpath('//ul[@id="jSearchHeroDiv"]/li/a/@href').extract()
        item['hero_name'] = response.xpath('//ul[@id="jSearchHeroDiv"]/li/a/p/text()').extract()

        # print(hrefs, item)
        for _ in hrefs:
            yield SplashRequest(response.urljoin(_),
                                args={'lua_source': self.lua_scripts},
                                meta={'item': item},
                                callback=self.parse_detail,
                                dont_filter=True)

    def parse_detail(self, response):
        item = response.meta['item']
        # print(item)
        print(response.xpath('//ul[@id="skinBG"]/li/img/@alt').extract())
        # li_list = response.xpath('//ul[@id="skinBG"]/li')
        # for li in li_list:
        #     item['image_name'] = li.xpath('./img/@alt').extract()
        #     item['image_urls'] = li.xpath('./img/@src').extacat()
        #     print(item)
        #
        #     yield item

