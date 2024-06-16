from abc import ABC, abstractmethod
import uuid


class ICountryRepository(ABC):
    """Country repository interface."""

    @abstractmethod
    def create(self, country) -> bool:
        """Creates a country in the repository."""
        pass

    @abstractmethod
    def update(self, country) -> bool:
        """Updates a country in the repository."""
        pass

    @abstractmethod
    def delete(self, country_id: uuid) -> bool:
        """Deletes a country from the repository."""
        pass

    @abstractmethod
    def get_by_id(self, country_id: uuid):
        """Gets a country by its ID."""
        pass

    @abstractmethod
    def get_by_code(self, code: str):
        """Gets a country by its code."""
        pass

    @abstractmethod
    def get_all(self) -> list:
        """Gets all countries from the repository."""
        pass

    @abstractmethod
    def exist(self, id: uuid, code: str = None) -> bool:
        """Checks if a country exists in the repository."""
        pass
