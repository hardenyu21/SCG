import json
import re
from collections import Counter

# Constants
REPLACE_NONE = "None"

def task_func(json_str):
    # Load JSON data
    data = json.loads(json_str)
    
    # Helper function to remove None values and replace emails
    def process_value(value):
        if isinstance(value, dict):
            return {k: process_value(v) for k, v in value.items() if v is not None}
        elif isinstance(value, list):
            return [process_value(v) for v in value if v is not None]
        elif isinstance(value, str) and re.match(r"[^@]+@[^@]+\.[^@]+", value):
            return REPLACE_NONE
        else:
            return value
    
    # Process the data
    processed_data = process_value(data)
    
    # Flatten the data to count values
    def flatten(data):
        if isinstance(data, dict):
            for v in data.values():
                yield from flatten(v)
        elif isinstance(data, list):
            for item in data:
                yield from flatten(item)
        else:
            yield data
    
    # Count the frequency of each unique value
    value_counts = Counter(flatten(processed_data))
    
    # Return the result
    return {
        "data": processed_data,
        "value_counts": value_counts
    }