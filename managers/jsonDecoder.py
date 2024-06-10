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
                    obj[key] = datetime.fromisoformat(value)
                except ValueError:
                    pass
                try:
                    obj[key] = uuid.UUID(value)
                except ValueError:
                    pass
        return obj
