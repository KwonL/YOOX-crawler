import scrapy
from scrapy.loader.processors import TakeFirst


class YooxItem(scrapy.Item):
    brand = scrapy.Field(output_processor=TakeFirst())
    name = scrapy.Field(output_processor=TakeFirst())
    price = scrapy.Field(output_processor=TakeFirst())
    image = scrapy.Field(output_processor=TakeFirst())
