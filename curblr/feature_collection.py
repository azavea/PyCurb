from curblr import CurbLRObject, Feature
from curblr.manifest import Manifest
class FeatureCollection(CurbLRObject):
    
    attrs = ['type', 'features', 'manifest']

    def __init__(self, feat_type='FeatureCollection', features=None, manifest=None):
        self.type = feat_type
        self.features = features
        self.manifest = manifest

    def add_feature(self, feature):
        if not self.features:
            self.features = []
        self.features.append(feature)

    @classmethod
    def from_dict(cls, d):
        feat_type = d.get('type') if d.get('type') else 'FetureCollection'
        features = None
        if d.get('features'):
            features = [Feature.from_dict(f) for f in d.get('features')]
        manifest = None
        if d.get('manifest'):
            manifest = Manifest.from_dict(d.get('manifest'))

        return cls(feat_type=feat_type, features=features, manifest=manifest)
    
    def to_dict(self):
        return super().to_dict(FeatureCollection)