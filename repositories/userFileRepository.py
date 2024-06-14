import uuid
from entities.customerPlace import CustomerPlace
from entities.user import User
from managers.persistenceFileManager import PersistenceFileManager
from repositories.iUserRepository import IUserRepository


class UserFileRepository(IUserRepository):
    def __init__(self):
        super().__init__()
        self._persistenceManager = PersistenceFileManager()

    def create(self, user) -> bool:
        return self._persistenceManager.save(user)

    def update(self, user) -> bool:
        return self._persistenceManager.update(user)

    def delete(self, user_id: uuid) -> bool:
        return self._persistenceManager.delete(user_id, User)

    def get_by_id(self, user_id: uuid):
        return self._persistenceManager.get(user_id, User)

    def get_all(self) -> list:
        return self._persistenceManager.get_all(User)

    def get_by_email(self, email: str):
        try:
            users = self._persistenceManager.get_all(User)
            if not users:
                return None
            else:
                users = [user for user in users if user.email == email]
                if not users:
                    return None
                else:
                    return users[0]
        except Exception:
            return False

    def exist(self, id: uuid) -> bool:
        try:
            entity = self._persistenceManager.get(id, User)
            if not entity:
                return False
            else:
                return True
        except Exception:
            return False
