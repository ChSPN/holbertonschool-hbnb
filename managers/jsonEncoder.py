import datetime
from json import JSONEncoder
import uuid


class JsonEncoder(JSONEncoder):
    """JSON encoder class."""

    def default(self, o):
        if isinstance(o, uuid.UUID):
            """Convert UUID to string."""
            return str(o)
        elif isinstance(o, datetime.datetime):
            """Convert datetime to string."""
            return o.isoformat()
        else:
            """Convert object to dictionary."""
            return o.to_dict()
