import unittest
import uuid
from entities.review import Review
from entities.user import User
from entities.amenity import Amenity
from entities.place import Place
from tests.cityMockRepository import CityMockRepository
from tests.repositoryMockManager import RepositoryMockManager
from tests.reviewMockRepository import ReviewMockRepository
from tests.userMockRepository import UserMockRepository
from tests.amenityMockRepository import AmenityMockRepository
from tests.placeMockRepository import PlaceMockRepository


class TestPlace(unittest.TestCase):
    def test_add_amenity_success(self):
        amenityRepo = AmenityMockRepository(True, True, [])
        placeRepo = PlaceMockRepository(add_amenity=True, update=True, create=True)
        manager = RepositoryMockManager(amenityRepository=amenityRepo,
                                        placeRepository=placeRepo,
                                        userRepository=UserMockRepository(exist=True),
                                        cityRepository=CityMockRepository(exist=True))
        place = Place(manager)
        place.name = "Test"
        place.address = "Test"
        place.city_id = uuid.uuid4()
        place.host_id = uuid.uuid4()
        place.latitude = 0.0
        place.longitude = 0.0
        place.number_of_bathrooms = 1
        place.number_of_rooms = 1
        place.max_guests = 1
        place.price_per_night = 1.0
        self.assertTrue(place.add_amenity(Amenity()),
                        "Amenity success created")

    def test_add_amenity_exist(self):
        amenity = Amenity()
        amenityRepo = AmenityMockRepository(True, False, [amenity])
        placeRepo = PlaceMockRepository(add_amenity=True)
        manager = RepositoryMockManager(amenityRepository=amenityRepo,
                                        placeRepository=placeRepo,
                                        userRepository=UserMockRepository(exist=True),
                                        cityRepository=CityMockRepository(exist=True))
        place = Place(manager)
        place.name = "Test"
        place.address = "Test"
        place.city_id = uuid.uuid4()
        place.host_id = uuid.uuid4()
        place.latitude = 0.0
        place.longitude = 0.0
        place.number_of_bathrooms = 1
        place.number_of_rooms = 1
        place.max_guests = 1
        place.price_per_night = 1.0
        self.assertFalse(place.add_amenity(amenity), "Amenity already exist")

    def test_add_amenity_failed(self):
        amenityRepo = AmenityMockRepository(False, False, [])
        placeRepo = PlaceMockRepository(add_amenity=True)
        manager = RepositoryMockManager(amenityRepository=amenityRepo,
                                        placeRepository=placeRepo,
                                        userRepository=UserMockRepository(exist=True),
                                        cityRepository=CityMockRepository(exist=True))
        place = Place(manager)
        place.name = "Test"
        place.address = "Test"
        place.city_id = uuid.uuid4()
        place.host_id = uuid.uuid4()
        place.latitude = 0.0
        place.longitude = 0.0
        place.number_of_bathrooms = 1
        place.number_of_rooms = 1
        place.max_guests = 1
        place.price_per_night = 1.0
        self.assertFalse(place.add_amenity(Amenity()),
                         "Amenity failed created")

    def test_add_amenity_attach(self):
        amenityRepo = AmenityMockRepository(True, False, [])
        placeRepo = PlaceMockRepository(add_amenity=False)
        manager = RepositoryMockManager(amenityRepository=amenityRepo,
                                        placeRepository=placeRepo,
                                        userRepository=UserMockRepository(exist=True),
                                        cityRepository=CityMockRepository(exist=True))
        place = Place(manager)
        place.name = "Test"
        place.address = "Test"
        place.city_id = uuid.uuid4()
        place.host_id = uuid.uuid4()
        place.latitude = 0.0
        place.longitude = 0.0
        place.number_of_bathrooms = 1
        place.number_of_rooms = 1
        place.max_guests = 1
        place.price_per_night = 1.0
        self.assertFalse(place.add_amenity(Amenity()),
                         "Amenity success attached")

    def test_add_review_success(self):
        reviewRepo = ReviewMockRepository(True, [])
        manager = RepositoryMockManager(reviewRepository=reviewRepo, userRepository=UserMockRepository(exist=True))
        user = User()
        place = Place(manager)
        place.host_id = uuid.uuid4()
        review = Review()
        review.comment = ""
        self.assertTrue(place.add_review(user.id, review), "Review success added")

    def test_add_review_host(self):
        reviewRepo = ReviewMockRepository(True, [])
        user = User()
        user.id = uuid.uuid4()
        manager = RepositoryMockManager(reviewRepository=reviewRepo, userRepository=UserMockRepository(exist=True))
        place = Place(manager)
        place.host_id = user.id
        place.host = user
        review = Review()
        review.comment = ""
        self.assertFalse(place.add_review(user.id, review.comment),
                         "Review not added because host")

    def test_add_review_exist(self):
        user = User()
        user.id = uuid.uuid4()
        review = Review()
        review.comment = ""
        review.customer = user
        review.customer_id = user.id
        reviewRepo = ReviewMockRepository(True, [review])
        manager = RepositoryMockManager(reviewRepository=reviewRepo, userRepository=UserMockRepository(exist=True))
        place = Place(manager)
        place.host_id = uuid.uuid4()
        self.assertFalse(place.add_review(user.id, review.comment),
                         "Review not added because exist")

    def test_add_review_failed(self):
        reviewRepo = ReviewMockRepository(False, [])
        user = User()
        manager = RepositoryMockManager(reviewRepository=reviewRepo, userRepository=UserMockRepository(exist=True))
        place = Place(manager)
        place.host_id = uuid.uuid4()
        review = Review()
        review.comment = ""
        self.assertFalse(place.add_review(user.id, review.comment),
                         "Review failed added")


if __name__ == '__main__':
    unittest.main()
