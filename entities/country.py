from datetime import datetime
import uuid
from managers.iRepositoryManager import IRepositoryManager


class Country:
    def __init__(self, manager: IRepositoryManager = None):
        self._repo = None if manager is None else manager.countryRepository()
        self.created_at = datetime.now()
        self.updated_at:datetime = None
        self.cities:list = None
        self.code:str
        self.id = uuid.uuid4()
        self.name:str 

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'code': self.code,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
        }

    @staticmethod
    def load(manager: IRepositoryManager, id: uuid = None):
        repo = manager.countryRepository()
        if id is None:
            return repo.get_all()
        else:
            return repo.get_by_id(id)

    @staticmethod
    def load_by_code(manager: IRepositoryManager, code: str):
        repo = manager.countryRepository()
        return repo.get_by_code(code)

    def delete(self) -> bool:
        if (not self._repo):
            return False

        return self._repo.delete(self.id)

    def save(self) -> bool:
        if (not self._repo
            or not self.name
            or not self.code):
            return False
        
        if (self._repo.exist(self.id)):
            self.updated_at = datetime.now()
            return self._repo.update(self)
        else:
            return self._repo.create(self)
