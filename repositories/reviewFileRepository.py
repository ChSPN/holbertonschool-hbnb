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
                return [
                    Review(self._repositoryManager, review)
                    for review in reviews
                    if str(review.get("user_id")) == str(user_id)
                ]
        except Exception:
            return []

    def get_by_place(self, place_id: uuid):
        try:
            reviews = self._persistenceManager.get_all(Review)
            if not reviews:
                return []
            else:
                return [
                    Review(self._repositoryManager, review)
                    for review in reviews
                    if str(review.get("place_id")) == str(place_id)
                ]
        except Exception:
            return []

    def get_all(self) -> list:
        reviews = self._persistenceManager.get_all(Review)
        if not reviews:
            return []
        else:
            return [
                Review(self._repositoryManager, review) for review in reviews
            ]

    def exist(
        self, id: uuid, place_id: uuid = None, user_id: uuid = None
    ) -> bool:
        try:
            if user_id is None:
                review = self._persistenceManager.get(id, Review)
                if not review:
                    return False
                else:
                    return True
            else:
                reviews = self._persistenceManager.get_all(Review)
                if not reviews or len(reviews) == 0:
                    return False
                else:
                    return any(
                        str(review.get("user_id")) == str(user_id)
                        and str(review.get("place_id")) == str(place_id)
                        and str(review.get("id")) != str(id)
                        for review in reviews
                    )
        except Exception:
            return False
