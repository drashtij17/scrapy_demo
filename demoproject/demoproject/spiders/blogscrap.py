import scrapy

class BlogscrapSpider(scrapy.Spider):
    name = 'blogscrap'
    allowed_domains = ['www.blog.yudiz.com']
    start_urls = ['https://blog.yudiz.com/']
    def parse(self, response):
        for title in response.xpath('//h4/a'):
            yield{
                'blog_title':title.xpath('.//text()').get().strip(),
            }
    
        for by in response.xpath('//div/small/a[2]'):
            yield{
                'author': by.xpath('.//text()').get().strip()
            }