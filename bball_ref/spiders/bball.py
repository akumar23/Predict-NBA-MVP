import scrapy

class Bball(scrapy.Spider):
    name = 'bball'
    start_urls = ['https://www.basketball-reference.com/awards/awards_2022.html#mvp',]

    years = list(range(1991, 2021))
    url_init = "https://www.basketball-reference.com/awards/awards_{}.html#mvp"

    for year in years:
        url = url_init.format(year)
        start_urls.append(url)    

#method 1: doesn't split team from player name
    def parse(self, response):
        for link in response.css('td.left *::text'):
            yield {
                'player' : link.get()
            }

#method 2: doesn't loop through all the years with response
"""
    def parse(self, response):

        data = {}

        for link in response.css('td.left *::text'):
            if len(link.get()) == 3:
                data['team'] = link.get()
            else:
                data['player'] = link.get()
        yield data
"""