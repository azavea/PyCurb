from curblr import CurbLRObject
from curblr.rule import Rule
from curblr.userclass import UserClass

class Regulation(CurbLRObject):

    attrs = ['rule', 'user_classes', 'time_spans', 'priority', 'payment']
    
    def __init__(self,
                 rule,
                 user_classes=None,
                 time_spans=None,
                 priority=None,
                 payment=None):
        self.rule = rule
        self.user_classes = user_classes
        self.time_spans = time_spans
        self.priority = priority
        self.payment = payment

    def to_dict(self):
        return super().to_dict(Regulation)