from abc import ABC, abstractmethod
import uuid


class IUserRepository(ABC):
    @abstractmethod
    def create(self, user) -> bool: pass

    @abstractmethod
    def update(self, user) -> bool: pass

    @abstractmethod
    def delete(self, user_id: uuid) -> bool: pass

    @abstractmethod
    def get_by_id(self, user_id: uuid): pass

    @abstractmethod
    def get_all(self) -> list: pass

    @abstractmethod
    def get_customers_by_place(self, id: uuid) -> list: pass

    @abstractmethod
    def get_by_email(self, email: str): pass

    @abstractmethod
    def exist(self, id: uuid) -> bool: pass
