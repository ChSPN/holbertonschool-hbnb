import uuid
from entities.country import Country
from managers.persistenceFileManager import PersistenceFileManager
from repositories.iCountryRepository import ICountryRepository


class CountryMockRepository(ICountryRepository):
    def __init__(self,
                 create: bool = True, 
                 update: bool = True, 
                 delete: bool = True,
                 exist: bool = True,
                 get_by_id: Country = None,
                 get_by_code: Country = None,
                 get_all: list[Country] = None):
        super().__init__()
        self._create = create
        self._update = update
        self._delete = delete
        self._exist = exist
        self._get_by_id = get_by_id
        self._get_by_code = get_by_code
        self._get_all = get_all

    def create(self, city) -> bool:
        return self._create

    def update(self, city) -> bool:
        return self._update

    def delete(self, city_id: uuid) -> bool:
        return self._delete

    def get_by_id(self, city_id: uuid):
        return self._get_by_id

    def get_by_code(self, code: str):
        return self._get_by_code

    def get_all(self) -> list:
        return self._get_all

    def exist(self, id: uuid) -> bool:
        return self._exist
