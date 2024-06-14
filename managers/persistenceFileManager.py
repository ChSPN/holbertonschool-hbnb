import json
import os
from managers.jsonDecoder import JsonDecoder
from managers.jsonEncoder import JsonEncoder


class PersistenceFileManager():
    def __get_file_contents(self, name) -> list[dict]:
        if os.path.isfile(f'datas/{name}.json'):
            with open(f'datas/{name}.json', 'r') as file:
                return json.load(file, cls=JsonDecoder)
        else:
            return []

    def __put_file_contents(self, name, raw):
        with open(f'datas/{name}.json', 'w') as file:
            json.dump(raw, file, cls=JsonEncoder, indent=4, sort_keys=True)

    def save(self, entity) -> bool:
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

    def get(self, entity_id, entity_type) -> dict:
        try:
            name = entity_type.__name__
            entities = self.__get_file_contents(name)
            if not entities:
                return None
            else:
                entities = [n for n in entities if n.get('id') == entity_id]
                if not entities or len(entities) == 0:
                    return None
                else:
                    return entities[0]
        except Exception:
            return None

    def get_all(self, entity_type) -> list[dict]:
        try:
            name = entity_type.__name__
            entities = self.__get_file_contents(name)
            if not entities:
                return []
            else:
                return entities
        except Exception:
            return []

    def update(self, entity) -> bool:
        try:
            name = type(entity).__name__
            entities = self.__get_file_contents(name)
            if not entities:
                entities = [entity]
            else:
                entities = [n for n in entities if n.get('id') != entity.id]
                if not entities or len(entities) == 0:
                    entities = [entity]
                else:
                    entities.append(entity)
            self.__put_file_contents(name, entities)
            return True
        except Exception:
            return False

    def delete(self, entity_id, entity_type) -> bool:
        try:
            name = entity_type.__name__
            entities = self.__get_file_contents(name)
            if not entities:
                return False
            else:
                entities = [n for n in entities if n.get('id') != entity_id]
                self.__put_file_contents(name, entities)
                return True
        except Exception:
            return False
