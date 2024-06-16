from datetime import datetime
import uuid
import tzlocal
from managers.iRepositoryManager import IRepositoryManager


class Country:
    def __init__(
        self, manager: IRepositoryManager = None, country: dict = None
    ):
        self._repo = None if manager is None else manager.countryRepository()
        self.id = uuid.uuid4()
        self.code: str
        self.name: str
        self.parse(country)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "code": self.code,
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
        if country and "id" in country:
            self.id = (
                uuid.UUID(country["id"])
                if country["id"] is str
                else country["id"]
            )
        self.name = country["name"] if country and "name" in country else None
        self.code = country["code"] if country and "code" in country else None
