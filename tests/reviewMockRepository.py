import uuid
from entities.review import Review
from repositories.iReviewRepository import IReviewRepository


class ReviewMockRepository(IReviewRepository):
    def __init__(self, 
                 create=bool or None, 
                 get_by_place=[] or None,
                 update:bool = None,
                 delete:bool = None,
                 get_by_id:Review = None,
                 get_all:list[Review] = None, 
                 exist=bool or None):
        super().__init__()
        self._create = create
        self._get_by_place = get_by_place
        self._update = update or None
        self._delete = delete or None
        self._get_by_id = get_by_id or None
        self._get_all = get_all or None
        self._exist = exist or None

    def create(self, review: Review) -> bool:
        return self._create

    def get_by_place(self, id: uuid) -> list[Review]:
        return self._get_by_place

    def update(self, review: Review) -> bool:
        return self._update

    def delete(self, review_id: uuid) -> bool:
        return self._delete

    def get_by_id(self, review_id: uuid) -> Review:
        return self._get_by_id

    def get_all(self) -> list[Review]:
        return self._get_all

    def exist(self, id: uuid) -> bool:
        return self._exist
