from scrapy.spiders import Spider

class GameskySpider(Spider):
    
    name = 'gamesky'

    def parse(self, response):
        pass