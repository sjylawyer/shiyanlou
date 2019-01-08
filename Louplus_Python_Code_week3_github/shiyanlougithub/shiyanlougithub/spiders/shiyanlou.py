# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import ShiyanlougithubItem

class ShiyanlouSpider(scrapy.Spider):
    name = 'shiyanlou'
    @property
    def start_urls(self):
        return ('https://github.com/shiyanlou?tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNy0wNi0wN1QwNjoyMToxMCswODowMM4FkpVn&tab=repositories',
                'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0yNlQxMTozMDoyNSswODowMM4Bx2JQ&tab=repositories',
                 'https://github.com/shiyanlou?after=Y3Vyc29yOnYyOpK5MjAxNS0wMS0yNlQxMTozMDoyNSswODowMM4Bx2JQ&tab=repositories',)
    def parse(self, response):
        for repository in response.css('li.public'):
            item = ShiyanlougithubItem({
                'name': repository.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first(r'\n\s*(.*)'),
                'update_time': repository.xpath('.//relative-time/@datetime').extract_first()
            })
            yield item 
