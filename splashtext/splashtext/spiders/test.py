import scrapy
from scrapy_splash import SplashRequest, SplashTextResponse


class TestSpider(scrapy.Spider):
    name = 'test'

    def start_requests(self):
        lua = """
        function main(splash, args)
            local get_high = splash:jsfunc([[
                function(){return document.getElementsByClassName('list')[0].clientHeight}
            ]])
            local scroll = splash:jsfunc([[window.scrollTo]])
            
            assert(splash:go(args.url))
            local next_high = get_high()
            for _=0, 10
            do
                scroll(0, next_high)
                splash:wait(args.wait)
            end
            return splash:html()
        end
        """

        # url = 'https://list.jd.com/list.html?cat=1713%2C3258%2C3297&page=1&s=1&click=0'
        url = 'https://show.1688.com/pinlei/industry/pllist.html?sceneSetId=872&sceneId=2743&adsSearchWord=%E8%83%B8%E5%8C%85'
        yield SplashRequest(url,
                            args={
                                "lua_source": lua,
                                'wait': 1,
                            },
                            endpoint='execute',
                            callback=self.parse,
                            # cache_args=['lua_source'],

                            )

    def parse(self, response):
        # print(response.text)
        # div_list = response.xpath('//div[@class="gl-i-wrap"]')
        # for div in div_list:
        #     name = div.xpath('./div[@class="p-name"]/a/em/text()').extract_first().strip()
        #     price = ''.join(div.xpath('./div[@class="p-price"]/strong//text()').extract()).strip()
        #     print(name, price)
        titles = response.xpath('//div[@class="offer-title"]/text()').extract()
        print(len(titles))
