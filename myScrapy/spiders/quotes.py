import scrapy
from scrapy_selenium import SeleniumRequest
from selenium import webdriver
import pandas as pd
from time import sleep

class QuotesSpider(scrapy.Spider):
  driver = webdriver.Chrome()
  driver.get('https://quotes.toscrape.com/page/1/')
  sleep(10)

  name = "quotes"
  allowed_domains = ["quotes.toscrape.com"]
  # start_urls = ["https://quotes.toscrape.com"]

  def start_requests(self):
    url='https://quotes.toscrape.com/'
    yield SeleniumRequest(
      url=url,
      callback=self.parse,
      wait_time=10
    )

  def parse(self, response):
      print('===== parse(self, response) =====')
      # print(response)
      # r = response.css('h1').get()
      # t = response.css('h1 > a::text').get()
      # print(r)
      # print(t)

      for quote in response.css('div.quote'):
        d = {
            'text': quote.css('span.text::text').get(),
            'author': quote.css('small.author::text').get(),
            'tags': quote.css('div.tags a.tag::text').getall(),
        }
        # print(d)
        yield d
      
      next_page = response.css('li.next a::attr(href)').get()
      print(f'=========={next_page}==========')
      if next_page is not None:
        yield response.follow(next_page, callback=self.parse)

      print('===========')

  driver.close()

      # pass
