from dataclasses import dataclass
from decimal import Decimal
from typing import Optional


@dataclass(slots=True)
class Row:
    name: str
    brand: Optional[str]
    price: Optional[int]
    rating: Optional[Decimal]