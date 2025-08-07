import json
import os
import re

def task_func(
    file_path,
    attribute,
    INPUT_JSON={
        "type": "object",
        "properties": {
            "name": {"type": str},  
            "age": {"type": int},   
            "email": {"type": str}  
        },
        "required": ["name", "age", "email"]
    },
    EMAIL_REGEX=r"^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
):
    # Check if the file exists
    if not os.path.exists(file_path):
        raise ValueError("The file does not exist.")
    
    # Load the JSON data from the file
    with open(file_path, 'r') as file:
        try:
            data = json.load(file)
        except json.JSONDecodeError:
            raise ValueError("The file is not a valid JSON.")
    
    # Validate the JSON structure against the schema
    def validate_json(data, schema):
        if schema["type"] != "object":
            raise ValueError("The JSON root must be an object.")
        
        required_fields = schema.get("required", [])
        properties = schema.get("properties", {})
        
        # Check for required fields
        for field in required_fields:
            if field not in data:
                raise ValueError(f"Missing required attribute: {field}")
        
        # Check types of each field
        for field, field_schema in properties.items():
            if field in data:
                if not isinstance(data[field], field_schema["type"]):
                    raise ValueError(f"Type mismatch for attribute '{field}': expected {field_schema['type'].__name__}, got {type(data[field]).__name__}")
        
        # Validate email format
        if "email" in data and not re.match(EMAIL_REGEX, data["email"]):
            raise ValueError("Invalid email format.")
    
    validate_json(data, INPUT_JSON)
    
    # Retrieve the specified attribute
    if attribute not in data:
        raise ValueError(f"The specified attribute '{attribute}' does not exist in the JSON data.")
    
    return data[attribute]