# Utility methods
import dateutil.parser
import pytz
import re

from .consts import ACTION_CLASSIFIERS
from .exceptions import SelectorError

TZ = pytz.timezone("PST8PDT")


def get_column_div(name, response):
    # lots of places where we have a <div class='col-md-2 font-weight-bold'>
    # followeed by a <div class='col'>
    # with interesting content in the latter element
    return response.xpath(
        f"//div[contains(text(),'{name}')]/following-sibling::div[@class='col']"
    )


def parse_date(date_str):
    return TZ.localize(dateutil.parser.parse(date_str))


def add_sponsors(bill, sponsor_links, primary):
    seen = set()
    for link in sponsor_links:
        name = link.xpath('text()').get().strip()
        if "Sponsors" in name or name == "":
            continue
        # Removes leg position from name
        # Example: Assemblywoman Alexis Hansen
        if name.split()[0] in ["Assemblywoman", "Assemblyman", "Senator"]:
            name = " ".join(name.split()[1:]).strip()
        if name not in seen:
            seen.add(name)
            bill.add_sponsorship(
                name=name,
                classification="sponsor" if primary else "cosponsor",
                entity_type="person",
                primary=primary,
            )


def add_actions(bill, chamber, response):
    # first action is from originating chamber
    actor = chamber

    # Sometimes NV bill page might just not have an actions section at all
    try:
        for row in response.xpath("//caption/parent::table/tbody/tr"):
            date = row.css('[data-th="Date"]::text').get()
            action = row.css('[data-th="Action"]::text').get()

            date = parse_date(date)

            # catch chamber changes
            if action.startswith("In Assembly"):
                actor = "lower"
            elif action.startswith("In Senate"):
                actor = "upper"
            elif "Governor" in action:
                actor = "executive"

            action_type = []
            for pattern, atype in ACTION_CLASSIFIERS:
                if not re.search(pattern, action, re.IGNORECASE):
                    continue
                # sometimes NV returns multiple actions in the same posting
                # so don't break here
                action_type = action_type + atype

            if not action_type:
                action_type = None
            else:
                action_type = list(set(action_type))

            related_entities = []
            if "Committee on" in action:
                committees = re.findall(
                    r"Committee on ([a-zA-Z, ]*)\.", action)
                for committee in committees:
                    related_entities.append(
                        {"type": "committee", "name": committee}
                    )

            bill.add_action(
                description=action,
                date=date,
                chamber=actor,
                classification=action_type,
                related_entities=related_entities,
            )
    except SelectorError:
        pass


def extract_bdr(title):
    """
    bills in NV start with a 'bill draft request'
    the number is in the title but it's useful as a structured extra
    """
    bdr = False
    bdr_regex = re.search(r"\(BDR (\w+-\w+)\)", title)
    if bdr_regex:
        bdr = bdr_regex.group(1)
    return bdr


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
