import warnings
from dataclasses import dataclass, fields
from typing import List


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
        field_names = set([f.name for f in fields(self)])
        for k, v in kwargs.items():
            if k in field_names:
                setattr(self, k, v)
        keys_not_considered = {k for k in kwargs.keys() if k not in field_names}
        if keys_not_considered:
            warnings.warn(
                f"Some keys aren't used in the Page Entity: {', '.join(keys_not_considered)}",
                Warning,
            )
