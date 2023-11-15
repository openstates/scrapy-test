import logging
import re
import time

from scrapy import Request, Spider
from dataclasses import dataclass

from core.scrape import Bill
from .consts import session_slugs, CARRYOVERS
from .exceptions import BillTitleLengthError, SelectorError
from .utils import (
    add_actions,
    add_sponsors,
    extract_bdr,
    get_column_div,
    shorten_bill_title,
)
from ..items import BillStub, Chamber


@dataclass
class NVBillStub(BillStub):
    subjects: list


class BillsSpider(Spider):
    name = "nv-bills"
    session = None

    def __init__(self, session=None, **kwargs):
        self.session = session
        super().__init__(**kwargs)

    def start_requests(self):
        # TODO default active sessions
        slug = session_slugs[self.session]
        bill_listing_url = (f"https://www.leg.state.nv.us/App/NELIS/REL/{slug}/"
                            "HomeBill/BillsTab?selectedTab=List&Filters.PageSize=2147483647"
                            f"&_={time.time()}")
        meta = {
            "is_scout": True
        }
        yield Request(url=bill_listing_url, callback=self.parse_bill_list, meta=meta)

    def parse_bill_list(self, response):
        bill_link_elems = response.css(".row a")
        logging.info(f"Found {len(bill_link_elems)} bill link elements")
        for link in bill_link_elems:
            bill_url = response.urljoin(link.xpath("@href").get())
            identifier = link.xpath("text()").get()
            chamber = Chamber.UPPER if identifier.startswith(
                "S") else Chamber.LOWER
            bill_stub = NVBillStub(
                bill_url,
                link.xpath("text()").get(),
                self.session,
                chamber,
                []
            )

            # Yield the stub
            yield bill_stub

            # Yield a request for the bill details page
            bill_key = bill_url.split("/")[-2]
            slug = session_slugs[self.session]
            bill_ajax_request_url = (
                f"https://www.leg.state.nv.us/App/NELIS/REL/{slug}/Bill/"
                f"FillSelectedBillTab?selectedTab=Overview&billKey={bill_key}"
                f"&_={time.time()}"
            )
            bill_overview_parser_args = {
                "bill_stub": bill_stub,
            }

            yield Request(
                url=bill_ajax_request_url,
                callback=self.parse_bill_overview,
                cb_kwargs=bill_overview_parser_args
            )

    def parse_bill_overview(self, response, bill_stub):
        short_title = get_column_div("Summary", response).xpath("text()").get()
        long_title = response.css("#title::text").get()

        if "*" in bill_stub.identifier:
            stars = re.search(r"\*+", bill_stub.identifier).group()
            if (
                    self.session in CARRYOVERS
                    and stars in CARRYOVERS[self.session]
            ):
                bill_stub.identifier = re.sub(
                    r"\*+",
                    "-" + CARRYOVERS[self.session][stars],
                    bill_stub.identifier,
                )
            else:
                logging.error(
                    f"Unidentified carryover bill {bill_stub.identifier}. Update CARRYOVERS dict in bills.py"
                )
                return

        # Only known cases where bill title is over 300 characters
        if self.session == "82":
            if bill_stub.identifier in ("SJR7-2021", "AB488"):
                short_title = shorten_bill_title(short_title)
            # If additional case arises in future
        elif len(short_title) > 300:
            raise BillTitleLengthError(bill_stub.identifier, short_title)

        bill = Bill(
            identifier=bill_stub.identifier,
            legislative_session=self.session,
            title=short_title,
            chamber=bill_stub.chamber,
        )
        bill.subject = bill_stub.subjects
        # use the pretty source URL
        bill.add_source(bill_stub.source_url)
        bill.add_title(long_title)

        try:
            sponsors = get_column_div("Primary Sponsor", response)
            add_sponsors(bill, sponsors.css("a"), primary=True)
        except SelectorError:
            pass
        try:
            cosponsors = get_column_div("Co-Sponsor", response)
            add_sponsors(bill, cosponsors.css("a"), primary=False)
        except SelectorError:
            pass

        # TODO: figure out cosponsor div name, can't find any as of Feb 2021
        add_actions(bill, bill_stub.chamber, response)

        bdr = extract_bdr(short_title)
        if bdr:
            bill.extras["BDR"] = bdr

        text_url = response.url.replace("Overview", "Text")
        bill_tab_text_parser_args = {"bill": bill}

        yield Request(
            url=text_url,
            callback=self.parse_bill_tab_text,
            cb_kwargs=bill_tab_text_parser_args
        )

    def parse_bill_tab_text(self, response, bill):
        # some BDRs have no text link
        for row in response.css(".d-md-none .h5 a"):
            title = row.xpath('text()').get().strip()
            link = response.urljoin(row.xpath("@href").get())
            bill.add_version_link(
                title, link, media_type="application/pdf", on_duplicate="ignore"
            )

        ex_url = response.url.replace("Text", "Exhibits")
        exhibit_tab_text_parser_args = {"bill": bill}

        yield Request(
            url=ex_url,
            callback=self.parse_exhibit_tab_text,
            cb_kwargs=exhibit_tab_text_parser_args
        )

    def parse_exhibit_tab_text(self, response, bill):
        for row in response.css("li.my-4 a"):
            title = row.xpath('text()').get().strip()
            link = response.urljoin(row.xpath("@href").get())
            bill.add_document_link(
                title, link, media_type="application/pdf", on_duplicate="ignore"
            )

        am_url = response.url.replace("Exhibits", "Amendments")
        amendment_tab_text_parser_args = {"bill": bill}

        yield Request(
            url=am_url,
            callback=self.parse_amendment_tab_text,
            cb_kwargs=amendment_tab_text_parser_args
        )

    def parse_amendment_tab_text(self, response, bill):
        for row in response.css(".col-11.col-md a"):
            title = row.xpath('text()').get().strip()
            link = response.urljoin(row.xpath("@href").get())
            bill.add_version_link(
                title, link, media_type="application/pdf", on_duplicate="ignore"
            )

        fn_url = response.url.replace("Amendments", "FiscalNotes")
        fiscal_tab_text_parser_args = {"bill": bill}

        yield Request(
            url=fn_url,
            callback=self.parse_fiscal_tab_text,
            cb_kwargs=fiscal_tab_text_parser_args
        )

    def parse_fiscal_tab_text(self, response, bill):
        for row in response.css("ul.list-unstyled li a"):
            title = row.xpath('text()').get().strip()
            title = f"Fiscal Note: {title}"
            link = response.urljoin(response.urljoin(row.xpath("@href").get()))
            bill.add_document_link(
                title, link, media_type="application/pdf", on_duplicate="ignore"
            )

        yield bill.as_dict()
