from unittest.mock import MagicMock, patch

from cachetools import TTLCache
from src.api.cache import cache


def test_cache_isinstance_success():
    assert isinstance(cache, TTLCache)
    assert cache.maxsize == 2000
    assert cache.ttl == 86400


@patch("src.api.cache.cache")
def test_cache_object(mock_cache):
    mock_cache.return_value = {"consultants": []}

    assert isinstance(mock_cache, MagicMock)
