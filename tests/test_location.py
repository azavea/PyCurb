import json
from unittest import TestCase

from pycurb import Location
from tests.utils.test_cases import get_path


class LocationTestCase(TestCase):
    def setUp(self):
        with open(get_path('data-files/location/location-1.json')) as src:
            self.location1_dict = json.load(src)
        with open(get_path('data-files/location/lr-feature.json')) as src:
            self.lr_feature_dict = json.load(src)

    def test_location_properties(self):
        location = Location.from_dict(self.location1_dict)
        self.assertDictEqual(self.location1_dict, location.to_dict())

        lfr_args = {
            'asset_type': 'asset_type',
            'object_id': 'pp_objectid',
            'derived_from': 'pp_derived',
            'bays_angle': 'pp_parking_angle',
            'street_name': 'pp_street',
            'status': 'pp_status'
        }

        location_from_lr = Location.from_lr_feature(self.lr_feature_dict,
                                                    **lfr_args)
        self.assertDictEqual(location.to_dict(), location_from_lr.to_dict())
