import unittest
import uuid
from entities.review import Review
from entities.user import User
from entities.amenity import Amenity
from entities.place import Place
from tests.repositoryMockManager import RepositoryMockManager
from tests.reviewMockRepository import ReviewMockRepository
from tests.userMockRepository import UserMockRepository
from tests.amenityMockRepository import AmenityMockRepository
from tests.placeMockRepository import PlaceMockRepository


class TestPlace(unittest.TestCase):
    def test_add_amenity_success(self):
        amenityRepo = AmenityMockRepository(True, False, [])
        placeRepo = PlaceMockRepository(add_amenity=True)
        manager = RepositoryMockManager(amenityRepository=amenityRepo, placeRepository=placeRepo)
        place = Place(manager)
        self.assertTrue(place.add_amenity(Amenity()),
                        "Amenity success created")

    def test_add_amenity_exist(self):
        amenity = Amenity()
        amenityRepo = AmenityMockRepository(True, False, [amenity])
        placeRepo = PlaceMockRepository(add_amenity=True)
        manager = RepositoryMockManager(amenityRepository=amenityRepo, placeRepository=placeRepo)
        place = Place(manager)
        self.assertFalse(place.add_amenity(amenity), "Amenity already exist")

    def test_add_amenity_failed(self):
        amenityRepo = AmenityMockRepository(False, False, [])
        placeRepo = PlaceMockRepository(add_amenity=True)
        manager = RepositoryMockManager(amenityRepository=amenityRepo, placeRepository=placeRepo)
        place = Place(manager)
        self.assertFalse(place.add_amenity(Amenity()),
                         "Amenity failed created")

    def test_add_amenity_attach(self):
        amenityRepo = AmenityMockRepository(True, False, [])
        placeRepo = PlaceMockRepository(add_amenity=False)
        manager = RepositoryMockManager(amenityRepository=amenityRepo, placeRepository=placeRepo)
        place = Place(manager)
        self.assertFalse(place.add_amenity(Amenity()),
                         "Amenity success attached")

    def test_add_customer_success(self):
        userRepo = UserMockRepository(customers=[])
        placeRepo = PlaceMockRepository(add_customer=True)
        manager = RepositoryMockManager(userRepository=userRepo, placeRepository=placeRepo)
        place = Place(manager)
        self.assertTrue(place.add_customer(User()), "Customer success added")

    def test_add_customer_exist(self):
        user = User()
        userRepo = UserMockRepository(customers=[user])
        placeRepo = PlaceMockRepository(add_customer=True)
        manager = RepositoryMockManager(userRepository=userRepo, placeRepository=placeRepo)
        place = Place(manager)
        self.assertFalse(place.add_customer(user), "Customer already exist")

    def test_add_customer_failed(self):
        userRepo = UserMockRepository(customers=[])
        placeRepo = PlaceMockRepository(add_customer=False)
        manager = RepositoryMockManager(userRepository=userRepo, placeRepository=placeRepo)
        place = Place(manager)
        self.assertFalse(place.add_customer(User()), "Customer failed added")

    def test_add_review_success(self):
        reviewRepo = ReviewMockRepository(True, [])
        manager = RepositoryMockManager(reviewRepository=reviewRepo)
        user = User()
        place = Place(manager)
        place.host_id = uuid.uuid4()
        review = Review()
        review.comment = ""
        self.assertTrue(place.add_review(user, review), "Review success added")

    def test_add_review_host(self):
        reviewRepo = ReviewMockRepository(True, [])
        user = User()
        user.id = uuid.uuid4()
        manager = RepositoryMockManager(reviewRepository=reviewRepo)
        place = Place(manager)
        place.host_id = user.id
        place.host = user
        review = Review()
        review.comment = ""
        self.assertFalse(place.add_review(user, review.comment),
                         "Review not added because host")

    def test_add_review_exist(self):
        user = User()
        user.id = uuid.uuid4()
        review = Review()
        review.comment = ""
        review.customer = user
        review.customer_id = user.id
        reviewRepo = ReviewMockRepository(True, [review])
        manager = RepositoryMockManager(reviewRepository=reviewRepo)
        place = Place(manager)
        place.host_id = uuid.uuid4()
        self.assertFalse(place.add_review(user, review.comment),
                         "Review not added because exist")

    def test_add_review_failed(self):
        reviewRepo = ReviewMockRepository(False, [])
        user = User()
        manager = RepositoryMockManager(reviewRepository=reviewRepo)
        place = Place(manager)
        place.host_id = uuid.uuid4()
        review = Review()
        review.comment = ""
        self.assertFalse(place.add_review(user, review.comment),
                         "Review failed added")


if __name__ == '__main__':
    unittest.main()
