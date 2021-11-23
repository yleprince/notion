import json
import os
from unittest import mock

import responses
from pytest import fixture

from notion.client import NotionClient


class TestNotionClient:
    @mock.patch.dict(os.environ, {"NOTION_TOKEN": "mockMyBearerToken"})
    def test_client_environment_token(self):
        myClient = NotionClient()
        assert str(myClient) == "mockMyBearerToken"

    def test_client_custom_token(self):
        myClient = NotionClient("secondMockMyBearerToken")
        assert str(myClient) == "secondMockMyBearerToken"


class TestNotionClientMethods:
    @fixture(autouse=True)
    def client(self) -> NotionClient:
        return NotionClient()

    @responses.activate
    def test__get_page(self, client, page_tutu_str, mock_tutu):
        response = client._get_page(page_uuid="tutu")

        assert response.json() == json.loads(page_tutu_str)

    @responses.activate
    def test_get_page(self, client, mock_tutu, page_tutu):
        result = client.get_page(page_uuid="tutu")

        assert result == page_tutu
