from pycurb import PyCurbObject


class Payment(PyCurbObject):

    fields = ['rates', 'methods', 'forms', 'operator', 'phone', 'device_ids']

    def __init__(self,
                 device_ids=None,
                 forms=None,
                 methods=None,
                 operator=None,
                 phone=None,
                 rates=None):
        self.rates = []
        self.methods = []
        self.forms = []
        self.device_ids = []

        self.add_list('rates', rates)
        self.add_list('methods', methods)
        self.add_list('forms', forms)
        self.add_list('device_ids', device_ids)

        self.operator = operator
        self.phone = phone

    def to_dict(self):
        return super().to_dict(Payment)


class Rate(PyCurbObject):

    fields = ['fees', 'durations', 'time_spans']

    def __init__(self, fees=None, durations=None, time_spans=None):
        self.fees = []
        self.durations = []
        self.time_spans = []

        self.add_list('fees', fees)
        self.add_list('durations', durations)
        self.add_list('time_spans', time_spans)

    def to_dict(self):
        return super().to_dict(Rate)
