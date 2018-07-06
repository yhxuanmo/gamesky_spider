# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
from scrapy.conf import settings

from gamesky_spider.items import GameskyGameInfoItem


class GameskySpiderPipeline(object):
    def process_item(self, item, spider):
        return item


class GameskyMongoPipeline(object):

    def __init__(self):
        conn = pymongo.MongoClient(host=settings['MONGODB_HOST'], port=settings['MONGODB_PORT'])
        db = conn[settings['MONGODB_DB']]
        self.collection = db[GameskyGameInfoItem.collections]

    def process_item(self, item, spider):
        self.collection.update({'game_en_name': item['game_en_name']}, {'$set': item}, True)

        return item