from datetime import datetime
import uuid

from managers.iRepositoryManager import IRepositoryManager


class Review:
    def __init__(self, manager: IRepositoryManager = None):
        self._review_repo = None if manager is None else manager.reviewRepository()
        self._user_repo = None if manager is None else manager.userRepository()
        self._place_repo = None if manager is None else manager.placeRepository()
        self.comment:str
        self.created_at = datetime.now()
        self.customer = None
        self.customer_id:uuid
        """Foreign key of customer"""
        self.id = uuid.uuid4()
        self.place = None
        self.place_id:uuid
        """Foreign key of place"""
        self.updated_at:datetime = None

    def to_dict(self):
        return {
            'comment': self.comment,
            'created_at': self.created_at,
            'customer_id': self.customer_id,
            'id': self.id,
            'place_id': self.place_id,
            'updated_at': self.updated_at,
        }

    @staticmethod
    def load(manager: IRepositoryManager, id: uuid = None):
        repo = manager.reviewRepository()
        if id is None:
            return repo.get_all()
        else:
            return repo.get_by_id(id)

    @staticmethod
    def load_by_customer(manager: IRepositoryManager, customer_id: uuid):
        repo = manager.reviewRepository()
        return repo.get_by_customer(customer_id)

    @staticmethod
    def load_by_place(manager: IRepositoryManager, place_id: uuid):
        repo = manager.reviewRepository()
        return repo.get_by_place(place_id)

    def delete(self) -> bool:
        if (not self._review_repo):
            return False

        return self._review_repo.delete(self.id)

    def save(self) -> bool:
        if (not self._review_repo
            or not self._user_repo
            or not self._place_repo
            or not self.comment
            or not self.customer_id
            or not self.place_id):
            return False
        
        if not self._place_repo.exist(self.place_id):
            return False
        
        if not self._user_repo.exist(self.customer_id):
            return False
        
        if (self._place_repo.exist(self.id)):
            self.updated_at = datetime.now()
            return self._place_repo.update(self)
        else:
            return self._place_repo.create(self)
