from os import getenv

import requests
from dotenv import load_dotenv
from requests.models import Response

from notion.types import Page

load_dotenv()


class NotionClient:
    def __init__(self, token: str | None = None):
        token = getenv("NOTION_TOKEN") if token is None else token
        assert isinstance(token, str)  # checks that the token != None
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
        r = self._get_page(page_uuid=page_uuid).json()
        return Page(**r)

    def __str__(self) -> str:
        return self.bearer_token
