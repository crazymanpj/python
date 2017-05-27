# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import os
from wallpaper import settings
import requests
from scrapy.pipelines.images import ImagesPipeline
import scrapy
from scrapy.exceptions import DropItem

class WallpaperPipeline(ImagesPipeline):
    # def process_item(self, item, spider):
    #     pass
        # save_path = os.path.join(os.getcwd(), settings.IMAGES_STORE, spider.name)
        # if not os.path.exists(save_path):
        #     os.makedirs(save_path)
        # file_path = os.path.join(save_path, item['name'])
        # # if os.path.exists(file_path):
        # #     continue
        # headers = {
        #     "user-agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"}
        # with open(file_path, 'wb') as f:
        #     response = requests.get(item['image_urls'], headers=headers, timeout=(120,360), stream=True)
        #     for block in response.iter_content(1024):
        #         if not block:
        #             break
        #         f.write(block)
        # return item

    def get_media_requests(self, item, info):
        '''
        :param item:
        :param info:
        :return:
        在工作流程中可以看到，
        管道会得到文件的URL并从项目中下载。
        为了这么做，你需要重写 get_media_requests() 方法，
        并对各个图片URL返回一个Request:
        '''
        for image_url in item['image_urls']:
            yield scrapy.Request(image_url)

    def item_completed(self, results, item, info):
        '''
        :param results:
        :param item:
        :param info:
        :return:
        当一个单独项目中的所有图片请求完成时（要么完成下载，要么因为某种原因下载失败），
        item_completed() 方法将被调用。
        '''
        image_path = [x['path'] for ok, x in results if ok]
        if not image_path:
            raise DropItem("Item contains no images")
        return item


