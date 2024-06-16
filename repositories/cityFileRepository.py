import uuid
from entities.city import City
from entities.country import Country
from entities.review import Review
from managers.iRepositoryManager import IRepositoryManager
from managers.persistenceFileManager import PersistenceFileManager
from repositories.iCityRepository import ICityRepository


class CityFileRepository(ICityRepository):
    """City file repository class."""

    def __init__(self, repositoryManager: IRepositoryManager):
        super().__init__()
        self._persistenceManager = PersistenceFileManager()
        self._repositoryManager = repositoryManager

    def create(self, city) -> bool:
        return self._persistenceManager.save(city)

    def update(self, city) -> bool:
        return self._persistenceManager.update(city)

    def delete(self, city_id: uuid) -> bool:
        return self._persistenceManager.delete(city_id, City)

    def get_by_id(self, city_id: uuid):
        city = self._persistenceManager.get(city_id, City)
        if not city:
            return None
        else:
            return City(self._repositoryManager, city)

    def get_by_country_code(self, code: str):
        countries = self._persistenceManager.get_all(Country)
        for country in countries:
            if country.get("code") == code:
                cities = self._persistenceManager.get_all(City)
                return [
                    City(self._repositoryManager, city)
                    for city in cities
                    if city.get("country_id") == country.get("id")
                ]
        return None

    def get_all(self) -> list:
        cities = self._persistenceManager.get_all(City)
        if not cities:
            return []
        else:
            return [City(self._repositoryManager, city) for city in cities]

    def exist(self, id: uuid, city_name: str = None) -> bool:
        try:
            if city_name is None:
                city = self._persistenceManager.get(id, City)
                if not city:
                    return False
                else:
                    return True
            else:
                cities = self._persistenceManager.get_all(City)
                if not cities or len(cities) == 0:
                    return False
                else:
                    return any(
                        str(city.get("country_id")) == str(id)
                        and city.get("name") == city_name
                        for city in cities
                    )
        except Exception:
            return False
