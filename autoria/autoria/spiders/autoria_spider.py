import json

from scrapy import Spider, Request
from ..items import AutoriaItem


class AutoriaSpider(Spider):
    name = 'cars'
    start_urls = [
        'https://auto.ria.com/uk/legkovie/tesla/'
    ]

    def parse(self, response):
        for car in response.css("div.content-bar"):
            model = car.css(".blue.bold::text").get()
            year = car.css(".address::text").get()
            race = car.css(".js-race::text").get()
            price_uan = car.css(".i-block span::text").get()
            price_usd = car.css(".size22:nth-child(1)::text").get()
            vin_code = car.css(".label-vin span:nth-child(2)::text").get()
            car_link = car.css("a.m-link-ticket::attr(href)").get()

            autoria_item = AutoriaItem()
            autoria_item['model'] = model
            autoria_item['year'] = year
            autoria_item['race'] = int(race.replace('тис. км', '').strip()) if race else None
            autoria_item['price_uan'] = price_uan
            autoria_item['price_usd'] = price_usd
            autoria_item['vin_code'] = vin_code
            autoria_item['car_link'] = car_link

            yield autoria_item

        next_page_url = response.css("span.page-item > link::attr(href)").extract_first()
        if next_page_url is not None:
            yield Request(response.urljoin(next_page_url))



# response.css(".blue.bold::text").get()    модель
# response.css(".address::text")[1::2].extract()       год
# response.css(".js-race::text").get()      пробег
# response.css(".i-block span::text").get()     price in UAN
# response.css(".size22:nth-child(1)::text").get()      price in USD
# response.css(".label-vin span:nth-child(2)::text").get()      vin-code
# response.css("a.m-link-ticket::attr(href)").get()      link on the car page
# response.css("span.page-item > link::attr(href)").get()      link to the next page
