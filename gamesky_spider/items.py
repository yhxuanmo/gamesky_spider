# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class GameskyGameInfoItem(scrapy.Item):

    collections = 'game_info'

    game_ch_name = scrapy.Field()  # 中文名
    game_en_name = scrapy.Field()  # 英文名
    game_type = scrapy.Field()  # 游戏类型
    game_maker = scrapy.Field()  # 游戏制作
    game_push = scrapy.Field()  # 游戏发行
    game_station = scrapy.Field()  # 游戏平台
    time_to_market = scrapy.Field()  # 发行时间
    game_website = scrapy.Field()  # 官网
    game_img_src = scrapy.Field()  # 游戏图片
    game_introduction = scrapy.Field()  # 游戏介绍


