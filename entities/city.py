import uuid
from entities.country import Country


class City:
    def __init__(self):
        self.country:Country
        self.country_id:uuid = None
        """Foreign key of country"""
        self.icon:str = None
        self.id = uuid.uuid4()
        self.name:str
