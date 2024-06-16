import datetime
import unittest
import uuid
from entities.amenity import Amenity
from entities.city import City
from entities.country import Country
from entities.place import Place
from entities.review import Review
from entities.user import User
from tests.amenityMockRepository import AmenityMockRepository
from tests.cityMockRepository import CityMockRepository
from tests.countryMockRepository import CountryMockRepository
from tests.placeMockRepository import PlaceMockRepository
from tests.repositoryMockManager import RepositoryMockManager
from tests.reviewMockRepository import ReviewMockRepository
from tests.userMockRepository import UserMockRepository


class TestAmenity(unittest.TestCase):
    def test_save_valid(self):
        amenityRepo = AmenityMockRepository(exist=False, create=True)
        manager = RepositoryMockManager(amenityRepository=amenityRepo)
        amenity = Amenity(manager)
        amenity.name = "test"
        self.assertIsInstance(amenity.id, uuid.UUID, "Amenity id don't exist")
        self.assertIsInstance(
            amenity.created_at,
            datetime.datetime,
            "Amenity created_at don't exist",
        )
        self.assertTrue(amenity.save(), "Create amenity don't work")
        amenityRepo._exists = False
        amenityRepo._exist = True
        amenityRepo._update = True
        self.assertTrue(amenity.save(), "Update amenity don't work")
        self.assertIsInstance(
            amenity.updated_at,
            datetime.datetime,
            "Amenity updated_at don't exist",
        )

    def test_save_invalid(self):
        amenityRepo = AmenityMockRepository(
            exist=False, create=True, exists=True
        )
        manager = RepositoryMockManager(amenityRepository=amenityRepo)
        amenity = Amenity(manager)
        self.assertFalse(amenity.save(), "Create amenity work")
        amenity.name = "test"
        self.assertFalse(amenity.save(), "Create amenity work")
        amenityRepo._exists = False
        self.assertTrue(amenity.save(), "Create amenity don't work")


class TestCity(unittest.TestCase):
    def test_save_valid(self):
        cityRepo = CityMockRepository(exist=False, create=True)
        countryRepo = CountryMockRepository(exist=True)
        manager = RepositoryMockManager(
            cityRepository=cityRepo, countryRepository=countryRepo
        )
        city = City(manager)
        city.name = "test"
        city.country_id = uuid.uuid4()
        self.assertIsInstance(city.id, uuid.UUID, "City id don't exist")
        self.assertIsInstance(
            city.created_at, datetime.datetime, "City created_at don't exist"
        )
        self.assertTrue(city.save(), "Create city don't work")
        cityRepo._exist = True
        cityRepo._update = True
        self.assertTrue(city.save(), "Update city don't work")
        self.assertIsInstance(
            city.updated_at, datetime.datetime, "City updated_at don't exist"
        )

    def test_save_invalid(self):
        cityRepo = CityMockRepository(exist=False, create=True)
        countryRepo = CountryMockRepository(exist=False)
        manager = RepositoryMockManager(
            cityRepository=cityRepo, countryRepository=countryRepo
        )
        city = City(manager)
        self.assertFalse(city.save(), "Create city work")
        city.name = "test"
        self.assertFalse(city.save(), "Create city work")
        city.country_id = uuid.uuid4()
        countryRepo._exist = True
        cityRepo._exists = False
        result = city.save()
        self.assertTrue(result, "Create city don't work")


class TestPlace(unittest.TestCase):
    def test_save_valid(self):
        placeRepo = PlaceMockRepository(exist=False, create=True)
        amenityRepo = AmenityMockRepository(exists=True)
        cityRepo = CityMockRepository(exist=True)
        userRepo = UserMockRepository(exist=True)
        manager = RepositoryMockManager(
            placeRepository=placeRepo,
            amenityRepository=amenityRepo,
            cityRepository=cityRepo,
            userRepository=userRepo,
        )
        place = Place(manager)
        place.name = "test"
        place.address = "test"
        place.number_of_rooms = 1
        place.number_of_bathrooms = 1
        place.max_guests = 1
        place.price_per_night = 1
        place.latitude = 1
        place.longitude = 1
        place.amenity_ids = [uuid.uuid4()]
        place.host_id = uuid.uuid4()
        place.city_id = uuid.uuid4()
        self.assertIsInstance(place.id, uuid.UUID, "Place id don't exist")
        self.assertIsInstance(
            place.created_at, datetime.datetime, "Place created_at don't exist"
        )
        self.assertTrue(place.save(), "Create place don't work")
        placeRepo._exist = True
        placeRepo._update = True
        self.assertTrue(place.save(), "Update place don't work")
        self.assertIsInstance(
            place.updated_at, datetime.datetime, "Place updated_at don't exist"
        )

    def test_save_invalid(self):
        placeRepo = PlaceMockRepository(exist=False, create=True)
        amenityRepo = AmenityMockRepository(exists=False)
        cityRepo = CityMockRepository(exist=False)
        userRepo = UserMockRepository(exist=False)
        manager = RepositoryMockManager(
            placeRepository=placeRepo,
            amenityRepository=amenityRepo,
            cityRepository=cityRepo,
            userRepository=userRepo,
        )
        place = Place(manager)
        self.assertFalse(place.save(), "Create place work")
        place.name = "test"
        place.address = "test"
        place.amenity_ids = [uuid.uuid4()]
        place.host_id = uuid.uuid4()
        place.city_id = uuid.uuid4()
        place.price_per_night = None
        place.number_of_rooms = -1
        place.number_of_bathrooms = -1
        place.max_guests = -1
        place.latitude = 200
        place.longitude = 200
        self.assertFalse(place.save(), "Create place work")
        place.price_per_night = 1
        self.assertFalse(place.save(), "Create place work")
        place.number_of_rooms = 1
        self.assertFalse(place.save(), "Create place work")
        place.number_of_bathrooms = 1
        self.assertFalse(place.save(), "Create place work")
        place.max_guests = 1
        self.assertFalse(place.save(), "Create place work")
        place.latitude = 1
        self.assertFalse(place.save(), "Create place work")
        place.longitude = 1
        self.assertFalse(place.save(), "Create place work")
        amenityRepo._exists = True
        self.assertFalse(place.save(), "Create place work")
        cityRepo._exist = True
        self.assertFalse(place.save(), "Create place work")
        userRepo._exist = True
        self.assertTrue(place.save(), "Create place don't work")


