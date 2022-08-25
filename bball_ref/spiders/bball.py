import scrapy

class Bball(scrapy.Spider):
    name = 'bball'
    start_urls = ['https://www.basketball-reference.com/awards/awards_2022.html#mvp',]

    years = list(range(1991, 2021))
    url_init = "https://www.basketball-reference.com/awards/awards_{}.html#mvp"

    for year in years:
        url = url_init.format(year)
        start_urls.append(url)    

    def parse(self, response):
        for link in response.css('td.left'):
            yield {
                'name': link.get()
            }