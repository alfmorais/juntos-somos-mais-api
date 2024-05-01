import json

import pytest
from pydantic import ValidationError
from src.api.schemas.base import (
    ConsultantsPreLoad,
    Coordinates,
    Dob,
    Location,
    Name,
    Picture,
    Registered,
    Timezone,
)


def test_dataclass_name_success():
    data = {"title": "mrs", "first": "ione", "last": "da costa"}
    name = Name(**data)

    assert name.title == data["title"]
    assert name.first == data["first"]
    assert name.last == data["last"]


def test_dataclass_name_error():
    expected_result = [
        {
            "type": "string_type",
            "loc": ("title",),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "string_type",
            "loc": ("first",),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "string_type",
            "loc": ("last",),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
    ]
    with pytest.raises(ValidationError) as error:
        Name(**{"title": None, "first": None, "last": None})

    assert error.value.error_count() == 3
    assert error.value.errors() == expected_result


def test_dataclass_coordinates_success():
    data = {"latitude": "-76.3253", "longitude": "137.9437"}
    coordinates = Coordinates(**data)

    assert coordinates.latitude == data["latitude"]
    assert coordinates.longitude == data["longitude"]


def test_dataclass_coordinates_error():
    expected_result = [
        {
            "type": "string_type",
            "loc": ("latitude",),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "string_type",
            "loc": ("longitude",),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
    ]
    with pytest.raises(ValidationError) as error:
        Coordinates(**{"latitude": None, "longitude": None})

    assert error.value.error_count() == 2
    assert error.value.errors() == expected_result


def test_dataclass_timezone_success():
    data = {"offset": "-1:00", "description": "Azores, Cape Verde Islands"}
    timezone = Timezone(**data)

    assert timezone.offset == data["offset"]
    assert timezone.description == data["description"]


def test_dataclass_timezone_error():
    expected_result = [
        {
            "type": "string_type",
            "loc": ("description",),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "string_type",
            "loc": ("offset",),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
    ]
    with pytest.raises(ValidationError) as error:
        Timezone(**{"offset": None, "description": None})

    assert error.value.error_count() == 2
    assert error.value.errors() == expected_result


def test_dataclass_location_success():
    data = {
        "street": "8614 avenida vinícius de morais",
        "city": "ponta grossa",
        "state": "rondonia",
        "postcode": 97701,
        "coordinates": {"latitude": "-76.3253", "longitude": "137.9437"},
        "timezone": {"offset": "-1:00", "description": "Azores, Cape Verde Islands"},
    }
    location = Location(**data)

    assert location.street == data["street"]
    assert location.city == data["city"]
    assert location.state == data["state"]
    assert location.postcode == data["postcode"]
    assert location.coordinates.latitude == data["coordinates"]["latitude"]
    assert location.coordinates.longitude == data["coordinates"]["longitude"]
    assert location.timezone.offset == data["timezone"]["offset"]
    assert location.timezone.description == data["timezone"]["description"]


def test_dataclass_location_error():
    expected_result = [
        {
            "type": "string_type",
            "loc": ("street",),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "string_type",
            "loc": ("city",),
            "msg": "Input should be a valid string",
            "input": False,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "string_type",
            "loc": ("state",),
            "msg": "Input should be a valid string",
            "input": True,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "int_type",
            "loc": ("postcode",),
            "msg": "Input should be a valid integer",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/int_type",
        },
        {
            "type": "string_type",
            "loc": ("coordinates", "latitude"),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "string_type",
            "loc": ("coordinates", "longitude"),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "string_type",
            "loc": ("timezone", "description"),
            "msg": "Input should be a valid string",
            "input": False,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "string_type",
            "loc": ("timezone", "offset"),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
    ]

    with pytest.raises(ValidationError) as error:
        Location(
            **{
                "street": None,
                "city": False,
                "state": True,
                "postcode": None,
                "coordinates": {"latitude": None, "longitude": None},
                "timezone": {
                    "offset": None,
                    "description": False,
                },
            }
        )

    assert error.value.error_count() == 8
    assert error.value.errors() == expected_result


def test_dataclass_dob_success():
    data = {"date": "1968-01-24T18:03:23Z", "age": 50}
    dob = Dob(**data)

    assert dob.date == data["date"]
    assert dob.age == data["age"]


def test_dataclass_dob_error(): ...


def test_dataclass_registered_success():
    data = {"date": "2004-01-23T23:54:33Z", "age": 14}
    registered = Registered(**data)

    assert registered.date == data["date"]
    assert registered.age == data["age"]


def test_dataclass_registered_error():
    expected_result = [
        {
            "type": "string_type",
            "loc": ("date",),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "int_type",
            "loc": ("age",),
            "msg": "Input should be a valid integer",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/int_type",
        },
    ]
    with pytest.raises(ValidationError) as error:
        Registered(**{"date": None, "age": None})

    assert error.value.error_count() == 2
    assert error.value.errors() == expected_result


def test_dataclass_picture_success():
    data = {
        "large": "https://randomuser.me/api/portraits/women/46.jpg",
        "medium": "https://randomuser.me/api/portraits/med/women/46.jpg",
        "thumbnail": "https://randomuser.me/api/portraits/thumb/women/46.jpg",
    }
    picture = Picture(**data)

    assert picture.large == data["large"]
    assert picture.medium == data["medium"]
    assert picture.thumbnail == data["thumbnail"]


def test_dataclass_picture_error():
    expected_result = [
        {
            "type": "string_type",
            "loc": ("large",),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "string_type",
            "loc": ("medium",),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "string_type",
            "loc": ("thumbnail",),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
    ]
    with pytest.raises(ValidationError) as error:
        Picture(
            **{
                "large": None,
                "medium": None,
                "thumbnail": None,
            }
        )

    assert error.value.error_count() == 3
    assert error.value.errors() == expected_result


def test_base_model_consultants_success():
    data = {
        "type": "laborious",
        "gender": "female",
        "name": {"title": "mrs", "first": "ione", "last": "da costa"},
        "location": {
            "street": "8614 avenida vinícius de morais",
            "city": "ponta grossa",
            "state": "rondonia",
            "postcode": 97701,
            "coordinates": {"latitude": "-76.3253", "longitude": "137.9437"},
            "timezone": {
                "offset": "-1:00",
                "description": "Azores, Cape Verde Islands",
            },
        },
        "email": "ione.dacosta@example.com",
        "dob": {"date": "1968-01-24T18:03:23Z", "age": 50},
        "registered": {"date": "2004-01-23T23:54:33Z", "age": 14},
        "phone": "(01) 5415-5648",
        "cell": "(10) 8264-5550",
        "picture": {
            "large": "https://randomuser.me/api/portraits/women/46.jpg",
            "medium": "https://randomuser.me/api/portraits/med/women/46.jpg",
            "thumbnail": "https://randomuser.me/api/portraits/thumb/women/46.jpg",
        },
    }
    consultants = ConsultantsPreLoad(**data).model_dump(warnings=False)

    assert consultants["type"] == "laborious"
    assert consultants["gender"] == "f"
    assert consultants["name"]["title"] == data["name"]["title"]
    assert consultants["name"]["first"] == data["name"]["first"]
    assert consultants["name"]["last"] == data["name"]["last"]
    assert consultants["location"]["street"] == data["location"]["street"]
    assert consultants["location"]["city"] == data["location"]["city"]
    assert consultants["location"]["state"] == data["location"]["state"]
    assert consultants["location"]["postcode"] == data["location"]["postcode"]
    assert (
        consultants["location"]["coordinates"]["latitude"]
        == data["location"]["coordinates"]["latitude"]
    )
    assert (
        consultants["location"]["coordinates"]["longitude"]
        == data["location"]["coordinates"]["longitude"]
    )
    assert (
        consultants["location"]["timezone"]["offset"]
        == data["location"]["timezone"]["offset"]
    )
    assert (
        consultants["location"]["timezone"]["description"]
        == data["location"]["timezone"]["description"]
    )
    assert consultants["email"] == data["email"]
    assert consultants["birthday"] == "1968-01-24T18:03:23Z"
    assert consultants["registered"] == data["registered"]["date"]
    assert consultants["telephone_numbers"] == ["+550154155648"]
    assert consultants["mobile_numbers"] == ["+551082645550"]
    assert consultants["picture"]["large"] == data["picture"]["large"]
    assert consultants["picture"]["medium"] == data["picture"]["medium"]
    assert consultants["picture"]["thumbnail"] == data["picture"]["thumbnail"]


def test_base_model_consultants_error():
    expected_result = [
        {
            "type": "string_type",
            "loc": ("type",),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "string_type",
            "loc": ("gender",),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "string_type",
            "loc": ("name", "title"),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "string_type",
            "loc": ("name", "first"),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "string_type",
            "loc": ("name", "last"),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "string_type",
            "loc": ("location", "street"),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "string_type",
            "loc": ("location", "city"),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "string_type",
            "loc": ("location", "state"),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "int_type",
            "loc": ("location", "postcode"),
            "msg": "Input should be a valid integer",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/int_type",
        },
        {
            "type": "string_type",
            "loc": ("location", "coordinates", "latitude"),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "string_type",
            "loc": ("location", "coordinates", "longitude"),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "string_type",
            "loc": ("location", "timezone", "description"),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "string_type",
            "loc": ("location", "timezone", "offset"),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "string_type",
            "loc": ("email",),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "string_type",
            "loc": ("dob", "date"),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "int_type",
            "loc": ("dob", "age"),
            "msg": "Input should be a valid integer",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/int_type",
        },
        {
            "type": "string_type",
            "loc": ("registered", "date"),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "int_type",
            "loc": ("registered", "age"),
            "msg": "Input should be a valid integer",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/int_type",
        },
        {
            "type": "string_type",
            "loc": ("phone",),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "string_type",
            "loc": ("cell",),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "string_type",
            "loc": ("picture", "large"),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "string_type",
            "loc": ("picture", "medium"),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
        {
            "type": "string_type",
            "loc": ("picture", "thumbnail"),
            "msg": "Input should be a valid string",
            "input": None,
            "url": "https://errors.pydantic.dev/2.7/v/string_type",
        },
    ]
    with pytest.raises(ValidationError) as error:
        ConsultantsPreLoad(
            **{
                "type": None,
                "gender": None,
                "name": {"title": None, "first": None, "last": None},
                "location": {
                    "street": None,
                    "city": None,
                    "state": None,
                    "postcode": None,
                    "coordinates": {"latitude": None, "longitude": None},
                    "timezone": {
                        "offset": None,
                        "description": None,
                    },
                },
                "email": None,
                "dob": {"date": None, "age": None},
                "registered": {"date": None, "age": None},
                "phone": None,
                "cell": None,
                "picture": {
                    "large": None,
                    "medium": None,
                    "thumbnail": None,
                },
            }
        )

    assert error.value.error_count() == 23
    assert error.value.errors() == expected_result


def test_base_model_load_success():
    response_file_path = "tests/data/response.json"

    with open(response_file_path, "r") as file:
        response = json.load(file)["results"]

    for data in response:
        dict(ConsultantsPreLoad(**data))

    assert len(response) == 1000
