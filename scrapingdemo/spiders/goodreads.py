# -*- coding: utf-8 -*-
import scrapy


class GoodreadsSpider(scrapy.Spider):
    name = 'goodreads'
    allowed_domains = ['goodreads.com']
    def start_requests(self):
        start_urls = [
        'https://goodreads.com/quotes?page=1',
        'https://goodreads.com/quotes?page=2',
        'https://goodreads.com/quotes?page=3',
        'https://goodreads.com/quotes?page=4',
        'https://goodreads.com/quotes?page=5'
    ]
        for url in start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        page_number = response.url.split("=")[1]
        _file = f'{page_number}.html'
        with open(_file,'wb') as f:
            f.write(response.body)


        
