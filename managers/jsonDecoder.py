import datetime
from json import JSONDecoder
import uuid


class JsonDecoder(JSONDecoder):
    def __init__(self, *args, **kwargs):
        super().__init__(object_hook=self.object_hook, *args, **kwargs)
    
    def object_hook(self, obj):
        for key, value in obj.items():
            if isinstance(value, str):
                try:
                    temp = datetime.datetime.strptime(value, "%Y-%m-%dT%H:%M:%S")
                    obj[key] = temp
                except ValueError:
                    try:
                        temp = uuid.UUID(value)
                        obj[key] = temp
                    except ValueError:
                        pass
            else:
                obj[key] = value
        return obj
