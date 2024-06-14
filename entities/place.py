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
        self._city_repository = None if manager is None else manager.cityRepository()
        self.amenities:list[Amenity] = None
        self.city:City = None
        self.city_id:uuid
        self.created_at = datetime.now()
        self.description:str = None
        self.host:User
        self.host_id:uuid
        self.id = uuid.uuid4()
        self.name:str
        self.address:str
        self.number_of_rooms:int
        self.number_of_bathrooms:int
        self.price_per_night:float
        self.latitude:float
        self.longitude:float
        self.max_guests:int
        self.amenity_ids:list = None
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
            'address': self.address,
            'number_of_rooms': self.number_of_rooms,
            'number_of_bathrooms': self.number_of_bathrooms,
            'price_per_night': self.price_per_night,
            'max_guests': self.max_guests,
            'latitude': self.latitude,
            'longitude': self.longitude,
            'amenity_ids': self.amenity_ids,
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

        if self.amenity_ids:
            self.amenity_ids.append(amenity)
        else:
            self.amenity_ids = [amenity.id]
        
        if self.amenities:
            self.amenities.append(amenity)
        else:
            self.amenities = [amenity]

        if not self.save():
            return False

        return True

    def add_review(self, user_id, comment: str):
        """Business logic for adding review"""
        if self.host_id == user_id:
            return False
        
        if not self._user_repository.exist(user_id):
            return False

        if not self.reviews:
            self.reviews = self._review_repository.get_by_place(self.id)

        if self.reviews and any(r.customer_id == user_id for r in self.reviews):
            return False

        review = Review()
        review.comment = comment
        review.customer_id = user_id
        review.place_id = self.id
        review.place = self

        if not self._review_repository.create(review):
            return False

        if self.reviews:
            self.reviews.append(review)
        else:
            self.reviews = [review]

        return True

    @staticmethod
    def load(manager: IRepositoryManager, id: uuid = None):
        repo = manager.placeRepository()
        if id is None:
            return repo.get_all()
        else:
            return repo.get_by_id(id)

    def delete(self) -> bool:
        if (not self._place_repository):
            return False

        return self._place_repository.delete(self.id)

    def save(self) -> bool:
        if (not self._place_repository
            or not self.name
            or not self.address
            or not self.number_of_rooms 
            or not self.number_of_bathrooms
            or not self.price_per_night
            or not self.max_guests
            or not self.host_id
            or not self.city_id):
            return False
        
        if not self._city_repository.exist(self.city_id):
            return False
        
        if not self._user_repository.exist(self.host_id):
            return False
        
        if (self._place_repository.exist(self.id)):
            self.updated_at = datetime.now()
            return self._place_repository.update(self)
        else:
            return self._place_repository.create(self)
