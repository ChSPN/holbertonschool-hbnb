import uuid
from entities.place import Place
from managers.iRepositoryManager import IRepositoryManager
from managers.persistenceFileManager import PersistenceFileManager
from repositories.iPlaceRepository import IPlaceRepository


class PlaceFileRepository(IPlaceRepository):
    def __init__(self, repositoryManager: IRepositoryManager):
        super().__init__()
        self._persistenceManager = PersistenceFileManager()
        self._repositoryManager = repositoryManager

    def create(self, place) -> bool:
        return self._persistenceManager.save(place)

    def update(self, place) -> bool:
        return self._persistenceManager.update(place)

    def delete(self, place_id: uuid) -> bool:
        return self._persistenceManager.delete(place_id, Place)

    def get_by_id(self, place_id: uuid) -> Place:
        place = self._persistenceManager.get(place_id, Place)
        if not place:
            return None
        else:
            return Place(self._repositoryManager, place)

    def get_all(self) -> list:
        places = self._persistenceManager.get_all(Place)
        if not places:
            return []
        else:
            return [Place(self._repositoryManager, place) for place in places]

    def get_by_host(self, id: uuid) -> list:
        try:
            places = self._persistenceManager.get_all(Place)
            if not places:
                return []
            else:
                return [
                    Place(self._repositoryManager, place)
                    for place in places
                    if str(place.get("host_id")) == str(id)
                ]
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
