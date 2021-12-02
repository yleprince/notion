from os import getenv

import requests
from dotenv import load_dotenv
from requests.models import Response

from notion.types import Page, Block

load_dotenv()


class NotionClient:
    def __init__(self, token: str | None = None):
        token = getenv("NOTION_TOKEN") if token is None else token
        if token is None or not isinstance(token, str):
            raise TypeError("Notion token should be defined.")

        self.bearer_token: str = token
        self.headers = {
            "Authorization": f"Bearer {self.bearer_token}",
            "Notion-Version": "2021-08-16",
        }
        self.api_root: str = "https://api.notion.com/v1"

    def _get_page(self, page_uuid: str) -> Response:
        page_route = f"{self.api_root}/pages/{page_uuid}"
        return requests.get(page_route, headers=self.headers)

    def get_page(self, page_uuid: str) -> Page:
        """
        Allow to retrieve a page from Notion.
        :param page_uuid: unique id (can be found within the url: `https://www.notion.so/test-page-cc7e60738e1143169432b3f75c6cc564`)
        :return: instance of Page (cf notion.types.Page)
        >>> client.get_page(page_uuid = "cc7e60738e1143169432b3f75c6cc564")
        Page(...)
        """
        r = self._get_page(page_uuid=page_uuid).json()
        return Page(**r)

    def _get_block(self, block_uuid: str) -> Response:
        block_route = f"{self.api_root}/blocks/{block_uuid}"
        return requests.get(block_route, headers=self.headers)

    def get_block(self, block_uuid: str) -> Block:
        """
        Allow to retrieve a block from Notion.
        :param block_uuid: unique id
        :return: instance of Page (cf notion.types.Page)
        >>> client.get_block(page_uuid = "cc7e60738e1143169432b3f75c6cc564")
        Block(...)
        """
        r = self._get_block(block_uuid=block_uuid).json()
        from pprint import pprint

        pprint(r)
        return Block(**r)

    def __str__(self) -> str:
        return self.bearer_token
