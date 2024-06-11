from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor


class CSpider(CrawlSpider):
    # to give the crawler a name so it can be called in terminal
    name = "tcrawler"

    # to allow where it can crawl when searching for links in a page and it doesn't go far like to FB, YT, etc.
    allowed_domains = ["toscrape.com"]

    # to give it a starting point to start crawling
    start_urls = ["http://books.toscrape.com/"]


    # to decide where to crawl within subpages or sub categories of a page
    rules = (
        Rule(LinkExtractor(allow="catalogue/category")),
        Rule(LinkExtractor(allow="catalogue", deny="category"), callback="parse_item")
    )


    # function parse_item to decide what kind of info to pick like title, price, availability, etc.
    def parse_item(self, response):
        yield {
            "title": response.css(".product_main h1::text").get(),
            "price": response.css(".price_color::text").get(),
            "availability": response.css(".availability::text")[1].get().replace("\n", "").replace(" ", "")
        }
