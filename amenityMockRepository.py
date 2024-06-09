import uuid
from amenityRepository import AmenityRepository

class AmenityMockRepository(AmenityRepository):
    def __init__(self, create = bool or None, exist = bool or None, get_by_place = list or None):
        super().__init__()
        self._create = create or None
        self._exist = exist or None
        self._get_by_place = get_by_place or None

    def create(self, amenity) -> bool:
        return self._create

    def exist(self, id:uuid) -> bool:
        return self._exist

    def get_by_place(self, id:uuid) -> list:
        return self._get_by_place