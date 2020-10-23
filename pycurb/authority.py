from typing import Optional

from pycurb import PyCurbObject


class Authority(PyCurbObject):

    name: Optional[str] = None
    url: Optional[str] = None
    phone_number: Optional[str] = None

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
