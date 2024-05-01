import json

import pytest
from fastapi.testclient import TestClient
from src.api.app import app
from src.api.cache import cache
from src.api.schemas.base import ConsultantsPreLoad


@pytest.mark.parametrize(
    "region,type,page,size,status_code",
    (
        ["norte", "laborious", 1, 1, 200],
        ["nordeste", "laborious", 1, 1, 200],
        ["centro-oeste", "laborious", 1, 1, 200],
        ["sudeste", "laborious", 1, 1, 200],
        ["sul", "laborious", 1, 1, 200],
    ),
)
def test_views_consultants_success(
    region,
    type,
    page,
    size,
    status_code,
):
    response_file_path = "tests/data/response.json"

    with open(response_file_path, "r") as file:
        response = json.load(file)["results"]

    api_response = []

    for data in response:
        mocked_response = ConsultantsPreLoad(**data).model_dump(warnings=False)
        api_response.append(mocked_response)

    client = TestClient(app)
    cache["consultants"] = api_response

    url = "/api/v1/consultants?region={}&type={}&page={}&size={}".format(
        region,
        type,
        page,
        size,
    )
    response = client.get(url)
    response_json = response.json()

    assert response.status_code == status_code
    assert isinstance(response_json, dict)
    assert response_json["page"] == page
    assert response_json["size"] == size
    assert sorted(response_json) == ["items", "page", "pages", "size", "total"]
    assert sorted(response_json["items"][0]) == [
        "birthday",
        "email",
        "gender",
        "location",
        "mobile_numbers",
        "nacionality",
        "name",
        "picture",
        "registered",
        "telephone_numbers",
        "type",
    ]
    assert sorted(response_json["items"][0]["name"]) == ["first", "last", "title"]
    assert sorted(response_json["items"][0]["location"]) == [
        "city",
        "coordinates",
        "postcode",
        "region",
        "state",
        "street",
        "timezone",
    ]
    assert sorted(response_json["items"][0]["location"]["coordinates"]) == [
        "latitude",
        "longitude",
    ]
    assert sorted(response_json["items"][0]["location"]["timezone"]) == [
        "description",
        "offset",
    ]
    assert sorted(response_json["items"][0]["picture"]) == [
        "large",
        "medium",
        "thumbnail",
    ]
    assert isinstance(response_json["items"][0]["telephone_numbers"], list)
    assert isinstance(response_json["items"][0]["mobile_numbers"], list)


@pytest.mark.parametrize(
    "region,type,page,size,status_code",
    (
        ["norte", "special", 1, 1, 200],
        ["norte", "normal", 1, 1, 200],
        ["nordeste", "special", 1, 1, 200],
        ["nordeste", "normal", 1, 1, 200],
        ["centro-oeste", "special", 1, 1, 200],
        ["centro-oeste", "normal", 1, 1, 200],
        ["sudeste", "special", 1, 1, 200],
        ["sudeste", "normal", 1, 1, 200],
        ["sul", "special", 1, 1, 200],
        ["sul", "normal", 1, 1, 200],
    ),
)
def test_views_consultants_empty_results_success(
    region,
    type,
    page,
    size,
    status_code,
):
    response_file_path = "tests/data/response.json"

    with open(response_file_path, "r") as file:
        response = json.load(file)["results"]

    api_response = []

    for data in response:
        mocked_response = ConsultantsPreLoad(**data).model_dump(warnings=False)
        api_response.append(mocked_response)

    client = TestClient(app)
    cache["consultants"] = api_response

    url = "/api/v1/consultants?region={}&type={}&page={}&size={}".format(
        region,
        type,
        page,
        size,
    )
    response = client.get(url)
    response_json = response.json()

    assert response.status_code == status_code
    assert isinstance(response_json, dict)
    assert response_json["page"] == page
    assert response_json["size"] == size
    assert response_json["total"] == 0
    assert response_json["pages"] == 0
    assert sorted(response_json.keys()) == ["items", "page", "pages", "size", "total"]


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
def test_views_consultants_error(
    region,
    type,
    page,
    size,
    status_code,
):
    expected_result = {
        "detail": [
            {
                "type": "enum",
                "loc": ["query", "region"],
                "msg": "Input should be 'norte', 'nordeste', 'centro-oeste', 'sudeste' or 'sul'",  # noqa E501
                "input": region,
                "ctx": {
                    "expected": "'norte', 'nordeste', 'centro-oeste', 'sudeste' or 'sul'"
                },
            },
            {
                "type": "enum",
                "loc": ["query", "type"],
                "msg": "Input should be 'special', 'normal' or 'laborious'",
                "input": type,
                "ctx": {"expected": "'special', 'normal' or 'laborious'"},
            },
        ]
    }
    client = TestClient(app)

    url = "/api/v1/consultants?region={}&type={}&page={}&size={}".format(
        region,
        type,
        page,
        size,
    )
    response = client.get(url)

    assert response.status_code == status_code
    assert response.json() == expected_result
