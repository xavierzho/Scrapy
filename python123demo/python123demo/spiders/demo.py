# -*- coding: utf-8 -*-
import scrapy
from scrapy_splash import SplashRequest

lua = {"lua_source": """
function main(splash, args)
    splash.images_enabled = false
    assert(splash:go(args.url))
    assert(splash:wait(2))
    splash:set_viewport_size(1980, 3000)
    local scroll_to = splash:jsfunc('window.scrollTo')
    scroll_to(0,300)
    return html = splash:html()

end
"""
       }


class DemoSpider(scrapy.Spider):
    name = 'demo'

    def start_requests(self):
        start_urls = ['https://list.jd.com/list.html?cat=9987,653,655']
        yield SplashRequest(start_urls[0],
                            callback=self.parse,
                            args=lua,
                            endpoint='execute'
                            )

    def parse(self, response):
        # print(response)
        # html = response.body.decode()
        # print(html)
        # tree = etree.HTML(html)
        info_list = response.xpath('//div[@class="res-info"]')
        for info in info_list:
            item = {
                'title': info.xpath('./p[@class="sell-point"]/a/text()').extract_first().strip(),
                'price': info.xpath('./p[@class="prive-tag"]/em//text()').extract()
            }
            item['price'] = ''.join(item['price'])
            print(item)
