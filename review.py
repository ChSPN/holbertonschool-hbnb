from datetime import datetime
import uuid

class Review:
    def __init__(self):
        self.comment = ""
        self.created_at = datetime.now()
        self.customer = None
        self.customer_id = None
        """Foreign key of customer"""
        self.id = uuid.uuid4()
        self.place = None
        self.place_id = None
        """Foreign key of place"""
        self.updated_at = None
