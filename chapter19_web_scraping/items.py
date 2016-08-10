import scrapy


class BlogScraperItem(scrapy.Item):
    title = scrapy.Field()
    link = scrapy.Field()