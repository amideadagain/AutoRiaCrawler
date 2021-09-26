# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

from scrapy import Item, Field


class AutoriaItem(Item):
    # define the fields for your item here like:
    model = Field()
    year = Field()
    race = Field()
    price_uan = Field()
    price_usd = Field()
    vin_code = Field()
    car_link = Field()
