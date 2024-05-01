import json

import pytest
from src.api.controllers.consultants import ConsultantsController
from src.api.schemas.base import ConsultantsPreLoad


@pytest.mark.parametrize(
    "region,type",
    (
        ["norte", "laborious"],
        ["nordeste", "laborious"],
        ["centro-oeste", "laborious"],
        ["sudeste", "laborious"],
        ["sul", "laborious"],
    ),
)
def test_controllers_consultants_success(region, type):
    response_file_path = "tests/data/response.json"

    with open(response_file_path, "r") as file:
        response = json.load(file)["results"]

    api_response = []

    for data in response:
        mocked_response = ConsultantsPreLoad(**data).model_dump(warnings=False)
        api_response.append(mocked_response)

    controller = ConsultantsController(api_response, region, type)
    response = controller.handle()

    assert isinstance(response, list)
    assert isinstance(response[0], dict)

    assert sorted(response[0]) == [
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
    assert sorted(response[0]["name"]) == ["first", "last", "title"]
    assert sorted(response[0]["location"]) == [
        "city",
        "coordinates",
        "postcode",
        "region",
        "state",
        "street",
        "timezone",
    ]
    assert sorted(response[0]["location"]["coordinates"]) == [
        "latitude",
        "longitude",
    ]
    assert sorted(response[0]["location"]["timezone"]) == [
        "description",
        "offset",
    ]
    assert sorted(response[0]["picture"]) == [
        "large",
        "medium",
        "thumbnail",
    ]
    assert isinstance(response[0]["telephone_numbers"], list)
    assert isinstance(response[0]["mobile_numbers"], list)


@pytest.mark.parametrize(
    "region,type",
    (
        ["norte", "special"],
        ["norte", "normal"],
        ["nordeste", "special"],
        ["nordeste", "normal"],
        ["centro-oeste", "special"],
        ["centro-oeste", "normal"],
        ["sudeste", "special"],
        ["sudeste", "normal"],
        ["sul", "special"],
        ["sul", "normal"],
    ),
)
def test_controllers_consultants_empty_results_success(region, type):
    response_file_path = "tests/data/response.json"

    with open(response_file_path, "r") as file:
        response = json.load(file)["results"]

    api_response = []

    for data in response:
        mocked_response = ConsultantsPreLoad(**data).model_dump(warnings=False)
        api_response.append(mocked_response)

    controller = ConsultantsController(api_response, region, type)
    response = controller.handle()

    assert isinstance(response, list)
    assert len(response) == 0
