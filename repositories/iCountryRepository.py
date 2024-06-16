from abc import ABC, abstractmethod
import uuid


class ICountryRepository(ABC):
    @abstractmethod
    def create(self, country) -> bool:
        pass

    @abstractmethod
    def update(self, country) -> bool:
        pass

    @abstractmethod
    def delete(self, country_id: uuid) -> bool:
        pass

    @abstractmethod
    def get_by_id(self, country_id: uuid):
        pass

    @abstractmethod
    def get_by_code(self, code: str):
        pass

    @abstractmethod
    def get_all(self) -> list:
        pass

    @abstractmethod
    def exist(self, id: uuid, code: str = None) -> bool:
        pass
