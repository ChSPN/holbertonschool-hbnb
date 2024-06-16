from managers.iRepositoryManager import IRepositoryManager
from repositories.amenityFileRepository import AmenityFileRepository
from repositories.cityFileRepository import CityFileRepository
from repositories.countryFileRepository import CountryFileRepository
from repositories.placeFileRepository import PlaceFileRepository
from repositories.reviewFileRepository import ReviewFileRepository
from repositories.userFileRepository import UserFileRepository


class RepositoryFileManager(IRepositoryManager):
    """Repository Manager class for file persistance."""

    def amenityRepository(self):
        """Amenity Repository for file persistance."""
        return AmenityFileRepository(self)

    def placeRepository(self):
        """Place Repository for file persistance."""
        return PlaceFileRepository(self)

    def reviewRepository(self):
        """Review Repository for file persistance."""
        return ReviewFileRepository(self)

    def userRepository(self):
        """User Repository for file persistance."""
        return UserFileRepository(self)

    def countryRepository(self):
        """Country Repository for file persistance."""
        return CountryFileRepository(self)

    def cityRepository(self):
        """City Repository for file persistance."""
        return CityFileRepository(self)
