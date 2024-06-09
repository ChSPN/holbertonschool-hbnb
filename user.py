from datetime import datetime
import uuid
from placeRepository import PlaceRepository
from userRepository import UserRepository


class User:
    def __init__(self, place_repository=PlaceRepository or None,
                 user_repository=UserRepository or None):
        self._place_repository = place_repository or None
        self._user_repository = user_repository or None
        self.created_at = datetime.now()
        self.email = str
        self.first_name = str
        self.id = uuid.uuid4()
        self.last_name = str
        self.password = str
        self.places = [] or None
        self.customers = [] or None
        self.reviews = [] or None
        self.updated_at = datetime or None

    def create_place(self, place):
        """Business logic for creating place"""
        if not self.places:
            self.places = self._place_repository.get_by_host(self.id)

        if self.places and any(p.id == place.id for p in self.places):
            return False

        if not self._place_repository.create(place, self):
            return False

        if self.places:
            self.places.append(place)
        else:
            self.places = [place]

        return True

    def validate_email(self):
        """Business logic for validating email"""
        return not self._user_repository.exist(self.email)
