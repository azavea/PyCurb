from unittest import TestCase

from pycurb.utils import to_camelcase


class UtilsTestCase(TestCase):
    def test_to_camelcase(self):
        self.assertEqual(to_camelcase(None), None)
        self.assertEqual(to_camelcase(''), '')
        self.assertEqual(to_camelcase('  '), '')
        self.assertEqual(to_camelcase(1), '1')

        cc = 'camelCase'
        self.assertEqual(to_camelcase('camel_case'), cc)
        self.assertEqual(to_camelcase('Camel_Case'), cc)
        self.assertEqual(to_camelcase(cc), cc)
        # no way to catch this
        self.assertEqual(to_camelcase('camelcase'), 'camelcase')

        self.assertEqual(to_camelcase('CamelCase'), cc)

        self.assertEqual(to_camelcase('camel case'), cc)
        self.assertEqual(to_camelcase('camel_case too'), 'camelCaseToo')
