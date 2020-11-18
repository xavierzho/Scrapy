import scrapy
import re


class GithubSpider(scrapy.Spider):
    name = 'github'
    allowed_domains = ['github.com']
    start_urls = ['https://github.com/Jonescy']

    def start_requests(self):
        cookies = '_octo=GH1.1.1546103862.1596744662; _ga=GA1.2.1064044041.1596744664; ' \
                  '_device_id=4d792a863a93e5fb36b2ea477a9ca173; tz=Asia%2FShanghai; has_recent_activity=1; ' \
                  'user_session=sSboH9tvPP7DXt5GNnbUPy1JaWE20Cb50gJec14YVyqZ-x4c; ' \
                  '__Host-user_session_same_site=sSboH9tvPP7DXt5GNnbUPy1JaWE20Cb50gJec14YVyqZ-x4c; ' \
                  'tz=Asia%2FShanghai; logged_in=yes; dotcom_user=Jonescy; _gat=1; ' \
                  '_gh_sess=Rb14dNq8vqSo9oD9MS5J2vE8WP08BAVFmmBEylLHVUKFqAc5jnpB96XgkCtigIE%2Fd50ZVQCcC5pGX' \
                  '%2Bn6xz9jZb1J%2FmnN0' \
                  '%2FdaJaFs5F1AlYXBC9fkJGGjRVu38NYxCHlG3ofCDsSgs8rr5GH5aJCr2W1CaTAUDNervlyQykZNd9vN4uQFWaI1xx9hRw9YtbLUYjfVNRFZqVt09Cg0HcwkYDnTkl9Z38L8py8zAec57v0IkDEX%2BhfREgZEJ4Xz%2Be4VdwNiSQEwPR%2BtPhQNSv2e0kAfcqPXgRCkULmwVb6fXmGvwSelejKrk4aISMOmuvSL5vaztRwoCKo%2BqXHBDe%2Be3kN28fBNWMOBs%2FkC7hipVGDVmJP1cyKL1x2HgUvBUjvAqxYO5CViqnUhrRchFLoDRyqQsRPouVM4c5AkMrt2FH%2FR48gZmFe%2Bfsbjt%2FEHZ%2FR101IBxQ7lFTgnCnunTulkHjSP%2Ff4jvRizCBbqF8znh4Cp27CfWRLFvxbrU26QgzFAZ4SC5CxijT5MOOopeKJG2X3s%2BTUjaLPaw9KcvUQx%2Fyar7al4lNWXbxNDKPQXU8VK1JQPjJtwnnZhnprb%2B1L5DtGfHC1Otj91FAHLhwqErsxNrN50sUMFCTvlcKx2Ewhg23GSGBbSXLYiQGKlXbduyLQiYM9pmarCBlUjvISgpQLCgBMdVdvJaESZ0J8S%2FmBq--P7gbUme3g0TFjQ7L--FhXAaqRZggrLttCFjZLlvg%3D%3D '
        cookies = {i.split('=')[0]: i.split('=')[1] for i in cookies.split(';')}
        yield scrapy.Request(self.start_urls[0],
                             callback=self.parse,
                             cookies=cookies)

    def parse(self, response):
        print(re.findall('Jonescy', response.body.decode()))
        yield scrapy.Request('https://github.com/Jonescy?tab=repositories',
                             callback=self.parse_detial,)

    def parse_detial(self, response):
        print(re.findall('Jonescy', response.body.decode()))

