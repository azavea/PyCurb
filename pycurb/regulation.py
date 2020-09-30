from pycurb import PyCurbObject
from pycurb.rule import Rule
from pycurb.userclass import UserClass


class Regulation(PyCurbObject):

    fields = ['rule', 'user_classes', 'time_spans', 'priority', 'payment']

    def __init__(self,
                 rule,
                 user_classes=None,
                 time_spans=None,
                 priority=None,
                 payment=None):
        self.rule = rule
        self.user_classes = None if user_classes == [{}] else user_classes
        self.time_spans = None if time_spans == [] else time_spans
        self.priority = priority
        self.payment = payment

    def to_dict(self):
        return super().to_dict(Regulation)
