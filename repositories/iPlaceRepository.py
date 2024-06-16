from abc import ABC, abstractmethod
import uuid


class IPlaceRepository(ABC):
    """Place repository interface."""

    @abstractmethod
    def create(self, place) -> bool:
        """Creates a place in the repository."""
        pass

    @abstractmethod
    def update(self, place) -> bool:
        """Updates a place in the repository."""
        pass

    @abstractmethod
    def delete(self, place_id: uuid) -> bool:
        """Deletes a place from the repository."""
        pass

    @abstractmethod
    def get_by_id(self, place_id: uuid):
        """Gets a place by its ID."""
        pass

    @abstractmethod
    def get_all(self) -> list:
        """Gets all places from the repository."""
        pass

    @abstractmethod
    def get_by_host(self, id: uuid) -> list:
        """Gets all places by host ID."""
        pass

    @abstractmethod
    def exist(self, id: uuid) -> bool:
        """Checks if a place exists in the repository."""
        pass
