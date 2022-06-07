import scrapy


class CoronacountSpider(scrapy.Spider):
    name = 'coronacount'
    allowed_domains = ['https://www.worldometers.info']
    start_urls = ['https://www.worldometers.info/coronavirus/']

    def parse(self, response):
        for country in response.xpath("//tr/td/a[@class='mt_a']"):
            name = country.xpath(".//text()").get()
            link = country.xpath(".//@href").get()
            yield{
                'country_name':name,
                'link': link
            }
