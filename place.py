from datetime import datetime
import uuid
from amenityRepository import AmenityRepository
from placeRepository import PlaceRepository
from userRepository import UserRepository
from reviewRepository import ReviewRepository
from amenity import Amenity
from city import City
from review import Review
from user import User


class Place:
    def __init__(self,
                 amenity_repository=AmenityRepository or None,
                 place_repository=PlaceRepository or None,
                 user_repository=UserRepository or None,
                 review_repository=ReviewRepository or None):
        self._amenity_repository = amenity_repository or None
        self._place_repository = place_repository or None
        self._user_repository = user_repository or None
        self._review_repository = review_repository or None
        self.amenities = [] or None
        self.city = City
        self.city_id = uuid
        self.created_at = datetime.now()
        self.customers = [] or None
        self.description = str or None
        self.host = User
        self.host_id = uuid
        self.id = uuid.uuid4()
        self.name = str
        self.reviews = [] or None
        self.updated_at = datetime or None

    def add_amenity(self, amenity: Amenity):
        """Business logic for adding amenity"""
        if not self.amenities:
            self.amenities = self._amenity_repository.get_by_place(self.id)

        if self.amenities and any(a.id == amenity.id for a in self.amenities):
            return False

        if not self._amenity_repository.exist(amenity.id)
        and not self._amenity_repository.create(amenity):
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
            self.customers =
            self._user_repository.get_customers_by_place(self.id)

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

        if self.reviews and
        any(r.customer_id == user.id for r in self.reviews):
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
