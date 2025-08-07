import json
from datetime import datetime
import numpy as np
from decimal import Decimal

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, np.ndarray):
            return obj.tolist()
        elif isinstance(obj, Decimal):
            return float(obj)
        # Add more custom serialization logic here if needed
        return super().default(obj)

def task_func(my_obj):
    try:
        return json.dumps(my_obj, cls=CustomJSONEncoder)
    except TypeError as e:
        raise TypeError(f"Object of type {type(my_obj).__name__} is not JSON serializable") from e

# Example usage:
# print(task_func({'name': 'Alice', 'age': 30}))