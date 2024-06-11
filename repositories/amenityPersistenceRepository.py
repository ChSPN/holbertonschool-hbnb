import uuid
from entities.amenityPlace import AmenityPlace
from entities.amenity import Amenity
from entities.place import Place
from iAmenityRepository import IAmenityRepository
from managers.iPersistenceManager import IPersistenceManager


class AmenityPersistentRepository(IAmenityRepository):
    def __init__(self, persistenceManager: IPersistenceManager):
        super().__init__()
        self._persistenceManager = persistenceManager

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
            amenities_places = self._persistenceManager.get_all(AmenityPlace)
            if not amenities_places:
                return []
            else:
                amenitiesId = [amenity.amenity_id for amenity in
                               amenities_places if amenity.place_id == id]
                amenities = self._persistenceManager.get_all(Amenity)
                if not amenities:
                    return []
                else:
                    return [amenity for amenity in amenities
                            if amenity.id in amenitiesId]
        except Exception:
            return []
