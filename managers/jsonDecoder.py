import datetime
from json import JSONDecoder
import uuid


class JsonDecoder(JSONDecoder):
    """JSON decoder class."""

    def __init__(self, *args, **kwargs):
        """Constructor for JsonDecoder class."""
        super().__init__(object_hook=self.object_hook, *args, **kwargs)

    def object_hook(self, obj):
        """Converts a dictionary to an object."""
        for key, value in obj.items():
            if isinstance(value, str):
                """Convert string to datetime or UUID."""
                try:
                    temp = datetime.datetime.strptime(
                        value, "%Y-%m-%dT%H:%M:%S%z"
                    )
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
