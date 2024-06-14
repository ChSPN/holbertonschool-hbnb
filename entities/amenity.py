from datetime import datetime
import uuid
from managers.iRepositoryManager import IRepositoryManager


class Amenity:
    def __init__(self, manager: IRepositoryManager = None):
        self._repo = None if manager is None else manager.amenityRepository()
        self.created_at = datetime.now()
        self.id = uuid.uuid4()
        self.name:str
        self.places:list = None
        self.updated_at:datetime = None

    def to_dict(self):
        return {
            'created_at': self.created_at,
            'id': self.id,
            'name': self.name,
            'updated_at': self.updated_at,
        }

    @staticmethod
    def load(manager: IRepositoryManager, id: uuid = None):
        repo = manager.amenityRepository()
        if id is None:
            return repo.get_all()
        else:
            return repo.get_by_id(id)

    def delete(self) -> bool:
        if (not self._repo):
            return False

        return self._repo.delete(self.id)

    def save(self) -> bool:
        if (not self._repo or not self.name):
            return False
        
        if (self._repo.exist(self.id)):
            self.updated_at = datetime.now()
            return self._repo.update(self)
        else:
            return self._repo.create(self)
