import uuid
from entities.user import User
from repositories.iUserRepository import IUserRepository


class UserMockRepository(IUserRepository):
    def __init__(
        self,
        exist=bool or None,
        user=User or None,
        customers=list[User] or None,
        create=bool or None,
        update: bool = None,
        delete: bool = None,
        get_by_id: User = None,
        get_by_email: User = None,
        get_all: list[User] = None,
    ):
        super().__init__()
        self._exist = exist or None
        self._user = user or None
        self._customers = customers or None
        self._create = create
        self._update = update or None
        self._delete = delete or None
        self._get_by_id = get_by_id or None
        self._get_all = get_all or None
        self._get_by_email = get_by_email or None

    def exist(self, id: uuid) -> bool:
        return self._exist

    def get_customers_by_place(self, id: uuid) -> list[User]:
        return self._customers

    def get_by_email(self, email: str) -> User:
        return self._get_by_email

    def create(self, user: User) -> bool:
        return self._create

    def update(self, user: User) -> bool:
        return self._update

    def delete(self, user_id: uuid) -> bool:
        return self._delete

    def get_by_id(self, user_id: uuid) -> User:
        return self._get_by_id

    def get_all(self) -> list[User]:
        return self._get_all
