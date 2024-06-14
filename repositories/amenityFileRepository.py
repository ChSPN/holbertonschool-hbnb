import uuid
from entities.amenity import Amenity
from iAmenityRepository import IAmenityRepository
from managers.persistenceFileManager import PersistenceFileManager


class AmenityFileRepository(IAmenityRepository):
    def __init__(self):
        super().__init__()
        self._persistenceManager = PersistenceFileManager()

    def create(self, amenity) -> bool:
        return self._persistenceManager.save(amenity)

    def update(self, amenity) -> bool:
        return self._persistenceManager.update(amenity)

    def delete(self, amenity_id: uuid) -> bool:
        return self._persistenceManager.delete(amenity_id, Amenity)

    def get_by_id(self, amenity_id: uuid):
        return self._persistenceManager.get(amenity_id, Amenity)

    def get_all(self) -> list:
        return self._persistenceManager.get_all(Amenity)

    def exist(self, id: uuid) -> bool:
        try:
            amenity = self._persistenceManager.get(id, Amenity)
            if not amenity:
                return False
            else:
                return True
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
                    return [amenity for amenity in amenities
                            if amenity.id in place.amenity_ids]
        except Exception:
            return []
