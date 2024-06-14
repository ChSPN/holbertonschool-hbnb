from datetime import datetime
import uuid
from entities.country import Country
from managers.iRepositoryManager import IRepositoryManager


class City:
    def __init__(self, manager: IRepositoryManager = None):
        self._repo = None if manager is None else manager.cityRepository()
        self.created_at = datetime.now()
        self.updated_at:datetime = None
        self.country:Country
        self.country_id:uuid = None
        """Foreign key of country"""
        self.id = uuid.uuid4()
        self.name:str

    def to_dict(self):
        return {
            'country_id': self.country_id,
            'id': self.id,
            'name': self.name,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

    @staticmethod
    def load(manager: IRepositoryManager, id: uuid = None):
        repo = manager.cityRepository()
        if id is None:
            return repo.get_all()
        else:
            return repo.get_by_id(id)

    @staticmethod
    def load_by_country_code(manager: IRepositoryManager, code: str):
        repo = manager.cityRepository()
        return repo.get_by_country_code(code)

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
