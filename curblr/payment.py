from curblr import CurbLRObject
from curblr.utils import from_camelcase, to_camelcase


class Payment(CurbLRObject):
    def __init__(self, rates=None, methods=None, forms=None, operator=None, phone=None, device_ids=None):
        self.add_list('rates', rates)
        self.add_list('methods', methods)
        self.add_list('forms', forms)
        self.operator = operator
        self.phone = phone
        self.add_list('device_ids', device_ids)

    @staticmethod
    def from_dict(d):
        nd = {}
        if 'rates' in d:
            d['rates'] = [Rate.from_dict(rd) for rd in d['rates']]
        for k in list(d.keys()):
            nd[from_camelcase(k)] = d.pop(k)
        return Payment(**nd)

    def to_dict(self):
        d = {}

        if self.rates:
            d['rates'] = [r.to_dict() for r in self.rates]
        if self.methods:
            d['methods'] = self.methods
        if self.forms:
            d['forms'] = self.forms
        if self.operator:
            d['operator'] = self.operator
        if self.phone:
            d['phone'] = self.phone
        if self.device_ids:
            d['deviceIds'] = self.device_ids
        
        return d


class Rate(CurbLRObject):
    def __init__(self, fees=None, durations=None, time_spans=None):
        self.add_list('fees', fees)
        self.add_list('durations', durations)
        self.add_list('time_spans', time_spans)
    
    @classmethod
    def from_dict(cls, d):
        nd = {}
        for k in list(d.keys()):
            nd[from_camelcase(k)] = d.pop(k)
        return cls(**d)

    def to_dict(self):
        d = {}
        if self.fees:
            d['fees'] = self.fees
        if self.durations:
            d['durations'] = self.durations
        if self.time_spans:
            d['timeSpans'] = self.time_spans

        return d