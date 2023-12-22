from dataclasses import dataclass
from enum import Enum
from scrapy.item import Item, Field
from core.scrape import Bill, State, Organization, VoteEvent
import inspect


class Chamber(str, Enum):
    UPPER = "upper"
    LOWER = "lower"
    LEGISLATURE = "legislature"
    EXECUTIVE = "executive"


@dataclass
class BillStub:
    source_url: str
    identifier: str
    session: str
    chamber: Chamber


class BaseItem:
    @classmethod
    def load(cls, item):
        for name, value in inspect.getmembers(item):
            if not name.startswith('__'):
                setattr(cls, name,  value)
        return cls()


@dataclass
class BillItem(BaseItem):
    def __repr__(self) -> str:
        return f'BillItem({self._id})'


@dataclass
class StateItem(BaseItem):
    def __repr__(self) -> str:
        return f'StateItem({self._id})'


@dataclass
class OrganizationItem(BaseItem):
    def __repr__(self) -> str:
        return f'OrganizationItem({self._id})'


@dataclass
class VoteEventItem(BaseItem):
    def __repr__(self) -> str:
        return f'VoteEventItem({self._id})'
