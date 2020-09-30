from pycurb import PyCurbObject
from pycurb.authority import Authority
from pycurb.utils import from_camelcase
from pycurb.constants import ACTIVITIES


class Rule(PyCurbObject):

    fields = ['activity', 'reason', 'max_stay',
              'no_return', 'payment', 'authority']

    def __init__(self,
                 activity,
                 reason=None,
                 max_stay=None,
                 no_return=None,
                 payment=False,
                 authority=None):

        if activity.lower() in ACTIVITIES:
            self.activity = activity.lower()
        else:
            Exception('"activity" value must be one of {}, got {}'.format(
                ACTIVITIES, activity))

        self.reason = reason
        self.max_stay = max_stay
        self.no_return = no_return
        self.payment = payment
        self.authority = authority

    def to_dict(self):
        return super().to_dict(Rule)
