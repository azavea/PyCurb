from abc import ABC, abstractmethod

from pycurb.time_rule import TimeRule
from pycurb.utils import from_camelcase, to_camelcase


class PyCurbObject(ABC):

    fields = []

    @classmethod
    def from_dict(cls, d):
        kwargs = {}
        for a in cls.fields:
            kwargs[a] = d.get(to_camelcase(a))

        return cls(**kwargs)

    def to_dict(self, sub_class):
        d = {}
        for f in sub_class.fields:
            obj = self.__getattribute__(f)
            if obj is not None:
                ccf = to_camelcase(f)
                if isinstance(obj, list):
                    d[ccf] = [x.to_dict() if isinstance(
                        x, (PyCurbObject, TimeRule)) else x for x in obj]
                else:
                    d[ccf] = obj.to_dict() if isinstance(
                        obj, (PyCurbObject, TimeRule)) else obj

        return d

    def add_list(self, name, list_attr):
        if list_attr:
            if isinstance(list_attr, (set, tuple)):
                list_attr = list(list_attr)
            if not isinstance(list_attr, list):
                list_attr = [list_attr]
        self.__setattr__(name, list_attr)
