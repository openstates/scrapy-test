from scrapy import Spider
from scrapers.items import StateItem, OrganizationItem


class BaseSpider(Spider):
    def __init__(self,  **kwargs):
        super().__init__(**kwargs)

    def parse(self, response):
        # Jurisdiction scraper
        # yield a single Jurisdiction object
        if self.jurisdiction:
            yield StateItem(self.jurisdiction)
            # yield all organizations
            for org in self.jurisdiction.get_organizations():
                yield OrganizationItem(org)

        for request in self.do_scrape(response):
            yield request

    def do_scrape(self, response):
        pass
