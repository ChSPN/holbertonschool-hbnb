import uuid
from entities.review import Review
from managers.iPersistenceManager import IPersistenceManager
from repositories.iReviewRepository import IReviewRepository


class ReviewPersistentRepository(IReviewRepository):
    def __init__(self, persistenceManager: IPersistenceManager):
        super().__init__()
        self._persistenceManager = persistenceManager

    def create(self, review) -> bool:
        return self._persistenceManager.save(review)

    def get_by_place(self, id: uuid) -> list[Review]:
        try:
            reviews = self._persistenceManager.get_all(Review)
            if not reviews:
                return []
            else:
                return [review for review in reviews if review.place_id == id]
        except Exception:
            return []
