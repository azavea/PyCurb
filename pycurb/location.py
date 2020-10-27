from typing import List, Optional
from enum import Enum
from pycurb import PyCurbObject
from pycurb.utils import from_camelcase


class SideOfStreet(Enum):
    LEFT = 'left'
    RIGHT = 'right'
    UNKNOWN = 'unknown'


class BaysAngle(Enum):
    PARRALLEL = 'parallel'
    PERPENDICULAR = 'perpendicular'
    DIAGONAL = 'diagonal'


class LocationStatus(Enum):
    ACTIVE = 'active'
    PLANNED = 'planned'
    PROPOSED = 'proposed'


class Location(PyCurbObject):
    shst_ref_id: str
    side_of_street: SideOfStreet
    shst_location_start: float
    shst_location_end: float
    object_id: Optional[str]
    derived_from: Optional[List[str]]
    asset_type: str
    asset_sub_type: Optional[str]
    bays_angle: Optional[BaysAngle]
    bays_count: Optional[int]
    street_name: Optional[str]
    status: Optional[LocationStatus]

    def __init__(self, **kwargs):
        d = {from_camelcase(k): v for k, v in kwargs.items()}

        super().__init__(**d)

    def to_dict(self):
        d = super().to_dict()

        for k, v in d.items():
            if isinstance(v, Enum):
                d[k] = v.value

        return d

    @classmethod
    def from_lr_feature(cls,
                        feature,
                        asset_type,
                        object_id=None,
                        derived_from=None,
                        asset_subtype=None,
                        bays_angle=None,
                        bays_count=None,
                        street_name=None,
                        status=None):

        props = feature['properties']

        d = {}
        d['shst_ref_id'] = props['shstReferenceId']
        d['shst_location_start'] = props['start']
        d['shst_location_end'] = props['end']
        d['side_of_street'] = props['sideOfStreet']
        d['asset_type'] = props[asset_type]

        if object_id:
            d['object_id'] = props[object_id]
        if derived_from:
            d['derived_from'] = props[derived_from]
        if asset_subtype:
            d['asset_subtype'] = props[asset_subtype]
        if bays_angle:
            d['bays_angle'] = props[bays_angle]
        if bays_count:
            d['bays_count'] = props[bays_count]
        if street_name:
            d['street_name'] = props[street_name]
        if status:
            d['status'] = props[status]

        return cls.from_dict(d)
