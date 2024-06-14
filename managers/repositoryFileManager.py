from abc import ABC, abstractmethod
from managers.iRepositoryManager import IRepositoryManager
from repositories.amenityFileRepository import AmenityFileRepository
from repositories.cityFileRepository import CityFileRepository
from repositories.countryFileRepository import CountryFileRepository
from repositories.iAmenityRepository import IAmenityRepository
from repositories.iCityRepository import ICityRepository
from repositories.iCountryRepository import ICountryRepository
from repositories.iPlaceRepository import IPlaceRepository
from repositories.iReviewRepository import IReviewRepository
from repositories.iUserRepository import IUserRepository
from repositories.placeFileRepository import PlaceFileRepository
from repositories.reviewFileRepository import ReviewFileRepository
from repositories.userFileRepository import UserFileRepository


class RepositoryFileManager(IRepositoryManager):
    def amenityRepository(self) -> IAmenityRepository:
        return AmenityFileRepository()

    def placeRepository(self) -> IPlaceRepository:
        return PlaceFileRepository()

    def reviewRepository(self) -> IReviewRepository:
        return ReviewFileRepository()

    def userRepository(self) -> IUserRepository:
        return UserFileRepository()

    def countryRepository(self) -> ICountryRepository:
        return CountryFileRepository()

    def cityRepository(self) -> ICityRepository:
        return CityFileRepository()
