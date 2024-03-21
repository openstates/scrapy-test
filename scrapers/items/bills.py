import inspect
import uuid
from typing import Any, Union
from dataclasses import dataclass
from enum import Enum
from core.scrape import Bill, State, Organization, VoteEvent
from core.scrape.base import BaseModel


class Chamber(str, Enum):
    UPPER = "upper"
    LOWER = "lower"
    LEGISLATURE = "legislature"
    EXECUTIVE = "executive"


bill_stub_schema = {
    "type": "object",
    "properties": {
        "source_url": {"type": "string", "minLength": 1},
        "identifier": {"type": "string", "minLength": 1},
        "legislative_session": {"type": "string", "minLength": 1},
        "chamber": {"type": "string", "enum": Chamber},
        "extras": {"type": "object"},
    },
}


class BillStub(BaseModel):
    _type = "bill_stub"
    _schema = bill_stub_schema

    def __init__(
            self,
            source_url,
            identifier,
            legislative_session,
            chamber,
    ):
        super(BillStub, self).__init__()

        self.source_url = source_url
        self.identifier = identifier
        self.legislative_session = legislative_session
        self.chamber = chamber

    def __str__(self):
        return self.identifier + " in " + self.legislative_session

# @dataclass
# class BillStub:
#     source_url: str
#     identifier: str
#     session: str
#     chamber: Chamber
#
#     def __init__(self):
#         self._id = str(uuid.uuid1())


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
    def __init__(self, item: Union[Bill, None] = None):
        super().__init__(item)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._id})'


@dataclass
class BillStubItem(BaseItem):
    def __init__(self, item: Union[BillStub, None] = None):
        super().__init__(item)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._id})'


@dataclass
class StateItem(BaseItem):
    def __init__(self, item: Union[State, None] = None):
        super().__init__(item)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._id})'


@dataclass
class OrganizationItem(BaseItem):
    def __init__(self, item: Union[Organization, None] = None):
        super().__init__(item)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._id})'


@dataclass
class VoteEventItem(BaseItem):
    def __init__(self, item: Union[VoteEvent, None] = None):
        super().__init__(item)

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self._id})'
