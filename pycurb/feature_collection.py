import json

from pycurb import PyCurbObject, Feature
from pycurb.manifest import Manifest
from pycurb.utils import time_str


class FeatureCollection(PyCurbObject):

    fields = ['type', 'features', 'manifest']

    def __init__(self, type='FeatureCollection', features=None, manifest=None):
        self.type = type
        if features:
            self.features = []
            for f in features:
                if isinstance(f, dict):
                    self.features.append(Feature.from_dict(f))
                else:
                    self.features.append(f)
        else:
            self.features = features
        if isinstance(manifest, dict):
            self.manifest = Manifest.from_dict(manifest)
        else:
            self.manifest = manifest

    def add_feature(self, feature):
        if not self.features:
            self.features = []
        self.features.append(feature)

    def to_dict(self):
        return super().to_dict(FeatureCollection)

    def save(self, uri, add_timestamp=False):
        if add_timestamp:
            uri = uri.replace('.pycurb.json',
                              '_{}.pycurb.json'.format(time_str()))

        with open(uri, 'w') as dst:
            json.dump(self.to_dict(),
                      dst,
                      sort_keys=True,
                      indent=4,
                      separators=(',', ': '))

    @staticmethod
    def from_file(uri):
        with open(uri, 'r') as src:
            d = json.load(src)
        return FeatureCollection.from_dict(d)
