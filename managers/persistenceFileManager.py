import json
import os
from managers.jsonDecoder import JsonDecoder
from managers.jsonEncoder import JsonEncoder


class PersistenceFileManager:
    """PersistenceFileManager class for JSON persistence."""

    def __get_file_contents(self, name) -> list[dict]:
        """Gets the contents of a file."""
        if os.path.isfile(f"datas/{name}.json"):
            """If the file exists, read it."""
            with open(f"datas/{name}.json", "r") as file:
                """Read the file and return the contents."""
                return json.load(file, cls=JsonDecoder)
        else:
            """If the file does not exist, return an empty list."""
            return []

    def __put_file_contents(self, name, raw):
        """Puts the contents of a file."""
        with open(f"datas/{name}.json", "w") as file:
            """Write the contents to the file."""
            json.dump(raw, file, cls=JsonEncoder, indent=4, sort_keys=True)

    def save(self, entity) -> bool:
        """Saves an entity to the JSON file."""
        try:
            name = type(entity).__name__
            """Get the name of the entity type."""
            entities = self.__get_file_contents(name)
            """Get the contents of the JSON file."""
            if not entities:
                """If the entities is empty, create and add the entity."""
                entities = [entity]
            else:
                """If the entities is not empty, append the entity to list."""
                entities.append(entity)
            self.__put_file_contents(name, entities)
            """Write the entities to the JSON file."""
            return True
        except Exception:
            return False

    def get(self, entity_id, entity_type) -> dict:
        """Gets an entity from the JSON file."""
        try:
            name = entity_type.__name__
            """Get the name of the entity type."""
            entities = self.__get_file_contents(name)
            """Get the contents of the JSON file."""
            if not entities:
                """If the entities is empty, return None."""
                return None
            else:
                """If the entities is not empty, filter the entity by id."""
                entities = [
                    n for n in entities if str(n.get("id")) == str(entity_id)
                ]
                if not entities or len(entities) == 0:
                    return None
                else:
                    return entities[0]
        except Exception:
            return None

    def get_all(self, entity_type) -> list[dict]:
        """Gets all entities from the JSON file."""
        try:
            name = entity_type.__name__
            """Get the name of the entity type."""
            entities = self.__get_file_contents(name)
            """Get the contents of the JSON file."""
            if not entities:
                return []
            else:
                return entities
        except Exception:
            return []

    def update(self, entity) -> bool:
        """Updates an entity in the JSON file."""
        try:
            name = type(entity).__name__
            """Get the name of the entity type."""
            entities = self.__get_file_contents(name)
            """Get the contents of the JSON file."""
            if not entities:
                """If the entities is empty, create and add the entity."""
                entities = [entity]
            else:
                """If the entities is not empty, update the entity."""
                entities = [
                    n for n in entities if str(n.get("id")) != str(entity.id)
                ]
                if not entities or len(entities) == 0:
                    entities = [entity]
                else:
                    entities.append(entity)
            self.__put_file_contents(name, entities)
            """Write the entities to the JSON file."""
            return True
        except Exception:
            return False

    def delete(self, entity_id, entity_type) -> bool:
        """Deletes an entity from the JSON file."""
        try:
            name = entity_type.__name__
            """Get the name of the entity type."""
            entities = self.__get_file_contents(name)
            """Get the contents of the JSON file."""
            if not entities:
                """If the entities is empty, return False."""
                return False
            else:
                """If the entities is not empty, filter the entity by id."""
                entities = [
                    n for n in entities if str(n.get("id")) != str(entity_id)
                ]
                self.__put_file_contents(name, entities)
                """Write the entities to the JSON file."""
                return True
        except Exception:
            return False
