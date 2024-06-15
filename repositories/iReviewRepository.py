from abc import ABC, abstractmethod
import uuid


class IReviewRepository(ABC):
    @abstractmethod
    def create(self, review) -> bool: pass

    @abstractmethod
    def update(self, review) -> bool: pass

    @abstractmethod
    def delete(self, review_id: uuid) -> bool: pass

    @abstractmethod
    def get_by_id(self, review_id: uuid): pass

    @abstractmethod
    def get_by_user(self, user_id: uuid): pass

    @abstractmethod
    def get_all(self) -> list: pass

    @abstractmethod
    def get_by_place(self, id: uuid) -> list: pass

    @abstractmethod
    def exist(self, id: uuid) -> bool: pass
