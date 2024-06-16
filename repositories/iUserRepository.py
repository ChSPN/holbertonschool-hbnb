from abc import ABC, abstractmethod
import uuid


class IUserRepository(ABC):
    """User repository interface."""

    @abstractmethod
    def create(self, user) -> bool:
        """Creates a user in the repository."""
        pass

    @abstractmethod
    def update(self, user) -> bool:
        """Updates a user in the repository."""
        pass

    @abstractmethod
    def delete(self, user_id: uuid) -> bool:
        """Deletes a user from the repository."""
        pass

    @abstractmethod
    def get_by_id(self, user_id: uuid):
        """Gets a user by its ID."""
        pass

    @abstractmethod
    def get_all(self) -> list:
        """Gets all users from the repository."""
        pass

    @abstractmethod
    def get_by_email(self, email: str):
        """Gets a user by its email."""
        pass

    @abstractmethod
    def exist(self, id: uuid) -> bool:
        """Checks if a user exists in the repository."""
        pass
