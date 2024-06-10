import uuid


class Country:
    def __init__(self):
        self.cities = [] or None
        self.icon = "" or None
        self.id = uuid.uuid4()
        self.name = ""
        