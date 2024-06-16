from abc import ABC, abstractmethod
from repositories.iAmenityRepository import IAmenityRepository
from repositories.iCityRepository import ICityRepository
from repositories.iCountryRepository import ICountryRepository
from repositories.iPlaceRepository import IPlaceRepository
from repositories.iReviewRepository import IReviewRepository
from repositories.iUserRepository import IUserRepository


class IRepositoryManager(ABC):
    """Interface for Repository Manager class."""

    @abstractmethod
    def amenityRepository(self) -> IAmenityRepository:
        """Abstract method for Amenity Repository."""
        pass

    @abstractmethod
    def placeRepository(self) -> IPlaceRepository:
        """Abstract method for Place Repository."""
        pass

    @abstractmethod
    def reviewRepository(self) -> IReviewRepository:
        """Abstract method for Review Repository."""
        pass

    @abstractmethod
    def userRepository(self) -> IUserRepository:
        """Abstract method for User Repository."""
        pass

    @abstractmethod
    def countryRepository(self) -> ICountryRepository:
        """Abstract method for Country Repository."""
        pass

    @abstractmethod
    def cityRepository(self) -> ICityRepository:
        """Abstract method for City Repository."""
        pass
