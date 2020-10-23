from abc import ABC

from pycurb.utils import to_camelcase, from_camelcase

from pydantic import BaseModel


class PyCurbObject(ABC, BaseModel):
    @classmethod
    def from_dict(cls, d):
        d = {from_camelcase(k): v for k, v in d.items() if v is not None}

        return cls(**d)

    def to_dict(self):
        d = self.dict()

        return {to_camelcase(k): v for k, v in d.items() if v is not None}

    def add_list(self, name, list_attr):
        if list_attr:
            if isinstance(list_attr, (set, tuple)):
                list_attr = list(list_attr)
            if not isinstance(list_attr, list):
                list_attr = [list_attr]
        self.__setattr__(name, list_attr)
