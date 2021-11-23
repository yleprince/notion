import json
import os
from unittest import mock

import responses
from pytest import fixture

from notion.client import NotionClient
from notion.types import Page


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

    @fixture(autouse=True)
    def page_tutu_str(self) -> str:
        return '{"object":"page","id":"tutu","created_time":"2021-09-29T13:36:00.000Z","last_edited_time":"2021-11-20T21:17:00.000Z","cover":{"type":"external","external":{"url":"https://www.notion.so/images/page-cover/gradients_10.jpg"}},"icon":{"type":"emoji","emoji":"🏆"},"parent":{"type":"workspace","workspace":true},"archived":false,"properties":{"title":{"id":"title","type":"title","title":[{"type":"text","text":{"content":"🎄test-page","link":null},"annotations":{"bold":false,"italic":false,"strikethrough":false,"underline":false,"code":false,"color":"default"},"plain_text":"🎄test-page","href":null}]}},"url":"https://www.notion.so/test-page-tutu"}'

    @fixture(autouse=True)
    def mock_tutu(self, page_tutu_str) -> None:
        responses.add(
            **{
                "method": responses.GET,
                "url": "https://api.notion.com/v1/pages/tutu",
                "body": page_tutu_str,
                "status": 200,
                "content_type": "application/json",
            }
        )

    @responses.activate
    def test__get_page(self, client, page_tutu_str, mock_tutu):
        response = client._get_page(page_uuid="tutu")

        assert response.json() == json.loads(page_tutu_str)

    @responses.activate
    def test_get_page(self, client, mock_tutu):
        expected_page: Page = Page(
            archived=False,
            cover={
                "type": "external",
                "external": {
                    "url": "https://www.notion.so/images/page-cover/gradients_10.jpg"
                },
            },
            created_time="2021-09-29T13:36:00.000Z",
            icon={"type": "emoji", "emoji": "🏆"},
            id="tutu",
            last_edited_time="2021-11-20T21:17:00.000Z",
            object="page",
            parent={"type": "workspace", "workspace": True},
            properties={
                "title": {
                    "id": "title",
                    "type": "title",
                    "title": [
                        {
                            "type": "text",
                            "text": {"content": "🎄test-page", "link": None},
                            "annotations": {
                                "bold": False,
                                "italic": False,
                                "strikethrough": False,
                                "underline": False,
                                "code": False,
                                "color": "default",
                            },
                            "plain_text": "🎄test-page",
                            "href": None,
                        }
                    ],
                }
            },
            url="https://www.notion.so/test-page-tutu",
        )
        result = client.get_page(page_uuid="tutu")

        assert result == expected_page
