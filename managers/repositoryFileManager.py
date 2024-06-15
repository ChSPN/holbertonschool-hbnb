from abc import ABC, abstractmethod
from managers.iRepositoryManager import IRepositoryManager
from repositories.amenityFileRepository import AmenityFileRepository
from repositories.cityFileRepository import CityFileRepository
from repositories.countryFileRepository import CountryFileRepository
from repositories.placeFileRepository import PlaceFileRepository
from repositories.reviewFileRepository import ReviewFileRepository
from repositories.userFileRepository import UserFileRepository


class RepositoryFileManager(IRepositoryManager):
    def amenityRepository(self):
        return AmenityFileRepository(self)

    def placeRepository(self):
        return PlaceFileRepository()

    def reviewRepository(self):
        return ReviewFileRepository()

    def userRepository(self):
        return UserFileRepository(self)

    def countryRepository(self):
        return CountryFileRepository()

    def cityRepository(self):
        return CityFileRepository()
