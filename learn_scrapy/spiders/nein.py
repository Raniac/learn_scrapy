# -*- coding: utf-8 -*-
import scrapy


class NeinSpider(scrapy.Spider):
    name = 'nein'
    allowed_domains = ['editorialmanager.com']
    start_urls = ['https://www.editorialmanager.com/nein/default.aspx']

    def parse(self, response):
        print(type(response))  # scrapy.http.response.html.HtmlResponse
        print(type(response.text))  # str
        print(type(response.body))  # bytes
        print(response.encoding)  # utf-8
        with open('/learn_scrapy/tmp/response_content.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
            f.flush()
