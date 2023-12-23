import inspect
from typing import Any
from dataclasses import dataclass
from enum import Enum
from core.scrape import Bill, State, Organization, VoteEvent


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
    def __init__(self, item: Any):
        # item should be Openstates class objects like Bill, State, Organization, VoteEvent
        if not item:
            raise TypeError(
                'item argument of BaseItem should\'t be empty.')
        for name, value in inspect.getmembers(item):
            if name.startswith('__'):
                continue
            self.__setattr__(name,  value)


@dataclass
class BillItem(BaseItem):
    def __init__(self, item: Bill | None = None):
        super().__init__(item)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._id})'


@dataclass
class StateItem(BaseItem):
    def __init__(self, item: State | None = None):
        super().__init__(item)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._id})'


@dataclass
class OrganizationItem(BaseItem):
    def __init__(self, item: Organization | None = None):
        super().__init__(item)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._id})'


@dataclass
class VoteEventItem(BaseItem):
    def __init__(self, item: VoteEvent | None = None):
        super().__init__(item)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._id})'
