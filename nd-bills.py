import scrapy
import pandas as pd
import logging

class NdBillsSpider(scrapy.Spider):
    name = "nd-bills"
    allowed_domains = ["ndlegis.gov"]
    start_urls = ["https://ndlegis.gov"]

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
        "Accept-Language": "en-US,en;q=0.9",
        "Host": "www.ndlegis.gov",
        "Connection": "keep-alive",
        "Upgrade-Insecure-Requests": "1",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36"
    }

    def start_requests(self):
        urls = [f'https://www.ndlegis.gov/assembly/68-2023/bill-index.html']
        for url in urls:
            yield scrapy.Request(url=url, callback=self.parse, headers=self.headers)

    def parse(self, response):
        try:
            cards = response.xpath("//div[@class='col bill']")
            logging.info(f"Number of cards: {len(cards)}")

            bill_status1 = []
            jurisdictions = []
            organization_classification = []
            bill_details = response.xpath("//h4[@class='bill-name flex']/text()").getall()
            bill_status = response.xpath("//span[1][@data-toggle='tooltip']/@class").getall()

            for b in bill_status:
                if b == "passed-bill flex-right hide":
                    bill_status1.append('Failed')
                else:
                    bill_status1.append('Passed')
                jurisdictions.append('North Dakota')

            for i in bill_details:
                if i.startswith('H'):
                    organization_classification.append('Lower')
                else:
                    organization_classification.append('Upper')

            bill_type1 = response.xpath("//div[@class='card']/ul/li[3]/text()").getall()
            chamber = response.xpath("//div[@class='card']/ul/li[4]/text()").getall()
            assembly = response.xpath("//div[@class='card']/ul/li[6]/text()").getall()
            session = response.xpath("//div[@class='card']/ul/li[7]/text()").getall()
            session_date_month = response.xpath("//div[@class='card']/ul/li[5]/text()").getall()

            bill_urls = response.xpath("//a[@class='card-link']/@href").getall()
            sponsors = response.xpath("//div[@class='sponsors scroll']/p/text()").getall()
            bill_description = response.xpath("//p[@class='title scroll']/text()").getall()
            last_official_action = response.xpath("//div[@class='final-action scroll']/p/text()").getall()

            logging.info(f"Number of bill details: {len(bill_details)}")
            logging.info(f"Number of last official actions: {len(last_official_action)}")
            logging.info(f"Number of bill URLs: {len(bill_urls)}")
            logging.info(f"Number of sponsors: {len(sponsors)}")
            logging.info(f"Number of bill descriptions: {len(bill_description)}")
            logging.info(f"Number of bill types: {len(bill_type1)}")
            logging.info(f"Number of chambers: {len(chamber)}")
            logging.info(f"Number of assemblies: {len(assembly)}")
            logging.info(f"Number of sessions: {len(session)}")
            logging.info(f"Number of bill statuses: {len(bill_status1)}")

            datadetails = {
                "identifier": bill_details,
                "title": bill_description,
                "classifications": bill_type1,
                "session_identifiers": assembly,
                "jurisdiction": jurisdictions,
                "organization_classification": organization_classification,
                "bill_urls": bill_urls,
                "sponsors": sponsors,
                "last_official_action": last_official_action,
                "chamber": chamber,
                "session": session,
                "bill_status": bill_status1,
                "session_date_month": session_date_month,
            }

            df = pd.DataFrame(datadetails)
            df.to_csv(r'D:/north_dakota_bills.csv')

        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
