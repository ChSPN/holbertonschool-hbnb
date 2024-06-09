from abc import ABC, abstractmethod
import uuid


class UserRepository(ABC):
    @abstractmethod
    def exist(self, email: str) -> bool: pass

    @abstractmethod
    def get_customers_by_place(self, id: uuid) -> list: pass

    @abstractmethod
    def get_by_id(self, id: uuid) -> any: pass
