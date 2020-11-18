import scrapy
import logging

# logger = logging.getLogger(__name__)


class ItcastspiderSpider(scrapy.Spider):
    name = 'itcastSpider'
    allowed_domains = ['itcast.cn']
    start_urls = ['http://www.itcast.cn/channel/teacher.shtml']

    def parse(self, response):
        # 处理start_url 内容

        # 分组
        # li_list = response.xpath('//div[@class="li_txt"]')
        # print(li_list)
        # for li in li_list:
            # item = {'teacher_name': li.xpath('./h3/text()').extract_first(),
                    # 'teacher_title': li.xpath('./h4/text()').extract_first(),
                    # 'teacher_introduction': li.xpath('./p/text()').extract_first(),
                    # 'come_from': 'itcast'}
            # logger.warning(item)

            # yield item
        pass
