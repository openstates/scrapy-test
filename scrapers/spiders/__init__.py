from scrapy import Spider


class BaseSpider(Spider):
    def __init__(self,  **kwargs):
        super().__init__(**kwargs)

    def parse(self, response):
        # Jurisdiction scraper
        # yield a single Jurisdiction object
        if self.jurisdiction:
            yield dict(jurisdiction=self.jurisdiction)
            # yield all organizations
            for org in self.jurisdiction.get_organizations():
                yield dict(organization=org)

        for request in self.do_scrape(response):
            yield request

    def do_scrape(self, response):
        pass
