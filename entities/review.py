from datetime import datetime
import uuid
import tzlocal
from managers.iRepositoryManager import IRepositoryManager


class Review:
    """Review entity class."""

    def __init__(
        self, manager: IRepositoryManager = None, review: dict = None
    ):
        """Constructor for Review entity class."""
        self._review_repo = (
            None if manager is None else manager.reviewRepository()
        )
        self._user_repo = None if manager is None else manager.userRepository()
        self._place_repo = (
            None if manager is None else manager.placeRepository()
        )
        self.id = uuid.uuid4()
        self.created_at = datetime.now(tzlocal.get_localzone())
        self.updated_at: datetime = None
        self.comment: str
        self.rating: int
        self.user_id: uuid
        self.place_id: uuid
        self.parse(review)

    def to_dict(self):
        """Converts Review entity class to dictionary."""
        return {
            "comment": self.comment,
            "created_at": self.created_at,
            "user_id": self.user_id,
            "id": self.id,
            "place_id": self.place_id,
            "updated_at": self.updated_at,
            "rating": self.rating,
        }

    @staticmethod
    def load(manager: IRepositoryManager, id: uuid = None):
        """Loads a Review entity from the repository."""
        repo = manager.reviewRepository()
        if id is None:
            return repo.get_all()
        else:
            return repo.get_by_id(id)

    @staticmethod
    def load_by_user(manager: IRepositoryManager, user_id: uuid):
        """Loads a Review entity from the repository by user."""
        repo = manager.reviewRepository()
        return repo.get_by_user(user_id)

    @staticmethod
    def load_by_place(manager: IRepositoryManager, place_id: uuid):
        """Loads a Review entity from the repository by place."""
        repo = manager.reviewRepository()
        return repo.get_by_place(place_id)

    def parse(self, review: dict = None):
        """Parses a dictionary to a Review entity class."""
        if review and "id" in review:
            self.id = (
                uuid.UUID(review["id"])
                if review["id"] is str
                else review["id"]
            )
        if review and "created_at" in review:
            self.created_at = review["created_at"]
        if review and "updated_at" in review:
            self.updated_at = review["updated_at"]
        self.comment = (
            review["comment"] if review and "comment" in review else None
        )
        self.rating = (
            review["rating"] if review and "rating" in review else None
        )
        self.user_id = (
            review["user_id"] if review and "user_id" in review else None
        )
        if self.user_id is str:
            self.user_id = uuid.UUID(self.user_id)
        self.place_id = (
            review["place_id"] if review and "place_id" in review else None
        )
        if self.place_id is str:
            self.place_id = uuid.UUID(self.place_id)

    def delete(self) -> bool:
        """Deletes a Review entity from the repository."""
        if not self._review_repo:
            return False

        return self._review_repo.delete(self.id)

    def exist_place(self) -> bool:
        """Check if a place exists in the repository."""
        if not self._place_repo:
            return False

        return self._place_repo.exist(self.place_id)

    def exist_user(self) -> bool:
        """Check if a user exists in the repository."""
        if not self._user_repo:
            return False

        return self._user_repo.exist(self.user_id)

    def exist(self) -> bool:
        """Check if a review exists in the repository."""
        if not self._review_repo:
            return False

        return self._review_repo.exist(self.id, self.place_id, self.user_id)

    def save(self) -> bool:
        """Saves a review entity to the repository."""
        if (
            not self._review_repo
            or not self._user_repo
            or not self._place_repo
            or not self.comment
            or not self.user_id
            or not self.place_id
            or not (1 <= self.rating <= 5)
        ):
            return False

        if self.exist():
            """Review already exists."""
            return False

        if not self.exist_place():
            """Place does not exist."""
            return False

        if not self.exist_user():
            """User does not exist."""
            return False

        if self._review_repo.exist(self.id):
            self.updated_at = datetime.now(tzlocal.get_localzone())
            return self._review_repo.update(self)
        else:
            return self._review_repo.create(self)
