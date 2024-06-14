import uuid
from entities.city import City
from repositories.iCityRepository import ICityRepository


class CityMockRepository(ICityRepository):
    def __init__(self,
                 create: bool = True, 
                 update: bool = True, 
                 delete: bool = True,
                 exist: bool = True,
                 get_by_id: City = None,
                 get_by_country_code: City = None,
                 get_all: list[City] = None):
        super().__init__()
        self._create = create
        self._update = update
        self._delete = delete
        self._exist = exist
        self._get_by_id = get_by_id
        self._get_by_country_code = get_by_country_code
        self._get_all = get_all

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

    def exist(self, id: uuid) -> bool:
        return self._exist
