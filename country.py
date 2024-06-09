import uuid
from city import City


class Country:
    def __init__(self):
        self.cities = list[City] or None
        self.icon = str or None
        self.id = uuid.uuid4()
        self.name = str
