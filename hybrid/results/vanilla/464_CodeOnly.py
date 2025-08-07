import json
from datetime import datetime
from decimal import Decimal

def task_func(my_obj):
    def custom_encoder(obj):
        if isinstance(obj, datetime):
            return obj.isoformat()
        elif isinstance(obj, Decimal):
            return float(obj)
        raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

    return json.dumps(my_obj, default=custom_encoder)

# Example usage:
# print(task_func({'name': 'Alice', 'age': 30}))
# print(task_func({'name': 'Alice', 'age': 30, 'balance': Decimal('100.50'), 'timestamp': datetime.now()}))