import uuid
from entities.review import Review
from managers.persistenceFileManager import PersistenceFileManager
from repositories.iReviewRepository import IReviewRepository


class ReviewFileRepository(IReviewRepository):
    def __init__(self):
        super().__init__()
        self._persistenceManager = PersistenceFileManager()

    def create(self, review) -> bool:
        return self._persistenceManager.save(review)

    def update(self, review) -> bool:
        return self._persistenceManager.update(review)

    def delete(self, review_id: uuid) -> bool:
        return self._persistenceManager.delete(review_id, Review)

    def get_by_id(self, review_id: uuid):
        return self._persistenceManager.get(review_id, Review)
    
    def get_by_customer(self, customer_id: uuid):
        try:
            reviews = self._persistenceManager.get_all(Review)
            if not reviews:
                return []
            else:
                return [review for review in reviews if review.customer_id == customer_id]
        except Exception:
            return []
    
    def get_by_place(self, place_id: uuid):
        try:
            reviews = self._persistenceManager.get_all(Review)
            if not reviews:
                return []
            else:
                return [review for review in reviews if review.place_id == place_id]
        except Exception:
            return []

    def get_all(self) -> list:
        return self._persistenceManager.get_all(Review)

    def get_by_place(self, id: uuid) -> list:
        try:
            reviews = self._persistenceManager.get_all(Review)
            if not reviews:
                return []
            else:
                return [review for review in reviews if review.place_id == id]
        except Exception:
            return []

    def exist(self, id: uuid) -> bool:
        try:
            entity = self._persistenceManager.get(id, Review)
            if not entity:
                return False
            else:
                return True
        except Exception:
            return False
