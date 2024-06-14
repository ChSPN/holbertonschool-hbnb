from abc import ABC, abstractmethod
import uuid


class ICityRepository(ABC):
    @abstractmethod
    def create(self, city) -> bool: pass

    @abstractmethod
    def update(self, city) -> bool: pass

    @abstractmethod
    def delete(self, city_id: uuid) -> bool: pass

    @abstractmethod
    def get_by_id(self, city_id: uuid): pass

    @abstractmethod
    def get_by_country_code(self, code: str): pass

    @abstractmethod
    def get_all(self) -> list: pass

    @abstractmethod
    def exist(self, id: uuid) -> bool: pass
