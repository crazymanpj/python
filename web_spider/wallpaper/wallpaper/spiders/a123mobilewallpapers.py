# -*- coding: utf-8 -*-
import scrapy
from wallpaper.items import WallpaperItem
import os

class A123mobilewallpapersSpider(scrapy.Spider):
    name = '123mobilewallpapers'
    allowed_domains = ['123mobilewallpapers.com']
    start_urls = ['http://www.123mobilewallpapers.com/']

    def parse(self, response):
        wallpapers = response.xpath('//img[contains(@src, "jpg")]')
        for each_wallpaper in wallpapers:
            item = WallpaperItem()
            item['image_urls'] = each_wallpaper.xpath('./@src').extract()
            print 'image_urls',' ', item['image_urls']
            print item['image_urls']
            # item['name'] = os.path.basename(item['image_urls'])
            yield item
        currentpage = response.xpath('//span[contains(@class,"current")]/text()').extract()[0]
        print currentpage
        totalpage = response.xpath('//span[contains(@class,"pages")]/text()').extract()[0]
        totalpage = totalpage.split(' ')[-1]
        print type(totalpage)
        if int(totalpage) >=2:
            nextpagelink = response.xpath('//a[contains(@class,"nextpostslink")]/@href').extract()[0]
            print nextpagelink
            request = scrapy.Request(nextpagelink, callback=self.parse)
            yield request

    def parse_item(self, response):
        print "ttt"
        wallpapers = response.xpath('//img[contains(@src, "jpg")]')
        for each_wallpaper in wallpapers:
            item = WallpaperItem()
            item['image_urls'] = each_wallpaper.xpath('./@src').extract()[0]
            print item['image_urls']
            yield item