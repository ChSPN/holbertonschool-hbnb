from datetime import datetime
import re
import uuid
import tzlocal
from managers.iRepositoryManager import IRepositoryManager


class User:
    def __init__(self, manager: IRepositoryManager = None, user: dict = None):
        self._place_repository = None if manager is None else manager.placeRepository()
        self._user_repository = None if manager is None else manager.userRepository()
        self.id:uuid = uuid.uuid4()
        self.created_at:datetime = datetime.now(tzlocal.get_localzone())
        self.updated_at:datetime = None
        self.email:str
        self.first_name:str
        self.last_name:str
        self.password:str
        self.places:list = None
        self.customers:list = None
        self.reviews:list = None
        self.parse(user)

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
        if not re.match(r"[^@]+@[^@]+\.[^@]+", self.email):
            return False

        user = self._user_repository.get_by_email(self.email)
        if user is None or user.id == self.id:
            return True

    @staticmethod
    def load(manager: IRepositoryManager, id: uuid = None):
        repo = manager.userRepository()
        if id is None:
            return repo.get_all()
        else:
            return repo.get_by_id(id)
        
    def parse(self, user: dict = None):
        if user and 'id' in user:
            self.id = user['id']
        if user and 'created_at' in user:
            self.created_at = user['created_at']
        if user and 'updated_at' in user:
            self.updated_at = user['updated_at']
        self.email = user['email'] if user and 'email' in user else None
        self.first_name = user['first_name'] if user and 'first_name' in user else None
        self.last_name = user['last_name'] if user and 'last_name' in user else None
        self.password = user['password'] if user and 'password' in user else None

    def delete(self) -> bool:
        if (not self._user_repository):
            return False

        return self._user_repository.delete(self.id)

    def save(self) -> bool:
        if (not self._user_repository
            or not self.email
            or not self.first_name
            or not self.last_name
            or not self.password
            or not self.validate_email()):
            return False
        
        if (self._user_repository.exist(self.id)):
            self.updated_at = datetime.now(tzlocal.get_localzone())
            return self._user_repository.update(self)
        else:
            return self._user_repository.create(self)
