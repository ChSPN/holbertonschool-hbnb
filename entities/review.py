from datetime import datetime
import uuid


class Review:
    def __init__(self):
        self.comment:str
        self.created_at = datetime.now()
        self.customer = None
        self.customer_id:uuid
        """Foreign key of customer"""
        self.id = uuid.uuid4()
        self.place = None
        self.place_id:uuid
        """Foreign key of place"""
        self.updated_at:datetime = None

    def to_dict(self):
        return {
            'comment': self.comment,
            'created_at': self.created_at,
            'customer_id': self.customer_id,
            'id': self.id,
            'place_id': self.place_id,
            'updated_at': self.updated_at,
        }
