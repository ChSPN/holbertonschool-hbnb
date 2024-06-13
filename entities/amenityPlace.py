import uuid


class AmenityPlace:
    def __init__(self):
        self.place_id:uuid
        self.amenity_id:uuid

    def to_dict(self):
        return {
            'place_id': self.place_id,
            'amenity_id': self.amenity_id,
        }
