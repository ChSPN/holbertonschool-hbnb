import uuid
from entities.amenity import Amenity
from repositories.iAmenityRepository import IAmenityRepository


class AmenityMockRepository(IAmenityRepository):
    def __init__(
        self,
        create: bool = None,
        exist: bool = None,
        exists: bool = None,
        get_by_place: list = None,
        update: bool = None,
        delete: bool = None,
        get_by_id: Amenity = None,
        get_all: list[Amenity] = None,
    ):
        super().__init__()
        self._create = create or None
        self._exist = exist or None
        self._exists = exists or None
        self._get_by_place = get_by_place or None
        self._update = update or None
        self._delete = delete or None
        self._get_by_id = get_by_id or None
        self._get_all = get_all or None

    def create(self, amenity) -> bool:
        return self._create

    def update(self, amenity: Amenity) -> bool:
        return self._update

    def delete(self, amenity_id: uuid) -> bool:
        return self._delete

    def get_by_id(self, amenity_id: uuid) -> Amenity:
        return self._get_by_id

    def get_all(self) -> list[Amenity]:
        return self._get_all

    def exist(self, id: uuid, name: str = None) -> bool:
        return self._exists if name is not None else self._exist

    def exists(self, ids: list) -> bool:
        return self._exists

    def get_by_place(self, id: uuid) -> list:
        return self._get_by_place
