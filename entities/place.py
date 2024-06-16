from datetime import datetime
import uuid
import tzlocal
from managers.iRepositoryManager import IRepositoryManager


class Place:
    """Place entity class."""

    def __init__(self, manager: IRepositoryManager = None, place: dict = None):
        """Constructor for Place entity class."""
        self._amenity_repository = (
            None if manager is None else manager.amenityRepository()
        )
        self._place_repository = (
            None if manager is None else manager.placeRepository()
        )
        self._user_repository = (
            None if manager is None else manager.userRepository()
        )
        self._review_repository = (
            None if manager is None else manager.reviewRepository()
        )
        self._city_repository = (
            None if manager is None else manager.cityRepository()
        )
        self.id = uuid.uuid4()
        self.created_at = datetime.now(tzlocal.get_localzone())
        self.updated_at: datetime = None
        self.description: str = None
        self.name: str
        self.address: str
        self.number_of_rooms: int
        self.number_of_bathrooms: int
        self.max_guests: int
        self.price_per_night: float
        self.latitude: float
        self.longitude: float
        self.amenity_ids: list = None
        self.host_id: uuid
        self.city_id: uuid
        self.parse(place)

    def to_dict(self):
        """Converts Place entity class to dictionary."""
        return {
            "city_id": self.city_id,
            "created_at": self.created_at,
            "description": self.description,
            "host_id": self.host_id,
            "id": self.id,
            "name": self.name,
            "address": self.address,
            "number_of_rooms": self.number_of_rooms,
            "number_of_bathrooms": self.number_of_bathrooms,
            "price_per_night": self.price_per_night,
            "max_guests": self.max_guests,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "amenity_ids": self.amenity_ids,
            "updated_at": self.updated_at,
        }

    @staticmethod
    def load(manager: IRepositoryManager, id: uuid = None):
        """Loads a Place entity from the repository."""
        repo = manager.placeRepository()
        if id is None:
            return repo.get_all()
        else:
            return repo.get_by_id(id)

    def parse(self, place: dict = None):
        """Parses a dictionary to a Place entity class."""
        if place and "id" in place:
            self.id = (
                uuid.UUID(place["id"]) if place["id"] is str else place["id"]
            )
        if place and "created_at" in place:
            self.created_at = place["created_at"]
        if place and "updated_at" in place:
            self.updated_at = place["updated_at"]
        self.description = (
            place["description"] if place and "description" in place else None
        )
        self.name = place["name"] if place and "name" in place else None
        self.address = (
            place["address"] if place and "address" in place else None
        )
        self.number_of_rooms = (
            place["number_of_rooms"]
            if place and "number_of_rooms" in place
            else None
        )
        self.number_of_bathrooms = (
            place["number_of_bathrooms"]
            if place and "number_of_bathrooms" in place
            else None
        )
        self.price_per_night = (
            place["price_per_night"]
            if place and "price_per_night" in place
            else None
        )
        self.latitude = (
            place["latitude"] if place and "latitude" in place else None
        )
        self.longitude = (
            place["longitude"] if place and "longitude" in place else None
        )
        self.max_guests = (
            place["max_guests"] if place and "max_guests" in place else None
        )
        self.amenity_ids: list = (
            place["amenity_ids"] if place and "amenity_ids" in place else None
        )
        self.host_id: uuid = (
            place["host_id"] if place and "host_id" in place else None
        )
        if self.host_id is str:
            self.host_id = uuid.UUID(self.host_id)

        self.city_id: uuid = (
            place["city_id"] if place and "city_id" in place else None
        )
        if self.city_id is str:
            self.city_id = uuid.UUID(self.city_id)

    def delete(self) -> bool:
        """Deletes a Place entity from the repository."""
        if not self._place_repository:
            return False

        return self._place_repository.delete(self.id)

    def save(self) -> bool:
        """Saves a Place entity to the repository."""
        if (
            not self._place_repository
            or not self.name
            or not self.address
            or not self.number_of_rooms
            or not self.number_of_bathrooms
            or not self.price_per_night
            or not self.max_guests
            or not self.host_id
            or not self.city_id
        ):
            return False

        if (
            not isinstance(self.price_per_night, (int, float))
            or not self.max_guests > 0
            or not self.number_of_rooms > 0
            or not self.number_of_bathrooms > 0
        ):
            return False

        if self.latitude < -90 or self.latitude > 90:
            """Latitude must be between -90 and 90."""
            return False

        if self.longitude < -180 or self.longitude > 180:
            """Longitude must be between -180 and 180."""
            return False

        if self.amenity_ids and not self._amenity_repository.exists(
            self.amenity_ids
        ):
            """Amenities do not exist."""
            return False

        if not self._city_repository.exist(self.city_id):
            """City does not exist."""
            return False

        if not self._user_repository.exist(self.host_id):
            """Host does not exist."""
            return False

        if self._place_repository.exist(self.id):
            self.updated_at = datetime.now(tzlocal.get_localzone())
            return self._place_repository.update(self)
        else:
            return self._place_repository.create(self)
