# -*- coding: utf-8 -*-
import scrapy
from ..items import TransfermarktItem

class TmSpiderSpider(scrapy.Spider):
    name = 'tm_spider'
    page_num = 2
    start_urls = [
        'https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop'
    ]

    def parse(self, response):
        items = TransfermarktItem()
        
        player_image = response.css('.bilderrahmen-fixed::attr(src)').extract()
        player_name = response.css('.bilderrahmen-fixed::attr(title)').extract()
        player_position = response.css('.inline-table tr+ tr td').css('::text').extract()
        player_age = response.css('#yw1 td:nth-child(3)').css('::text').extract()
        player_value = response.css('#yw1 b').css('::text').extract()
        
        items['player_image'] = player_image 
        items['player_name'] = player_name
        items['player_position'] = player_position
        items['player_age'] = player_age
        items['player_value'] = player_value 
        
        yield items 
        
        next_page = 'https://www.transfermarkt.com/spieler-statistik/wertvollstespieler/marktwertetop?ajax=yw1&page=' + str(TmSpiderSpider.page_num)
        
        if TmSpiderSpider.page_num <= 20:
            TmSpiderSpider.page_num += 1 
            yield response.follow(next_page, callback = self.parse)
        
        
        
        
        
        
        
        
        
