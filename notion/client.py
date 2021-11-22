import requests
from requests.models import Response
from dotenv import load_dotenv
from dataclasses import fields
from os import getenv

from notion.types import Page

load_dotenv()


class NotionClient:
    def __init__(self, bearer_token: str = None):
        self.bearer_token = bearer_token or getenv("NOTION_TOKEN")
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


if __name__ == "__main__":
    myClient = NotionClient()

    from pprint import pprint

    pprint(myClient._get_page("cc7e60738e1143169432b3f75c6cc564").json())
    print()
    print("\n", myClient.get_page("cc7e60738e1143169432b3f75c6cc564"))