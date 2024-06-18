from datetime import datetime
import re
import uuid
import tzlocal
from managers.iRepositoryManager import IRepositoryManager


class User:
    """User entity class."""

    def __init__(self, manager: IRepositoryManager = None, user: dict = None):
        """Constructor for User entity class."""
        self._place_repository = (
            None if manager is None else manager.placeRepository()
        )
        self._user_repository = (
            None if manager is None else manager.userRepository()
        )
        self.id: uuid = uuid.uuid4()
        self.created_at: datetime = datetime.now(tzlocal.get_localzone())
        self.updated_at: datetime = None
        self.email: str
        self.first_name: str
        self.last_name: str
        self.password: str
        self.parse(user)

    def to_dict(self):
        """Converts User entity class to dictionary."""
        return {
            "created_at": self.created_at,
            "email": self.email,
            "first_name": self.first_name,
            "id": self.id,
            "last_name": self.last_name,
            "password": self.password,
            "updated_at": self.updated_at,
        }

    def validate_email(self):
        """Validates email address."""
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            """Invalid email address."""
            return False

        user = self._user_repository.get_by_email(self.email)
        if user is None or user.id == self.id:
            """Valid email address."""
            return True
        else:
            """Email address already exists."""
            return False

    @staticmethod
    def load(manager: IRepositoryManager, id: uuid = None):
        """Loads a User entity from the repository."""
        repo = manager.userRepository()
        if id is None:
            return repo.get_all()
        else:
            return repo.get_by_id(id)

    def parse(self, user: dict = None):
        """Parses a dictionary to a User entity class."""
        if user and "id" in user:
            self.id = (
                uuid.UUID(user["id"]) if user["id"] is str else user["id"]
            )
        if user and "created_at" in user:
            self.created_at = user["created_at"]
        if user and "updated_at" in user:
            self.updated_at = user["updated_at"]
        self.email = user["email"] if user and "email" in user else None
        self.first_name = (
            user["first_name"] if user and "first_name" in user else None
        )
        self.last_name = (
            user["last_name"] if user and "last_name" in user else None
        )
        self.password = (
            user["password"] if user and "password" in user else None
        )

    def delete(self) -> bool:
        """Deletes a User entity from the repository."""
        if not self._user_repository:
            return False

        return self._user_repository.delete(self.id)

    def save(self) -> bool:
        """Saves a User entity to the repository."""
        if (
            not self._user_repository
            or not self.email
            or not self.first_name
            or not self.last_name
            or not self.password
            or not self.validate_email()
        ):
            return False

        if self._user_repository.exist(self.id):
            self.updated_at = datetime.now(tzlocal.get_localzone())
            return self._user_repository.update(self)
        else:
            return self._user_repository.create(self)
