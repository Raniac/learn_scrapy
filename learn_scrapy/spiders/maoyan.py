# -*- coding: utf-8 -*-
import scrapy
from learn_scrapy.items import MaoyanreyingItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['editorialmanager.com']
    start_urls = ['https://www.editorialmanager.com/nein/default.aspx']

    def parse(self, response):
        # dl = response.css('.board-wrapper dd')
        # for dd in dl:
        #     item = MaoyanreyingItem()
        #     item['index'] = dd.css('.board-index::text').extract_first()
        #     item['title'] = dd.css('.name a::text').extract_first()
        #     item['star'] = dd.css('.star::text').extract_first()
        #     item['releasetime'] = dd.css('.releasetime::text').extract_first()
        #     item['score'] = dd.css('.integer::text').extract_first() + dd.css('.fraction::text').extract_first()
        #     yield item
        print(type(response))  # scrapy.http.response.html.HtmlResponse
        print(type(response.text))  # str
        print(type(response.body))  # bytes
        print(response.encoding)  # utf-8
        # 将网页内容写入book.html文件内
        with open('/learn_scrapy/response_content.html', 'w', encoding='utf-8') as f:
            f.write(response.text)
            f.flush()
        # except Exception as e:
        #     print(e)
