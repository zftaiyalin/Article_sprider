# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from urllib import parse
from ArticleSpider.items import ArticleItemLoader,ZhongTuiItem
from ArticleSpider.utils.common import extract_zhongtui_num

class ZhongtuSpider(scrapy.Spider):
    name = 'zhongtu'
    allowed_domains = ['www.49358.com']
    start_urls = ['http://www.49358.com/weixin/list/']

    def parse(self, response):
        """
                1. 获取文章列表页中的文章url并交给scrapy下载后并进行解析
                2. 获取下一页的url并交给scrapy进行下载， 下载完成后交给parse
                """

        # 解析列表页中的所有文章url并交给scrapy下载后并进行解析front_image_url

        post_nodes = response.css('.liebk')
        for post_node in post_nodes:
            # yield 关键字 代表下载解析request
            post_url = post_node.css('a::attr(href)').extract_first("")

            yield Request(url=parse.urljoin(response.url, post_url),
                          callback=self.parse_detail)

        # 提取下一页并交给scrapy进行下载
        next_url = response.css(".pagelink a:nth-last-child(2)::attr(href)").extract_first("")

        if 'javascript' not in next_url :
            yield Request(url=parse.urljoin(response.url, next_url), callback=self.parse)

    def parse_detail(self, response):

        item_loader = ArticleItemLoader(item=ZhongTuiItem(), response=response)

        item_loader.add_value("url",response.url)
        item_loader.add_value("id", extract_zhongtui_num(response.url))
        item_loader.add_css("title", "div.title h1::text")
        item_loader.add_css("money", "div.amount span.fl::text")
        item_loader.add_css("title_content", "div.rigth_detail")
        item_loader.add_css("start_date", "div.item_startdate::text")
        item_loader.add_css("end_date", "div.item_enddate::text")
        item_loader.add_css("task_type", "span.tag::text")
        item_loader.add_css("content", "div.itemrequest_border")

        article_item = item_loader.load_item()

        yield article_item