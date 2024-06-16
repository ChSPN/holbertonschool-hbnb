import uuid
from entities.place import Place
from repositories.iPlaceRepository import IPlaceRepository
from entities.user import User


class PlaceMockRepository(IPlaceRepository):
    def __init__(
        self,
        add_amenity: bool = None,
        add_customer: bool = None,
        create: bool = None,
        get_by_host: list[User] = None,
        update: bool = None,
        delete: bool = None,
        get_by_id: Place = None,
        get_all: list[Place] = None,
        exist=bool or None,
    ):
        super().__init__()
        self._add_amenity = add_amenity or None
        self._add_customer = add_customer or None
        self._create = create or None
        self._get_by_host = get_by_host or None
        self._update = update or None
        self._delete = delete or None
        self._get_by_id = get_by_id or None
        self._get_all = get_all or None
        self._exist = exist or None

    def create(self, place) -> bool:
        return self._create

    def update(self, place: Place) -> bool:
        return self._update

    def delete(self, place_id: uuid) -> bool:
        return self._delete

    def get_by_id(self, place_id: uuid) -> Place:
        return self._get_by_id

    def get_all(self) -> list[Place]:
        return self._get_all

    def get_by_host(self, id: uuid) -> list:
        return self._get_by_host

    def exist(self, id: uuid) -> bool:
        return self._exist
