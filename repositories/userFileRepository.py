import uuid
from entities.user import User
from managers.iRepositoryManager import IRepositoryManager
from managers.persistenceFileManager import PersistenceFileManager
from repositories.iUserRepository import IUserRepository


class UserFileRepository(IUserRepository):
    """User file repository class."""

    def __init__(self, repositoryManager: IRepositoryManager):
        super().__init__()
        self._persistenceManager = PersistenceFileManager()
        self._repositoryManager = repositoryManager

    def create(self, user) -> bool:
        return self._persistenceManager.save(user)

    def update(self, user) -> bool:
        return self._persistenceManager.update(user)

    def delete(self, user_id: uuid) -> bool:
        return self._persistenceManager.delete(user_id, User)

    def get_by_id(self, user_id: uuid):
        user = self._persistenceManager.get(user_id, User)
        if not user:
            return None
        else:
            return User(self._repositoryManager, user)

    def get_all(self) -> list:
        users = self._persistenceManager.get_all(User)
        if not users:
            return []
        else:
            return [User(self._repositoryManager, user) for user in users]

    def get_by_email(self, email: str):
        try:
            users = self._persistenceManager.get_all(User)
            if not users:
                return None
            else:
                users = [user for user in users if user.get("email") == email]
                if not users or len(users) == 0:
                    return None
                else:
                    return User(self._repositoryManager, users[0])
        except Exception:
            return None

    def exist(self, id: uuid) -> bool:
        try:
            entity = self._persistenceManager.get(id, User)
            if not entity:
                return False
            else:
                return True
        except Exception:
            return False
