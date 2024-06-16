import datetime
from json import JSONEncoder
import uuid


class JsonEncoder(JSONEncoder):
    def default(self, o):
        if isinstance(o, uuid.UUID):
            return str(o)
        elif isinstance(o, datetime.datetime):
            return o.isoformat()
        else:
            return o.to_dict()
