import json
from unittest import TestCase

from pycurb import Manifest
from tests.utils.test_cases import get_path


class AuthorityTestCase(TestCase):
    def setUp(self):
        with open(get_path('data-files/manifest/manifest.json')) as src:
            self.manifest_dict = json.load(src)

    def test_manifest_properties(self):
        self.maxDiff = 900
        manifest = Manifest.from_dict(self.manifest_dict)
        self.assertDictEqual(self.manifest_dict, manifest.to_dict())
