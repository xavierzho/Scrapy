import scrapy
import re


class GithubPost2Spider(scrapy.Spider):
    name = 'github_post2'
    allowed_domains = ['github.com']
    start_urls = ['http://github.com/login']

    def parse(self, response):
        yield scrapy.FormRequest.from_response(
            response,  # 自动从response中寻找from表单
            formdata={'login': 'jonescyna@gmail.com',
                      'password': 'Snq1997.'},
            callback=self.after_login
        )

    def after_login(self, response):

        print(re.findall('Jonescy|jonescy', response.body.decode()))

