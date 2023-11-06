from dataclasses import dataclass
from enum import Enum


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
