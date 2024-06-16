import uuid
from entities.city import City
from repositories.iCityRepository import ICityRepository


class CityMockRepository(ICityRepository):
    def __init__(self,
                 create: bool = True, 
                 update: bool = True, 
                 delete: bool = True,
                 exist: bool = True,
                 exists:bool = None,
                 get_by_id: City = None,
                 get_by_country_code: City = None,
                 get_all: list[City] = None):
        super().__init__()
        self._create = create or None
        self._update = update or None
        self._delete = delete or None
        self._exist = exist or None
        self._exists = exists or None
        self._get_by_id = get_by_id or None
        self._get_by_country_code = get_by_country_code or None
        self._get_all = get_all or None

    def create(self, city) -> bool:
        return self._create

    def update(self, city) -> bool:
        return self._update

    def delete(self, city_id: uuid) -> bool:
        return self._delete

    def get_by_id(self, city_id: uuid):
        return self._get_by_id

    def get_by_country_code(self, code: str):
        return self._get_by_country_code

    def get_all(self) -> list:
        return self._get_all

    def exist(self, id: uuid, name:str = None) -> bool:
        return self._exists if name is not None else self._exist
