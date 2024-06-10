import unittest
from entities.place import Place
from entities.user import User
from tests.placeMockRepository import PlaceMockRepository
from tests.userMockRepository import UserMockRepository


class TestUser(unittest.TestCase):
    def test_create_place_success(self):
        placeRepo = PlaceMockRepository(create=True, get_by_host=[])
        user = User(placeRepo, UserMockRepository())
        self.assertTrue(user.create_place(Place()), "Place success created")

    def test_create_place_exist(self):
        place = Place()
        placeRepo = PlaceMockRepository(create=True, get_by_host=[place])
        user = User(placeRepo, UserMockRepository())
        self.assertFalse(user.create_place(place), "Place already exist")

    def test_email_invalid(self):
        userRepo = UserMockRepository("test@test.tt")
        user = User(PlaceMockRepository(), userRepo)
        user.email = "test@test.tt"
        self.assertFalse(user.validate_email(), "Email exist")

    def test_email_valid(self):
        userRepo = UserMockRepository("test@test.tt")
        user = User(PlaceMockRepository(), userRepo)
        user.email = "tt@test.tt"
        self.assertTrue(user.validate_email(), "Email don't exist")


if __name__ == '__main__':
    unittest.main()
