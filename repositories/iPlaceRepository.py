from abc import ABC, abstractmethod
import uuid


class IPlaceRepository(ABC):
    @abstractmethod
    def create(self, place) -> bool: pass

    @abstractmethod
    def update(self, place) -> bool: pass

    @abstractmethod
    def delete(self, place_id: uuid) -> bool: pass

    @abstractmethod
    def get_by_id(self, place_id: uuid): pass

    @abstractmethod
    def get_all(self) -> list: pass

    @abstractmethod
    def get_by_host(self, id: uuid) -> list: pass

    @abstractmethod
    def exist(self, id: uuid) -> bool: pass
