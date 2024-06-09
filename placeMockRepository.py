import uuid
from placeRepository import PlaceRepository
from user import User


class PlaceMockRepository(PlaceRepository):
    def __init__(self, add_amenity=bool or None,
                 add_customer=bool or None,
                 create=bool or None,
                 get_by_host=list[User] or None):
        super().__init__()
        self._add_amenity = add_amenity or None
        self._add_customer = add_customer or None
        self._create = create or None
        self._get_by_host = get_by_host or None

    def add_amenity(self, place, amenity) -> bool:
        return self._add_amenity

    def add_customer(self, place, customer) -> bool:
        return self._add_customer

    def create(self, place, host) -> bool:
        return self._create

    def get_by_host(self, id: uuid) -> list:
        return self._get_by_host
