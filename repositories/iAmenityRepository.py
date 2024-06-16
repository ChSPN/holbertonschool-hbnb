from abc import ABC, abstractmethod
import uuid


class IAmenityRepository(ABC):
    """Amenity repository interface."""

    @abstractmethod
    def create(self, amenity) -> bool:
        """Creates an amenity."""
        pass

    @abstractmethod
    def update(self, amenity) -> bool:
        """Updates an amenity."""
        pass

    @abstractmethod
    def delete(self, amenity_id: uuid) -> bool:
        """Deletes an amenity."""
        pass

    @abstractmethod
    def get_by_id(self, amenity_id: uuid):
        """Gets an amenity by ID."""
        pass

    @abstractmethod
    def get_all(self) -> list:
        """Gets all amenities."""
        pass

    @abstractmethod
    def exist(self, id: uuid, name: str = None) -> bool:
        """Checks if an amenity exists."""
        pass

    @abstractmethod
    def exists(self, ids: list) -> bool:
        """Checks if amenities exist."""
        pass

    @abstractmethod
    def get_by_place(self, id: uuid) -> list:
        """Gets amenities by place."""
        pass
