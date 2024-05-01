from unittest.mock import patch

import pytest
from src.api.controllers.csv import ConsultantsCsvController
from src.api.exceptions.http import HttpException
from src.api.integrations.client import CsvClient
from src.api.schemas.base import ConsultantsPreLoad


@pytest.mark.vcr()
async def test_format_consultants_csv_success():
    expected_result = {
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
    client = CsvClient(
        url="https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.csv"  # noqa E501
    )
    format_consultants = ConsultantsCsvController(
        client=client,
        schema=ConsultantsPreLoad,
    )

    response = await format_consultants.request()

    assert isinstance(response, list)
    assert isinstance(response[0], dict)
    assert len(response) == 1000
    assert response[0] == expected_result


@patch("src.api.controllers.csv.CsvClient.request")
async def test_format_consultants_csv_error(mock_client):
    mock_client.return_value = (
        {"results": "error"},
        400,
    )
    client = CsvClient(
        url="https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.csv"  # noqa E501
    )

    with pytest.raises(HttpException) as error:
        format_consultants = ConsultantsCsvController(
            client=client,
            schema=ConsultantsPreLoad,
        )

        await format_consultants.request()

    assert error.value.mensage == "Error when collect data from api."
