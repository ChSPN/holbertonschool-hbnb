import uuid
from entities.customerPlace import CustomerPlace
from entities.place import Place
from entities.user import User
from managers.iPersistenceManager import IPersistenceManager
from repositories.iUserRepository import IUserRepository


class UserPersistentRepository(IUserRepository):
    def __init__(self, persistenceManager: IPersistenceManager):
        super().__init__()
        self._persistenceManager = persistenceManager

    def exist(self, email: str) -> bool:
        try:
            users = self._persistenceManager.get_all(User)
            if not users
            or not any(user for user in users if user.email == email):
                return False
            else:
                return True
        except Exception:
            return False

    def get_customers_by_place(self, id: uuid) -> list:
        try:
            customers_places = self._persistenceManager.get_all(CustomerPlace)
            if not customers_places:
                return []
            else:
                customersId = [customer.user_id for customer
                               in customers_places if customer.place_id == id]
                customers = self._persistenceManager.get_all(User)
                if not customers:
                    return []
                else:
                    return [customer for customer
                            in customers if customer.id in customersId]
        except Exception:
            return []

    def get_by_id(self, id: uuid):
        return self._persistenceManager.get(id, User)
