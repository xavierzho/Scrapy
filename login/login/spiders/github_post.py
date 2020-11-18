import scrapy
import re


class GithubPostSpider(scrapy.Spider):
    name = 'github_post'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/login']

    def parse(self, response):
        post_data = dict(
            login='jonescyna@gmail.com',
            password='Snq1997.',
            commit=response.xpath('//input[@name="commit"]/@value').extract_first(),
            authenticity_token=response.xpath('//input[@name="authenticity_token"]/@value').extract_first(),
            ga_id=response.xpath('//input[@name="ga_id"]/@value').extract_first(),
            # 'webauthn-support'=response.xpath('//input[@name=""]'),
            timestamp=response.xpath('//input[@name="timestamp"]/@value').extract_first(),
            timestamp_secret=response.xpath('//input[@name="timestamp_secret"]/@value').extract_first()
        )
        yield scrapy.FormRequest(
            'https://github.com/session',
            formdata=post_data,
            callback=self.after_login
                                 )

    def after_login(self, response):
        with open('github.html', 'w', encoding='utf-8') as f:
            f.write(response.body.decode())
        print(re.findall('Jonescy', response.body.decode()))

