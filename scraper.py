import scrapy


class OtomotoSpider(scrapy.Spider):
    name = "otomotospider"
    start_urls = ['https://www.otomoto.pl/osobowe/poznan/?'
                  'search[filter_enum_authorized_dealer]=1&'
                  'search[private_business]=business&'
                  'search[dist]=50']

    def parse(self, response):
        offer_item = '.offer-item'
        dealers = set()
        for item in response.css(offer_item):

            # offer-item__link-seller
            # item.css('li.next a::attr(href)').extract_first()
            # dealer_selector = 'h2 a ::text'
            dealer_selector = 'div.offer-item__photo  a.offer-item__link-seller::attr(href)'
            dealers.add(item.css(dealer_selector).extract_first())
        return {'dealers': dealers}
            # yield {
            #     'name': item.css(dealer_selector).extract_first(),
            # }
