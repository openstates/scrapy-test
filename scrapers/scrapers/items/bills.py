from dataclasses import dataclass
from enum import Enum
from core.scrape import Bill, VoteEvent, Organization, State


class Chamber(str, Enum):
    UPPER = "upper"
    LOWER = "lower"
    LEGISLATURE = "legislature"


@dataclass
class BillStub:
    source_url: str
    identifier: str
    session: str
    chamber: Chamber


@dataclass
class BillItem:
    bill: Bill
    vote_event: VoteEvent
    jurisdiction: State
    organization: Organization
