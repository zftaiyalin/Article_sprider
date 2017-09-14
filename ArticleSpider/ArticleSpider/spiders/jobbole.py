# -*- coding: utf-8 -*-
import scrapy
import re

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/112366/']

    def parse(self, response):
        title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]
        content = response.xpath('//div[@class="entry"]').extract()[0]
        thumbsup = response.xpath('//span[contains(@class,"vote-post-up")]/h10/text()').extract()[0]
        #bookmark = re.match(".*(\d+).*", response.xpath('//span[contains(@class,"bookmark-btn")]/text()').extract()[0])
        bookmark = response.xpath('//span[contains(@class,"bookmark-btn")]/text()').extract()[0]
        bookmarkre = re.match('.*(\d{1,9}).*', bookmark).group(1)
        comment_nums = response.xpath('//a[@href="#article-comment"]/text()').extract()[0]
        commentre = re.match('.*(\d{1,9}).*', comment_nums).group(1)
        create_date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip().replace(' ·','')
        tag_list = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
        tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        tag = ",".join(tag_list)
        pass

