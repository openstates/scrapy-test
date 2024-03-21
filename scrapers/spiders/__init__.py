from scrapy import Request, Spider
from scrapers.items import StateItem, OrganizationItem


class BaseSpider(Spider):
    def __init__(self, jurisdiction, **kwargs):
        self.jurisdiction = jurisdiction
        super().__init__(**kwargs)

    def start_requests(self):
        # "fake" request in order to get a callback called: callback doesn't actually use the response
        # this is a bit of a hack to get entities yielded that Open States convention expects
        yield Request(url=self.jurisdiction.url, callback=self.yield_jurisdiction_organizations)

        for request in self.do_scrape():
            yield request

    def yield_jurisdiction_organizations(self, jurisdiction_url_response):
        # Jurisdiction scraper
        # yield a single Jurisdiction object
        if self.jurisdiction:
            yield StateItem(self.jurisdiction)
            # yield all organizations
            for org in self.jurisdiction.get_organizations():
                yield OrganizationItem(org)

    def do_scrape(self):
        pass
