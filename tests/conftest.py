import responses
from pytest import fixture

from notion.types import Page


@fixture(autouse=True)
def page_tutu_str() -> str:
    return '{"object":"page","id":"tutu",\
        "created_time":"2021-09-29T13:36:00.000Z",\
        "last_edited_time":"2021-11-20T21:17:00.000Z",\
        "cover":{\
        "type":"external","external":{\
        "url":"https://www.notion.so/images/page-cover/gradients_10.jpg"\
        }},\
        "icon":{"type":"emoji","emoji":"🏆"},\
        "parent":{"type":"workspace","workspace":true},\
        "archived":false,\
        "properties":{\
        "title":{\
            "id":"title",\
            "type":"title",\
            "title":[{\
            "type":"text",\
            "text":{"content":"🎄test-page","link":null},\
            "annotations":{\
                "bold":false,"italic":false,"strikethrough":false,\
                "underline":false,"code":false,"color":"default"\
            },\
            "plain_text":"🎄test-page",\
            "href":null\
            }]\
        }\
        },\
        "url":"https://www.notion.so/test-page-tutu"\
    }'


@fixture(autouse=True)
def mock_tutu(page_tutu_str) -> None:
    responses.add(
        **{
            "method": responses.GET,
            "url": "https://api.notion.com/v1/pages/tutu",
            "body": page_tutu_str,
            "status": 200,
            "content_type": "application/json",
        }
    )


@fixture(autouse=True)
def page_tutu() -> Page:
    cover_url = "https://www.notion.so/images/page-cover/gradients_10.jpg"
    return Page(
        archived=False,
        cover={
            "type": "external",
            "external": {"url": cover_url},
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
