import uuid
from entities.amenityPlace import AmenityPlace
from entities.customerPlace import CustomerPlace
from entities.place import Place
from managers.iPersistenceManager import IPersistenceManager
from repositories.iPlaceRepository import IPlaceRepository


class PlacePersistentRepository(IPlaceRepository):
    def __init__(self, persistenceManager: IPersistenceManager):
        super().__init__()
        self._persistenceManager = persistenceManager

    def add_amenity(self, place, amenity) -> bool:
        try:
            amenities_places = self._persistenceManager.get_all(AmenityPlace)
            if amenities_places and any(amenity for amenity in amenities_places
                                        if amenity.place_id == id
                                        and amenity.amenity_id == amenity.id):
                return False
            else:
                return self._persistenceManager.save(
                    AmenityPlace(place_id=place.id, amenity_id=amenity.id))
        except Exception:
            return False

    def add_customer(self, place, customer) -> bool:
        try:
            customer_places = self._persistenceManager.get_all(CustomerPlace)
            if customer_places and any(customer for customer in
                                       customer_places if
                                       customer.place_id == id
                                       and customer.user_id == customer.id):
                return False
            else:
                return self._persistenceManager.save(
                    CustomerPlace(place_id=place.id, user_id=customer.id))
        except Exception:
            return False

    def create(self, place) -> bool:
        return self._persistenceManager.save(place)

    def update(self, place) -> bool:
        return self._persistenceManager.update(place)

    def delete(self, place_id: uuid) -> bool:
        return self._persistenceManager.delete(place_id, Place)

    def get_by_id(self, place_id: uuid) -> Place:
        return self._persistenceManager.get(place_id, Place)

    def get_all(self) -> list:
        return self._persistenceManager.get_all(Place)

    def get_by_host(self, id: uuid) -> list:
        try:
            places = self._persistenceManager.get_all(Place)
            if not places:
                return []
            else:
                return [place for place in places if places.host_id in id]
        except Exception:
            return []

    def exist(self, id: uuid) -> bool:
        try:
            entity = self._persistenceManager.get(id, Place)
            if not entity:
                return False
            else:
                return True
        except Exception:
            return False
