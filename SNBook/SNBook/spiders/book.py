import scrapy
from copy import deepcopy


class BookSpider(scrapy.Spider):
    name = 'book'
    allowed_domains = ['suning.com']
    start_urls = ['https://book.suning.com/']

    def parse(self, response):
        """
        获取分类
        :param response:
        :return:
        """
        # 1.获取一级分类
        a_menu_list = response.xpath('//div[@class="menu-list"]/div[@class="menu-item"]')
        for menu in a_menu_list:
            item = {'a_menu': menu.xpath("./dl/dt/h3/a/text()").extract_first(),
                    }
        # 2.获取二级分类
            b_menu_list = menu.xpath('./dl/dd/a')
            for b_menu in b_menu_list:
                item['b_menu_href'] = b_menu.xpath('./@href').extract_first()
                item['b_menu_name'] = b_menu.xpath('./text()').extract_first()
                yield scrapy.Request(item['b_menu_href'],
                                     callback=self.parse_c_menu,
                                     meta={'item': item})

    def parse_c_menu(self, response):
        item = response.meta['item']
        # c_menu分组
        c_menu_list = response.xpath('//div[@class="item"]/div/a')
        for c_menu in c_menu_list:
            item['c_menu_name'] = c_menu.xpath('./text()').extract_first()
            item['c_menu_href'] = 'https:' + c_menu.xpath('./@href').extract_first()
            # print(item)
            yield scrapy.Request(item['c_menu_href'],
                                 callback=self.parse_book_list,
                                 meta={'item': deepcopy(item)})

    def parse_book_list(self, response):
        # 3.获取书信息
        item = response.meta['item']
        # 分组
        book_list = response.xpath('//ul[@class="clearfix"]/li')
