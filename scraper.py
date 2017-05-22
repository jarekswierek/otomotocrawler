import scrapy


class OtomotoSpider(scrapy.Spider):
    name = "otomotospider"
    start_urls = ['https://www.otomoto.pl/osobowe/poznan/?'
                  'search[filter_enum_authorized_dealer]=1&'
                  'search[private_business]=business&'
                  'search[dist]=50']
    dealers = set()

    def parse(self, response):
        offer_item = '.offer-item'
        for item in response.css(offer_item):
            dealer_selector = 'div.offer-item__photo  a.offer-item__link-seller::attr(href)'
            self.dealers.add(item.css(dealer_selector).extract_first())
        yield {'dealers': self.dealers}
        next_page = response.css('li.next a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
