import uuid
from entities.review import Review
from repositories.iReviewRepository import IReviewRepository


class ReviewMockRepository(IReviewRepository):
    def __init__(self, create=bool or None, get_by_place=[] or None):
        super().__init__()
        self._create = create
        self._get_by_place = get_by_place

    def create(self, review: Review) -> bool:
        return self._create

    def get_by_place(self, id: uuid) -> list[Review]:
        return self._get_by_place
