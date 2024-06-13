import uuid


class CustomerPlace:
    def __init__(self):
        self.place_id:uuid
        self.user_id:uuid

    def to_dict(self):
        return {
            'place_id': self.place_id,
            'user_id': self.user_id,
        }
