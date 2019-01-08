# -*- coding: utf-8 -*-
import scrapy
from shiyanlougithub.items import ShiyanlougithubItem

class ShiyanlouSpider(scrapy.Spider):
    name = 'shiyanlou'
    allowed_domains = ['github.com']
    def start_urls(self):
        return ('https://github.com/shiyanlou?tab=repositories',) 
    def parse(self, response):
        for repository in response.css('li.public'):
            item = shiyanlougithubItem()
            item['name']= repository.xpath('.//a[@itemprop="name codeRepository"]/text()').re_first(r'\n\s*(.*)')   
            item['update_time']=repository.xpath('.//relative-time/@datetime').extract_first()
            respository_url=response.urljoin(respository.xpath('.//a/@href').extract_first())
            request=scrapy.Request(responsitory_url,callback=self.parse_commits)
            resquest.meta['item']=item
            yield request
        spans = response.css('div.pagination span.disabled::text')
        if len(spans)==0 or spans[-1].extract()!='Next':
            next_url=response.css('div.pagination a:last-child::attr(href)').extract_first()
            yield response.folow(next_url,callback=self.parse)

    def parse_commit(self,response):
        item=response.meta['item']
        item['commits']=response.xpath('//span[@class="num text-emphasized"]/text()').extract()[0].split()
        item['branches']=response.xpath('//span[@class="num text-emphasized"]/text()').extract()[1].split()
        item['releases']=response.xpath('//span[@class="num text-emphasized"]/text()').extract()[2].split()
        yield item
