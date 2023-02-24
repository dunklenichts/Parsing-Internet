# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class JobParserItem(scrapy.Item):
    # define the fields for your item here like:
    name = scrapy.Field()
    company_name = scrapy.Field()
    salary = scrapy.Field()
    photo = scrapy.Field()
    url = scrapy.Field()