class TestReview(unittest.TestCase):
    def test_save_valid(self):
        reviewRepo = ReviewMockRepository(
            exist=False, create=True, exists=False
        )
        placeRepo = PlaceMockRepository(exist=True)
        userRepo = UserMockRepository(exist=True)
        manager = RepositoryMockManager(
            reviewRepository=reviewRepo,
            placeRepository=placeRepo,
            userRepository=userRepo,
        )
        review = Review(manager)
        review.comment = "test"
        review.rating = 1
        review.user_id = uuid.uuid4()
        review.place_id = uuid.uuid4()
        self.assertIsInstance(review.id, uuid.UUID, "Review id don't exist")
        self.assertIsInstance(
            review.created_at,
            datetime.datetime,
            "Review created_at don't exist",
        )
        self.assertTrue(review.save(), "Create review don't work")
        reviewRepo._exist = True
        reviewRepo._update = True
        self.assertTrue(review.save(), "Update review don't work")
        self.assertIsInstance(
            review.updated_at,
            datetime.datetime,
            "Review updated_at don't exist",
        )

    def test_save_invalid(self):
        reviewRepo = ReviewMockRepository(
            exist=False, create=True, exists=True
        )
        placeRepo = PlaceMockRepository(exist=False)
        userRepo = UserMockRepository(exist=False)
        manager = RepositoryMockManager(
            reviewRepository=reviewRepo,
            placeRepository=placeRepo,
            userRepository=userRepo,
        )
        review = Review(manager)
        review.rating = -1
        self.assertFalse(review.save(), "Create review work")
        review.comment = "test"
        self.assertFalse(review.save(), "Create review work")
        review.user_id = uuid.uuid4()
        self.assertFalse(review.save(), "Create review work")
        review.place_id = uuid.uuid4()
        self.assertFalse(review.save(), "Create review work")
        reviewRepo._exists = False
        self.assertFalse(review.save(), "Create review work")
        placeRepo._exist = True
        self.assertFalse(review.save(), "Create review work")
        userRepo._exist = True
        self.assertFalse(review.save(), "Create review work")
        review.rating = 1
        self.assertTrue(review.save(), "Create review don't work")


class TestUser(unittest.TestCase):
    def test_email_invalid(self):
        userRepo = UserMockRepository(get_by_email=User())
        manager = RepositoryMockManager(userRepository=userRepo)
        user = User(manager)
        user.email = "test@test.tt"
        self.assertFalse(user.validate_email(), "User email exist")

    def test_email_valid(self):
        userRepo = UserMockRepository("test@test.tt")
        manager = RepositoryMockManager(userRepository=userRepo)
        user = User(manager)
        user.email = "tt@test.tt"
        self.assertTrue(user.validate_email(), "User email don't exist")

    def test_save_valid(self):
        userRepo = UserMockRepository(exist=False, create=True)
        manager = RepositoryMockManager(userRepository=userRepo)
        user = User(manager)
        user.email = "tt@test.tt"
        user.first_name = "test"
        user.last_name = "test"
        user.password = "test"
        self.assertIsInstance(user.id, uuid.UUID, "User id don't exist")
        self.assertIsInstance(
            user.created_at, datetime.datetime, "User created_at don't exist"
        )
        self.assertTrue(user.save(), "Create user don't work")
        userRepo._exist = True
        userRepo._update = True
        self.assertTrue(user.save(), "Update user don't work")
        self.assertIsInstance(
            user.updated_at, datetime.datetime, "User updated_at don't exist"
        )

    def test_save_invalid(self):
        userRepo = UserMockRepository(exist=False, create=True)
        manager = RepositoryMockManager(userRepository=userRepo)
        user = User(manager)
        self.assertFalse(user.save(), "Create user work")
        user.email = "tt@test.tt"
        self.assertFalse(user.save(), "Create user work")
        user.first_name = "test"
        self.assertFalse(user.save(), "Create user work")
        user.last_name = "test"
        self.assertFalse(user.save(), "Create user work")
        user.password = "test"
        self.assertTrue(user.save(), "Create user don't work")
        user.email = "tt@test"
        self.assertFalse(user.save(), "Create user work")


if __name__ == "__main__":
    unittest.main()
