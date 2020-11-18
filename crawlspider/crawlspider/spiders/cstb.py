import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class CstbSpider(CrawlSpider):
    name = 'cstb'
    start_urls = ['https://tieba.baidu.com/f?kw=steam']

    rules = (
        # Rule(LinkExtractor(allow=r'href="(\/p/\d+)"', ), callback='parse_item'),
        Rule(LinkExtractor(allow=r'href="(//tieba.baidu.com/f\?kw=steam&ie=utf-8&cid=&tab=corearea&pn=\d+")'), follow=True),
    )

    # 解析函数
    def parse_item(self, response):
        title = response.xpath('//h3[@class="core_title_txt pull-left text-overflow  "]/text()').extract_first()
        print(title)
        # item = {
        #     'title': response.xpath("//h3[@class='core_title_txt pull-left text-overflow  ']/text()").extract_first(),
        # }
        # div_list = response.xpath('//div[@class="p_postlist"]/div')
        # for div in div_list:
        #     floor = div.xpath('.//span[@class="tail-info"]/text()').extract()[-2]
        #     # print(floor)
        #     item[floor] = {
        #         'author':
        #             div.xpath('./div[@class="d_author"]/ul/li[@class="d_name"]/a/text()').extract_first(),
        #         "user_id":
        #             eval(div.xpath('./div[@class="d_author"]/ul/li[@class="d_name"]/@data-field').extract_first())[
        #                 "user_id"],
        #         "badge_title":
        #             div.xpath('./div[@class="d_author"]/ul/li[@class="l_badge"]/div/a/div[1]/text()').extract_first(),
        #         "badge_level":
        #             div.xpath('./div[@class="d_author"]/ul/li[@class="l_badge"]/div/a/div[2]/text()').extract_first(),
        #         "content":
        #             [i.strip() for i in div.xpath('./div[2]/div[@class="p_content  "]/cc/div[2]//text()').extract() if
        #              i],
        #         "img": div.xpath('./div[2]/div[@class="p_content  "]/cc/div[2]/img/@src').extract(),
        #         'post_time': div.xpath('.//span[@class="tail-info"]/text()').extract()[-1]
        #     }
        # print(item)
