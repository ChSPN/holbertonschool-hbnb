import json
import os
from jsonEconder import JsonEncoder
from iPersistenceManager import IPersistenceManager


class FilePersistenceManager(IPersistenceManager):
    def __get_file_contents(self, name):
        if os.path.isfile(f'datas/{name}.json'):
            with open(f'datas/{name}.json', 'r') as file:
                return json.load(file)
        else:
            return []

    def __put_file_contents(self, name, raw):
        with open(f'datas/{name}.json', 'w') as file:
            json.dump(raw, file, cls=JsonEncoder, indent=4, sort_keys=True)

    def save(self, entity):
        try:
            name = type(entity).__name__
            entities = self.__get_file_contents(name)
            if not entities:
                entities = [entity]
            else:
                entities.append(entity)
            self.__put_file_contents(name, entities)
            return True
        except Exception:
            return False

    def get(self, entity_id, entity_type):
        try:
            name = entity_type.__name__
            entities = self.__get_file_contents(name)
            if not entities:
                return None
            else:
                entities = [n for n in entities if n.id == entity_id]
                if not entities or entities.count() == 0:
                    return None
                else:
                    return entities[0]
        except Exception:
            return None

    def get_all(self, entity_type):
        try:
            name = entity_type.__name__
            entities = self.__get_file_contents(name)
            if not entities:
                return []
            else:
                entities
        except Exception:
            return []

    def update(self, entity):
        try:
            name = type(entity).__name__
            entities = self.__get_file_contents(name)
            if not entities:
                entities = [entity]
            else:
                entities = [n for n in entities if n.id != entity.id]
                if not entities or entities.count() == 0:
                    entities = [entity]
                else:
                    entities.append(entity)
            self.__put_file_contents(name, entities)
            return True
        except Exception:
            return False

    def delete(self, entity_id, entity_type):
        try:
            name = entity_type.__name__
            entities = self.__get_file_contents(name)
            if not entities:
                return False
            else:
                entities = [n for n in entities if n.id != entity_id]
                self.__put_file_contents(name, entities)
                return True
        except Exception:
            return False
