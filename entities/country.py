from datetime import datetime
import uuid
import tzlocal
from managers.iRepositoryManager import IRepositoryManager


class Country:
    def __init__(self, manager: IRepositoryManager = None, country: dict = None):
        self._repo = None if manager is None else manager.countryRepository()
        self.id = uuid.uuid4()
        self.created_at = datetime.now(tzlocal.get_localzone())
        self.updated_at:datetime = None
        self.code:str
        self.name:str
        self.parse(country)

    def to_dict(self):
        return {
            'id': self.id,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'name': self.name,
            'code': self.code,
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
    
    def parse(self, country: dict = None):
        if country and 'id' in country:
            self.id = uuid.UUID(country['id']) if country['id'] is str else country['id']
        if country and 'created_at' in country:
            self.created_at = country['created_at']
        if country and 'updated_at' in country:
            self.updated_at = country['updated_at']
        self.name = country['name'] if country and 'name' in country else None
        self.code = country['code'] if country and 'code' in country else None

    def delete(self) -> bool:
        if (not self._repo):
            return False

        return self._repo.delete(self.id)
    
    def exist(self, code: str) -> bool:
        if (not self._repo):
            return False

        return self._repo.exist(self.id, code)

    def save(self) -> bool:
        if (not self._repo
            or not self.name
            or not self.code
            or self.exist(self.code)):
            return False
        
        if (self._repo.exist(self.id)):
            self.updated_at = datetime.now(tzlocal.get_localzone())
            return self._repo.update(self)
        else:
            return self._repo.create(self)
