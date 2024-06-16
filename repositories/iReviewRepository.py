from abc import ABC, abstractmethod
import uuid


class IReviewRepository(ABC):
    """Review repository interface."""

    @abstractmethod
    def create(self, review) -> bool:
        """Creates a review in the repository."""
        pass

    @abstractmethod
    def update(self, review) -> bool:
        """Updates a review in the repository."""
        pass

    @abstractmethod
    def delete(self, review_id: uuid) -> bool:
        """Deletes a review from the repository."""
        pass

    @abstractmethod
    def get_by_id(self, review_id: uuid):
        """Gets a review by its ID."""
        pass

    @abstractmethod
    def get_by_user(self, user_id: uuid):
        """Gets a review by its user ID."""
        pass

    @abstractmethod
    def get_all(self) -> list:
        """Gets all reviews from the repository."""
        pass

    @abstractmethod
    def get_by_place(self, id: uuid) -> list:
        """Gets all reviews by place ID."""
        pass

    @abstractmethod
    def exist(
        self, id: uuid, place_id: uuid = None, user_id: uuid = None
    ) -> bool:
        """Checks if a review exists in the repository."""
        pass
