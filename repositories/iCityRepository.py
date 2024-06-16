from abc import ABC, abstractmethod
import uuid


class ICityRepository(ABC):
    """City repository interface."""

    @abstractmethod
    def create(self, city) -> bool:
        """Creates a city in the repository."""
        pass

    @abstractmethod
    def update(self, city) -> bool:
        """Updates a city in the repository."""
        pass

    @abstractmethod
    def delete(self, city_id: uuid) -> bool:
        """Deletes a city from the repository."""
        pass

    @abstractmethod
    def get_by_id(self, city_id: uuid):
        """Gets a city by its ID."""
        pass

    @abstractmethod
    def get_by_country_code(self, code: str):
        """Gets a city by its country code."""
        pass

    @abstractmethod
    def get_all(self) -> list:
        """Gets all cities from the repository."""
        pass

    @abstractmethod
    def exist(self, id: uuid, city_name: str = None) -> bool:
        """Checks if a city exists in the repository."""
        pass
