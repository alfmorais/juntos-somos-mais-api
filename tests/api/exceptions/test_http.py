from src.api.exceptions.http import HttpException


def test_http_exceptions():
    error = HttpException("API Gateway timeout")

    assert error.mensage == "API Gateway timeout"
    assert str(error) == "Error: API Gateway timeout"
