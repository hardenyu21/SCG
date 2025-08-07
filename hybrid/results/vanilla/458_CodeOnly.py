import json
import re
import pandas as pd

def task_func(json_str):
    # Check if the input JSON string is empty
    if not json_str.strip():
        return pd.DataFrame()

    try:
        # Load the JSON string into a dictionary
        data_dict = json.loads(json_str)
    except json.JSONDecodeError:
        # Return an empty DataFrame if JSON is invalid
        return pd.DataFrame()

    # Function to double numerical values
    def double_value(value):
        if isinstance(value, (int, float)):
            return value * 2
        elif isinstance(value, str):
            # Try to find numbers in the string and double them
            return re.sub(r'\d+', lambda x: str(float(x.group()) * 2), value)
        elif isinstance(value, list):
            # Double each numerical value in the list
            return [double_value(item) for item in value]
        else:
            # Return the value as-is if it's not a number or list
            return value

    # Normalize the dictionary by doubling numerical values
    normalized_dict = {key: double_value(value) for key, value in data_dict.items()}

    # Create a Pandas DataFrame from the normalized dictionary
    df = pd.DataFrame([normalized_dict])

    return df