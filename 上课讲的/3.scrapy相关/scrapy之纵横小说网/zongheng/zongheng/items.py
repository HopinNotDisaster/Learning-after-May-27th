# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    book_name = scrapy.Field()
    book_url = scrapy.Field()
    book_id = scrapy.Field()


# 类似django里面的一个class就是一个数据类型！
class ChapterItem(scrapy.Item):
    chapter_name = scrapy.Field()
    chapter_url = scrapy.Field()
    chapter_id = scrapy.Field()
    content = scrapy.Field()
