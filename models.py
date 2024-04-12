from pydantic import BaseModel
from enum import Enum


class Brand(Enum):
    NITRO = "Nitro"
    SALOMAN = "Saloman"
    BURTON = "BURTON"

class Snowboard(BaseModel):
    id: int
    length: int
    color: str
    has_bindings: bool
    brand: str