from abc import ABC, abstractmethod
import uuid
from entities.review import Review


class IReviewRepository(ABC):
    @abstractmethod
    def create(self, review: Review) -> bool: pass

    @abstractmethod
    def get_by_place(self, id: uuid) -> list[Review]: pass
