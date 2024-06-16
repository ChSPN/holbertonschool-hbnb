import uuid
from entities.country import Country
from managers.iRepositoryManager import IRepositoryManager
from managers.persistenceFileManager import PersistenceFileManager
from repositories.iCountryRepository import ICountryRepository


class CountryFileRepository(ICountryRepository):
    """Country file repository class."""

    def __init__(self, repositoryManager: IRepositoryManager):
        super().__init__()
        self._persistenceManager = PersistenceFileManager()
        self._repositoryManager = repositoryManager

    def create(self, country) -> bool:
        return self._persistenceManager.save(country)

    def update(self, country) -> bool:
        return self._persistenceManager.update(country)

    def delete(self, country_id: uuid) -> bool:
        return self._persistenceManager.delete(country_id, Country)

    def get_by_id(self, country_id: uuid):
        country = self._persistenceManager.get(country_id, Country)
        if not country:
            return None
        else:
            return Country(self._repositoryManager, country)

    def get_by_code(self, code: str):
        countries = self._persistenceManager.get_all(Country)
        for country in countries:
            if country.get("code") == code:
                return Country(self._repositoryManager, country)
        return None

    def get_all(self) -> list:
        countries = self._persistenceManager.get_all(Country)
        if not countries:
            return []
        else:
            return [
                Country(self._repositoryManager, country)
                for country in countries
            ]

    def exist(self, id: uuid, code: str = None) -> bool:
        try:
            if code is None:
                country = self._persistenceManager.get(id, Country)
                if not country:
                    return False
                else:
                    return True
            else:
                countries = self._persistenceManager.get_all(Country)
                if not countries or len(countries) == 0:
                    return False
                else:
                    return any(
                        country.get("id") != id
                        and (
                            country.get("code") == code
                            or country.get("name") == code
                        )
                        for country in countries
                    )
        except Exception:
            return False
