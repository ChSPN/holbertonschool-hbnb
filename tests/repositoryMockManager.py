from managers.iRepositoryManager import IRepositoryManager
from repositories.iAmenityRepository import IAmenityRepository
from repositories.iCityRepository import ICityRepository
from repositories.iCountryRepository import ICountryRepository
from repositories.iPlaceRepository import IPlaceRepository
from repositories.iReviewRepository import IReviewRepository
from repositories.iUserRepository import IUserRepository
from tests.amenityMockRepository import AmenityMockRepository
from tests.cityMockRepository import CityMockRepository
from tests.countryMockRepository import CountryMockRepository
from tests.placeMockRepository import PlaceMockRepository
from tests.reviewMockRepository import ReviewMockRepository
from tests.userMockRepository import UserMockRepository


class RepositoryMockManager(IRepositoryManager):
    def __init__(
        self,
        amenityRepository: AmenityMockRepository = None,
        placeRepository: PlaceMockRepository = None,
        reviewRepository: ReviewMockRepository = None,
        userRepository: UserMockRepository = None,
        cityRepository: CityMockRepository = None,
        countryRepository: CountryMockRepository = None,
    ):
        self._amenityRepository = amenityRepository
        self._placeRepository = placeRepository
        self._reviewRepository = reviewRepository
        self._userRepository = userRepository
        self._cityRepository = cityRepository
        self._countryRepository = countryRepository

    def amenityRepository(self) -> IAmenityRepository:
        return self._amenityRepository

    def placeRepository(self) -> IPlaceRepository:
        return self._placeRepository

    def reviewRepository(self) -> IReviewRepository:
        return self._reviewRepository

    def userRepository(self) -> IUserRepository:
        return self._userRepository

    def countryRepository(self) -> ICountryRepository:
        return self._countryRepository

    def cityRepository(self) -> ICityRepository:
        return self._cityRepository
