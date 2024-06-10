import uuid


class Country:
    def __init__(self):
        self.cities:list = None
        self.icon:str = None
        self.id = uuid.uuid4()
        self.name:str
