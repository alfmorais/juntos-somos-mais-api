from typing import AnyStr, Dict, Tuple

from aiohttp import ClientSession


class BaseClient:
    def __init__(self, url: str) -> None:
        self.url = url


class JsonClient(BaseClient):
    async def request(self) -> Tuple[Dict, int]:
        async with ClientSession() as session:
            async with session.get(url=self.url) as response:
                return await response.json(), response.status


class CsvClient(BaseClient):
    async def request(self) -> Tuple[AnyStr, int]:
        async with ClientSession() as session:
            async with session.get(url=self.url) as response:
                return (
                    await response.text(encoding="utf-8-sig"),
                    response.status,
                )  # noqa E501
