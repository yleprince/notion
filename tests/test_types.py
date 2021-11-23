from pytest import warns

from notion.types import Page


class TestTypePage:
    def test_page(self, page_tutu):
        assert isinstance(page_tutu, Page)

    # Tests that a warning is raised when extra argument is given to the
    # constructor.
    def test_page_warning(self):
        assert warns(
            Warning,
            Page,
            **{
                "extra_argument": 12,
                "archived": False,
                "cover": dict(),
                "created_time": "",
                "icon": dict(),
                "id": "",
                "last_edited_time": "",
                "object": "",
                "parent": dict(),
                "properties": dict(),
                "url": "",
            },
        )
