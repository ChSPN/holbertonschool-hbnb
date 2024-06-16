import uuid
from entities.country import Country
from managers.persistenceFileManager import PersistenceFileManager
from repositories.iCountryRepository import ICountryRepository


class CountryMockRepository(ICountryRepository):
    def __init__(
        self,
        create: bool = True,
        update: bool = True,
        delete: bool = True,
        exist: bool = True,
        exists: bool = None,
        get_by_id: Country = None,
        get_by_code: Country = None,
        get_all: list[Country] = None,
    ):
        super().__init__()
        self._create = create or None
        self._update = update or None
        self._delete = delete or None
        self._exist = exist or None
        self._exists = exists or None
        self._get_by_id = get_by_id or None
        self._get_by_code = get_by_code or None
        self._get_all = get_all or None

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

    def exist(self, id: uuid, name: str = None) -> bool:
        return self._exists if name is not None else self._exist
