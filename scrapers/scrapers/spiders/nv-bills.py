import logging
import re
import scrapy
import time
from dataclasses import dataclass
from core.scrape import Bill
from ..items import BillStub, Chamber


session_slugs = {
    "2010Special26": "26th2010Special",
    "2013Special27": "27th2013Special",
    "2014Special28": "28th2014Special",
    "2015Special29": "29th2015Special",
    "2016Special30": "30th2016Special",
    "2020Special31": "31st2020Special",
    "2020Special32": "32nd2020Special",
    "2021Special33": "33rd2021Special",
    "2023Special34": "34th2023Special",
    "2023Special35": "35th2023Special",
    "75": "75th2009",
    "76": "76th2011",
    "77": "77th2013",
    "78": "78th2015",
    "79": "79th2017",
    "80": "80th2019",
    "81": "81st2021",
    "82": "82nd2023",
}

# NV sometimes carries-over bills from previous sessions,
# without regard for bill number conflicts.
# so AB1* could get carried in, even if there's already an existing AB1
# The number of asterisks represent which past session it was pulled in from,
# which can include specials, and skip around, so this can't be automated.
# The list is at https://www.leg.state.nv.us/Session/81st2021/Reports/BillsListLegacy.cfm?DoctypeID=1
# where 81st2021 will need to be swapped in for the session code.
CARRYOVERS = {
    "80": {
        "*": "2017",
    },
    "81": {
        "*": "2019",
        "**": "2020Special32",
    },
    "82": {"*": "2021"},
}


@dataclass
class NVBillStub(BillStub):
    subjects: list


# Utility methods
def get_column_div(name, response):
    # lots of places where we have a <div class='col-md-2 font-weight-bold'>
    # followeed by a <div class='col'>
    # with interesting content in the latter element
    return response.xpath(
        f"//div[contains(text(),'{name}')]/following-sibling::div[@class='col']"
    )


def shorten_bill_title(title):
    """
    Used in cases where the bill title exceeds the
    300-character limit that we have on this attribute.
    """
    title_bdr_re = re.compile(r"(.+)(\(BDR \w+-\w+\))")
    title_bdr_match = title_bdr_re.search(title)
    bdr_full = ""
    if title_bdr_match:
        title, bdr_full = title_bdr_match.groups()
    title = f"{title[:280]}... + {bdr_full}"
    return title


class BillTitleLengthError(BaseException):
    def __init__(self, bill_id, title):
        super().__init__(
            f"Title of {bill_id} exceeds 300 characters:"
            f"\n title -> '{title}'"
            f"\n character length -> {len(title)}"
        )


class BillsSpider(scrapy.Spider):
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
        yield scrapy.Request(url=bill_listing_url, callback=self.parse_bill_list, meta=meta)

    def parse_bill_list(self, response):
        bill_link_elems = response.css(".row a")
        logging.info(f"Found {len(bill_link_elems)} bill link elements")
        for link in bill_link_elems:
            bill_url = response.urljoin(link.xpath("@href").get())
            identifier = link.xpath("text()").get()
            chamber = Chamber.UPPER if identifier.startswith("S") else Chamber.LOWER
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
            yield scrapy.Request(
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

        yield bill.as_dict()
