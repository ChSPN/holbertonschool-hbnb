import unittest
from entities.place import Place
from entities.user import User
from tests.placeMockRepository import PlaceMockRepository
from tests.repositoryMockManager import RepositoryMockManager
from tests.userMockRepository import UserMockRepository


class TestUser(unittest.TestCase):
    def test_email_invalid(self):
        userRepo = UserMockRepository(get_by_email=User())
        placeRepo = PlaceMockRepository()
        manager = RepositoryMockManager(userRepository=userRepo,placeRepository=placeRepo)
        user = User(manager)
        user.email = "test@test.tt"
        self.assertFalse(user.validate_email(), "Email exist")

    def test_email_valid(self):
        userRepo = UserMockRepository("test@test.tt")
        placeRepo = PlaceMockRepository()
        manager = RepositoryMockManager(userRepository=userRepo,placeRepository=placeRepo)
        user = User(manager)
        user.email = "tt@test.tt"
        self.assertTrue(user.validate_email(), "Email don't exist")


if __name__ == '__main__':
    unittest.main()
