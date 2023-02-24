# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import scrapy
# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from scrapy.pipelines.images import ImagesPipeline
from pymongo import MongoClient
import pymongo

class JobParserPipeline:
    def __init__(self):
        client = MongoClient('localhost', 27017)
        self.mongobase = client.superjob
        print(client.list_database_names())

    def process_item(self, item, spider):
        collection = self.mongobase['Jobs']
        collection.create_index([('name', 1)])
        collection.insert_one(dict(item))
        return item

class JobPhotosPipeline(ImagesPipeline):
    def get_media_requests(self, item, info):
        if item.get('photo'):
            for img in item.get('photo'):
                try:
                    yield scrapy.Request(img)
                except Exception as e:
                    print(e)