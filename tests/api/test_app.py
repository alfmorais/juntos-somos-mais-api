from unittest.mock import patch

from fastapi.testclient import TestClient
from src.api.app import BASE_URL, CSV, JSON, app, lifespan

client = TestClient(app)


def test_juntos_somos_mais_success():
    response = client.get("/")

    assert response.status_code == 200
    assert response.json() == {"message": "Quero fazer parte do time!!!"}


def test_app_urls_variables():
    assert BASE_URL == "https://storage.googleapis.com/juntossomosmais-code-challenge/"
    assert CSV == "input-backend.csv"
    assert JSON == "input-backend.json"


@patch("src.api.app.ConsultantsJsonController.request")
@patch("src.api.app.ConsultantsCsvController.request")
async def test_lifespan_success(mock_csv, mock_json):
    async with lifespan(app):
        ...

    assert mock_csv.await_count == 1
    assert mock_json.await_count == 1
