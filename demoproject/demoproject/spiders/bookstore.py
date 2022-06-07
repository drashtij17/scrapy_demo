from gc import callbacks
from urllib import response
import scrapy


class BookstoreSpider(scrapy.Spider):
    name = 'bookstore'
    allowed_domains = ['www.boookart.com']
    start_urls = ['https://www.boookart.com/categories/general-knowledge']

    def parse(self, response):
        for book in response.xpath("//div[@class = 'position-relative align-top teaser' ]/div"):
            yield {
                'booktitle': book.xpath('.//a/div/div[@class = "teaser-name"]/text()').get()
               
            }

        next_page = response.css("a[rel=next]").attrib["href"]
        if next_page is not None:
            yield response.follow(next_page, callback=self.parse)