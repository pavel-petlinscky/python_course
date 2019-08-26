# -*- coding: utf-8 -*-

import scrapy
from scrapy.selector import Selector
from scrapy.loader import ItemLoader
from scrapy.loader.processors import TakeFirst


class CustomPipeline(object):
    def process_item(self, item, spider):
        if isinstance(item, BlogPost):
            item['name'] = 'URL: ' + item['name']
        return item


class BlogPost(scrapy.Item):
    name = scrapy.Field(output_processor=TakeFirst())
    post_text = scrapy.Field()
    # post_text = scrapy.Field(output_processor=TakeFirst())


class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://habrahabr.ru/users/olegchir/posts/', ]
    #start_urls = ['https://blog.scrapinghub.com', ]

    custom_settings = {
        'ITEM_PIPELINES': {
            'spider.CustomPipeline': 1
        }
    }

    def parse(self, response):
        selector = Selector(response)

        for post in selector.css('article.post_full'):
            print('---------------------------------')


            loader = ItemLoader(BlogPost(), post)
            # loader.add_css('name', '.entry-title > a::text')
            loader.add_css('name', '.post__title_full > span::text')
            #loader.add_css('name', '.post__title_full > span::text')
            #loader.add_css('post_text', '.post__body_full::text')
            loader.add_xpath('post_text', "//div[contains(@class, 'post__body_full')]//text()")
            #print("EXTRACTED", response.selector.css('.post__body_full::text').extract())
            #print("EXTRACTED", response.selector.xpath("//div[contains(@class, 'post__body_full')]//text()").extract())

            yield loader.load_item()

        for url in response.xpath("//h2[contains(@class, 'post__title')]/a/@href").extract():
            #print('URL TO POST FOUND! {}'.format(url))
            yield scrapy.Request(url, callback=self.parse)

        # for url in response.xpath("//ul[@id='nav-pagess']//a/@href").extract():
        #     #print('URL TO ANOTHER PAGE FOUND! {}'.format(url))
        #     yield scrapy.Request("https://habrahabr.ru"+url, callback=self.parse)
