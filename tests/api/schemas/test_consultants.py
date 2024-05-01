import pytest
from src.api.schemas.consultants import (
    Consultants,
    Location,
    QueryParams,
    Region,
    Type,
)


@pytest.mark.parametrize(
    "region,type,expected_region,expected_type",
    (
        [Region.norte, Type.special, "norte", "special"],
        [Region.norte, Type.normal, "norte", "normal"],
        [Region.norte, Type.laborious, "norte", "laborious"],
        [Region.nordeste, Type.special, "nordeste", "special"],
        [Region.nordeste, Type.normal, "nordeste", "normal"],
        [Region.nordeste, Type.laborious, "nordeste", "laborious"],
        [Region.centro_oeste, Type.special, "centro-oeste", "special"],
        [Region.centro_oeste, Type.normal, "centro-oeste", "normal"],
        [Region.centro_oeste, Type.laborious, "centro-oeste", "laborious"],
        [Region.sudeste, Type.special, "sudeste", "special"],
        [Region.sudeste, Type.normal, "sudeste", "normal"],
        [Region.sudeste, Type.laborious, "sudeste", "laborious"],
        [Region.sul, Type.special, "sul", "special"],
        [Region.sul, Type.normal, "sul", "normal"],
        [Region.sul, Type.laborious, "sul", "laborious"],
    ),
)
def test_consultant_query_params_success(
    region,
    type,
    expected_region,
    expected_type,
):
    query_params = QueryParams(region=region, type=type)

    assert query_params.region == expected_region
    assert query_params.type == expected_type


@pytest.mark.parametrize(
    "region,type,page,size,status_code",
    (
        ["north", "mid", 1, 1, 422],
        ["north", "low", 1, 1, 422],
        ["north_east", "mid", 1, 1, 422],
        ["north_east", "low", 1, 1, 422],
        ["midwest", "mid", 1, 1, 422],
        ["midwest", "low", 1, 1, 422],
        ["southeast", "mid", 1, 1, 422],
        ["southeast", "low", 1, 1, 422],
        ["south", "mid", 1, 1, 422],
        ["south", "low", 1, 1, 422],
    ),
)
def test_consultant_query_params_errors(
    region,
    type,
    page,
    size,
    status_code,
):
    pass


def test_location_success():
    data = {
        "street": "8614 avenida vinícius de morais",
        "city": "ponta grossa",
        "state": "rondonia",
        "postcode": 97701,
        "coordinates": {
            "latitude": "-76.3253",
            "longitude": "137.9437",
        },
        "timezone": {
            "description": "Azores, Cape Verde Islands",
            "offset": "-1:00",
        },
        "region": "norte",
    }

    location = Location(**data)

    assert isinstance(location, Location)
    assert location.street == "8614 avenida vinícius de morais"
    assert location.city == "ponta grossa"
    assert location.state == "rondonia"
    assert location.postcode == 97701
    assert location.coordinates.latitude == "-76.3253"
    assert location.coordinates.longitude == "137.9437"
    assert location.timezone.description == "Azores, Cape Verde Islands"
    assert location.timezone.offset == "-1:00"
    assert location.region == "norte"


def test_location_error(): ...


def test_consultant_output_success():
    data = {
        "type": "laborious",
        "gender": "f",
        "name": {"title": "mrs", "first": "ione", "last": "da costa"},
        "location": {
            "street": "8614 avenida vinícius de morais",
            "city": "ponta grossa",
            "state": "rondonia",
            "postcode": 97701,
            "coordinates": {"latitude": "-76.3253", "longitude": "137.9437"},
            "timezone": {
                "description": "Azores, Cape Verde Islands",
                "offset": "-1:00",
            },
            "region": "norte",
        },
        "email": "ione.dacosta@example.com",
        "birthday": "1968-01-24T18:03:23Z",
        "registered": "2004-01-23T23:54:33Z",
        "telephone_numbers": ["+550154155648"],
        "mobile_numbers": ["+551082645550"],
        "picture": {
            "large": "https://randomuser.me/api/portraits/women/46.jpg",
            "medium": "https://randomuser.me/api/portraits/med/women/46.jpg",
            "thumbnail": "https://randomuser.me/api/portraits/thumb/women/46.jpg",
        },
        "nacionality": "BR",
    }

    consultant = Consultants(**data).model_dump()

    assert isinstance(consultant, dict)
    assert consultant == data


def test_consultant_output_error(): ...
