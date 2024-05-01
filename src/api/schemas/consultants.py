from enum import Enum
from typing import List

from pydantic import BaseModel
from pydantic.dataclasses import dataclass
from src.api.schemas.base import Coordinates, Name, Picture, Timezone


class Region(str, Enum):
    norte = "norte"
    nordeste = "nordeste"
    centro_oeste = "centro-oeste"
    sudeste = "sudeste"
    sul = "sul"


class Type(str, Enum):
    special = "special"
    normal = "normal"
    laborious = "laborious"


class QueryParams(BaseModel):
    region: Region
    type: Type


@dataclass
class Location:
    street: str
    city: str
    state: str
    postcode: int
    coordinates: Coordinates
    timezone: Timezone
    region: str


class Consultants(BaseModel):
    type: str
    gender: str
    name: Name
    location: Location
    email: str
    birthday: str
    registered: str
    telephone_numbers: List[str]
    mobile_numbers: List[str]
    picture: Picture
    nacionality: str

    class ConfigDict:
        validate_assignment = True
