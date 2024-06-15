import uuid
from entities.review import Review
from managers.iRepositoryManager import IRepositoryManager
from managers.persistenceFileManager import PersistenceFileManager
from repositories.iReviewRepository import IReviewRepository


class ReviewFileRepository(IReviewRepository):
    def __init__(self, repositoryManager: IRepositoryManager):
        super().__init__()
        self._persistenceManager = PersistenceFileManager()
        self._repositoryManager = repositoryManager

    def create(self, review) -> bool:
        return self._persistenceManager.save(review)

    def update(self, review) -> bool:
        return self._persistenceManager.update(review)

    def delete(self, review_id: uuid) -> bool:
        return self._persistenceManager.delete(review_id, Review)

    def get_by_id(self, review_id: uuid):
        review = self._persistenceManager.get(review_id, Review)
        if not review:
            return None
        else:
            return Review(self._repositoryManager, review)
    
    def get_by_user(self, user_id: uuid):
        try:
            reviews = self._persistenceManager.get_all(Review)
            if not reviews:
                return []
            else:
                return [Review(self._repositoryManager, review) for review in reviews
                        if str(review.get('user_id')) == str(user_id)]
        except Exception:
            return []
    
    def get_by_place(self, place_id: uuid):
        try:
            reviews = self._persistenceManager.get_all(Review)
            if not reviews:
                return []
            else:
                return [Review(self._repositoryManager, review) for review in reviews 
                        if str(review.get('place_id')) == str(place_id)]
        except Exception:
            return []

    def get_all(self) -> list:
        reviews = self._persistenceManager.get_all(Review)
        if not reviews:
            return []
        else: 
            return [Review(self._repositoryManager, review) for review in reviews]

    def exist(self, id: uuid) -> bool:
        try:
            entity = self._persistenceManager.get(id, Review)
            if not entity:
                return False
            else:
                return True
        except Exception:
            return False
