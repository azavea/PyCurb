from abc import ABC, abstractmethod

from curblr import CurbLRObject
from curblr.utils import (parse_date, parse_day_of_month, parse_day_of_week,
                          parse_occurrence, parse_time, from_camelcase)

class TimeRule(ABC):
    pass

class EffectiveDates(TimeRule):
    def __init__(self, date_from, date_to):
        self.date_from = parse_date(date_from)
        self.date_to = parse_date(date_to)
        self.year = False
        if len(date_from.split('-')) > 2 and len(date_to.split('-')) > 2:
            self.year = True

    @staticmethod
    def from_dict(d):
        return EffectiveDates(d['from'], d['to'])

    def to_dict(self):
        d = {
            'from': '{}-{}'.format(self.date_from.month, self.date_from.day),
            'to': '{}-{}'.format(self.date_to.month, self.date_to.day)
        }

        if self.year:
            d['from'] = '{}-'.format(self.date_from.year) + d['from']
            d['to'] = '{}-'.format(self.date_to.year) + d['to']

        return d


class TimeOfDay(TimeRule):
    def __init__(self, time_from, time_to):
        self.time_from = parse_time(time_from)
        self.time_to = parse_time(time_to)

    def is_equal(self, time_of_day):
        return self.to_dict() == time_of_day.to_dict()

    @staticmethod
    def from_dict(d):
        return TimeOfDay(d['from'], d['to'])

    def to_dict(self):
        st_h = str(self.time_from.hour).zfill(2)
        st_m = str(self.time_from.minute).zfill(2)
        en_h = str(self.time_to.hour).zfill(2)
        en_m = str(self.time_to.minute).zfill(2)
        return {'from': '{}:{}'.format(st_h, st_m), 'to': '{}:{}'.format(en_h, en_m)}


class DaysOfWeek(TimeRule):
    def __init__(self, days, occurences_in_month=None):
        if isinstance(days, str):
            days = [days]
        self.days = [parse_day_of_week(day) for day in days]
        self.occurences_in_month = None
        if occurences_in_month:
            self.occurences_in_month = [
                parse_occurrence(o) for o in occurences_in_month]

    @staticmethod
    def from_dict(d):
        return DaysOfWeek(d['days'])

    def to_dict(self):
        return {'days': self.days}


class DaysOfMonth(TimeRule):
    def __init__(self, days):
        if isinstance(days, 'str'):
            days = [days]
        self.days = [parse_day_of_month(day) for day in days]

    @staticmethod
    def from_dict(d):
        return DaysOfMonth(d['days'])

    def to_dict(self):
        return {'days': self.days}


class DesignatedPeriod(TimeRule):
    def __init__(self, name, apply):
        self.name = name
        apply = apply.lower()
        self.apply = None
        if apply in ('except during', 'only during'):
            self.apply = apply

    @staticmethod
    def from_dict(d):
        return DesignatedPeriod(d['name'], d['apply'])

    def to_dict(self):
        d = {'name': self.name}
        if self.apply:
            d['apply'] = self.apply

        return d

class TimeSpan(CurbLRObject):
    name_to_class = {
        'effectiveDates': EffectiveDates,
        'daysOfWeek': DaysOfWeek,
        'daysOfMonth': DaysOfMonth,
        'timesOfDay': TimeOfDay,
        'designatedPeriods': DesignatedPeriod}
    
    def __init__(self,
                 effective_dates=None,
                 days_of_week=None,
                 days_of_month=None,
                 times_of_day=None,
                 designated_periods=None):
        self.effective_dates = effective_dates
        self.days_of_week = days_of_week
        self.days_of_month = days_of_month
        self.times_of_day = times_of_day
        self.designated_periods = designated_periods
    
    def add_time_of_day(self, time_of_day):
        if not self.times_of_day:
            self.times_of_day = []
        for tod in self.times_of_day:
            if tod.is_equal(time_of_day):
                return
        self.times_of_day.append(time_of_day)

    @staticmethod
    def from_dict(d):
        pass

    def to_dict(self):
        d = {}
        for k, _ in TimeSpan.name_to_class.items():
            a = getattr(self, from_camelcase(k))
            aa = [a] if not isinstance(a, list) else a
            if not None in aa:
                if k == 'timesOfDay':
                    d[k] = [t.to_dict() for t in a]
                else:
                    try:
                        if isinstance(a, list):
                            d[k] = [ka.to_dict() for ka in a]
                        else:
                            d[k] = a.to_dict()
                    except AttributeError:
                        print()
        
        return d