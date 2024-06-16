from datetime import datetime
import uuid
import tzlocal
from managers.iRepositoryManager import IRepositoryManager


class Amenity:
    """Amenity entity class."""

    def __init__(
        self, manager: IRepositoryManager = None, amenity: dict = None
    ):
        """Constructor for Amenity entity class."""
        self._repo = None if manager is None else manager.amenityRepository()
        self.id: uuid = uuid.uuid4()
        self.created_at: datetime = datetime.now(tzlocal.get_localzone())
        self.updated_at: datetime = None
        self.name: str
        self.parse(amenity)

    def to_dict(self):
        """Converts Amenity entity class to dictionary."""
        return {
            "created_at": self.created_at,
            "id": self.id,
            "name": self.name,
            "updated_at": self.updated_at,
        }

    @staticmethod
    def load(manager: IRepositoryManager, id: uuid = None):
        repo = manager.amenityRepository()
        if id is None:
            return repo.get_all()
        else:
            return repo.get_by_id(id)

    def parse(self, amenity: dict = None):
        """Parses a dictionary to an Amenity entity class"""
        if amenity and "id" in amenity:
            self.id = (
                uuid.UUID(amenity["id"])
                if amenity["id"] is str
                else amenity["id"]
            )
        if amenity and "created_at" in amenity:
            self.created_at = amenity["created_at"]
        if amenity and "updated_at" in amenity:
            self.updated_at = amenity["updated_at"]
        self.name = amenity["name"] if amenity and "name" in amenity else None

    def delete(self) -> bool:
        """Deletes an Amenity entity from the repository."""
        if not self._repo:
            return False

        return self._repo.delete(self.id)

    def exist(self, name: str) -> bool:
        """Check if an amenity exists in the repository"""
        if not self._repo:
            return False

        return self._repo.exist(self.id, name)

    def save(self) -> bool:
        """Saves an amenity entity to the repository"""
        if not self._repo or not self.name or self.exist(self.name):
            """If the repository is not set
            or the name is empty
            or the amenity already exists, return False"""
            return False

        if self._repo.exist(self.id):
            self.updated_at = datetime.now(tzlocal.get_localzone())
            return self._repo.update(self)
        else:
            return self._repo.create(self)
