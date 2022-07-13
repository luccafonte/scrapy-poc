import scrapy


class Quotes2Spider(scrapy.Spider):
    name = "quotes_2"
    start_urls = [
        'https://quotes.toscrape.com/page/1/',
    ]

    def parse(self, response):
        for quote in response.css('div.quote'):
            yield {
                'page': response.url.split("/")[-2],
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }

        yield from response.follow_all(css='ul.pager a', callback=self.parse)