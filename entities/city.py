from datetime import datetime
import uuid
import tzlocal
from managers.iRepositoryManager import IRepositoryManager


class City:
    def __init__(self, manager: IRepositoryManager = None, city: dict = None):
        self._repo = None if manager is None else manager.cityRepository()
        self._countryRepo = (
            None if manager is None else manager.countryRepository()
        )
        self.id = uuid.uuid4()
        self.created_at = datetime.now(tzlocal.get_localzone())
        self.updated_at: datetime = None
        self.name: str
        self.country_id: uuid = None
        self.parse(city)

    def to_dict(self):
        return {
            "country_id": self.country_id,
            "id": self.id,
            "name": self.name,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
        }

    @staticmethod
    def load(manager: IRepositoryManager, id: uuid = None):
        repo = manager.cityRepository()
        if id is None:
            return repo.get_all()
        else:
            return repo.get_by_id(id)

    def parse(self, city: dict = None):
        if city and "id" in city:
            self.id = (
                uuid.UUID(city["id"]) if city["id"] is str else city["id"]
            )
        if city and "created_at" in city:
            self.created_at = city["created_at"]
        if city and "updated_at" in city:
            self.updated_at = city["updated_at"]
        self.name = city["name"] if city and "name" in city else None
        self.country_id = (
            city["country_id"] if city and "country_id" in city else None
        )
        if self.country_id is str:
            self.country_id = uuid.UUID(self.country_id)

    @staticmethod
    def load_by_country_code(manager: IRepositoryManager, code: str):
        repo = manager.cityRepository()
        return repo.get_by_country_code(code)

    def delete(self) -> bool:
        if not self._repo:
            return False

        return self._repo.delete(self.id)

    def exist(self) -> bool:
        if not self._repo:
            return False

        return self._repo.exist(self.country_id, self.name)

    def save(self) -> bool:
        if (
            not self._repo
            or not self.name
            or not self.country_id
            or not self._countryRepo.exist(self.country_id)
            or self.exist()
        ):
            return False

        if self._repo.exist(self.id):
            self.updated_at = datetime.now(tzlocal.get_localzone())
            return self._repo.update(self)
        else:
            return self._repo.create(self)
