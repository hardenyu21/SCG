import json
import base64
from datetime import datetime

def task_func(data: dict, DATE_FORMAT="%Y-%m-%d %H:%M:%S") -> str:
    # Add the current timestamp to the dictionary
    current_timestamp = datetime.now().strftime(DATE_FORMAT)
    data['timestamp'] = current_timestamp
    
    # Serialize the dictionary to a JSON-formatted string
    json_string = json.dumps(data)
    
    # Encode the JSON string using base64 with ASCII encoding
    base64_encoded = base64.b64encode(json_string.encode('ascii')).decode('ascii')
    
    return base64_encoded