from datetime import datetime
import uuid
from managers.iRepositoryManager import IRepositoryManager
from entities.amenity import Amenity
from entities.city import City
from entities.review import Review
from entities.user import User


class Place:
    def __init__(self, manager: IRepositoryManager = None):
        self._amenity_repository = None if manager is None else manager.amenityRepository()
        self._place_repository = None if manager is None else manager.placeRepository()
        self._user_repository = None if manager is None else manager.userRepository()
        self._review_repository = None if manager is None else manager.reviewRepository()
        self.amenities:list[Amenity] = None
        self.city:City = None
        self.city_id:uuid
        self.created_at = datetime.now()
        self.customers:list[User] = None
        self.description:str = None
        self.host:User
        self.host_id:uuid
        self.id = uuid.uuid4()
        self.name:str
        self.reviews:list[Review] = None
        self.updated_at:datetime = None

    def to_dict(self):
        return {
            'city_id': self.city_id,
            'created_at': self.created_at,
            'description': self.description,
            'host_id': self.host_id,
            'id': self.id,
            'name': self.name,
            'updated_at': self.updated_at,
        }

    def add_amenity(self, amenity: Amenity):
        """Business logic for adding amenity"""
        if not self.amenities:
            self.amenities = self._amenity_repository.get_by_place(self.id)

        if self.amenities and any(a.id == amenity.id for a in self.amenities):
            return False

        if not self._amenity_repository.exist(amenity.id) and not self._amenity_repository.create(amenity):
            return False

        if not self._place_repository.add_amenity(self, amenity):
            return False
        
        if self.amenities:
            self.amenities.append(amenity)
        else:
            self.amenities = [amenity]

        return True

    def add_customer(self, user):
        """Business logic for adding customer"""
        if not self.customers:
            self.customers = self._user_repository.get_customers_by_place(self.id)

        if self.customers and any(c.id == user.id for c in self.customers):
            return False

        if not self._place_repository.add_customer(self, user):
            return False

        if self.customers:
            self.customers.append(user)
        else:
            self.customers = [user]

        return True

    def add_review(self, user, comment: str):
        """Business logic for adding review"""
        if self.host_id == user.id:
            return False

        if not self.reviews:
            self.reviews = self._review_repository.get_by_place(self.id)

        if self.reviews and any(r.customer_id == user.id for r in self.reviews):
            return False

        review = Review()
        review.comment = comment
        review.customer = user
        review.customer_id = user.id
        review.place_id = self.id
        review.place = self

        if not self._review_repository.create(review):
            return False

        if self.reviews:
            self.reviews.append(review)
        else:
            self.reviews = [review]

        return True

    def create(self, user):
        """Business logic for creating place"""
        if not self._user_repository.exist(user.id):
            return False

        self.host_id = user.id
        self.host = user
        if not self._place_repository.create(self):
            return False
        
        return True
