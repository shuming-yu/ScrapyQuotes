import scrapy
from scrapy_selenium import SeleniumRequest

class InsideSpider(scrapy.Spider):
  name = "inside"
  allowed_domains = ["www.inside.com.tw"]
  # start_urls = ["https://www.inside.com.tw/tag/ai"]

  def start_requests(self):
    url='https://www.inside.com.tw/tag/ai'
    yield SeleniumRequest(
      url=url,
      callback=self.parse,
      wait_time=10
    )

  def parse(self, response):
    # urls = response.css("a.js-auto_break_title::attr(href)").getall()
    
    # titles = response.xpath("//a[@class='js-auto_break_title']/text()").getall()
    # titles = response.xpath("//div[@class='post_list_item_content']/h3[@class='post_title']/a/text()").getall()
    # titles = response.xpath("//a[@class='js-auto_break_title']/@href").getall()

    # print('===== parse(self, response) =====')

    # for t in titles:
    #   print(t)

    # print('===========')


    print('===== parse(self, response) =====')

    # 爬取文章標題
    # post_titles = response.xpath("//h3[@class='post_title']/a[@class='js-auto_break_title']/text()").getall()
    post_titles = response.xpath("//h3[@class='post_title']/a/text()").getall()
    # 爬取發佈日期
    post_dates = response.xpath("//li[@class='post_date']/span/text()").getall()
    # 爬取作者
    post_authors = response.xpath("//span[@class='post_author']/a/text()").getall()

    for data in zip(post_titles, post_dates, post_authors):
      newItem = {
        "post_title": data[0],
        "post_date": data[1],
        "post_author": data[2]
      }
      yield newItem

    print('===========')

    # pass