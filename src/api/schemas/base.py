from typing import List

from pydantic import BaseModel, EmailStr, Field, field_validator
from pydantic.dataclasses import dataclass
from unidecode import unidecode

from .region import Region


@dataclass
class Name:
    title: str
    first: str
    last: str


@dataclass
class Coordinates:
    latitude: str
    longitude: str


@dataclass
class Timezone:
    description: str
    offset: str


@dataclass
class Location:
    street: str
    city: str
    state: str
    postcode: int
    coordinates: Coordinates
    timezone: Timezone
    region: str = Field(default=None)

    def __post_init__(self):
        self.state = unidecode(self.state).replace(" ", "_")
        self.region = Region().get(self.state)


@dataclass
class Dob:
    date: str
    age: int


@dataclass
class Registered:
    date: str
    age: int


@dataclass
class Picture:
    large: str
    medium: str
    thumbnail: str


class ConsultantsPreLoad(BaseModel):
    type: str = Field(default="laborious")
    gender: str
    name: Name
    location: Location
    email: str
    birthday: Dob = Field(alias="dob")
    registered: Registered
    telephone_numbers: str = Field(alias="phone")
    mobile_numbers: str = Field(alias="cell")
    picture: Picture
    nacionality: str = Field(default="BR")

    class ConfigDict:
        validate_assignment = True

    @field_validator("gender")
    @classmethod
    def set_representative_gender_letter(cls, gender: str) -> str:
        gender_representative_letter = {
            "female": "f",
            "male": "m",
        }
        return gender_representative_letter[gender.lower()]

    @field_validator("email")
    @classmethod
    def set_email(cls, email: EmailStr) -> str:
        return email.replace(" ", "")

    @field_validator("birthday")
    @classmethod
    def set_birthday(cls, dob: Dob) -> str:
        return dob.date

    @field_validator("registered")
    @classmethod
    def set_registered(cls, registered: Registered) -> str:
        return registered.date

    @field_validator("telephone_numbers")
    @classmethod
    def format_telephone_numbers(cls, telephone_numbers: str) -> List:
        return cls.__format_general_numbers(telephone_numbers)

    @field_validator("mobile_numbers")
    @classmethod
    def format_mobile_numbers(cls, mobile_numbers: str) -> List:
        return cls.__format_general_numbers(mobile_numbers)

    @classmethod
    def __format_general_numbers(cls, phone: str) -> List:
        if phone:
            numbers = "".join(
                filter(
                    str.isdigit,
                    phone,
                )
            )
            formatted_phone = "+55{}".format(numbers)
            return [formatted_phone]
