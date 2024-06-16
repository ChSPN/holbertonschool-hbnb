from abc import ABC, abstractmethod
import uuid


class IAmenityRepository(ABC):
    @abstractmethod
    def create(self, amenity) -> bool:
        pass

    @abstractmethod
    def update(self, amenity) -> bool:
        pass

    @abstractmethod
    def delete(self, amenity_id: uuid) -> bool:
        pass

    @abstractmethod
    def get_by_id(self, amenity_id: uuid):
        pass

    @abstractmethod
    def get_all(self) -> list:
        pass

    @abstractmethod
    def exist(self, id: uuid, name: str = None) -> bool:
        pass

    @abstractmethod
    def exists(self, ids: list) -> bool:
        pass

    @abstractmethod
    def get_by_place(self, id: uuid) -> list:
        pass
