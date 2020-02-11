from abc import ABC, abstractmethod
from curblr.utils import from_camelcase, to_camelcase

class CurbLRObject(ABC):
    
    attrs = []

    @classmethod
    def from_dict(cls, d):
        kwargs = {}
        for a in cls.attrs:
            kwargs[a] = d.get(to_camelcase(a))
        
        return cls(**kwargs)

    def to_dict(self, sub_class):
        d = {}
        for a in sub_class.attrs:
            attr = self.__getattribute__(a)
            if attr:
                cca = to_camelcase(a)
                if isinstance(attr, list):
                    d[cca] = [x.to_dict() if isinstance(x, CurbLRObject) else x for x in attr]
                else:
                    d[cca] = attr.to_dict() if isinstance(attr, CurbLRObject) else attr
        
        return d

    def add_list(self, name, list_attr):
        if list_attr:
            if isinstance(list_attr, (set, tuple)):
                list_attr = list(list_attr)
            if not isinstance(list_attr, list):
                list_attr = [list_attr]
        self.__setattr__(name, list_attr)
