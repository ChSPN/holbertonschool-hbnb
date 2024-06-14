import uuid
from entities.city import City
from entities.country import Country
from entities.review import Review
from managers.persistenceFileManager import PersistenceFileManager
from repositories.iCityRepository import ICityRepository


class CityFileRepository(ICityRepository):
    def __init__(self):
        super().__init__()
        self._persistenceManager = PersistenceFileManager()

    def create(self, city) -> bool:
        return self._persistenceManager.save(city)

    def update(self, city) -> bool:
        return self._persistenceManager.update(city)

    def delete(self, city_id: uuid) -> bool:
        return self._persistenceManager.delete(city_id, City)

    def get_by_id(self, city_id: uuid):
        return self._persistenceManager.get(city_id, City)

    def get_by_country_code(self, code: str):
        countries = self._persistenceManager.get_all(Country)
        for country in countries:
            if country.code == code:
                cities = self._persistenceManager.get_all(City)
                return [city for city in cities if city.country_id == country.id]
        return None

    def get_all(self) -> list:
        return self._persistenceManager.get_all(City)

    def exist(self, id: uuid) -> bool:
        try:
            entity = self._persistenceManager.get(id, City)
            if not entity:
                return False
            else:
                return True
        except Exception:
            return False
