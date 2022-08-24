import scrapy

class Bball(scrapy.Spider):
    name = 'bball'
    start_urls = ['https://www.basketball-reference.com/players/']

    def parse(self, response):
        for link in response.css('li'):
            yield {
                'name': link.css()
            }