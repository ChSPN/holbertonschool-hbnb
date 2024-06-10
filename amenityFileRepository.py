import datetime
import json
import os
import uuid
from jsonEconder import JsonEncoder
from amenityRepository import AmenityRepository


class AmenityFileRepository(AmenityRepository):
    def __init__(self):
        super().__init__()

    def __get_file_contents(self, name):
        if os.path.isfile(f'datas/{name}.json'):
            with open(f'datas/{name}.json', 'r') as file:
                return json.load(file)
        else:
            return []
        
    def __put_file_contents(self, name, raw):
        with open(f'datas/{name}.json', 'w') as file:
            json.dump(raw, file, cls=JsonEncoder, indent=4, sort_keys=True)

    def create(self, amenity) -> bool:
        try:
            amenities = self.__get_file_contents('amenities')
            if not amenities:
                amenities.append(amenity)
            else:
                amenities = [amenity]
            self.__put_file_contents('amenities', amenities)
            return True
        except Exception:
            return False

    def exist(self, id:uuid) -> bool:
        try:
            amenities = self.__get_file_contents('amenities')
            if not amenities:
                return False
            else:
                return any(amenity for amenity in amenities if amenity.id == id)
        except:
            return False

    def get_by_place(self, id:uuid) -> list:
        try:
            amenities_places = self.__get_file_contents('amenities_places')
            if not amenities_places:
                return []
            else:
                amenitiesId = [amenity for amenity in amenities_places if amenity.place_id == id]
                amenities = self.__get_file_contents('amenities')
                if not amenities:
                    return []
                else:
                    return [amenity for amenity in amenities if amenity.id in amenitiesId]
        except:
            return []