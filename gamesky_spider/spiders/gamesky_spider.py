from scrapy.spiders import Spider

from scrapy.selector import Selector
from scrapy import Request

from gamesky_spider.items import GameskyGameInfoItem


class GameskySpider(Spider):

    name = 'gamesky'

    start_urls = ['http://www.gamersky.com/z/list_hot/',]

    def parse(self, response):
        sel = Selector(response)
        lis = sel.xpath('//ul[@class="pictxt"]/li')
        print(len(lis))
        for li in lis:
            game_url = li.xpath('./a/@href').extract()[0]
            yield Request(url=game_url, callback=self.game_info_parse)

    def game_info_parse(self,response):
        sel = Selector(response)
        game_info = GameskyGameInfoItem()
        game_info['game_ch_name'] = sel.xpath('//div[@class="gametit"]/div[@class="CHtit"]/text()').extract()[0]
        game_info['game_en_name'] = sel.xpath('//div[@class="gametit"]/div[@class="ENtit"]/text()').extract()[0]
        game_info['game_type'] =sel.xpath('//ul[@class="YXXX"]/li[1]/div[@class="u2"]/text()').extract()[0]
        game_info['game_maker'] = sel.xpath('//ul[@class="YXXX"]/li[2]/div[@class="u2"]/text()').extract()[0]
        game_info['game_push'] = sel.xpath('//ul[@class="YXXX"]/li[3]/div[@class="u2"]/text()').extract()[0]
        game_info['game_station'] = sel.xpath('//ul[@class="YXXX"]/li[4]/div[@class="u2"]/text()').extract()[0]
        game_info['time_to_market'] = sel.xpath('//ul[@class="YXXX"]/li[5]/div[@class="u2"]/text()').extract()[0]
        game_info['game_website'] = sel.xpath('//ul[@class="YXXX"]/li[6]/div[@class="u2"]/a/@href').extract()[0]
        game_info['game_img_src'] = sel.xpath('//div[@class="gameimg"]/a/img/@src').extract()[0]
        game_info['game_introduction'] = sel.xpath('//div[@class="intr"]/p/text()').extract()[-1].replace('\u3000','')

        yield game_info
