# -*- coding: utf-8 -*-
import scrapy


class ContentSpider(scrapy.Spider):
    name = "content"
    start_urls = [
        'https://www.voaswahili.com/a/uchumi-wa-kernya-wakuwa-kwa-asilimia-5-6-/7619683.html',
    ]

    def parse(self, response):
            yield {
                'intro': response.xpath('//div[has-class("intro intro--bold")]/p').getall(),
                'article': response.xpath('//div[has-class("wsw")]/p').getall()
            }

            for href in response.css("ul.pager a::attr(href)"):
                 yield response.follow(href, callback=self.parse)

# response.xpath('//div[has-class("intro intro--bold")]/p').getall()
# response.xpath('//div[has-class("wsw")]/p').getall()
# these work but they have p tags
# add next page
