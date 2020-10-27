from datetime import datetime
from typing import List, Optional

from pycurb import PyCurbObject
from pycurb.utils import from_camelcase, parse_date


class Authority(PyCurbObject):
    name: str
    url: str
    phone: Optional[str] = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class Date:
    # Pycurb stores timestamps as python datetime objects. CurbLR
    # requires ISO8601 format for the strings in the JSON but as of
    # now is not specific about which variant to use so this class
    # is necessary to store the original string.
    def __init__(self, date_string: str) -> None:
        self.date_string = date_string
        self.date = parse_date(date_string)

    def to_dict(self):
        return self.date_string


class Manifest(PyCurbObject):
    created_date: Date
    last_updated_date: Optional[datetime] = None
    curblr_version: Optional[str] = None
    time_zone: str
    currency: str
    unit_height_length: Optional[str] = None
    unit_weight: Optional[str] = None
    priority_hierarchy: List[str]
    authority: Authority

    def __init__(self, **kwargs):
        d = {from_camelcase(k): v for k, v in kwargs.items()}

        if not isinstance(d['created_date'], datetime):
            d['created_date'] = Date(d['created_date'])

        if 'last_updated_date' in d:
            if not isinstance(d['last_updated_date'], datetime):
                d['last_updated_date'] = Date(d['last_updated_date'])

        d['authority'] = Authority.from_dict(d['authority'])

        super().__init__(**d)

    def to_dict(self):
        d = super().to_dict()

        # manually convert the date feilds back to the original string
        for k, v in d.items():
            if isinstance(v, Date):
                d[k] = v.date_string

        return d
