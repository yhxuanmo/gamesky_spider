from scrapy.spiders import Spider

from scrapy.selector import Selector
from scrapy import Request

from gamesky_spider.items import GameskyGameInfoItem


class GameskySpider(Spider):

    name = 'gamesky'

    # 热门单机/近期新作/即将上市
    start_urls = ['http://www.gamersky.com/z/',
                  'http://www.gamersky.com/z/list_hot/',
                  'http://www.gamersky.com/z/list_unlisted/',
                  ]


    def parse(self, response):
        sel = Selector(response)
        lis = sel.xpath('//ul[@class="pictxt"]/li')
        list_type = sel.xpath('//div[@class="Midtit lx0"]/div[@class="tit"]/text()').extract()[0]
        for li in lis:
            game_url = li.xpath('./a/@href').extract()[0]
            yield Request(url=game_url, callback=self.game_info_parse, meta={'list_type': list_type})

    def game_info_parse(self,response):
        sel = Selector(response)
        game_info = GameskyGameInfoItem()
        game_info['list_type'] = response.meta.get('list_type')
        game_info['game_ch_name'] = sel.xpath('//div[@class="gametit"]/div[@class="CHtit"]/text()').extract()[0]
        game_info['game_en_name'] = sel.xpath('//div[@class="gametit"]/div[@class="ENtit"]/text()').extract()[0]
        game_info['game_type'] =sel.xpath('//div[@class="gamecon"]/ul/li[1]/div[@class="u2"]/text()').extract()[0]
        game_info['game_maker'] = sel.xpath('//div[@class="gamecon"]/ul/li[2]/div[@class="u2"]/text()').extract()[0]
        game_info['game_push'] = sel.xpath('//div[@class="gamecon"]/ul/li[3]/div[@class="u2"]/text()').extract()[0]
        game_info['game_station'] = sel.xpath('//div[@class="gamecon"]/ul/li[4]/div[@class="u2"]/text()').extract()[0]
        if sel.xpath('//div[@class="gamecon"]/ul/li[5]/div[@class="u2"]/text()'):
            game_info['time_to_market'] = sel.xpath('//div[@class="gamecon"]/ul/li[5]/div[@class="u2"]/text()').extract()[0]
        elif sel.xpath('//div[@class="gamecon"]/ul/li[5]/div[@class="u2"]/span/text()'):
            game_info['time_to_market'] =sel.xpath('//div[@class="gamecon"]/ul/li[5]/div[@class="u2"]/span/text()').extract()[0]
        game_info['game_website'] = sel.xpath('//div[@class="gamecon"]/ul/li[6]/div[@class="u2"]/a/@href').extract()[0]
        game_info['game_img_src'] = sel.xpath('//div[@class="gameimg"]/a/img/@src').extract()[0]
        if sel.xpath('//div[@class="intr"]/p/text()'):
            game_info['game_introduction'] = sel.xpath('//div[@class="intr"]/p/text()').extract()[-1].replace('\u3000','')
        elif sel.xpath('//div[@class="intr"]/text()'):
            game_info['game_introduction'] = sel.xpath('//div[@class="intr"]/text()').extract()[-1].replace('\u3000','')

        yield game_info
