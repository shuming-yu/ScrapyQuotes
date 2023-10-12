import scrapy
from bs4 import BeautifulSoup
from myScrapy.items import NikeItem

class NikeSpider(scrapy.Spider):
  name = "nike"
  allowed_domains = ["nike.com"]
  # start_urls = ["https://nike.com"]
  start_urls = ["https://www.nike.com/tw/w/new-3n82y"]

  def parse(self, response):
    # res = BeautifulSoup(response.text,"html.parser")
    # for n in res.select('.product-card'):
    #   print("n:", n)
    #   nikeitem['href'] = res.select('#pdp_product_title')[0].text
    #   yield scrapy.Request(n.select('a.product-card__link-overlay')[0]['href'], self.parse_detail)


    for product in response.css('div.product-card'):
      # d = {
      #   "title": product.css('div.product-card__title::text').get(),
      #   "price": product.css('div.is--current-price::text').get(),
      #   "href" : product.css('a.product-card__link-overlay::attr(href)').get()
      # }
      # yield d

      # nikeitem = NikeItem()
      # nikeitem['title'] = product.css('div.product-card__title::text').get()
      # nikeitem['price'] = product.css('div.is--current-price::text').get()
      # nikeitem['href'] = product.css('a.product-card__link-overlay::attr(href)').get()
      # return nikeitem
      yield scrapy.Request(product.css('a.product-card__link-overlay::attr(href)').get(), self.parse_detail)

  def parse_detail(self, response):
    res = BeautifulSoup(response.text,"html.parser")
    nikeitem = NikeItem()


    # print(res.select('#pdp_product_title')[0].text)

    nikeitem['title'] = res.select('#pdp_product_title')[0].text
    nikeitem['price'] = res.select('.is--current-price')[0].text
    return nikeitem
    # nikeitem['href'] = res.select('#pdp_product_title')[0].text
    # print(res.find('h1').text)
    # res = response.css('#PDP')
    # print(res.css('h1#pdp_product_title::text').get())
