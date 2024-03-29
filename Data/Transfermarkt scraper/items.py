# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class TransfermarktItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    player_image = scrapy.Field()
    player_name = scrapy.Field()
    player_position = scrapy.Field()
    player_age = scrapy.Field()
    player_value = scrapy.Field()
    pass
