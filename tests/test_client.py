from notion.client import NotionClient


def test_client():
    myClient = NotionClient()
    assert str(NotionClient) == "toto"
