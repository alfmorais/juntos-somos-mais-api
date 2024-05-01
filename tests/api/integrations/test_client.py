from unittest.mock import patch

import pytest
from src.api.integrations.client import CsvClient, JsonClient


@pytest.mark.vcr()
async def test_json_client_success():
    url = "https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.json"  # noqa E501
    client = JsonClient(url=url)

    response, status_code = await client.request()

    assert isinstance(response, dict)
    assert isinstance(status_code, int)
    assert status_code == 200


@patch("src.api.integrations.client.JsonClient.request")
async def test_json_client_error(mock_json_client):
    expected_error_message = "Attempt to decode JSON with unexpected mimetype: application/xml; charset=utf-8"  # noqa E501
    mock_json_client.return_value = ({"error": expected_error_message}, 400)

    url = "https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.json"  # noqa E501

    client = JsonClient(url=url)
    response, status_code = await client.request()

    assert response == {"error": expected_error_message}
    assert status_code == 400


@pytest.mark.vcr()
async def test_csv_client_success():
    url = "https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.csv"  # noqa E501

    client = CsvClient(url=url)

    response, status_code = await client.request()

    assert isinstance(response, str)
    assert isinstance(status_code, int)
    assert status_code == 200


@patch("src.api.integrations.client.CsvClient.request")
async def test_csv_client_error(mock_json_client):
    expected_error_message = "Attempt to decode JSON with unexpected mimetype: application/xml; charset=utf-8"  # noqa E501
    mock_json_client.return_value = ({"error": expected_error_message}, 400)

    url = "https://storage.googleapis.com/juntossomosmais-code-challenge/input-backend.csv"  # noqa E501

    client = CsvClient(url=url)
    response, status_code = await client.request()

    assert response == {"error": expected_error_message}
    assert status_code == 400
