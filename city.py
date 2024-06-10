import uuid


class City:
    def __init__(self):
        self.country = None
        self.country_id = None
        """Foreign key of country"""
        self.icon = "" or None
        self.id = uuid.uuid4()
        self.name = ""
