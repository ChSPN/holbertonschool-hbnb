from abc import ABC, abstractmethod
import uuid


class PlaceRepository(ABC):
    @abstractmethod
    def add_amenity(self, place, amenity) -> bool: pass

    @abstractmethod
    def add_customer(self, place, customer) -> bool: pass

    @abstractmethod
    def create(self, place, host) -> bool: pass

    @abstractmethod
    def get_by_host(self, id: uuid) -> list: pass
