import uuid
from user import User
from userRepository import UserRepository

class UserMockRepository(UserRepository):
    def __init__(self, email = str or None, user = User or None, customers = list[User] or None):
        super().__init__()
        self._email = email or None
        self._user = user or None
        self._customers = customers or None

    def exist(self, email:str) -> bool:
        return self._email == email

    def get_customers_by_place(self, id:uuid) -> list[User]:
        return self._customers

    def get_by_id(self, id:uuid) -> User:
        return self._user