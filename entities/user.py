from datetime import datetime
import uuid
from managers.iRepositoryManager import IRepositoryManager


class User:
    def __init__(self, manager: IRepositoryManager = None):
        self._place_repository = None if manager is None else manager.placeRepository()
        self._user_repository = None if manager is None else manager.userRepository()
        self.created_at = datetime.now()
        self.email:str
        self.first_name:str
        self.id = uuid.uuid4()
        self.last_name:str
        self.password:str
        self.places:list = None
        self.customers:list = None
        self.reviews:list = None
        self.updated_at:datetime = None

    def to_dict(self):
        return {
            'created_at': self.created_at,
            'email': self.email,
            'first_name': self.first_name,
            'id': self.id,
            'last_name': self.last_name,
            'password': self.password,
            'updated_at': self.updated_at,
        }

    def validate_email(self):
        """Business logic for validating email"""
        return not self._user_repository.get_by_email(self.email)

    @staticmethod
    def load(manager: IRepositoryManager, id: uuid = None):
        repo = manager.userRepository()
        if id is None:
            return repo.get_all()
        else:
            return repo.get_by_id(id)

    def delete(self) -> bool:
        if (not self._user_repository):
            return False

        return self._user_repository.delete(self.id)

    def save(self) -> bool:
        if (not self._user_repository
            or not self.email
            or not self.first_name
            or not self.last_name
            or not self.password):
            return False
        
        if (self._user_repository.exist(self.id)):
            self.updated_at = datetime.now()
            return self._user_repository.update(self)
        else:
            return self._user_repository.create(self)
