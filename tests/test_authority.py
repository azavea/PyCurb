import json
from unittest import TestCase

from pycurb.manifest import Authority
from tests.utils.test_cases import get_path


class AuthorityTestCase(TestCase):
    def setUp(self):
        with open(get_path('data-files/authority/authority.json')) as src:
            self.authority_dict = json.load(src)

    def test_authority_properties(self):
        authority = Authority.from_dict(self.authority_dict)
        self.assertDictEqual(self.authority_dict, authority.to_dict())
