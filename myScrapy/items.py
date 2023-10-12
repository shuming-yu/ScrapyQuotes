# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class MyscrapyItem(scrapy.Item):
  # define the fields for your item here like:
  # name = scrapy.Field()
  pass

  # # 對應 quotes.py -> d
  # text = scrapy.Field()
  # author = scrapy.Field()
  # tags = scrapy.Field()

  # # 對應 inside.py -> newItem
  # post_title = scrapy.Field()
  # post_date = scrapy.Field()
  # post_author = scrapy.Field()

class NikeItem(scrapy.Item):
  title = scrapy.Field()
  price = scrapy.Field()
  href = scrapy.Field()