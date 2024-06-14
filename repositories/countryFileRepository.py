import uuid
from entities.country import Country
from managers.persistenceFileManager import PersistenceFileManager
from repositories.iCountryRepository import ICountryRepository


class CountryFileRepository(ICountryRepository):
    def __init__(self):
        super().__init__()
        self._persistenceManager = PersistenceFileManager()

    def create(self, country) -> bool:
        return self._persistenceManager.save(country)

    def update(self, country) -> bool:
        return self._persistenceManager.update(country)

    def delete(self, country_id: uuid) -> bool:
        return self._persistenceManager.delete(country_id, Country)

    def get_by_id(self, country_id: uuid):
        return self._persistenceManager.get(country_id, Country)

    def get_by_code(self, code: str):
        countries = self._persistenceManager.get_all(Country)
        for country in countries:
            if country.code == code:
                return country
        return None

    def get_all(self) -> list:
        return self._persistenceManager.get_all(Country)

    def exist(self, id: uuid) -> bool:
        try:
            entity = self._persistenceManager.get(id, Country)
            if not entity:
                return False
            else:
                return True
        except Exception:
            return False
