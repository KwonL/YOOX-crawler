from scrapy import Spider
from scrapy.http import Response
from scrapy.loader import ItemLoader

from yoox.items import YooxItem


class YooxSpider(Spider):
    name = "yoox"
    start_urls = [
        "https://www.yoox.com/kr/%EB%82%A8%EC%84%B1/"
        "%EC%8B%A0%EC%83%81%ED%92%88/shoponline",
        "https://www.yoox.com/kr/%EB%82%A8%EC%84%B1/sale/shoponline",
        "https://www.yoox.com/kr/%EC%97%AC%EC%84%B1/"
        "%EC%8B%A0%EC%83%81%ED%92%88/shoponline",
        "https://www.yoox.com/kr/%EC%97%AC%EC%84%B1/sale/shoponline",
    ]

    def parse(self, response: Response):
        yield from response.follow_all(
            xpath='//*[starts-with(@id, "item_")]/div[1]/a/@href',
            callback=self.parse_item,
        )

        link = response.xpath(
            '//*[@id="navigation-bar-bottom"]/div[2]/ul/'
            'li[contains(@class, "next-page")]/a/@href'
        ).get()

        yield response.follow(link, callback=self.parse)

    def parse_item(self, response: Response):
        loader = ItemLoader(item=YooxItem(), response=response)

        loader.add_xpath("name", '//*[@id="itemTitle"]/div/a/text()')
        loader.add_xpath("brand", '//*[@id="itemTitle"]/h1/a/text()')
        loader.add_xpath("price", '//*[@id="item-price"]/span/span[1]/text()')
        loader.add_xpath("image", '//*[@id="openZoom"]/img/@src')

        return loader.load_item()
