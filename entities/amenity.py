from datetime import datetime
import uuid
from repositories.iAmenityRepository import IAmenityRepository


class Amenity:
    def __init__(self, repo: IAmenityRepository = None):
        self._repo = repo or None
        self.created_at = datetime.now()
        self.icon: str = None
        self.id = uuid.uuid4()
        self.name:str
        self.places:list = None
        self.updated_at:datetime = None

    def save(self) -> bool:
        if (not self._repo):
            return False
        
        if (not self.name):
            return False
        
        if (self._repo.exist(self.id)):
            self.updated_at = datetime.now()
            return self._repo.update(self)
        else:
            return self._repo.create(self)
