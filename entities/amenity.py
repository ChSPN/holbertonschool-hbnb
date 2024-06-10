from datetime import datetime
import uuid


class Amenity:
    def __init__(self):
        self.created_at = datetime.now()
        self.icon: str = None
        self.id = uuid.uuid4()
        self.name:str
        self.places:list = None
        self.updated_at:datetime = None
