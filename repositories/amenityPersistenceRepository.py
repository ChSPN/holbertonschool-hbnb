import uuid
from entities.amenityPlace import AmenityPlace
from entities.amenity import Amenity
from iAmenityRepository import IAmenityRepository
from managers.iPersistenceManager import IPersistenceManager


class AmenityPersistentRepository(IAmenityRepository):
    def __init__(self, persistenceManager: IPersistenceManager):
        super().__init__()
        self._persistenceManager = persistenceManager

    def create(self, amenity) -> bool:
        return self._persistenceManager.save(amenity)

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
