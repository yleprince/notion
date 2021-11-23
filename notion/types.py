import warnings
from dataclasses import dataclass, fields


@dataclass(init=False)
class Page:
    archived: bool
    cover: dict
    created_time: str
    icon: dict
    id: str
    last_edited_time: str
    object: str
    parent: dict
    properties: dict
    url: str

    def __init__(self, **kwargs):
        attributes = set([f.name for f in fields(self)])
        for k, v in kwargs.items():
            if k in attributes:
                setattr(self, k, v)
        ignored_keys = {k for k in kwargs.keys() if k not in attributes}
        if ignored_keys:
            warnings.warn(
                f"Some keys aren't used in the Page Entity:\
                    {', '.join(ignored_keys)}",
                Warning,
            )
