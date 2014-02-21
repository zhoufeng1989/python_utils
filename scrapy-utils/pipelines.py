#-*- coding:utf-8 -*-
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/topics/item-pipeline.html
from scrapy.contrib.pipeline.images import ImagesPipeline
from urlparse import urlparse


class DownloadImagesPipeline(ImagesPipeline):
    '''
    根据url来确定图片路径
    '''
    def image_key(self, url):
        image_guid = urlparse(url).netloc + urlparse(url).path
        return image_guid
