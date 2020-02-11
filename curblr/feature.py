from curblr import Regulation, Location, CurbLRObject


class Feature(CurbLRObject):

    fields = ['geometry', 'location', 'regulations', 'images']

    def __init__(self, geometry, location=None, regulations=None, images=None):
        self.type = 'Feature'
        self.geometry = geometry
        self.location = location
        self.regulations = regulations
        self.images = images

    def add_regulation(self, reg):
        if not self.regulations:
            self.regulations = []
        self.regulations.append(reg)

    def add_image(self, image):
        if not self.images:
            self.images = []
        self.images.append(image)

    def to_dict(self, keep_shapely=False):
        ld = None
        if self.location:
            ld = self.location.to_dict()

        d = {
            'type': self.type,
            'geometry': self.geometry,
            'properties': {
                'location': ld,
                'regulations': [r.to_dict() for r in self.regulations]
            }
        }

        if self.images:
            d['properties']['images'] = self.images

        if not keep_shapely:
            d['geometry'] = d['geometry'].__geo_interface__

        return d

    def add_location(self, location):
        self.location = Location

    @staticmethod
    def from_lr_feature(feature, **kwargs):
        return Feature(feature['geometry'], Location.from_lr_feature(feature, **kwargs))
