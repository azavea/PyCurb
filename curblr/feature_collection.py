import json
from datetime import datetime

from curblr import CurbLRObject, Feature
from curblr.manifest import Manifest
from curblr.utils import time_str


class FeatureCollection(CurbLRObject):

    fields = ['type', 'features', 'manifest']

    def __init__(self, feat_type='FeatureCollection', features=None, manifest=None):
        self.type = feat_type
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
            uri = uri.replace('.json', '_{}.json'.format(time_str()))

        with open(uri, 'w') as dst:
            json.dump(self.to_dict(), dst)
