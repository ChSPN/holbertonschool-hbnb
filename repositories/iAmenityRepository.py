from abc import ABC, abstractmethod
import uuid


class IAmenityRepository(ABC):
    @abstractmethod
    def create(self, amenity) -> bool: pass

    @abstractmethod
    def exist(self, id: uuid) -> bool: pass

    @abstractmethod
    def get_by_place(self, id: uuid) -> list: pass
