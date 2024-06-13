from abc import ABC, abstractmethod
from repositories.iAmenityRepository import IAmenityRepository
from repositories.iPlaceRepository import IPlaceRepository
from repositories.iReviewRepository import IReviewRepository
from repositories.iUserRepository import IUserRepository


class IRepositoryManager(ABC):
    @abstractmethod
    def amenityRepository(self) -> IAmenityRepository: pass

    @abstractmethod
    def placeRepository(self) -> IPlaceRepository: pass

    @abstractmethod
    def reviewRepository(self) -> IReviewRepository: pass

    @abstractmethod
    def userRepository(self) -> IUserRepository: pass
