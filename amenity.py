from datetime import datetime
import uuid


class Amenity:
    def __init__(self):
        self.created_at = datetime.now()
        self.icon = "" or None
        self.id = uuid.uuid4()
        self.name = ""
        self.places = [] or None
        self.updated_at = None
