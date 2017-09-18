# -*- coding: utf-8 -*-
import scrapy
import re
import datetime
from scrapy.http import Request
from urllib import parse
from ArticleSpider.items import JobBoleArticleItem,ArticleItemLoader
from ArticleSpider.utils.common import get_md5
from scrapy.loader import ItemLoader

class JobboleSpider(scrapy.Spider):
    name = 'jobbole'
    allowed_domains = ['blog.jobbole.com']
    start_urls = ['http://blog.jobbole.com/all-posts/']

    def parse(self, response):
        """
        1. 获取文章列表页中的文章url并交给scrapy下载后并进行解析
        2. 获取下一页的url并交给scrapy进行下载， 下载完成后交给parse
        """

        # 解析列表页中的所有文章url并交给scrapy下载后并进行解析front_image_url

        post_nodes = response.css('#archive .floated-thumb .post-thumb a')
        for post_node in post_nodes:
           #yield 关键字 代表下载解析request
           front_image_url = post_node.css('img::attr(src)').extract_first("")
           post_url = post_node.css('::attr(href)').extract_first("")

           yield Request(url=parse.urljoin(response.url,post_url),meta={"front_image_url":parse.urljoin(response.url,front_image_url)},callback=self.parse_detail)

         # 提取下一页并交给scrapy进行下载
        next_url = response.css('.next.page-numbers::attr(href)').extract_first("")
        if next_url:
            yield Request(url=parse.urljoin(response.url,next_url),callback=self.parse)



    def parse_detail(self,response):

        # 提取文章的具体字段
        # front_image_url = response.meta.get("front_image_url","")#文章封面图
        # title = response.xpath('//div[@class="entry-header"]/h1/text()').extract()[0]
        # content = response.xpath('//div[@class="entry"]').extract()[0]
        # thumbsup = response.xpath('//span[contains(@class,"vote-post-up")]/h10/text()').extract()[0]
        # #bookmark = re.match(".*(\d+).*", response.xpath('//span[contains(@class,"bookmark-btn")]/text()').extract()[0])
        # bookmark = response.xpath('//span[contains(@class,"bookmark-btn")]/text()').extract()[0]
        # bookmarkre = re.match('.*(\d{1,9}).*', bookmark)
        #
        # if bookmarkre:
        #     bookmark = int(bookmarkre.group(1))
        # else:
        #     bookmark = 0
        #
        # comment_nums = response.xpath('//a[@href="#article-comment"]/text()').extract_first("")
        # commentre = re.match('.*(\d{1,9}).*', comment_nums)
        #
        # if commentre:
        #     comment_nums = int(commentre.group(1))
        # else:
        #     comment_nums = 0
        #
        # create_date = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/text()').extract()[0].strip().replace(' ·','')
        # tag_list = response.xpath('//p[@class="entry-meta-hide-on-mobile"]/a/text()').extract()
        # tag_list = [element for element in tag_list if not element.strip().endswith("评论")]
        # tags = ",".join(tag_list)
        #
        # #通过css选择器选取数据
        # # titile_css = response.css(".entry-header h1::text").extract_first()
        # # create_date_css = response.css("p.entry-meta-hide-on-mobile::text").extract()[0].strip().replace(' ·','')
        #
        # #extract()[0] = extract_first() 前一个写法可能存在数字为空后数组月结而抛异常，第二个就不存在了
        #
        # article_item = JobBoleArticleItem()
        # article_item["title"] = title
        #
        #
        # try:
        #     create_date = datetime.datetime.strftime(create_date,"%Y/%m/%d").date()
        # except Exception as e:
        #     create_date = datetime.datetime.now().date()
        #
        # article_item["create_date"] = create_date
        #
        # article_item["content"] = content
        # article_item["url"] = response.url
        # article_item["comment_nums"] = comment_nums
        # article_item["fav_nums"] = bookmark
        # article_item["praise_nums"] = thumbsup
        # article_item["tags"] = tags
        # article_item["front_image_url"] = [front_image_url]
        # article_item["url_object_id"] = get_md5(response.url)

        # 通过item loader加载item

        front_image_url = response.meta.get("front_image_url", "")  # 文章封面图
        item_loader = ArticleItemLoader(item=JobBoleArticleItem(),response=response)
        item_loader.add_css("title",".entry-header h1::text")
        item_loader.add_value("url",response.url)
        item_loader.add_value("url_object_id",get_md5(response.url))
        item_loader.add_css("create_date", "p.entry-meta-hide-on-mobile::text")
        item_loader.add_value("front_image_url", [front_image_url])
        item_loader.add_css("praise_nums", ".vote-post-up h10::text")
        item_loader.add_css("comment_nums", "a[href='#article-comment'] span::text")
        item_loader.add_css("fav_nums", ".bookmark-btn::text")
        item_loader.add_css("tags", "p.entry-meta-hide-on-mobile a::text")
        item_loader.add_css("content", "div.entry")

        article_item = item_loader.load_item()

        yield article_item


