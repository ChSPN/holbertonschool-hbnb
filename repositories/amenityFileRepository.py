import uuid
from entities.amenity import Amenity
from managers.iRepositoryManager import IRepositoryManager
from repositories.iAmenityRepository import IAmenityRepository
from managers.persistenceFileManager import PersistenceFileManager


class AmenityFileRepository(IAmenityRepository):
    def __init__(self, repositoryManager: IRepositoryManager):
        super().__init__()
        self._persistenceManager = PersistenceFileManager()
        self._repositoryManager = repositoryManager

    def create(self, amenity) -> bool:
        return self._persistenceManager.save(amenity)

    def update(self, amenity) -> bool:
        return self._persistenceManager.update(amenity)

    def delete(self, amenity_id: uuid) -> bool:
        return self._persistenceManager.delete(amenity_id, Amenity)

    def get_by_id(self, amenity_id: uuid):
        amenity = self._persistenceManager.get(amenity_id, Amenity)
        if not amenity:
            return None
        else:
            return Amenity(self._repositoryManager, amenity)

    def get_all(self) -> list:
        amenities = self._persistenceManager.get_all(Amenity)
        if not amenities or len(amenities) == 0:
            return []
        else:
            return [Amenity(self._repositoryManager, amenity) for amenity in amenities]

    def exist(self, id: uuid, name: str = None) -> bool:
        try:
            if name is None:
                amenity = self._persistenceManager.get(id, Amenity)
                if not amenity:
                    return False
                else:
                    return True
            else:
                amenities = self._persistenceManager.get_all(Amenity)
                if not amenities or len(amenities) == 0:
                    return False
                else:
                    return any(amenity.get('id') != id and amenity.get('name') == name for amenity in amenities)
        except Exception:
            return False

    def get_by_place(self, id: uuid) -> list:
        try:
            place = self.get_by_id(id)
            if not place:
                return []
            else:
                amenities = self._persistenceManager.get_all(Amenity)
                if not amenities or not place.amenity_ids:
                    return []
                else:
                    return [Amenity(self._repositoryManager, amenity) for amenity in amenities 
                            if amenity.get('id') in place.amenity_ids]
        except Exception:
            return []
