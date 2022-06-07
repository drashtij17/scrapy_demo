from gc import callbacks
from pkg_resources import yield_lines
import scrapy


class AsiacountSpider(scrapy.Spider):
    name = 'Asiacount'
    allowed_domains = ['https://www.worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def parse(self, response):

        
        for d in response.xpath('//tr'):
            total_case = d.xpath('.//td[3]/text()').extract()
            population = d.xpath('.//td[15]/a/text()').extract()
            total_death = d.xpath('.//td[5]/text()').extract()
            total_recover = d.xpath('.//td[7]/text()').extract()
            yield{
                " total_case": total_case,
                "population":population,
                "total_death":total_death,
                "total_recover":total_recover 
                }
