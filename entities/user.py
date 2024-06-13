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
